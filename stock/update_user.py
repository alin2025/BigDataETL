import psycopg2
from telegram import Bot

TELEGRAM_BOT_TOKEN = "6883664205:AAFJTQyP6KpUt_beKkTBoldQbosgMKsZ8VY" #bot token
bot = Bot(token=TELEGRAM_BOT_TOKEN)

conn = psycopg2.connect(host='postgresql-container',port='5432',database='postgres',user='postgres',password='NayaPass123!')
cursor = conn.cursor()

def send_stock_info_to_subscribers():
        #user_id and last action for each user
    cursor.execute("""SELECT user_id, action  FROM user_actions WHERE timestamp = (
                SELECT MAX(timestamp) FROM user_actions AS ua WHERE user_actions.user_id = ua.user_id )""")
    rows = cursor.fetchall()

    for row in rows:
       user_id, last_action = row
       if last_action == 'subscribe':
        cursor.execute(""" SELECT * FROM stocks_data LIMIT 1 """) #get the line from the stocks_info table
        stock_row = cursor.fetchone()

        if stock_row:
            pre_massege="hellow friend!!! remmeber me :)?"
            stock_info = f"grait revenue on Stock: {stock_row[0]}\n run to: {stock_row[9]}\non price: {stock_row[12]}"
            bot.send_message(chat_id=user_id, text=pre_massege)
            bot.send_message(chat_id=user_id, text=stock_info)# Send to user via bot
            print("info sent to user:", user_id)

# run the function
send_stock_info_to_subscribers()
cursor.close()
conn.close()