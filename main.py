import discord
from discord.ext import commands
import wikipedia
import googlesearch
from tldextract import extract
import requests
#import json

client=commands.Bot(command_prefix = "&")
client.remove_command("help")

@client.event
async def on_ready():
  print("Bot is ready to deploy")

@client.command(pass_context=True)
async def summary(cxt,*args):
  channel=cxt.message.channel
  keyword=" ".join(args)
  embed=discord.Embed(
    title=keyword,
    color=discord.Color.red()
  )
  
  try:
    embed.description=wikipedia.summary(keyword, sentences=2, auto_suggest=False)
    embed.set_footer(text="source: Wikipedia")
  
  except Exception as error:
    embed.title="Invalid term"
    embed.description="Please enter a valid term"
    embed.set_footer(text="error-invalid term")
  finally:
    await channel.send(embed=embed)


@client.command(pass_context=True)
async def links(cxt,*args):
  channel=cxt.message.channel
  keyword=" ".join(args)
  embed=discord.Embed(
    title=keyword,
    color=discord.Color.blue()
  )
  invalid=True
  for i in googlesearch.search(keyword, tld="co.in", num=10, stop=10, pause=2):
    invalid=False
    tsd, td, tsu = extract(i)
    url = td + '.' + tsu
    embed.add_field(name=url,value=i,inline=False)
  embed.set_footer(text="source: Google")
  if invalid:
    embed.title="Invalid term"
    embed.description="Enter a valid term"
    embed.set_footer(text="source: error-invalid term")
  await channel.send(embed=embed)

@client.command(pass_context=True)
async def cats(cxt):
  channel=cxt.message.channel
  pics=[]
  for i in range(5):
    link=requests.get("https://api.thecatapi.com/v1/images/search",
                   headers={"x-api-key":"b84b17a0-d0d6-4fec-b7af-eb386e4b34ae"}).json()[0]["url"]
    pics.append(link)
  for pic in pics:
    await channel.send(pic)

@client.command(pass_context=True)
async def dogs(cxt):
  channel=cxt.message.channel
  pics=[]
  for i in range(5):
    link=requests.get("https://api.thedogapi.com/v1/images/search",
                   headers={"x-api-key":"2592ff6f-cd41-4362-a665-b7df356f95c6"}).json()[0]["url"]
    pics.append(link)

  for pic in pics:
    await channel.send(pic)
  
client.run("OTcyMzMyNTU0MTY0MjQ0NTMx.YnXhQQ.bu5ErgLbgxqBABb8SuC49Mvtft4")