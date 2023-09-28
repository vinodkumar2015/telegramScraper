import asyncio
from telethon import TelegramClient, events
import time

api_id = 23140919  # Convert the api_id to an integer
api_hash = '9e0d078397cce5bacac56bba711a2a58'

# Replace 'YOUR_PHONE_NUMBER' with your phone number with country code, e.g., +1234567890
phone_number = '+919354747522'

# Create a new TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start(phone_number)

    # Replace 'channel_entity_id' with the actual entity ID of the channel you want to access
    channel_entity_id = -1001246709657

    highest_message_id = 0
    latest_message_id = 0
    # Set the time limit to run the loop (1 minute)
    end_time = time.time() + 3600

    while time.time() < end_time:
        # The number of recent messages you want to retrieve (1 in this case)
        recent_message_limit = 2
        
        async for message in client.iter_messages(channel_entity_id, limit=recent_message_limit, reverse=False):
            if message.text and (latest_message_id is None or message.id > latest_message_id):
                # Check if the message contains "https" or "http" text
                if "https" not in message.text and "http" not in message.text and "**.**" not in message.text:
                    print(f"Message ID: {message.id}")
                    print(f"Message Text: {message.text}\n")
                    print(f"Message Text: {message.text}\n")
                    #await client.send_message('trading_line_future_option', f"\n {message.text}")
                    await client.send_message('charlie_line_cricket_live', f"\n {message.text}")
                latest_message_id = message.id
                break

        # Introduce a 1-second delay before the next iteration
        await asyncio.sleep(1)
    # Disconnect from Telegram
    await client.disconnect()
# Run the main function using await
asyncio.run(main())
