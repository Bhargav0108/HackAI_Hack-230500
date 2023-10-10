# temperatureAlertAgent
Project Name: Temperature Alert Agent
Description of the Project:
* Agent on startup will ask the user for the location to which it needs to get the temperature data
* It then prompts the user to set the threshold of temperature
* Then ask the mobile number to send the notification to the user (if not provided user will not receive any notification)
* Then the agent will collect the temperature details at a particular location periodically every 20 seconds and if the temperature crosses the threshold it notifies the user (with an interval gap of 1 hour).

For local testing, you need to follow to following steps
* Replace the constants in constants.py with your API key, Twilio account ID, Auth token, and mobile number
* To get the open weather API key login/sign in at 'https://openweathermap.org/' and get the API key from your account
* To get your Twilio account ID, Auth token, and mobile number log in/sign in at 'https://www.twilio.com/en-us' and get the details in your account console
* Remember to use the sender as the mobile number present in the Twilio account
* Then run the following commands to test locally:
```
cd src
poetry install
poetry run python main.py
```
