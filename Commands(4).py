#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG 


from pyrogram import filters, Client, __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import asyncio
from pyrogram.errors import FloodWait
from bot.bot import Bot
from bot import ADMINS, OWNER_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode, decode, get_messages

db = Database()


@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<b>File Name :</b> \n " + "<code>" + file_name + "</code>" + " \n \n \n <b> ❤️ 𝚃𝚑𝚊𝚗𝚔𝚢𝚘𝚞 𝙵𝚘𝚛 𝚄𝚜𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚒𝚌𝚎 𝙿𝚕𝚎𝚊𝚜𝚎 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝚄𝚜 𝙱𝚢 𝚂𝚑𝚊𝚛𝚒𝚗𝚐 𝙾𝚞𝚛 𝙲𝚑𝚊𝚗𝚗𝚎𝚕/𝙶𝚛𝚘𝚞𝚙 𝙻𝚒𝚗𝚔 𝚃𝚘 𝚈𝚘𝚞𝚛 𝙵𝚛𝚒𝚎𝚗𝚍𝚜</b> \n \n <b>❁𝕁𝕠𝕚𝕟 𝕆𝕦𝕣 ℂ𝕙𝕒𝕟𝕟𝕖𝕝𝕤❁</b> \n \n <b>⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱</b> \n \n <b>𝕮𝖍𝖆𝖓𝖓𝖊𝖑: @MoviE_LinkS_0nlY</b> \n <b>➻ 📌𝕮𝖍𝖆𝖓𝖓𝖊𝖑 : @BoX_0fFiCe</b> \n <b>➻ 👥𝕲𝖗𝖔𝖚𝖕 : @Mv_mania</b> \n <b>➻ 👥𝕲𝖗𝖔𝖚𝖕 : @agorimovies </b> \n ") 
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴🌐', url='https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Mv_Mania%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@BoX_0fFiCe%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@MoviE_LinkS_0nlY')
                ],
                [
                    InlineKeyboardButton('🎥𝙶𝚁𝙾𝚄𝙿', url='https://t.me/mv_mania'),
                    InlineKeyboardButton('𝙲𝙷𝙰𝙽𝙽𝙴𝙻🎭', url='https://t.me/MoviE_LinkS_0nlY')
                ]
            ]
        )
    ) 
 
        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴🌐', url='https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Mv_Mania%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@BoX_0fFiCe%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@MoviE_LinkS_0nlY')
                ],
                [
                    InlineKeyboardButton('🎥𝙶𝚁𝙾𝚄𝙿', url='https://t.me/mv_mania'),
                    InlineKeyboardButton('𝙲𝙷𝙰𝙽𝙽𝙴𝙻🎭', url='https://t.me/MoviE_LinkS_0nlY')
                ]
            ]
        )
    )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴🌐', url='https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Mv_Mania%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@BoX_0fFiCe%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@MoviE_LinkS_0nlY')
                ],
                [
                    InlineKeyboardButton('🎥𝙶𝚁𝙾𝚄𝙿', url='https://t.me/mv_mania'),
                    InlineKeyboardButton('𝙲𝙷𝙰𝙽𝙽𝙴𝙻🎭', url='https://t.me/MoviE_LinkS_0nlY')
                ]
            ]
        )
    )

        else:
            print(file_type)
        
        return

        
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/fe403b72f9dd617f96441.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton("⚙️𝙷𝙴𝙻𝙿", callback_data = "ghelp")
                ],
                [
                    InlineKeyboardButton('🏘️𝙶𝚁𝙾𝚄𝙿', url='https://t.me/mv_mania'),
                    InlineKeyboardButton('🎬𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/BoX_0fFiCe')
                ],
                [
                    InlineKeyboardButton('🔎𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/MoviE_LinkS_0nlY'),
                    InlineKeyboardButton('🗃️𝚂𝙾𝚄𝚁𝙲𝙴', callback_data = "source_help")
                ]
            ]
        ), 
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
        
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Auto Filter', callback_data = "auto_fltr"),
                    InlineKeyboardButton('File Store', callback_data = "file_saver")
                ],
                [
                    InlineKeyboardButton('Vc Player', callback_data = "vcbots"),
                    InlineKeyboardButton('Filters', callback_data = "filetr")
                ],
                [
                    InlineKeyboardButton('💬About', callback_data = "about")
                ]
            ]
        )
    )

@Client.on_message(filters.text & ~ filters.command(["start","help","batch","genlink","cccurrent","userbotjoinchannel","channelplay","play","dplay","splay","player","skip","pause","resume","end","current","playlist","cresume","cplayer","cplaylist","cdplay","unset","csplay","cplay","pmpermit","gcast","userbotleaveall","userbotjoin","admincache","remall","rem","viewfilters","filter","info","set","sets","id","status"]) & filters.private & ~ filters.me)
async def note(bot, update):
    buttons = [[
        InlineKeyboardButton('🏡𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url='https://t.me/MoviE_LinkS_0nlY'),
        InlineKeyboardButton('📽️𝙼𝙾𝚅𝙸𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻', url ='https://t.me/BoX_0fFiCe')
    ],[
        InlineKeyboardButton('🤔𝙷𝙾𝚆 𝚃𝙾 𝚁𝙴𝚀?', url='https://t.me/MoviE_LinkS_0nlY/5')
    ],[
        InlineKeyboardButton('𝚂𝙷𝙰𝚁𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙵𝚁𝙸𝙴𝙽𝙳𝚂😍', url='https://t.me/share/url?url=💯%20𝙽𝙾%201%20𝙼𝙾𝚅𝙸𝙴%20𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙸𝙽𝙶%20𝙶𝚁𝙾𝚄𝙿%20𝙸𝙽%20𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼%20✅%20%0A%0A𝙹𝙾𝙸𝙽%20𝙰𝙽𝙳%20𝚁𝙴𝚀%20𝚈𝙾𝚄𝚁%20𝙵𝙰𝚅𝙾𝚁𝙸𝚃𝙴%20𝙼𝙾𝚅𝙸𝙴𝚂%20𝚁𝙸𝙶𝙷𝚃%20𝙽𝙾𝚆%20%0A%0A💠%20➠%20𝙶𝚁𝙾𝚄𝙿%20:-%20@Mv_Mania%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@BoX_0fFiCe%20%0A💠%20➠%20𝙲𝙷𝙰𝙽𝙽𝙴𝙻%20:-%20@MoviE_LinkS_0nlY')
  
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)

    if update.from_user.id not in ADMINS:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.REQ_IN_PM,
            reply_markup=reply_markup,
            parse_mode="html",
            reply_to_message_id=update.message_id
        )
    
