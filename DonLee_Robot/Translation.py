import os
class Translation(object):
  
    START_TEXT = """
  else:
        await cmd.reply_photo(
            photo="https://i.ibb.co/1mWkBzK/Photo-1704157292.jpg",
            caption=f"𝐘𝐨..𝐘𝐨..{cmd.from_user.mention} 🙋, 𝐈'𝐦 𝐏𝐨𝐰𝐞𝐫𝐟𝐮𝐥 𝐌𝐞𝐝𝐢𝐚 𝐒𝐞𝐚𝐫𝐜𝐡 𝐁𝐨𝐭 𝐨𝐫 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐜𝐚𝐥𝐥 𝐦𝐞 𝐚𝐬 𝐀𝐮𝐭𝐨-𝐅𝐢𝐥𝐭𝐞𝐫 𝐁𝐨𝐭\n\n𝐇𝐞𝐫𝐞 𝐲𝐨𝐮 𝐜𝐚𝐧 𝐬𝐞𝐚𝐫𝐜𝐡 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 𝐈𝐧𝐥𝐢𝐧𝐞 𝐦𝐨𝐝𝐞 𝐚𝐬 𝐰𝐞𝐥𝐥 𝐚𝐬 𝐏𝐌, 𝐔𝐬𝐞 𝐭𝐡𝐞 𝐛𝐞𝐥𝐨𝐰 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐭𝐨 𝐬𝐞𝐚𝐫𝐜𝐡 𝐟𝐢𝐥𝐞𝐬 𝐨𝐫 𝐬𝐞𝐧𝐝 𝐦𝐞 𝐭𝐡𝐞 𝐧𝐚𝐦𝐞 𝐨𝐟 𝐟𝐢𝐥𝐞 𝐭𝐨 𝐬𝐞𝐚𝐫𝐜𝐡\n©️MᴀɪɴᴛᴀɪɴᴇD Bʏ  <a href=tg://user?id=1704157292>FARSHAD K</a>"""    
    
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
<b>➥ 🤖Bot</b> : <b>Adv Auto Filter Bot v2.9</b>
    
<b>➥ 😎Creator</b> : <b>@AlbertEinstein_TG</b> 

<b>➥ 👨‍💻Editor</b> : <b>@Mrk_YT</b>

<b>➥ 🗣️Language</b> : <b>Python3</b>

<b>➥ 📚Library</b> : <b>Pyrogram Asyncio 1.13.0</b>

<b>➥ 📖Source Code</b> : <b><a href="https://github.com/PR0FESS0R-99/DonLee_Robot">💥Click Me</a></b>
"""
