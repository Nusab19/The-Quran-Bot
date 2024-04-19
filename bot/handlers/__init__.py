from ..quran import QuranClass

# Variables has to be declared before importing handlers
Quran = QuranClass()

from .helpers import generateSurahButtons


class Constants:
    # --- Stickers ---
    salamSticker = (
        "CAACAgUAAxkBAAIBEGOtH-MLc6D7antAIRlma1YgnMe7AAJnBAAC3uq4VANpwAelURpaLAQ"
    )

    inShaAllah = (
        "CAACAgUAAxkBAAIBEWOtH-OoB2EaecZw_DAqRwvbHlOZAALWAwACkni4VLa6DL4cB1H6LAQ"
    )
    jazakAllah = (
        "CAACAgUAAxkBAAIBEmOtH-No3_xEGMh2YpM6ErBQ2BHHAAK4AwAC8Yq5VFbQH8fyZNceLAQ"
    )
    allSurahInlineButtons = generateSurahButtons(Quran)


from .middleware import middleware
from .errorHandler import handleErrors
from .command import handlers as commandHandlers
from .message import handlers as messageHandlers
from .inlineQuery import handlers as inlineQueryHandlers
from .callbackQuery import handlers as callbackQueryHandlers

exportedHandlers = [
    *commandHandlers,
    *messageHandlers,
    *inlineQueryHandlers,
    *callbackQueryHandlers
]