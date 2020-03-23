from pyrogram import Client, Filters
import json

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


commands =  data.keys()
for command in commands:
    exec_admin_command(command)

app.run()