import requests
import os
import sys

with open(os.path.expanduser('/etc/pocsagbot/KEY'), 'r') as f:
    TELEGRAM_TOKEN = f.read().strip()

with open(os.path.expanduser('/etc/pocsagbot/CHATID'), 'r') as f:
    TELEGRAM_CHATID = int(f.read().strip())


def send_message(id, message):
    result = requests.post(url=f"https://api.telegram.org/{TELEGRAM_TOKEN}/sendMessage", data={'chat_id': id, 'text': message})
    print(result.text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test.py <message>")
        sys.exit(1)
    msg = " ".join(sys.argv[1:])
    send_message(TELEGRAM_CHATID, msg)




