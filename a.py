import os
import re
import requests
from telethon import TelegramClient, events

# Telegram API bilgilerini environment variable'dan alıyoruz
api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')
source_channel = os.environ.get('SOURCE_CHANNEL')  # Kanal kullanıcı adı: @ornekkanal
target_channel = os.environ.get('TARGET_CHANNEL')  # Hedef grup veya kanal: @hedefgrup

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    text = event.message.message
    match = re.search(r'(https?://\S+)', text)
    if match:
        original_url = match.group(1)
        # API çağrısı
        api_url = f'https://ay.live/st/?api=98da093c43dcd0ccb29b307ba1cda03d9bf94209&url={original_url}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            new_link = response.text
            # Yeni linki hedef kanala gönder
            await client.send_message(target_channel, f'Yeni link: {new_link}')
            print(f'Link başarıyla gönderildi: {new_link}')
        except Exception as e:
            print(f'API çağrısı başarısız: {e}')

client.start()
print("Bot çalışıyor...")
client.run_until_disconnected()