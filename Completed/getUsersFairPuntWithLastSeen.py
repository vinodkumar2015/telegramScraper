from telethon.sync import TelegramClient
from datetime import date
from telethon.tl.types import UserStatusOnline, UserStatusOffline, UserStatusRecently
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import datetime,time,pytz

# Replace these values with your own API ID, API HASH, and phone number.
api_id, api_hash, phone_number = '24599598', '1feea786b8d9ebefd24af45ddd3cf419', '+919354747522'

channel_username = 'fairpuntofficail'  # Replace with the channel username

batch_size, offset, all_participants = 500, 0, []

with TelegramClient('PG001', api_id, api_hash) as client:
    channel_entity = client.get_entity(channel_username)

    while True:
        participants = client(GetParticipantsRequest(
            channel=channel_entity,
            filter=ChannelParticipantsSearch(''),
            offset=offset,
            limit=batch_size,
            hash=0
        ))
        
        if not participants.users:
            break
        
        all_participants.extend(participants.users)
        offset += len(participants.users)
        time.sleep(1)
# Generate current_datetime for file name
current_datetime= datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y%m%d_%H%M%S')

# Generate filename and write data to file
filename = f"Users_fairpunt_{channel_username}_{current_datetime}.txt"

with open(filename, 'w', encoding='utf-8') as file:
    for participant in all_participants:
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
print(f"Total users fetched: {len(all_participants)}")