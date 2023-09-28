from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Replace these values with your own API ID, API HASH, and phone number.
api_id, api_hash, phone_number = '24599598', '1feea786b8d9ebefd24af45ddd3cf419', '++919354747522'

async def main():
    # Create a new Telegram client session.
    client = TelegramClient("CH001", api_id, api_hash)

    # Start the client.
    await client.start()

    # Get a list of dialogs (channels and groups) that the user is a member of.
    dialogs = await client.get_dialogs()

    # Save information to a text file and count the number of entries.
    entry_count = 0
    with open("channel_List_info.txt", "w", encoding="utf-8") as file:
        # Print information about each channel/group.
        for dialog in dialogs:
            if dialog.is_channel or dialog.is_group:
                file.write(f"Title: {dialog.title}\n")
                file.write(f"Entity Type: {'Channel' if dialog.is_channel else 'Group'}\n")
                file.write(f"Entity ID: {dialog.id}\n")
                file.write("--------------------\n")
                entry_count += 1

    # Stop the client.
    await client.disconnect()

    # Print the number of entries written to the file.
    print(f"{entry_count} entries have been written to channel_List_info.txt.")


if __name__ == '__main__':
    # Run the main function to get the information.
    import asyncio
    asyncio.run(main())
