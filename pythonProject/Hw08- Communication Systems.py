"""
Project name: Hw08- Communication-Systems.py
Description: A program that tells you the weather and temperature of a given place based on the zipcode and texts you
Name: Samuel Rabinor
Date:
"""

# import twilio
from twilio.rest import Client
import urllib.request
import json
import ssl
import logging
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(level=logging.DEBUG, filename='debug3.log')


class Communication:
    """
    A class containing info on communication
    """
    def __init__(self):
        self.temp = ""
        self.weather = ""
        self.city = ""

    def get_weather(self, zipcode):
        """
        Requests the weather data from a weathermap api and prints out the city, temp and weather that corresponds to the zipcode
        :param zipcode: The zipcode of the place you want the info for
        :return: The city, temperature and weather of the given zipcodes city
        """
        url = "https://api.openweathermap.org/data/2.5/weather?zip=10128&APPID=e4aa8534106fa684b5c95fcaf6e566b7"

        f = urllib.request.urlopen(url)  # request the URL from openweathermap
        json_string = f.read()  # read the data returned into a string variable
        print('json_string: {}'.format(json_string))

        parsed_json = json.loads(json_string)  # convert the string to a json object

        self.city = parsed_json['name']
        self.temp = parsed_json['main']['temp']
        self.weather = parsed_json['weather'][0]['description']

        message = "Current temperature in {} is: {} Kelvin, and the weather is {}.".format(self.city, self.temp, self.weather)

        f.close()  # close the URL request
        print(message)
        logging.debug('Obtaining and printing out city, temperature in kelvin and weather from weathermap api based on zipcode...')
        return message

    def send_sms(self, phone_number, message):
        """
        Texts a given message to the given phone number
        :param phone_number: The phone number that should be texted to
        :param message: The message to send the number
        :return: nothing
        """
        # My Account Sid and Authorization Token from twilio.com/user/account
        account_sid = "ACf56fa67b44f22cb04e464b73b0ac4f78"
        auth_token = "104c2679df48bd6a6f7a577e52361531"

        client = Client(account_sid, auth_token)  # Create an client object

        try:
            client.api.account.messages.create(
                body=message,  # Replace with a string containing the message
                to=phone_number,  # My real cell phone number
                from_="+17203367612"  # My Twilio number
            )
        except:
            print("There was an error sending your message")
        logging.debug('Sending unspecified message to an unspecified phone number (specified when function is called)...')

    def create_message(self):
        """
        Prints a clothing recommendation based on the weather and temperature
        :return: The clothing recommendation
        """
        if 'rain' in com.weather:
            print("User, you should wear a rain coat!")
        elif com.temp < '283' and com.weather == 'sunny' or 'clear':
            print("User, you should wear a warm coat!")
        logging.debug('Printing out clothing recommendation based on weather and temperature...')

    def kelvin_to_celsius(self):
        url = "https://api.openweathermap.org/data/2.5/weather?zip=10128&APPID=e4aa8534106fa684b5c95fcaf6e566b7"

        f = urllib.request.urlopen(url)  # request the URL from openweathermap
        json_string = f.read()  # read the data returned into a string variable

        parsed_json = json.loads(json_string)  # convert the string to a json object

        temp = parsed_json['main']['temp']

        tempc = round(temp - 273.15, 2)
        return "Celsius = {}° C".format(tempc)


if __name__ == "__main__":
    com = Communication()
    com.send_sms("9175887133", "Hello")   # Number and message to send to specified number
    forecast = com.get_weather("10128")   # zip code to find data of
    com.send_sms("9175887133", forecast)  # send forecast to specified number
    celsius = com.kelvin_to_celsius()
    com.send_sms("9175887133", celsius)
