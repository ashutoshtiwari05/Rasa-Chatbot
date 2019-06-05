## Generated Story -6346758080366131614
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": "rishikesh"}
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_validate_location
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - utter_ask_should_be_emailed
* restaurant_search
    - utter_ask_email_address
* restaurant_search{"email": "rupahr39@gmail.com"}
    - slot{"email": "rupahr39@gmail.com"}
    - action_send_email
    - slot{"location": "senthilnathan.shanmugam066@gmail.com"}
    - utter_goodbye
    - export

## Generated Story -8308233090305143727
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_range
* restaurant_search{"pricerange": ">700"}
    - slot{"pricerange": ">700"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - utter_ask_should_be_emailed
* restaurant_search
    - utter_goodbye
    - export

## Generated Story -5447857127357300183
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chandigarh"}
    - action_validate_location
    - slot{"location": "Chandigarh"}
    - utter_ask_range
* restaurant_search{"pricerange": "<300"}
    - slot{"pricerange": "<300"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - utter_ask_should_be_emailed
* restaurant_search
    - utter_goodbye
    - export

## Generated Story -5378880649279427274
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_validate_location
    - slot{"location": "mubaim"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_validate_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_range
* restaurant_search{"pricerange": "<300"}
    - slot{"pricerange": "<300"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - utter_ask_should_be_emailed
* restaurant_search
    - utter_ask_email_address
* restaurant_search{"email": "senthilnathan.shanmugam066@gmail.com"}
    - slot{"email": "senthilnathan.shanmugam066@gmail.com"}
    - action_send_email
    - slot{"location": "senthilnathan.shanmugam066@gmail.com"}
    - utter_goodbye
    - export

## Generated Story 990274456701545242
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_range
* restaurant_search{"pricerange": "<300"}
    - slot{"pricerange": "<300"}
    - utter_response_restaurant_list
    - action_restaurant_inrange
    - utter_ask_should_be_emailed
* restaurant_search
    - utter_ask_email_address
* restaurant_search
    - action_send_email
    - slot{"location": null}
    - utter_goodbye
    - export

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
