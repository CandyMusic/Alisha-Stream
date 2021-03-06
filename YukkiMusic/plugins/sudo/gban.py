


import asyncio
import os
import shutil
import subprocess
from sys import version as pyver

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from config import OWNER_ID, MUSIC_BOT_NAME, OWNER_ID
from YukkiMusic.utils.database import (add_gban_user, add_off, add_on, add_sudo,
                            get_active_chats, get_served_chats, get_sudoers,
                            is_gbanned_user, remove_active_chat,
                            remove_gban_user, remove_served_chat, remove_sudo,
                            set_video_limit)


## Gban Module


@app.on_message(filters.command("gban")  & SUDOERS)
async def ban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**Usage:**\n/gban [USERNAME | USER_ID]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            return await message.reply_text(
                "ʙᴇᴡᴋᴜғ ᴀᴘɴᴇ ᴀᴀᴘ ᴋᴏ ʜɪ ʙᴀɴ ᴋᴀʀ ʀʜᴀ ʜᴀɪ ɴᴏᴏʙ ᴋɪᴅx!"
            )
        elif user.id in SUDOERS:
            await message.reply_text("ᴍᴀɪɴ sᴜᴅᴏ ᴍᴇ ʜᴜ ᴍᴜᴊᴇ ʙʟᴏᴄᴋ ᴋᴀʀɴᴀ ɪᴍᴘᴏsɪʙʟᴇ ʜᴀɪ")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**Mᴀᴊᴅᴜʀ ᴋᴏ ᴋʜᴏᴅɴᴀ ᴀᴜʀ ʙᴀᴘ ᴋᴏ ᴄʜᴏᴅɴᴀ ɴᴀʜɪ Sɪᴋᴀᴛᴇ - ᴀʙ ɴɪᴋᴀʟ ᴍᴀᴅʀᴄʜᴏᴅ {user.mention}**\n\nɢʙᴀɴ ᴍᴇ ʟᴀɢɴᴇ ᴡᴀᴋᴀ ᴛɪᴍᴇ : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.ban_chat_member(sex, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
__**New Global Ban on {MUSIC_BOT_NAME}**__

**Origin:** {message.chat.title} [`{message.chat.id}`]
**Sudo User:** {from_user.mention}
**Banned User:** {user.mention}
**Banned User ID:** `{user.id}`
**Chats:** {number_of_chats}"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    sudoers = await get_sudoers()
    if user_id == from_user_id:
        await message.reply_text("ʙᴇᴡᴋᴜғ ᴀᴘɴᴇ ᴀᴀᴘ ᴋᴏ ʜɪ ʙᴀɴ ᴋᴀʀ ʀʜᴀ ʜᴀɪ ɴᴏᴏʙ ᴋɪᴅx!")
    elif user_id in sudoers:
        await message.reply_text("ʙᴇᴡᴋᴜғ ᴀᴘɴᴇ ᴀᴀᴘ ᴋᴏ ʜɪ ʙᴀɴ ᴋᴀʀ ʀʜᴀ ʜᴀɪ ɴᴏᴏʙ ᴋɪᴅx")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("ᴘᴀʜʟᴇ sᴇ ʜɪ ɢʙᴀɴ ʜᴀɪ ᴅᴜғғᴇʀ.")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**ᴀʟɪsʜᴀ ᴊɪ ʙᴀɴ ᴋᴀʀ ʀʜɪ ʜᴀɪɴ ᴀᴘᴋᴏ {mention}**\n\nᴛɪᴍᴇ ᴛᴀᴋᴇɴ : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.ban_chat_member(sex, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
__**ɴᴇᴡ ɢʟᴏʙᴀʟ ʙᴀɴ ᴏɴ {MUSIC_BOT_NAME}**__

**ɢʀᴏᴜᴘ ɴᴀᴍᴇ:** {message.chat.title} [`{message.chat.id}`]
**sᴜᴅᴏ ᴜsᴇʀ:** {from_user_mention}
**ʙᴀɴ ʜᴏɴᴇ ᴡᴀʟᴇ ᴋᴀ ɴᴀᴀᴍ:** {mention}
**ʙᴀɴ ʜᴏɴᴇ ᴡᴀʟᴇ ᴋɪ ɪᴅ:** `{user_id}`
**ɪᴛɴᴇ ᴄʜᴀᴛ sᴇ ɢᴀʏᴀ ʜᴀɪ ᴛᴜ ʙᴇʜɴᴄʜᴏᴅ:** {number_of_chats}"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return

          
@app.on_message(filters.command("ungban") & SUDOERS)
async def unban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**Usage:**\n/ungban [USERNAME | USER_ID]"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        sudoers = await get_sudoers()
        if user.id == from_user.id:
            await message.reply_text("You want to unblock yourself?")
        elif user.id in sudoers:
            await message.reply_text("Sudo users can't be blocked/unblocked.")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("He's already free, why bully him?")
            else:
                await remove_gban_user(user.id)
                await message.reply_text(f"Ungbanned!")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    sudoers = await get_sudoers()
    if user_id == from_user_id:
        await message.reply_text("You want to unblock yourself?")
    elif user_id in sudoers:
        await message.reply_text("Sudo users can't be blocked/unblocked.")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("He's already free, why bully him?")
        else:
            await remove_gban_user(user_id)
            await message.reply_text(f"Ungbanned!")
