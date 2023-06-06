import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update
from dotenv import load_dotenv
from services.integrate import download_file
from services.handler import handle_response
load_dotenv()


BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_USERNAME = os.environ.get('USER_NAME')

# Commands
async def start_command(update : Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'user {update.message.chat_id} as joined.')
    await update.message.reply_text('Hello, Thankyou for subscribing to me.')

async def help_command(update : Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a downloder bot plese send any link which you need to download.')

async def custom_command(update : Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command.')

# Responses
async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'user {update.message.chat_id} in {message_type}: {text}')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return
    elif 'http' in text:
        response = download_file(text)
        title = response[0]
        with open(title+response[1],'rb') as r:
            if response[1] == '.mp4':
                await update.message.reply_video(r)
            elif response[1] == '.png':
                await update.message.reply_photo(r)
        if os.path.exists(title+response[1]):
            os.remove(title+response[1])
        else:
            print("The file does not exist")
        
    else:
        response = handle_response(text)
        print('BOT:', response)
        await update.message.reply_text(response)

async def handle_file(update:Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'user {update.message.chat_id} in {message_type}: {text}')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = download_file(new_text)
        else:
            return
    else:
        response = download_file(text)
    print('BOT:', response)
    title = response
    with open(title+'.mp4','rb') as r:
        await update.message.reply_video(r)



if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.TEXT, handle_file))
    print('polling...')
    app.run_polling(poll_interval=3)



