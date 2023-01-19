#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Oωηєя : <a href='https://t.me/ANKIT3690'><Aⲛⲕⲓⲧ/a>\n○ Oωηєя : <a href='https://t.me/Saurav3BV6SA9LLElon7Musk'>Sαυrαv</a>\n ○ Group : <a href='https://t.me/thewarriorsreal'>Group</a>\n ○ Oωηєя : <a href='https://t.me/defenderofthemultiverse'>Channel</a>\n </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
