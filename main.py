import discord
import time
from bs4 import BeautifulSoup
from discord import state
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
  if msg.content.startswith("$weather"):
    resp = requests.get("http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/193826?apikey=2A7yNWDokHDYBNQuyRJVYvgrdeg58flk%20&language=en-us&details=true&metric=true")
    await msg.channel.send(resp.json()[0]['RainProbability'])
    await msg.channel.send(" - Rain probability")
  if msg.content.startswith("$sc"):
    sc = msg.content[3:]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    url2 = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(sc)
    resp2 = requests.get(url2, headers=headers)
    data2 = resp2.json()['districts']
    await msg.channel.send("district codes acording to state you selected ")
    for d in data2:
      await msg.channel.send(d)
    await msg.channel.send("enter in following format : '$cowin disctrict_code date_dd-mm-yyyy'")
  if msg.content.startswith("$cowin"):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    if len(msg.content) == 6:
      await msg.channel.send("State codes are ")
      url3 = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
      resp3 = requests.get(url3,headers=headers)
      data3 = resp3.json()['states']
      for states in data3:
        await msg.channel.send(states)
      await msg.channel.send("Enter your state code as $sc'statecode'")
      
    dis = msg.content[7:10]
    date = msg.content[11:21]
    url1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(dis,date)
    
    resp1 = requests.get(url1,headers=headers)
    data = resp1.json()['sessions']

    for x in data:
      await msg.channel.send(x)
client.run('ODQzNDg1NTMzNDM4MzQ1MjU2.YKEjHg.C78_Lw3NknbU4boPB90gkQuDFgI')
