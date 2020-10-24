from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk.events import AllSlotsReset
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import pandas as pd
import re

email_response = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"7c5b4cda151a68ab847143b592e4c232"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = 'norml'
		budget = tracker.get_slot('budget')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'italian':55,'north indian':50,'south indian':85, 'american':1,'mexican':73}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine.lower())), 30)
		d = json.loads(results)
		if d['results_found'] == 0:
			chat_response= "No Results found for your criteria. Try again with some other choices."
		else: 
			res_list = d['restaurants']
			res_frame = pd.DataFrame([{'name': x['restaurant']['name'], 'rating': x['restaurant']['user_rating']['aggregate_rating'],\
				'address': x['restaurant']['location']['address'],'cost_for_2': x['restaurant']['average_cost_for_two']} for x in res_list])
			res_frame.sort_values(by = 'rating', ascending = False,inplace = True)
			if budget == 'budg':
				final_frame = res_frame.loc[(res_frame.cost_for_2 <= 300)][:10].reset_index()
			elif budget == 'norml':
				final_frame = res_frame.loc[(res_frame.cost_for_2 > 300) & (res_frame.cost_for_2 <= 700)][:10].reset_index()
			elif budget == 'expnsv':
				final_frame = res_frame.loc[(res_frame.cost_for_2 > 700)][:10].reset_index()
			else:
				final_frame = res_frame[:10]
			global email_response
			email_response = 'Below are the top restaurants for your search: \n'
			chat_response = ''
			for i in range(len(final_frame)):
				j = i
				email_response += str(j+1) + ". " + final_frame.loc[i,'name'] + " with average rating of " + str(final_frame.loc[i,'rating']) + " found at " \
				+ final_frame.loc[i,'address'] + " and the average cost for 2 would be INR " + str(final_frame.loc[i,'cost_for_2']) + ". \n"
			if len(final_frame) <5:
				chat_response = 'Got ' + str(len(final_frame)) + ' restaurants that matched your criteria. Try with a different cuisine or higher budget if possible. \n' \
								+ email_response
			elif len(final_frame) == 5:
				chat_response = email_response
			elif len(final_frame) > 5:
				for i in range(5):
					j = i
					chat_response += 'Below are the top restaurants for your search: \n' + str(j+1) + ". " + final_frame.loc[i,'name'] + \
					" with average rating of " + str(final_frame.loc[i,'rating']) + " found at " \
					+ final_frame.loc[i,'address'] + " and the average cost for 2 would be INR " + str(final_frame.loc[i,'cost_for_2']) + ". \n"			
		
		dispatcher.utter_message(chat_response)
		return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('budget',''),SlotSet('email_body',email_response)]

tier_city_list = ['ahmedabad', 'bengaluru', 'bangalore', 'chennai', 'madras', 'delhi', 'new delhi', 'hyderabad', 'kolkata', 'calcutta', 
					'mumbai', 'bombay', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 
					'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 
					'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'dindigul', 'erode', 'faridabad', 'firozabad', 
					'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 
					'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 
					'kannur', 'kanpur', 'karnal', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 
					'madurai', 'malappuram', 'mathura', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 
					'nellore', 'noida', 'patna', 'pondicherry', 'purulia', 'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 
					'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 'thanjavur', 'thiruvananthapuram', 
					'thrissur', 'tiruchirappalli', 'tirunelveli', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 
					'visakhapatnam', 'vellore', 'warangal']
class ValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		if loc.lower() not in tier_city_list:
			return [SlotSet('loc_chk','nomatch')]
		return [SlotSet('loc_chk','match')]					

class SendEmail(Action):
	def name(self):
		return 'action_send_email'

	def checkmail(self, email):
		#complete the function
		#the function should return the strings "invalid" or "valid" based on the email ID entered
		email_regex = re.compile('^[a-zA-Z0-9-_]+(\.[a-zA-Z0-9-_])*@[a-z]+\.[a-z]{2,3}$')
		valid = email_regex.match(email)
		if valid == None:
			return 'invalid'
		else:
			return 'valid'
	def run(self, dispatcher, tracker, domain):
		from_email = 'foodie.restaurantfinder@gmail.com'
		to_email = tracker.get_slot('email')
		#to_email = 'sundararajan.n@gmail.com'
		global email_response
		if self.checkmail(to_email) == 'valid':
			tracker.slots['email_chk'] = 'valid'
			cred = 'Upgrad123'
			gmail = smtplib.SMTP('smtp.gmail.com',587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login(from_email, cred)
			email_subject = 'Hello from Foodie'
			email_msg = MIMEMultipart()
			email_msg['From'] = from_email
			email_msg['TO'] = to_email
			email_msg['Subject'] = email_subject
			email_body = email_response
			email_msg.attach(MIMEText(email_body,'plain'))
			email_text = email_msg.as_string()
			gmail.sendmail(from_email,to_email,email_text)
			gmail.quit()
			return[SlotSet('email_chk','valid')]
		else:
			return[SlotSet('email_chk','invalid')]

class ActionChatReset(Action): 
	def name(self): 
		return 'action_reset_chat' 
	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]
