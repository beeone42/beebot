import sys
import time
import pprint
import telepot
import json

def read_config(confname):
    with open(confname) as json_data_file:
        data = json.load(json_data_file)
        return (data)

def handle(msg):
    pprint.pprint(msg)
    # Do your stuff here ...

    flavor = telepot.flavor(msg)

    # normal message
    if flavor == 'normal':
        content_type, chat_type, chat_id = telepot.glance(msg)
        print 'Normal Message:', content_type, chat_type, chat_id

        # Do your stuff according to `content_type` ...
        if content_type == 'text':
            if msg['text'] == 'ping':
                bot.sendMessage(chat_id, 'pong')


config = read_config("config.json")
TOKEN = config['token']

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
