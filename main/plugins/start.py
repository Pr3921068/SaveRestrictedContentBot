import os
from .. import bot as Altron
from telethon import events


@Altron.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    AltronX = event.client
    await event.delete()
    async with AltronX.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Altron.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Altron.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    text = "Send me Link of any message to clone it here, For private channel message, send invite link first.\n\n**SUPPORT:** @TheAltron"
    await event.reply(text, parse_mode=None, link_preview=None )
