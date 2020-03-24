from pyrogram import Client, Filters
from pyrogram.errors import FloodWait
import json
import time 


# User Authorization
app = Client("my_account")

with open("messages.json") as file:
    messages = file.read()

data = json.loads(messages)

# admin's Commands 
def exec_admin_command(command):
    @app.on_message(
            Filters.command(command, "!") &
            Filters.me)
    def do(client, message):
        app.edit_message_text(
            message.chat.id,
            message.message_id,
            data[command]
        )

# Spam
@app.on_message(
    Filters.command("spam", "!") &
    Filters.me)
def spam(client, message):
    try:
        for _ in range(int(message.command[1])):
            app.send_message(
                message.chat.id,
                ' '.join(message.command[2:])
            )
    except FloodWait as e:
        time.sleep(e.x)

# Let me google it for you!
@app.on_message(
    Filters.command("g", "!") &
    Filters.me)
def google(client, message):
    text = message.command[1:]
    google_it = "http://google.com/search?q=" + '+'.join(text)
    edited_message = """Let me 🔎 Google that for you:
🔎[{}]({})""".format(' '.join(text), google_it) 
    app.edit_message_text(
        message.chat.id,
        message.message_id,
        edited_message,
        disable_web_page_preview=True
    )

commands =  data.keys()
for command in commands:
    exec_admin_command(command)

app.run()