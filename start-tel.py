from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import multiprocessing 
import configparser
import time
from time import sleep
import random
 
 
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("./config.ini")  
symbol = config["code"]["symbol"] 
team_percentage  = config["code"]["team_percentage"] 
texte_hack1   = config["code"]["texte_hack1"] 
percentage1  = int(config["code"]["percentage1"])
texte_hack1_1   = config["code"]["texte_hack1_1"] 
texte_hack2   = config["code"]["texte_hack2"] 
percentage2  = int(config["code"]["percentage2"])
texte_hack2_1   = config["code"]["texte_hack2_1"] 

app = Client("my_account")
 
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = symbol
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 
# Команда взлома 
@app.on_message(filters.command(team_percentage, prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < percentage1):
        try:
            text = texte_hack1 + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit(texte_hack1_1)
    sleep(3)
 
    msg.edit(texte_hack2 )
    perc = 0
 
    while(perc < percentage2):
        try:
            text = texte_hack2  + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit(texte_hack2_1)
 
 
app.run()