from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )


def start(updater,context):
    keyboard = 
        [[
        InlineKeyboardButton('Channel', url='https://telegram.me/HTechMedia'),
        InlineKeyboardButton('Support😎', url='https://telegram.me/HTechMediaSupport')
        ],[
        InlineKeyboardButton('Devoloper👀', url='https://telegram.me/NxtStark'),
        InlineKeyboardButton('Website🪐', url='https://htechmediayt.wixsite.com/htechmedia'),
        InlineKeyboardButton('Youtube🚀', url='https:/youtube.com/c/HTechMedia')
        ]]
   
    reply_markup = InlineKeyboardMarkup(keyboard)
   
    updater.message.reply_text('''👋Hi Bro Iam Welcome Messanger bot\nAdd Me In Your Group And See My Pever🔥\n😮More Details Clcik /help Button\n\nMade By @HTechMedia''')

 def help(updater,context):
 updater.message.reply_text("⚕️Add ME TO YOUR GROUP\n⚕️MAKE ME AS ADMIN ON GROUP")
 

def add_group(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        update.message.reply_text(f'👋Hello {member.full_name} , Welcome to {group.full_name}\n\nThank You For Joining💖')

add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
