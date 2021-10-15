import os
class Translation(object):
  
    START_TEXT = """<b>🙋‍♂️Hey {}!!</b>

<b>Am Just A Pro Auto Filter Bot....😉</b>

<b>Just Add Me To Your Group And Channel And Connect Them And See My Pevers 🔥🔥😝</b>

<b>Subscribe to the update channel to learn about my updates and activity...</b>

<b>Press /help to know about available commands🤪</b>

<b>Maintained By @Mo_Tech_YT</b>"""    
    
    HELP_TEXT = """
<b><u>Notice</u></b>
<code>Imdb Poster Imdb is available on this bot
Rating Not Available</codd> 

<b><u>Bot Commands (Works Only In Groups)</u></b>

☞ <code>/add chat_id</code> - <b>To Connect A Group With A Channel (Bot Should Be Admin With Full Previlages In Both Group And Channel)</b>
  
☞ <code>/del chat_id</code> - <b>To disconnect A Group With A Channel</b>
     
☞ <code>/delall</code>  - <b>This Command Will Disconnect All Connected Channel With The Group And Deletes All Its File From DB</b>
    
☞ <code>/settings</code> -  <b>This Command Will Display You A Settings Pannel Instance Which Can Be Used To Tweek Bot's Settings Accordingly</b>

   ☞ <code>Channel</code> - <b>Button Will Show You All The Connected Chats With The Group And Will Show Buttons Correspnding To There Order For Furthur Controls</b>
            
   ☞ <code>Filter Types</code> - <b>Button Will Show You The 3 Filter Option Available In Bot... Pressing Each Buttons Will Either Enable or Disable Them And This Will Take Into Action As Soon As You Use Them Without The Need Of A Restart</b>

   ☞ <code>Configure</code> - <b>Button Will Helps You To Change No. of Pages/ Buttons Per Page/ Total Result Without Acutally Editing The Repo... Also It Provide Option To Enable/Disable For Showing Invite Link In Each Results</b>
            
   ☞ <code>Status</code> - <b>Button Will Shows The Stats Of Your Channel</b>

Maintained By @Mo_Tech_YT"""
    
    ABOUT_TEXT = """
<b>○ My Name :</b> <code>Movie Searching Bot</code>
<b>○ Creator :</b> <a href="https://t.me/farshadck">Muhammed farshad🇵🇹</a>
<b>○ Credits :</b> <code>Everyone in this journey</code>
<b>○ Language :</b> <code>Python3</code>
<b>○ Library :</b> <a href="https://docs.pyrogram.org/">Pyrogram asyncio 0.17.1</a>
<b>○ Supported Site :</b> <a href="https://my.telegram.org/">Only Telegram</a>
<b>○ Source Code :</b> <a href="https://t.me/botupdatechannelfarshad">👉 Click Here</a>
<b>○ Server :</b> <a href="https://herokuapp.com/">Heroku</a>
<b>○ Database :</b> <a href="https://www.mongodb.com/">MongoDB</a>
<b>○ Build Status :</b> <code>V2.1 [BETA]</code>
<b>📜 Quote :</b> <code>ആരും പേടിക്കണ്ട എല്ലാവർക്കും കിട്ടും™️</code>""".format(query.from_user.mention), reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
"""
