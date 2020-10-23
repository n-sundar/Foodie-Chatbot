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

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"7c5b4cda151a68ab847143b592e4c232"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'italian':55,'north indian':50,'south indian':85, 'american':1,'mexican':73}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

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
			return [SlotSet('location','nomatch')]
		return [SlotSet('location',loc)]					

class SendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):	
		from_email = 'foodie.restaurantfinder@gmail.com'
		to_email = 'sundararajan.n@gmail.com'
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
		email_body = 'Test Email Body'
		email_msg.attach(MIMEText(email_body,'plain'))
		email_text = email_msg.as_string()
		gmail.sendmail(from_email,to_email,email_text)
		gmail.close()
		return[AllSlotsReset()]

class ActionChatReset(Action): 
	def name(self): 
		return 'action_reset_chat' 
	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]
