import json
from bot.handlers.database import db


path = "bot/Data/audio/{reciterNo}.txt"

_data = {}
_reciters = 1, 2
for i in _reciters:
    with open(path.format(reciterNo=i), "r") as f:
        fileIDs = f.read().split()
        _data[i] = fileIDs


def getSurahAudio(surah: int, userID: int) -> str:
    user = db.getUser(userID)
    if not user:
        user = db.addUser(userID)

    preferredReciter = int(user["settings"]["reciter"])
    return _data[preferredReciter][int(surah) - 1]
