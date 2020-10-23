## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- we are good
- alright
- okie
- that's good

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one
- thank you
- see you
- adios
- see you around
- nice talking to you
- bbye
- tc
- take care
- see you soon
- thanks

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- my dear watson
- hello there

## intent:restaurant_search
- I am hungry
- I want some breakfast
- I want some dinner
- I am starving
- Find a food joint in [Chennai](location)
- Looking for some restaurants in [Bengaluru](location)
- Find some restaurants in [Mumbai](location)
- I am looking for a [American](cuisine) restaurant in [Delhi](location)
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [chennai](location) in a [normal]{"entity": "budget", "value": "norml"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- can you find me a [chinese](cuisine) restaurant in [delhi](location)
- [expnsv](budget)
- [norml](budget)
- [budg](budget)
- [Pocket-Friendly < Rs.300]{"entity": "budget", "value": "budg"}
- [Moderate Rs.300 - 700]{"entity": "budget", "value": "norml"}
- [Fine Dining > Rs.700]{"entity": "budget", "value": "expnsv"}
- [less than 300]{"entity": "budget", "value": "budg"}
- costing [less than 300]{"entity": "budget", "value": "budg"}
- Find me a [fine dining]{"entity": "budget", "value": "expnsv"} restaurant for two please
- I want to ear
- i am starving
- [chennai](location)
- search
- i am hungry
- i want to search for a [american](cuisine) restaurant in [chennai](location)
- find me a [italian](cuisine) restaurant in [mayapur](location)
- [Chennai](location)
- find me a [pocket friendly]{"entity": "budget", "value": "budg"} [chinese](cuisine) restaurant in [chennai](location)

## synonym:4
- four

## synonym:bangalore
- Bengaluru

## synonym:budg
- Pocket-Friendly < Rs.300
- less than 300
- <300
- budget friendly
- low cost
- pocket friendly
- < 300
- lessthan 300

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:delhi
- New Delhi

## synonym:expnsv
- Fine Dining > Rs.700
- fine dining
- Fine Dining
- more than 700
- morethan 700

## synonym:norml
- normal
- Moderate Rs.300 - 700
- 300 to 700
- <700
- medium budget
- less than 700
- < 700
- lessthan 700

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*
