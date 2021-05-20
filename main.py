import discord
from bs4 import BeautifulSoup
import requests
url = "https://www.cricbuzz.com/cricket-match/live-scores"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
mydivs = soup.find_all(class_="cb-hmscg-bat-txt")
client = discord.Client()
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event

async def on_message(msg):
  if msg.author==client.user:
    return
  if msg.content.startswith("$score"):
    for x in mydivs:
      await msg.channel.send(x.get_text())
client.run('ODQzNDg1NTMzNDM4MzQ1MjU2.YKEjHg.ZMKOETN9UbGrGVn3u7V7Ynssrgs')