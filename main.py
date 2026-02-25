import telebot
import requests
import os

# هذا السطر يسحب التوكن من إعدادات الموقع اللي بنشغل فيه البوت
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "هلا سالم! البوت شغال الآن من GitHub. أرسل الرابط!")

@bot.message_handler(func=lambda m: True)
def download(message):
    url = message.text
    if "tiktok.com" in url:
        bot.send_message(message.chat.id, "جاري التحميل... 🚀")
        try:
            res = requests.get(f"https://www.tikwm.com/api/?url={url}").json()
            video_url = res['data']['play']
            bot.send_video(message.chat.id, video_url, caption="تم التحميل ✅")
        except:
            bot.send_message(message.chat.id, "المعذرة، الرابط فيه مشكلة.")
    else:
        bot.send_message(message.chat.id, "أرسل رابط تيك توك.")

bot.infinity_polling()
