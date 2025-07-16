import asyncio

from pyrogram.client import Client
from pyrogram.types import Message
from config import api_id, api_hash

def is_special_message(m: Message) -> bool:
    # TODO: check caption prop
    return (m.audio is not None or
            m.document is not None or
            m.photo is not None or
            m.sticker is not None or
            m.animation is not None or
            m.game is not None or
            m.giveaway is not None or
            m.invoice is not None or
            m.story is not None or
            m.video is not None or
            m.voice is not None or 
            m.contact is not None or
            m.location is not None or
            m.venue is not None or
            m.poll is not None or
            m.dice is not None or
            m.new_chat_members is not None or
            m.left_chat_member  is not None or
            m.command is not None 
            )


def is_service_message(m: Message) -> bool:
    return (
        m.forum_topic_created is not None
        or m.forum_topic_closed is not None
        or m.forum_topic_reopened is not None
        or m.forum_topic_edited is not None
        or m.general_forum_topic_hidden is not None
        or m.general_forum_topic_unhidden is not None
        or m.video_chat_scheduled is not None
        or m.history_cleared is not None
        or m.video_chat_started is not None
        or m.video_chat_ended is not None
        or m.video_chat_members_invited is not None
        or m.phone_call_started is not None
        or m.phone_call_ended is not None
        or m.web_app_data is not None
        or m.paid_messages_refunded is not None
        or m.paid_messages_price_changed is not None
        or m.direct_message_price_changed is not None
        or m.checklist_tasks_done is not None
        or m.checklist_tasks_added is not None
        or m.gift_code is not None
        or m.gifted_premium is not None
        or m.gifted_stars is not None
        or m.gift is not None
        or m.suggest_profile_photo is not None
        or m.users_shared is not None
        or m.chat_shared is not None
        or m.successful_payment is not None
        or m.refunded_payment is not None
        or m.giveaway_created is not None
        or m.giveaway_completed is not None
        or m.chat_set_theme is not None
        or m.chat_set_background is not None
        or m.set_message_auto_delete_time is not None
        or m.chat_boost is not None
        or m.write_access_allowed is not None
        or m.contact_registered is not None
        or m.proximity_alert_triggered is not None
        or m.giveaway_prize_stars is not None
        or m.screenshot_taken is not None
        or m.delete_chat_photo is not None
        or m.group_chat_created is not None
        or m.supergroup_chat_created is not None
        or m.channel_chat_created is not None
        
        or m.giveaway_winners is not None
    )


def classify_message(m: Message): ...


async def main():
    async with Client("LLMSummarizer", api_id=api_id, api_hash=api_hash) as app:
        async for message in app.get_chat_history(
            "natural_language_processing", limit=7, offset=0
        ):
            message.text

            # async for reply in app.get_discussion_replies(chat_id="natural_language_processing", message_id=message.id):
            #     print(f"Reply: {reply.text}")
            print("--------------------------------")


asyncio.run(main())

