from pyrogram import Client, Filters
import sqlite3

# User Authorization
app = Client("my_account")

db_admin = sqlite3.connect("../database/admin.db", check_same_thread=False)

def get_command_text(conn, command):
    cursor = conn.cursor()
    query = cursor.execute('SELECT message FROM commands WHERE command IS "%s"' % command)
    for row in query:
        text = ' '.join(row)
    return text

# admin's Commands 
def exec_admin_command(conn, command):
    @app.on_message(
            Filters.command(command, "!") &
            Filters.me)
    def do(client, message):
        text = get_command_text(conn, command)
        app.send_message(
                message.chat.id, 
                text,
                reply_to_message_id=message.reply_to_message.message_id
                )

commands = db_admin.execute('SELECT command FROM commands')
for row in commands:
    exec_admin_command(db_admin, row[0])

app.run()
