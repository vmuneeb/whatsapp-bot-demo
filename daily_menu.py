import os
import sqlite3
from dotenv import load_dotenv
from twilio.rest import Client


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

load_dotenv('.env')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


conn = get_db_connection()
phone_numbers = conn.execute('select phone from user').fetchall()
for row in phone_numbers:
    message = client.messages \
    .create(
         media_url=['https://i.imgur.com/oIsdpYm.png'],
         from_='whatsapp:+14155238886',
         body="Please select your choice from todays menu.",
         to='whatsapp:+'+str(row['phone'])
     )
    print(message.sid)
