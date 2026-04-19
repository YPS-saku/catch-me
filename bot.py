import telebot

# BotFather ගෙන් ලැබුණු Token එක මෙතනට දාන්න
API_TOKEN = '8605655449:AAHAJaIqQ4r_UV8EzZCUxDMj3JUTrt1hbXs'

# @userinfobot එකෙන් ගත්තු ඔබේ ID එක මෙතනට දාන්න
MY_CHAT_ID = '1943478263'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True, content_types=['text', 'photo', 'document', 'video', 'audio'])
def handle_messages(message):
    try:
        # පණිවිඩය එවූ පුද්ගලයාගේ විස්තර
        info = f"📩 පණිවිඩයක් ලැබුණා!\n👤 සිට: {message.from_user.first_name}\n🆔 ID: {message.from_user.id}"
        
        # විස්තරය ඔබට එවයි
        bot.send_message(MY_CHAT_ID, info)
        
        # පණිවිඩය ඔබට Forward කරයි
        bot.forward_message(MY_CHAT_ID, message.chat.id, message.message_id)
        
        # එවූ පුද්ගලයාට පිළිතුරක් යවයි
        bot.reply_to(message, "ඔබේ පණිවිඩය මගේ හිමිකරුට ලැබුණා. ස්තූතියි!")
    except Exception as e:
        print(f"Error: {e}")

print("Bot is starting...")
bot.infinity_polling()
