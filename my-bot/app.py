from flask import Flask, request
from telegram import Bot
import os

app = Flask(__name__)

# Replace with your Bot's API token
API_TOKEN = '7806770273:AAF6rXZhHXzBZlcTxESm7aUlqiDf3_X--EY'
bot = Bot(API_TOKEN)

# Root route for basic testing
@app.route('/')
def home():
    return 'Bot is running!'

# Webhook endpoint to receive messages
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if not data:
        return 'No data received', 400

    message = data.get('message')
    if message:
        chat_id = message['chat']['id']
        text = message.get('text', '')
        bot.send_message(chat_id=chat_id, text="Received your message: " + text)

    return '', 200

if __name__ == '__main__':
    # Use the Heroku-assigned port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
