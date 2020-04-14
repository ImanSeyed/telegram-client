#!/usr/bin/python3
#coding=utf-8

from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
from googletrans import Translator
import json
import time 

# User Authorization
app = Client("my_account")

with open("messages.json") as file:
    messages = file.read()

data = json.loads(messages)

# JSON messages 
def handler(command):
    @app.on_message(
            Filters.command(command, "!") &
            Filters.me
            )
    def do(client, message):
        client.edit_message_text(
            message.chat.id,
            message.message_id,
            data[command]
        )

# Making handler for all commands that depend on JSON file 
commands =  data.keys()
for command in commands:
    handler(command)

# Kick the member that repiled to 
@app.on_message(
        Filters.command("kick", "!") &
        Filters.me
        )
def kick(client, message):
    client.kick_chat_member(
            message.chat.id,
            message.reply_to_message.from_user.id
            )
    remove_message = "[{}](tg://user?id={}) **banned**.".format(
            message.reply_to_message.from_user.first_name,
            message.reply_to_message.from_user.id
            )
    client.edit_message_text(
            message.chat.id,
            message.message_id,
            remove_message
            )


# Spam <num> <text>
@app.on_message(
    Filters.command("spam", "!") &
    Filters.me
    )
def spam(client, message):
    try:
        for _ in range(int(message.command[1])):
            client.send_message(
                message.chat.id,
                ' '.join(message.command[2:])
            )
    except FloodWait as e:
        time.sleep(e.x)

# Check client is up or down (Ping/Pong)
@app.on_message(
        Filters.command("ping", "!") &
        Filters.me
        )
def ping(client, message):
    client.edit_message_text(
            message.chat.id,
            message.message_id,
            "**pong!**"
            )

# Let me google it for you
@app.on_message(
    Filters.command("g", "!") &
    Filters.me
    )
def google(client, message):
    text = message.command[1:]
    query_text = "http://google.com/search?q=" + '+'.join(text)
    edited_message = """Let me 🔎 Google that for you:
🔎 [{}]({})""".format(' '.join(text), query_text) 
    client.edit_message_text(
        message.chat.id,
        message.message_id,
        edited_message,
        disable_web_page_preview=True
    )

# Google translate
@app.on_message(
        Filters.command("translate", "!") &
        Filters.me
        )
def translate(client, message):
    translator = Translator()
    client.edit_message_text(
            message.chat.id,
            message.message_id,
            translator.translate(
                message.reply_to_message.text, 
                dest=message.command[1]).text,
            disable_web_page_preview=True
        )


@app.on_message(
        Filters.command("haxor", "!") &
        Filters.me
        )
def haxor(client, message):
    text = ' '.join(message.command[1:])
    current = ""
    for i in text:
        current = current + i
        client.edit_message_text(
                message.chat.id,
                message.message_id,
                current + "|"
                )
        time.sleep(0.2)
        
    client.edit_message_text(
            message.chat.id,
            message.message_id,
            text
            )

    
app.run()
