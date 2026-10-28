import telebot

# Aapka naya API Token jo aapne diya hai
TOKEN = '9127499675:AAF909QEhuAqrF2GUpoQuTqGwtACPFjtLMo'
bot = telebot.TeleBot(TOKEN)

# Jab user link par click karke bot par aayega aur /start dabayega
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Yeh check karta hai ki user ne kis parameter ke sath click kiya hai
    command_arg = message.text.split()
    
    # Agar user ne 'series' parameter wale link par click kiya hai
    if len(command_arg) > 1 and command_arg[1] == 'series':
        bot.reply_to(message, "Bhai, aapka $100 to $500 series mein swagat hai! Details jaldi share ki jayengi.")
    else:
        bot.reply_to(message, "Hello! Series join karne ke liye diye gaye link par click karein.")

# Bot ko continuously run rakhne ke liye
print("Bot is running successfully...")
bot.infinity_polling()