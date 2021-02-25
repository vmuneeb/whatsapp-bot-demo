from flask import Flask, request
import sqlite3
from dotenv import load_dotenv
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    phone = request.values.get('WaId')
    name = request.values.get('ProfileName')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'menu' in incoming_msg:
        conn = get_db_connection()
        menu_items = conn.execute('select id, item_name, image_url from menu').fetchall()
        message = "Hi "+name+", todays menu \n"
        for item in menu_items:
            message = message +str(item['id'])+" "+ item['item_name']+" \n"
        message = message + " Please select your choice" 
        msg.body(message)
        msg.media("https://i.imgur.com/jG0KQx5.png")
        conn.close()
        responded = True
    if 'selection' in incoming_msg:
        conn = get_db_connection()
        menu_items = conn.execute('select menu.item_name, menu.image_url, user.id,user_selection.menu_id from user, user_selection, menu where user.phone='+phone+' and user_selection.user_id=user.id and menu.id=user_selection.menu_id').fetchall()
        if menu_items:
            message = "Your selection is "+menu_items[0]['item_name']
            menu_image = menu_items[0]['image_url']
            msg.body(message)
            if menu_image:
                msg.media(menu_image)
        else:
            msg.body("Please choose a dish from the menu.")
            msg.media("https://i.imgur.com/jG0KQx5.png")
        conn.close()
        responded = True

    if 'choose' in incoming_msg:
        conn = get_db_connection()
        item_id = incoming_msg.split(' ')[1]
        conn.execute('INSERT OR REPLACE INTO user(phone) values (?)', [int(phone)])
        conn.execute('INSERT OR REPLACE INTO user_selection (user_id, menu_id) select id as user_id, '+item_id+' as menu_id from user where phone='+phone+'')
        menu_items = conn.execute('select menu.item_name, menu.image_url, user.id,user_selection.menu_id from user, user_selection, menu where phone='+phone+' and user_selection.user_id=user.id and menu.id=user_selection.menu_id').fetchall()
        message = 'Congrats '+name+"!!\n You have selected \n"+menu_items[0]['item_name']+" for your meal."
        menu_image = menu_items[0]['image_url']
        msg.body(message)
        if menu_image:
            msg.media(menu_image)
        conn.commit()
        conn.close()
        responded = True

    if not responded:
        msg.body('Hi '+name+' please choose \n 1. menu to see menu \n 2. selection to see your selection \n 3. choose to select item.')
    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
