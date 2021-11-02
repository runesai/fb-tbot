import os
import random
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)
PAGE_ACCESS_TOKEN = 'EAADX5ZB94LX8BAO3APdUVakmNyOirDXyBgH5GGGwdlc8ZBXg83pD1WcRgKeStefruw5v4P8hqcSUpcM3ZABm1ZAJxtDicwzNKMbli45QAoNlUrE5KlxR067LPNDC2LurX1RgpE4wnGYAuZAwCPebSYgs8U1Qxh7CYKZA9QqYr1yoRARSO782jhgzdgNu2XPzgZD' #os.environ['PAGE_ACCESS_TOKEN']
VERIFY_TOKEN = 'start_now' #os.environ['VERIFY_TOKEN']
bot = Bot(PAGE_ACCESS_TOKEN)

def process_message(text):
    formatted_message = text.lower()

    greetings = ["Hi!", "Oh hello there!", "Greetings!", "Hello iskolar!", "Good day!"]
    goodbye = ["Bye", "See you later!"]

    if formatted_message == "1" or formatted_message == "one" or formatted_message == "first" or formatted_message == "1st":
        response = f"{random.choice(greetings}"
    else:
        response = f"{random.choice(goodbye)}"
    return response

#We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['POST', 'GET'])

def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")

        else:
            return 'Bot not connected to Facebook.'

    elif request.method == "POST":
        payload = request.json
        event = payload['entry'][0]['messaging']

        for msg in event:
            text = msg['message']['text']
            sender_id = msg['sender']['id']

            response = process_message(text)
            bot.send_text_message(sender_id, response)

        return "Message received"

    else:
        return "200"


if __name__ == "__main__":
    app.run()
