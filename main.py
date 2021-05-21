import discord
from bs4 import BeautifulSoup
import requests
url = "https://www.cricbuzz.com/cricket-match/live-scores"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
mydivs = soup.find_all(class_="cb-hmscg-bat-txt")
url1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=300&date=21-05-2021"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
resp1 = requests.get(url1,headers=headers)
data = resp1.json()['sessions']
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
  if msg.content.startswith("$weather"):
    resp = requests.get("http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/193826?apikey=2A7yNWDokHDYBNQuyRJVYvgrdeg58flk%20&language=en-us&details=true&metric=true")
    await msg.channel.send(resp.json()[0]['RainProbability'])
    await msg.channel.send(" - Rain probability")
    await msg.channel.send(resp.content)
  if msg.content.startswith("$cowin"):
    for x in data:
      await msg.channel.send(x)
    
client.run('ODQzNDg1NTMzNDM4MzQ1MjU2.YKEjHg.ZMKOETN9UbGrGVn3u7V7Ynssrgs')