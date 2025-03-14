import requests
import time
import random
import os
from flask import Flask

app = Flask(__name__)

# Get webhook URLs from Render environment variables
WEBHOOKS = [
    os.getenv("WEBHOOK1"),
    os.getenv("WEBHOOK2"),
    os.getenv("WEBHOOK3"),
    os.getenv("WEBHOOK4"),
    os.getenv("WEBHOOK5")
]

# Messages to send
MESSAGES = [
    "**🔥 W H A T ' S   Y O U R   F A V O R I T E   P O K É M O N ? 🔥**",
    "__⚡ W H O O O ' S   S T R O N G E R R R :   P I K A C H U U U U   O R   C H A R I Z A R D D D ? ⚡__",
    "**💎 I   H O P E   A   R A R E E E E   P O K É M O N   S P A W N S   S O O O O N ! 💎**",
    "__🎯 G U E S S S S   T H E   N E X T   P O K É M O N   T O   A P P E A R R R ! 🎯__",
    "**🌀 A N Y O N E   L U C K Y   E N O U G H   T O   F I N D   A   S H I N Y ? ✨**",
]

def send_message():
    webhook = random.choice(WEBHOOKS)
    message = random.choice(MESSAGES)
    if webhook:
        requests.post(webhook, json={"content": message})
        print(f"✅ Sent message: {message}")
    else:
        print("⚠️ Webhook URL missing!")

# Keep sending messages in the background
def start_spamming():
    while True:
        send_message()
        time.sleep(random.randint(20, 60))  # Random wait time

# Run Flask server
@app.route('/')
def home():
    return "✅ Webhook bot is running!"

if __name__ == "__main__":
    from threading import Thread
    spam_thread = Thread(target=start_spamming)
    spam_thread.start()

    port = int(os.getenv("PORT", 8080))  # Get port from environment variables
    app.run(host="0.0.0.0", port=port)
