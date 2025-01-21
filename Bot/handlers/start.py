from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Create a Pyrogram Client instance
app = Client("Bot")  # Replace "my_bot" with your bot's session name or credentials

@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    first_name = message.from_user.first_name

    # Step 1: Send the initial welcome message
    initial_message = await message.reply_text(
        f"𝐇𝐞𝐥𝐥𝐨 {first_name},\n"
        "𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐀𝐫𝐥𝐞𝐜𝐜𝐡𝐢𝐧𝐨'𝐬 𝐝𝐨𝐦𝐚𝐢𝐧"
    )
    await asyncio.sleep(3)  # Wait for 3 seconds
    await initial_message.delete()

    # Step 2: Send a bomb emoji
    bomb_message = await message.reply_text("💣")
    await asyncio.sleep(1.5)  # Wait for 1.5 seconds
    await bomb_message.delete()

    # Step 3: Send a heart emoji and the detailed welcome message
    heart_message = await message.reply_text("❤️")
    await asyncio.sleep(1.5)  # Wait for 1.5 seconds
    await heart_message.delete()

    # Final message with the description
    final_message = await message.reply_text(
        f"𝖧𝖾𝗅𝗅𝗈 {first_name}\n"
        "➻ 𝖬𝗒𝗌𝖾𝗅𝖿 Aʀʟᴇᴄᴄʜɪɴᴏ! 𝖳𝗁𝖾 𝖬𝗈𝗌𝗍 𝖯𝗈𝗐𝖾𝗋𝖿𝗎𝗅 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖦𝗋𝗈𝗎𝗉 𝖬𝖺𝗇𝖺𝗀𝖾𝗆𝖾𝗇𝗍 𝖡𝗈𝗍 𝖶𝗂𝗍𝗁 𝖲𝗈𝗆𝖾 𝖠𝗐𝖾𝗌𝗈𝗆𝖾 𝖠𝗇𝖽 𝖴𝗌𝖾𝖿𝗎𝗅 𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌.\n"
        "──────────────────────\n"
        "๏ 𝖢𝗅𝗂𝖼𝗄 𝖮𝗇 𝖳𝗁𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 𝖡𝗎𝗍𝗍𝗈𝗇 𝖳𝗈 𝖦𝖾𝗍 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇 𝖠𝖻𝗈𝗎𝗍 𝖬𝗒 𝖬𝗈𝖽𝗎𝗅𝖾𝗌 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌."
    )

    # Step 4: Send the photo with a caption
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://files.catbox.moe/d06nlj.jpg",
        caption="👑 𝖳𝗁𝖾 𝖯𝗈𝗐𝖾𝗋 𝖻𝖾𝗅𝗈𝗇𝗀𝗌 𝗍𝗈 𝖦𝗋𝖺𝗇𝖽𝖢𝗁𝗂𝗅𝖽𝗋𝖾𝗇 𝗈𝖿 𝖧𝖾𝗅𝗅."
    )

# Run the bot
if __name__ == "__main__":
    app.run()
