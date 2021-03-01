from telegram import*
from telegram.ext import*

bot = Bot("1629687579:AAFyYRBZaWr72RseYdI8whThtmhLRJlsPVs")

print(bot.get_me())

updater = Updater(token="1629687579:AAFyYRBZaWr72RseYdI8whThtmhLRJlsPVs", use_context=True)

dispatcher = updater.dispatcher

def test_function(update:Update,context:CallbackContext):
	bot.send_message(
	chat_id = update.effective_chat.id,
	text = "https://y.music.163.com/m/song?id=1500426368"

start_value = CommandHandler("motion", test_function)

dispatcher.add_handler(start_value)

updater.start_polling()

# https://music.163.com/#/discover/recommend/taste
