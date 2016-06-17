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
            m = msg['text'].split()
            if m[0] == 'ping':
                bot.sendMessage(chat_id, 'pong')
            if m[0] == 'pic':
                if (config['pics'].has_key(m[1])):
                    bot.sendPhoto(chat_id, config['pics'][m[1]])
                else:
                    bot.sendMessage(chat_id, 'unknown pic')
            if m[0] == 'file':
                if (config['files'].has_key(m[1])):
                    bot.sendDocument(chat_id, config['files'][m[1]])
                else:
                    bot.sendMessage(chat_id, 'unknown file')


config = read_config("config.json")
TOKEN = config['token']

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
