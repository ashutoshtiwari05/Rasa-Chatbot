from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib 
import zomatopy
import json
import sys
Restaurant_data = ''

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b48450bc56c13d370c756085aa379597"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
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

class ActionSearchRestInRange(Action):
	def name(self):
		return 'action_restaurant_inrange'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b48450bc56c13d370c756085aa379597"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		priceRangeForTwo = tracker.get_slot('pricerange')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""	
		restaurants = []
		restaurantsInRange = []
		try:
			if d['results_found'] == 0:
				response= "no results"
			else:
				for restaurant in d['restaurants']:
					restaurantObj = Restaurant()
					restaurantObj.name = restaurant['restaurant']['name']
					restaurantObj.address =  restaurant['restaurant']['location']['address']
					restaurantObj.pricerange = restaurant['restaurant']['average_cost_for_two']
					restaurantObj.rating = restaurant['restaurant']['user_rating']['aggregate_rating']
					restaurants.append(restaurantObj)
		
			if len(restaurants) > 0 :
				if priceRangeForTwo == 1 or priceRangeForTwo == '<300':
					restaurantsInRange = [restaurant for restaurant in restaurants if restaurant.pricerange >= 0 and restaurant.pricerange < 300]
				elif priceRangeForTwo == 2 or priceRangeForTwo == '300-700' :
					restaurantsInRange = [restaurant for restaurant in restaurants if restaurant.pricerange >= 300 and restaurant.pricerange < 700]
				elif priceRangeForTwo == 3 or priceRangeForTwo == '>700' :
					restaurantsInRange = [restaurant for restaurant in restaurants if restaurant.pricerange >= 700]
				else :
					restaurantsInRange = restaurants
			
				sorted(restaurantsInRange, key=lambda restaurant: restaurant.rating,reverse=True)
				Top5RestaurantsInRange = restaurantsInRange[:5]
				
				for restaurant in Top5RestaurantsInRange :
					response=response+ "Restaurant "+ restaurant.name + " in Area :"+ restaurant.address + " with top ratings : "+ restaurant.rating + " and the average price range for two people here is : " + str(restaurant.pricerange) + " Rs." + "\n"
			else:
				response= "No data found. Please try again"
			
			global Restaurant_data
			Restaurant_data = response
			
			dispatcher.utter_message(response)
		except :
			print("Unexpected error:", sys.exc_info()[0])
			raise
		
		return [SlotSet('location',loc)]


class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b48450bc56c13d370c756085aa379597"}
		zomato = zomatopy.initialize_app(config)
		toemailaddress = tracker.get_slot('email')
		response ='email logic starts here'
		try:
		  msg = MIMEMultipart()
		  msg['From'] = "appfoodie822@gmail.com"
		  msg['To']= str(toemailaddress)
		  msg['Subject'] = 'Foodie - Resturant Search'
		  body = 'Please find resturants below:\n'+ Restaurant_data
		  msg.attach(MIMEText(body,'plain'))
		  text = msg.as_string()
		  server = smtplib.SMTP('smtp.gmail.com',587)
		  server.ehlo()
		  server.starttls()
		  server.login(msg['From'], "samplepassword")
		  server.sendmail(msg['From'],toemailaddress,text)
		  server.quit()
		  response="Email sent successfully"
		except Exception as error:
  		  response="Unable to send email due to exception" + str(error)
		  #print('Caught this error: ' + error))
		  #raise
		  
		response = response + str(toemailaddress)
		dispatcher.utter_message(response)
		return [SlotSet('email',toemailaddress)]

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b48450bc56c13d370c756085aa379597"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		tier1Location  = ['Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai']
		tier2Location = ['Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad','Ahmedabad','Bareilly', 'Belgaum','Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bokaro Steel City', 'Chandigarh','Coimbatore','nagpur', 'Cuttack', 'Dehradun', 'Dhanbad', 'Durg-Bhilai Nagar', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad','Gorakhpur', 'Gulbarga', 'Guntur','Gwalior', 'Gurgaon', 'Guwahati', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kottayam', 'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Prayagraj', 'Pune','Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']
		tier1LocationFinalList = map(lambda x:x.lower(),tier1Location)
		tier2LocationFinalList = map(lambda x:x.lower(),tier2Location)
		
		response=""	
		#response = loc
		## validation city..
		if loc is None :
			response= response + " Sorry, we don't operate in this city. Can you please specify some other location"
		elif loc.lower() not in tier1LocationFinalList and loc.lower() not in tier2LocationFinalList :
			response= response + " Sorry, we don't operate in this city. Can you please specify some other location"
		else :
			response = loc
			return [SlotSet('location',loc)]
			
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"b48450bc56c13d370c756085aa379597"}
		zomato = zomatopy.initialize_app(config)
		cuisine = tracker.get_slot('cuisine')
		cuisineList  = ['chinese', 'italian', 'south indian', 'north indian', 'american', 'mexican', 'thai']
		cuisineFinalList = map(str.lower,cuisineList)
		response=""	
		response = response + cuisine
		if cuisine.lower() not in cuisineFinalList :
			response= response + "Sorry, we don't have any restaurant in this cuisine"
		else :
			response = cuisine
			return [SlotSet('cuisine',cuisine)]
			
		dispatcher.utter_message(response)
		return [SlotSet('cuisine',cuisine)]
		
class Restaurant(object) :
	name = ''
	address = ''
	pricerange = ''
	rating = ''