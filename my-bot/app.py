from flask import Flask, request
from telegram import Bot
import os

app = Flask(__name__)

# Replace with your Bot's API token
API_TOKEN = '7806770273:AAF6rXZhHXzBZlcTxESm7aUlqiDf3_X--EY'
bot = Bot(API_TOKEN)

# Root route for testing
@app.route('/')
def home():
    return 'Bot is running!'

# Webhook endpoint to receive messages
@app.route('/webhook', methods=['POST'])  # Ensure it accepts POST requests
# Example: Correct way to call an async method
@app.route('/webhook', methods=['POST'])
async def webhook():
    # Parse the incoming request (assuming JSON payload)
    data = request.get_json()
    chat_id = data.get('chat_id')
    text = data.get('text')

    # Send a message using the bot (await is required)
    await bot.send_message(chat_id=chat_id, text=f"Received your message: {text}")

    return "OK", 200

if __name__ == '__main__':
    # Use the port assigned by Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
