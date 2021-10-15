import os
class Translation(object):
  
    START_TEXT = """<b>🙋‍♂️Hey {}!!</b>

<b>Am Just A Pro Auto Filter Bot....😉</b>
<b>ഈ ബോട്ട് സിനിമ കോടതി ഗ്രൂപ്പിന് ഉള്ളത് ആണ്..😎</b> 
<b>നിങ്ങൾക് സിനിമക് ആണെങ്കിൽ @farshad555_bot 👈 ഈ ബോട്ടിൽ കേറി വേണ്ട സിനിമ അടിച്ചാൽ മതി..😀</b>
<b>©️MᴀɪɴᴛᴀɪɴᴇD Bʏ  <a href=tg://user?id=1704157292>FARSHAD K</a>"""    
    
    HELP_TEXT = """
<b><u>Notice</u></b>
ഒന്ന് പോടെ അവൻ ഹെല്പ് ചോദിച്ചു വന്നിരിക്കുന്നു...😆😆</b>

©️MᴀɪɴᴛᴀɪɴᴇD Bʏ  <a href=tg://user?id=1704157292>FARSHAD K</a>"""
    
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
