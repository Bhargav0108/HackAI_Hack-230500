from twilio.rest import Client
from messages.constants import TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN, MOBILE_NUMBER


def send_notification(recipient_phoneNumber, temperature):
    ACCOUNT_SID = TWILIO_ACCOUNT_ID
    AUTH_TOKEN = TWILIO_AUTH_TOKEN
    FROM_NUMBER = MOBILE_NUMBER
    TO_NUMBER = recipient_phoneNumber

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body= f"Current temperature is {temperature}C which is not within set threshold.",
        from_=FROM_NUMBER,
        to=TO_NUMBER,
    )

    if message.sid:
        print("SMS message sent successfully!")
    else:
        print("Error sending SMS message:", message.error_message)
