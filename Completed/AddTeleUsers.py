from telethon import TelegramClient
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser, InputPeerChannel
import csv


# Credentials and settings
api_id, api_hash, phone_number, channel_username = '24599598', '1feea786b8d9ebefd24af45ddd3cf419', '+917232836063', 'charlie_live_cricket'

# Replace this with the path to your text file
file_path = 'Download/greyexchange_20230806_194101.txt'

# Replace these with the starting and ending row numbers for adding users (1-based index)
start_row = 1
end_row = 1000  # For example, to add users from row 1 to row 10, set start_row = 1 and end_row = 10

# Create the TelegramClient
client = TelegramClient(phone_number, api_id, api_hash)

async def main():
    await client.start()
    me = await client.get_me()
    print(f"Logged in as: {me.first_name} (ID: {me.id})")

async def add_users_to_channel():
    try:
        # Fetch the entity (channel) to get the access hash
        entity = await client.get_entity(channel_username)
        # if not isinstance(entity, InputPeerChannel):
            # raise ValueError("Invalid channel username or ID.")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line_num in range(start_row - 1, min(end_row, len(lines))):
                line = lines[line_num].strip()
                try:
                    user_id_str = line.split(":")[1].split(',')[0].strip()
                    # user_name1 = line.split(":")[2].split(',')[0].strip()
                    access_hash = line.split(":")[2].split(',')[0].strip()
                    user_id = int(user_id_str)
                    # user = await client.get_entity(user_name1)
                    input_user = InputPeerUser(user_id=user_id, access_hash=int(access_hash))
                except Exception as e:
                    print(f"Error: {e}")
                try:
                    await client(InviteToChannelRequest(channel=entity, users=[input_user]))
                    print(f"Added user with ID {user_id} to the channel '{channel_username}' successfully.")
                except Exception as e:
                    print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

with client:
    client.loop.run_until_complete(main())
    client.loop.run_until_complete(add_users_to_channel())