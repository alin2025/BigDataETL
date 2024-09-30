#pip install python-telegram-bot==13.7

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from kafka import KafkaProducer
import logging
from datetime import datetime
import json
# Enable logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Kafka configuration
KAFKA_SERVER = 'Cnt7-naya-cdh63:9092'
KAFKA_TOPIC = 'stock'

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


# Define start command handler
def start(update, context):
    update.message.reply_text(
        "Hello! Welcome to the Telegram Bot. Type /subscribe to receive updates or /unsubscribe to stop receiving updates.")


# Define subscribe command handler
def subscribe(update, context):
    # Capture user details
    user_id = update.message.chat_id
    user_name = context.user_data.get("username")
    user_action = "subscribe"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log user details
    logger.info("User ID: %s, Name: %s, Action: %s, Timestamp: %s", user_id, user_name, user_action, timestamp)
    user_info = {"user_id": user_id, "Name": user_name, "action": user_action, "timestamp": timestamp, "subscribe": 1}
    user_info_json = json.dumps(user_info)

    producer.send(KAFKA_TOPIC, user_info_json.encode('utf-8'))
    print(user_info_json)
    # Reply to user
    update.message.reply_text("Thank you for subscribing! You will receive updates.")


# Define unsubscribe command handler
def unsubscribe(update, context):
    # Capture user details
    user_id = update.message.chat_id
    user_name = context.user_data.get("username")
    user_action = "unsubscribe"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log user details
    logger.info("User ID: %s, Name: %s, Action: %s, Timestamp: %s", user_id, user_name, user_action, timestamp)
    user_info = {"user_id": user_id, "Name": user_name, "action": user_action, "timestamp": timestamp, "subscribe": 0}
    user_info_json = json.dumps(user_info)

    producer.send(KAFKA_TOPIC, user_info_json.encode('utf-8'))
    print(user_info_json)

    # Reply to user
    update.message.reply_text("You have unsubscribed. You will no longer receive updates.")


def main():
    # Set up the updater and dispatcher
    updater = Updater("6883664205:AAFJTQyP6KpUt_beKkTBoldQbosgMKsZ8VY", use_context=True)
    dp = updater.dispatcher

    # Add handlers for commands and messages
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # Start the bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()