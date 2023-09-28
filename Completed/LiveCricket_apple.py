from telethon import TelegramClient, events
import time
import asyncio

api_id = '23140919'
api_hash = '9e0d078397cce5bacac56bba711a2a58'

# Replace 'YOUR_PHONE_NUMBER' with your phone number with country code, e.g., +1234567890
phone_number = '+919354747522'

# Create a new TelegramClient instance
client = TelegramClient('session_name1', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start(phone_number)

    # Replace 'channel_username' with the username of the channel you want to access
    channel_username = -1001246709657

    highest_message_id = 0
    latest_message_id = None
    # Set the time limit to run the loop (1 minute)
    end_time = time.time() + 3600

    while time.time() < end_time:
        # The number of recent messages you want to retrieve (1 in this case)
        recent_message_limit = 2
        async for message in client.iter_messages(channel_username, limit=recent_message_limit, reverse=False):
            if message.text and (latest_message_id is None or message.id > latest_message_id):
                # Check if the message contains "https" or "http" text
                if "https" not in message.text and "http" not in message.text and "**.**" not in message.text:
                    print(f"Message ID: {message.id}")
                    print(f"Message Text: {message.text}\n")
                    print(f"Message Text: {message.text}\n")
                    await client.send_message('cricketpulse', f"\n {message.text}")

                    if "**RUKA✔️✔️**" in message.text:
                        await client.send_message('charlie_line_cricket_live', f"\n wait for a moment")
                latest_message_id = message.id
                break

            # Introduce a 1-second delay before the next iteration
        await asyncio.sleep(1)
    # Disconnect from Telegram
    await client.disconnect()
# Run the main function using await
asyncio.run(main())
