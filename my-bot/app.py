from flask import Flask, request
from telegram import Bot

app = Flask(__name__)

# Replace with your Bot's API token
API_TOKEN = '7806770273:AAF6rXZhHXzBZlcTxESm7aUlqiDf3_X--EY'
bot = Bot(API_TOKEN)

# Webhook endpoint to receive messages
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    # Check if the message is in the incoming data
    if 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message['text']

        # Here, you can forward the message to another bot or process the message
        bot.send_message(chat_id=chat_id, text="Received your message: " + text)

    return '', 200

if __name__ == '__main__':
    # Run the Flask server
    app.run(port=5000)
