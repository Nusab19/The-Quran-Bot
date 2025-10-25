from telegram.ext import CommandHandler
from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup


from bot.handlers.localDB import db
from bot.handlers.defaults import reciterNames
from bot.handlers import Quran
from bot.handlers.helpers.decorators import onlyGroupAdmin

arabicStyles = {
    "1": "Uthmani",
    "2": "Simple",
}


async def updateSettings(u: Update, c):
    """Sends the settings message to change preferences"""

    message = u.effective_message
    userID = u.effective_user.id
    chatID = u.effective_chat.id

    if u.effective_chat.type in ("group", "supergroup"):  # if group
        return await updateSettingsForGroup(u, c)

    user = db.users.get(userID)

    settings = user["settings"]

    primary = settings["primary"]
    secondary = settings["secondary"]
    other = settings["other"]
    primary, secondary, other = map(
        Quran.getTitleLanguageFromAbbr, [primary, secondary, other]
    )

    font = settings["font"]
    showTafsir = settings["showTafsir"]
    reciter = settings["reciter"]

    reply = f"""
<u><b>Settings</b></u>
Change your settings to your preference.


<b>Languages:</b>
- <b>Primary</b>    : {primary}
- <b>Secondary</b>  : {secondary}
- <b>Other</b>      : {other}

<b>Arabic Style</b> : {arabicStyles[str(font)]}
<b>Show Tafsir</b>  : {["No", "Yes"][showTafsir]}
<b>Reciter</b>      : {reciterNames[str(reciter)]}
"""

    buttons = [
        [
            InlineKeyboardButton("Languages", callback_data="settings languages"),
            InlineKeyboardButton("Arabic Style", callback_data="settings font"),
        ],
        [
            InlineKeyboardButton("Tafsir", callback_data="settings showTafsir"),
            InlineKeyboardButton("Reciter", callback_data="settings reciter"),
        ],
    ]

    await message.reply_html(reply, reply_markup=InlineKeyboardMarkup(buttons))


# Will be called when the user is in a group
@onlyGroupAdmin(allowDev=True)
async def updateSettingsForGroup(u: Update, c):
    """Sends the settings message to groups to change preferences (only for group admins)"""

    bot: Bot = c.bot
    message = u.effective_message
    userID = u.effective_user.id
    chatID = u.effective_chat.id

    chat = db.chats.get(chatID)

    settings = chat["settings"]
    handleMessages = settings["handleMessages"]
    allowAudio = settings["allowAudio"]
    previewLink = settings["previewLink"]
    restrictedLangs = settings["restrictedLangs"]
    allLangs = dict(Quran.getLanguages())

    # <a href="https://t.me/quraniumbot?startgroup=bot">Add me to your group</a>

    reply = f"""
<u><b>Group Settings</b></u>
Change the settings of the group from here.


<b>Handle Messages</b>  : {["No", "Yes"][handleMessages]}
<b>Allow Audio</b>      : {["No", "Yes"][allowAudio]}
<b>Preview Link</b>     : {["No", "Yes"][previewLink]}
<b>Restricted Languages: </b> {', '.join(allLangs[i] for i in restrictedLangs) or None}
"""

    buttons = [
        [
            InlineKeyboardButton(
                "Handle Messages", callback_data=f"settings handleMessages {userID}"
            ),
            InlineKeyboardButton(
                "Allow Audio", callback_data=f"settings allowAudio {userID}"
            ),
        ],
        [
            InlineKeyboardButton(
                "Preview Link", callback_data=f"settings previewLink {userID}"
            ),
            InlineKeyboardButton(
                "Restricted Languages",
                callback_data=f"settings restrictedLangs {userID}",
            ),
        ],
        [
            InlineKeyboardButton("Close", callback_data=f"close {userID}"),
        ],
    ]

    await message.reply_html(reply, reply_markup=InlineKeyboardMarkup(buttons))


exportedHandlers = [
    CommandHandler("settings", updateSettings),
]
