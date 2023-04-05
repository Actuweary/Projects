# DSC 510
# Week 10
# Programming Assignment Week 10.1
# Author Michael Ersevim
# 8/12/2021

'''Purpose of code is to use and API request to retreive the weather forecast for a user
and present it in a nice looking format, then ask if they'd like to see another forecast
'''

import json #Needed to parse JSON data
import requests #gets data from a URL using API

def get_weather_city(): #the JSON weather generator
    input_city = input("Please enter the city name: ") #gets city loc and...
    input_state = input("Please enter the state abbreviation: ") #gets state loc
    input_temp = input("Would you like to view temps in Fahrenheit, Celsius, or Kelvin? \n Enter 'F' for "
                       "Fahrenheit, 'C' for Celsius, 'K' for Kelvin: ")#gets pref
    if input_temp == 'K' or input_temp == 'k': #tests for temp units and submits correct code for those units
        url = f'http://api.openweathermap.org/data/2.5/weather?q={input_city},{input_state},' \
                     f'us&appid=4beb051f720dbfe14568322d1bff5b5c'
    elif input_temp == 'F' or input_temp == 'f': #tests for temp units and submits correct code for those units
        url = f'http://api.openweathermap.org/data/2.5/weather?q={input_city},{input_state},' \
                  f'us&units=imperial&appid=4beb051f720dbfe14568322d1bff5b5c'
    elif input_temp == 'C' or input_temp == 'c': #tests for temp units and submits correct code for those units
        url = f'http://api.openweathermap.org/data/2.5/weather?q={input_city},{input_state},' \
                  f'us&units=metric&appid=4beb051f720dbfe14568322d1bff5b5c'
    else:
        print("Please enter F, C, or K") #if no F, Cor K, asks again for a valid input
        input_temp = input("Would you like to view temps in Fahrenheit, Celsius, or "
                           "Kelvin? \nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: ")
    print_nicely(url,input_temp) #calls the display function

def get_weather_zip():  # the JSON weather generator
    input_zip = input("Please enter the five digit zip code: ") #get zipcode
    if len(input_zip) != 5:
        print("Zip code must be 5 digits long!")
        get_weather_zip()
    else:
        input_temp = input("Would you like to view temps in Fahrenheit, Celsius, or Kelvin? \nEnter 'F' "
                       "for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: ")
        if input_temp == 'K' or input_temp == 'k': #tests for temp units and submits correct code for those units
            url = f'http://api.openweathermap.org/data/2.5/weather?zip={input_zip},' \
                      f'us&appid=4beb051f720dbfe14568322d1bff5b5c'
        elif input_temp == 'F' or input_temp == 'f': #tests for temp units and submits correct code for those units
            url = f'http://api.openweathermap.org/data/2.5/weather?zip={input_zip},' \
                      f'us&units=imperial&appid=4beb051f720dbfe14568322d1bff5b5c'
        elif input_temp == 'C' or input_temp == 'c': #tests for temp units and submits correct code for those units
            url = f'http://api.openweathermap.org/data/2.5/weather?zip={input_zip},' \
                      f'us&units=metric&appid=4beb051f720dbfe14568322d1bff5b5c'
        else: #loops back if invalid input
            print("Please enter F, C, or K")
            input_temp = input("Would you like to view temps in Fahrenheit, Celsius, or "
                           "Kelvin? \nEnter 'F' for Fahrenheit, 'C' for Celsius, 'K' for Kelvin: ")
        print_nicely(url,input_temp) #calls the display function

def print_nicely(url,input_temp):
    try:
        json_file = requests.get(url)   #uses GET and assigns to var
        json_object = json.loads(json_file.text)  # JSON parser
        #json_formated_str = json.dumps(json_object, indent=2)  # dump string file - used in development
        print("")  # prints a blank line for a less cluttered look
        print("Current weather conditions for",json_object["name"]) #sets up the title header for the report
    except:
        print("Your location entry is invalid. Please try again.") # if connection already good, loc most likely invalid
        try_another()
    print("Current Temp:",json_object["main"]["temp"],"degrees",input_temp.upper()) # temp
    print("High Temp:",json_object["main"]["temp_max"],"degrees",input_temp.upper()) # hi temp
    print("Low Temp:",json_object["main"]["temp_min"],"degrees",input_temp.upper()) #and low temp
    print("Pressure:",json_object["main"]["pressure"],"hPa",sep="") # atmospheric pressure
    print("Humidity:",json_object["main"]["humidity"],"%",sep="") # relative humidity
    print("Clouds:",json_object["weather"][0]["description"]) #weather description
    print("") # looks less cluttered with space before next question to continue...
    try_another()

def try_another():
    go_again = input(
        "Would you like to lookup the weather for another area? (Y/N): ")  # gets user input to do another or not
    if go_again == 'Y' or go_again == 'y': # allows upper or lower cases
        main()  # decision tree calls appropriate function
    elif go_again == 'N' or go_again == 'n':
        print("")
        print("Thank you for using my weather lookup tool! Goodbye!")  # goodbye message if 'no'
    else:
        print("Please make a valid selection! (Enter 'Y' or 'N')")  # checks for error input
        try_another()  # asks again if error

def test_connection(): #ensures that a test url returns a clean code (200)
    url_test = 'http://api.openweathermap.org/data/2.5/weather?zip=06033,us&units=metric&appid=4beb051f720dbfe14568322d1bff5b5c' #A test connection
    try:
        json_file = requests.get(url_test)   #uses GET and assigns to var
        json_object = json.loads(json_file.text)  # JSON parser
        if json_object["cod"] == 200:  # if '200', no problem with server
            print("")  # prints a blank line for a less cluttered look
            print("Welcome to Weather Lookup! Your connection to the weather server is established!") #confirms if good connection
            print("")  # prints a blank line for a less cluttered look
    except:
        print("Your connection or weather server is experiencing difficutlies. Please try again later.")
        quit()

def main(): #the main input/response handler
    input_choose = input("Would you like to lookup weather data by U.S. City or zip code? Enter '1' for U.S. City, or '2' for zip: ") #gets user input
    if input_choose == '1':
        get_weather_city() #decision tree calls appropriate function
    elif input_choose == '2':
        get_weather_zip() #decision tree calls appropriate function
    else:
        print("Please make a valid selection! (Enter 1 or 2)") #checks for error input
        main() #asks again if error

test_connection()

if __name__ == "__main__": #good practice to use this setup
    main()