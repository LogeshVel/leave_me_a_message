import requests
import os


def send_msg(msg):
    if os.environ.get("BOT_TOKEN") and os.environ.get("TELEGRAM_CHAT_ID"):
        bot_msg_snd_url = "https://api.telegram.org/bot{BOT_Token}/sendMessage".format(BOT_Token=os.environ.get("BOT_TOKEN"))
        params = {"chat_id": os.environ.get("TELEGRAM_CHAT_ID"), "text": str(msg)}
        resp = requests.get(bot_msg_snd_url, data=params)
        if resp.json()["ok"]:
            print("Successfully sent the msg")
            print(msg)
        else:
            print("Failed to sent the msg")
            print(msg)
    else:
        print("Not all required env var is set")
          