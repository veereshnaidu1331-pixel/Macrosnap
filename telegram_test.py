import requests

BOT_TOKEN = "8851499628:AAHY_MT5OF1kskI9WhhPSGByVBaX5HnuN_Y"

data = requests.get(
    f"https://api.telegram.org/bot8851499628:AAHY_MT5OF1kskI9WhhPSGByVBaX5HnuN_Y/getUpdates"
).json()

for update in data["result"]:
    message = update.get("message", {})
    chat = message.get("chat", {})

    print("Chat ID:", chat.get("id"))
    print("Message:", message.get("text"))