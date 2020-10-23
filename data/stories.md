## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
    - slot{"budget": "expnsv"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export
    
## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
    - slot{"budget": "expnsv"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_validate_location
    - slot{"location": "Chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search
    - action_search_restaurants
    - slot{"location": "Chennai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"budget": "budg", "cuisine": "chinese", "location": "chennai"}
    - slot{"budget": "budg"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_goodbye
