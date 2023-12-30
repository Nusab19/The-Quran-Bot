start = """
Assalamu Alaikum <b>{firstName}!</b>

This bot will give you verses from the Al-Quran.

It can give you the <b>Arabic</b> or <b>English</b> text and also the <b>Audio</b> of each ayah.

See, /use to know how to use this bot.

This bot is <a href="{repoURL}">open-source</a>. Your contribution can make it more helpful for the Ummah."""

help = """
To know how to use the bot:
/use - A brief overview on how to use the bot


For any questions or discussions, reach out to @AlQuranDiscussion.
Stay updated with @AlQuranUpdates

Contact Maintainers: @Roboter403,  @Nusab19"""

howToUse = """
<u>Basic Commands:</u>
/start - Check if the bot is Alive.
/help - Where to contact the dev and the community.
/info - Details of the current chat.
/ping - Check server's ping.

<u>Usage of Bot:</u>
/surah - The list of all the Surahs

Send any message like:
<code>
surah : ayah </code>
<code>1:3</code>

<b>
Here, `1` means Surah-Fatiha and `3` means ayah 3</b>

For more in depth usage, check the <a href="{telegraphURL}">Telegraph</a> link."""


sendAyah = """
Surah : <b>{surahName} ({surahNo})</b>
Ayah  : <b>{ayahNo} out of {totalAyah}</b>
"""
