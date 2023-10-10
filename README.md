# temperatureAlertAgent
For local testing you need to follow to following steps
* Replace the constants in constants.py with your api key, Twilio account id, Auth token and mobile number
* To get the open weather api key login/signup at 'https://openweathermap.org/' and get the api key from your account
* To get Twilio Account id, Auth token and mobile number login/signUp at 'https://www.twilio.com/en-us' and get the details in your account console
* Remember to use the sender as the mobile number present in twilio account
* Then run the following commands:
```
cd src
poetry intall
poetry run python main.py
```