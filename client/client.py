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

# Commands of admin
def exec_admin_command(command):
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

# Making handler for all commands of admin
commands =  data.keys()
for command in commands:
    exec_admin_command(command)

# Spam
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

# Let me google it for you!
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


app.run()
