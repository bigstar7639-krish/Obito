import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Render la Environment Variable ah add pannanum
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "obito123")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

# Simple AI reply logic - Obito style
def get_ai_reply(user_msg):
    user_msg = user_msg.lower()
    if "hi" in user_msg or "hello" in user_msg or "da" in user_msg:
        return "Yo! I'm Obito da! 🔥 Enna da scene? Epdi irukka?"
    elif "love" in user_msg:
        return "Love uh? Rin pathi sollriya da? 🥺"
    elif "who are you" in user_msg:
        return "Naan Obito da! Uchiha Obito! Madara voda student! 😎"
    else:
        return f"Obito here da! Nee sonna: '{user_msg}' - Adhukku enna artham da? Sollu!"

@app.route("/")
def home():
    return "Obito Whatsapp Bot Running da! 🔥"

# Whatsapp verification ku
@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed da!", 403

# Message varum pothu
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    try:
        message = data['entry'][0]['changes'][0]['value']['messages'][0]
        from_number = message['from']
        msg_body = message['text']['body']

        reply = get_ai_reply(msg_body)

        # Reply anuppurathu
        url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": from_number,
            "text": {"body": reply}
        }
        requests.post(url, headers=headers, json=payload)
    except:
        pass
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
