from telethon.sync import TelegramClient
from telethon.tl.types import User
from telethon.sync import TelegramClient
from datetime import date
from telethon.tl.types import UserStatusOnline, UserStatusOffline, UserStatusRecently
import datetime,pytz

# Replace these values with your own API ID, API HASH, and phone number.
api_id, api_hash, phone_number = '24599598', '1feea786b8d9ebefd24af45ddd3cf419', '+919354747522'
channel_username=-1001781446918

async def main():
    async with TelegramClient('PG001', api_id, api_hash) as client:
        entity = await client.get_entity(channel_username)
        
        allParticipant=[]
        
        async for message in client.iter_messages(entity):
            if message.sender_id:
                user = await message.get_sender()
                if isinstance(user, User) and user not in allParticipant:
                    allParticipant.append(user)
        # Generate current_datetime for file name
        current_datetime= datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y%m%d_%H%M%S')

        # Generate filename and write data to file
        filename = f"Users_CBTF_{channel_username}_{current_datetime}.txt"

        with open(filename, 'w', encoding='utf-8') as file:
            for participant in allParticipant:
                if participant.status:
                        if isinstance(participant.status, UserStatusOnline):
                            _last = date(participant.status.expires.year, participant.status.expires.month, participant.status.expires.day)
                        elif isinstance(participant.status, UserStatusOffline):
                            _last = date(participant.status.was_online.year, participant.status.was_online.month, participant.status.was_online.day)
                        elif isinstance(participant.status, UserStatusRecently):
                            _last = "Recently"  # Handle UserStatusRecently
                        else:
                            _last = None  # Handle other cases
                        file.write('\n'.join([f"UserId:{participant.id},AccessHash:{participant.access_hash}, Username:{participant.username}, First Name:{participant.first_name}, Last Name:{participant.last_name}, Last Online:{_last}"]))
                        file.write('\n')  # New line after each user's info
        # Print total fetched users and success message
        print(f"Total users fetched: {len(allParticipant)}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
