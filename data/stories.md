## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"loc_chk": "match"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "norml"}
    - slot{"budget": "norml"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "Italian"}
    - slot{"budget": ""}
    - slot{"email_body": "Below are the top restaurants for your search: \n1. Yaa Mohaideen Biryani with average rating of 4.4 found at Old Shop 4/158, Church Road, Opposite Uzhavar Santhai, Pallavaram, Chennai and the average cost for 2 would be INR 600. \n"}
    - utter_ask_send_email
* restaurant_search{"email": "sundararajan.n@gmail.com"}
    - slot{"email": "sundararajan.n@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
