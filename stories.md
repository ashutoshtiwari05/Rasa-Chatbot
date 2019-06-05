## Generated Story 5000720342611490606
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - slot{"location": "delhi"}
	- slot{"cuisine": "chinese"}
	- slot{"pricerange": ">700"}
    - utter_ask_email_address
* restaurant_search{"email": "siblingstrio@gmail.com"}
	- slot{"email": "siblingstrio@gmail.com"}
    - action_send_email
    - slot{"email": "siblingstrio@gmail.com"}
	- utter_respond_email_sent
	- utter_goodbye

## Generated Story -5674603577456429799
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - slot{"location": "delhi"}
    - utter_ask_email_address
* restaurant_search{"email": "siblingstrio@gmail.com"}
    - action_send_email
    - slot{"email": "siblingstrio@gmail.com"}
    - utter_respond_email_sent
    - utter_goodbye

## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "dumka"}
    - slot{"location": "dumka"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "udupi"}
    - slot{"location": "udupi"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "mizoram"}
    - slot{"location": "mizoram"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bangalore"}
	- action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_range
* restaurant_search{"pricerange": "300-700 range"}
    - slot{"pricerange": "300-700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - utter_ask_should_be_emailed
* restaurant_search{"email": "yes. Please send it to ahbcdj@gmail.com"}
    - slot{"email": "ahbcdj@gmail.com"}
	- action_send_email
    - slot{"email": "ahbcdj@gmail.com"}
    - utter_goodbye
	- export
	
## Generated Story 1212273218580989647
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - slot{"location": "Delhi"}
    - utter_ask_email_address
* restaurant_search{"email": "siblingstrio@gmail.com"}
    - slot{"email": "siblingstrio@gmail.com"}
    - action_send_email
    - slot{"email": "siblingstrio@gmail.com"}
    - utter_respond_email_sent
    - utter_goodbye

## Generated Story -4345413980550491731
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - slot{"location": "mumbai"}
    - utter_ask_should_be_emailed
* deny
    - utter_deny

## Generated Story -4890972850853876939
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - action_restaurant_inrange
    - slot{"location": "Chandigarh"}
    - utter_ask_email_address
* restaurant_search{"email": "siblingstrio@gmail.com"}
    - slot{"email": "siblingstrio@gmail.com"}
    - action_send_email
    - slot{"email": "siblingstrio@gmail.com"}
    - utter_goodbye
