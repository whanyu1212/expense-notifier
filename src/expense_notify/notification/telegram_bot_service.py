import requests


def send_telegram_message(token: str, chat_id: str, message: str):
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url).json()
    if response["ok"]:
        print("Message sent successfully")
    else:
        print("Failed to send message")
        print(response)
