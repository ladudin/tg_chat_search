"""
    Parameters:
        id (``int``):
            Unique message identifier inside this chat.

        from_user (:obj:`~pyrogram.types.User`, *optional*):
            Sender, empty for messages sent to channels.

        sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Sender of the message, sent on behalf of a chat.
            The channel itself for channel messages.
            The supergroup itself for messages from anonymous group administrators.
            The linked channel for messages automatically forwarded to the discussion group.

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date the message was sent.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Conversation the message belongs to.

        [?] topic_message (``bool``, *optional*):
            True, if the message is a forum topic message.

        automatic_forward (``bool``, *optional*):
            True, if the message is a channel post that was automatically forwarded to the connected discussion group.

        [?] topic (:obj:`~pyrogram.types.ForumTopic`, *optional*):
            Topic the message belongs to.

        forward_origin (:obj:`~pyrogram.types.MessageOrigin`, *optional*):
            Information about the original message for forwarded messages.

        [**Threads are usually automatically created when replying to any message in a group.**]
        message_thread_id (``int``, *optional*):
            Unique identifier of a message thread to which the message belongs.
            For forums only.

        -> reply_to_message_id (``int``, *optional*):
            The id of the message which this message directly replied to.

        reply_to_story_id (``int``, *optional*):
            The id of the story which this message directly replied to.

            * reply_to_story_user_id (``int``, *optional*):
                  The id of the story sender which this message directly replied to.

            * reply_to_story (:obj:`~pyrogram.types.Story`, *optional*):
                  For replies, the original story.

        -> reply_to_top_message_id (``int``, *optional*):
            The id of the first message which started this message thread.

        -> reply_to_message (:obj:`~pyrogram.types.Message`, *optional*):
            For replies, the original message. Note that the Message object in this field will not contain
            further reply_to_message fields even if it itself is a reply.

        mentioned (``bool``, *optional*):
            The message contains a mention.

        empty (``bool``, *optional*):
            The message is empty.
            A message can be empty in case it was deleted or you tried to retrieve a message that doesn't exist yet.

        service (:obj:`~pyrogram.enums.MessageServiceType`, *optional*):
            The message is a service message.
            This field will contain the enumeration type of the service message.
            You can use ``service = getattr(message, message.service.value)`` to access the service message.

        media (:obj:`~pyrogram.enums.MessageMediaType`, *optional*):
            The message is a media message.
            This field will contain the enumeration type of the media message.
            You can use ``media = getattr(message, message.media.value)`` to access the media message.

        paid_media (:obj:`~pyrogram.types.PaidMediaInfo`, *optional*):
            The message is a paid media message.

        checklist (:obj:`~pyrogram.types.Checklist`, *optional*):
            The message is a checklist message.

        show_caption_above_media (``bool``, *optional*):
            If True, caption must be shown above the message media.

        edit_date (:py:obj:`~datetime.datetime`, *optional*):
            Date the message was last edited.

        edit_hidden (``bool``, *optional*):
            The message shown as not modified.
            A message can be not modified in case it has received a reaction.

        media_group_id (``int``, *optional*):
            The unique identifier of a media message group this message belongs to.

        author_signature (``str``, *optional*):
            Signature of the post author for messages in channels, or the custom title of an anonymous group
            administrator.

        has_protected_content (``bool``, *optional*):
            True, if the message can't be forwarded.

        has_media_spoiler (``bool``, *optional*):
            True, if the message media is covered by a spoiler animation.

        text (``str``, *optional*):
            For text messages, the actual UTF-8 text of the message, 0-4096 characters.
            If the message contains entities (bold, italic, ...) you can access *text.markdown* or
            *text.html* to get the marked up message text. In case there is no entity, the fields
            will contain the same text as *text*.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear
            in the caption.

        audio (:obj:`~pyrogram.types.Audio`, *optional*):
            Message is an audio file, information about the file.

        # document (:obj:`~pyrogram.types.Document`, *optional*):
        #     Message is a general file, information about the file.
        #
        # photo (:obj:`~pyrogram.types.Photo`, *optional*):
        #     Message is a photo, information about the photo.
        #
        # sticker (:obj:`~pyrogram.types.Sticker`, *optional*):
        #     Message is a sticker, information about the sticker.
        #
        # animation (:obj:`~pyrogram.types.Animation`, *optional*):
        #     Message is an animation, information about the animation.
        #
        # game (:obj:`~pyrogram.types.Game`, *optional*):
        #     Message is a game, information about the game.
        #
        # giveaway (:obj:`~pyrogram.types.Giveaway`, *optional*):
        #     Message is a giveaway, information about the giveaway.
        #
        # invoice (:obj:`~pyrogram.types.Invoice`, *optional*):
        #     Message is a invoice, information about the invoice.
        #     `More about payments » <https://core.telegram.org/bots/api#payments>`_
        #
        # story (:obj:`~pyrogram.types.Story`, *optional*):
        #     Message is a story, information about the story.
        #
        # video (:obj:`~pyrogram.types.Video`, *optional*):
        #     Message is a video, information about the video.
        #
        # video_processing_pending (``bool``, *optional*):
        #     True, if the video is still processing.
        #
        # voice (:obj:`~pyrogram.types.Voice`, *optional*):
        #     Message is a voice message, information about the file.
        #
        # video_note (:obj:`~pyrogram.types.VideoNote`, *optional*):
        #     Message is a video note, information about the video message.
        #
        # caption (``str``, *optional*):
        #     Caption for the audio, document, photo, video or voice, 0-1024 characters.
        #     If the message contains caption entities (bold, italic, ...) you can access *caption.markdown* or
        #     *caption.html* to get the marked up caption text. In case there is no caption entity, the fields
        #     will contain the same text as *caption*.
        #
        # contact (:obj:`~pyrogram.types.Contact`, *optional*):
        #     Message is a shared contact, information about the contact.
        #
        # location (:obj:`~pyrogram.types.Location`, *optional*):
        #     Message is a shared location, information about the location.
        #
        # venue (:obj:`~pyrogram.types.Venue`, *optional*):
        #     Message is a venue, information about the venue.

        web_page (:obj:`~pyrogram.types.WebPage`, *optional*):
            Message was sent with a webpage preview.

        link_preview_options (:obj:`~pyrogram.types.LinkPreviewOptions`, *optional*):
            Options used for link preview generation for the message.

        # poll (:obj:`~pyrogram.types.Poll`, *optional*):
        #     Message is a native poll, information about the poll.
        #
        # dice (:obj:`~pyrogram.types.Dice`, *optional*):
        #     A dice containing a value that is randomly generated by Telegram.
        #
        # new_chat_members (List of :obj:`~pyrogram.types.User`, *optional*):
        #     New members that were added to the group or supergroup and information about them
        #     (the bot itself may be one of these members).
        #
        # left_chat_member (:obj:`~pyrogram.types.User`, *optional*):
        #     A member was removed from the group, information about them (this member may be the bot itself).
        #
        # chat_join_type (:obj:`~pyrogram.enums.ChatJoinType`, *optional*):
        #     This field will contain the enumeration type of how the user had joined the chat.

        new_chat_title (``str``, *optional*):
            A chat title was changed to this value.

        new_chat_photo (:obj:`~pyrogram.types.Photo`, *optional*):
            A chat photo was change to this value.

        # delete_chat_photo (``bool``, *optional*):
        #     Service message: the chat photo was deleted.
        #
        # group_chat_created (``bool``, *optional*):
        #     Service message: the group has been created.
        #
        # supergroup_chat_created (``bool``, *optional*):
        #     Service message: the supergroup has been created.
        #     This field can't be received in a message coming through updates, because bot can't be a member of a
        #     supergroup when it is created. It can only be found in reply_to_message if someone replies to a very
        #     first message in a directly created supergroup.
        #
        # channel_chat_created (``bool``, *optional*):
        #     Service message: the channel has been created.
        #     This field can't be received in a message coming through updates, because bot can't be a member of a
        #     channel when it is created. It can only be found in reply_to_message if someone replies to a very
        #     first message in a channel.

        migrate_to_chat_id (``int``, *optional*):
            The group has been migrated to a supergroup with the specified identifier.
            This number may be greater than 32 bits and some programming languages may have difficulty/silent defects
            in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float
            type are safe for storing this identifier.

        migrate_from_chat_id (``int``, *optional*):
            The supergroup has been migrated from a group with the specified identifier.
            This number may be greater than 32 bits and some programming languages may have difficulty/silent defects
            in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float
            type are safe for storing this identifier.

        pinned_message (:obj:`~pyrogram.types.Message`, *optional*):
            Specified message was pinned.
            Note that the Message object in this field will not contain further reply_to_message fields even if it
            is itself a reply.

        game_high_score (:obj:`~pyrogram.types.GameHighScore`, *optional*):
            The game score for a user.
            The reply_to_message field will contain the game Message.

        views (``int``, *optional*):
            Channel post views.

        forwards (``int``, *optional*):
            Channel post forwards.

        via_bot (:obj:`~pyrogram.types.User`):
            The information of the bot that generated the message from an inline query of a user.

        outgoing (``bool``, *optional*):
            Whether the message is incoming or outgoing.
            Messages received from other chats are incoming (*outgoing* is False).
            Messages sent from yourself to other chats are outgoing (*outgoing* is True).
            An exception is made for your own personal chat; messages sent there will be incoming.

        external_reply (:obj:`~pyrogram.types.ExternalReplyInfo`, *optional*):
            Information about the message that is being replied to, which may come from another chat or forum topic.

        quote (:obj:`~pyrogram.types.TextQuote`, *optional*):
            Chosen quote from the replied message.

        matches (List of regex Matches, *optional*):
            A list containing all `Match Objects <https://docs.python.org/3/library/re.html#match-objects>`_ that match
            the text of this message. Only applicable when using :obj:`Filters.regex <pyrogram.Filters.regex>`.

        # command (List of ``str``, *optional*):
        #     A list containing the command and its arguments, if any.
        #     E.g.: "/start 1 2 3" would produce ["start", "1", "2", "3"].
        #     Only applicable when using :obj:`~pyrogram.filters.command`.
        #
        # forum_topic_created (:obj:`~pyrogram.types.ForumTopicCreated`, *optional*):
        #     Service message: forum topic created
        #
        # forum_topic_closed (:obj:`~pyrogram.types.ForumTopicClosed`, *optional*):
        #     Service message: forum topic closed
        #
        # forum_topic_reopened (:obj:`~pyrogram.types.ForumTopicReopened`, *optional*):
        #     Service message: forum topic reopened
        #
        # forum_topic_edited (:obj:`~pyrogram.types.ForumTopicEdited`, *optional*):
        #     Service message: forum topic edited
        #
        # general_forum_topic_hidden (:obj:`~pyrogram.types.GeneralForumTopicHidden`, *optional*):
        #     Service message: general forum topic hidden
        #
        # general_forum_topic_unhidden (:obj:`~pyrogram.types.GeneralForumTopicUnhidden`, *optional*):
        #     Service message: general forum topic unhidden
        #
        # video_chat_scheduled (:obj:`~pyrogram.types.VideoChatScheduled`, *optional*):
        #     Service message: voice chat scheduled.
        #
        # history_cleared (:obj:`~pyrogram.types.HistoryCleared`, *optional*):
        #     Service message: history cleared
        #
        # video_chat_started (:obj:`~pyrogram.types.VideoChatStarted`, *optional*):
        #     Service message: the voice chat started.
        #
        # video_chat_ended (:obj:`~pyrogram.types.VideoChatEnded`, *optional*):
        #     Service message: the voice chat has ended.
        #
        # video_chat_members_invited (:obj:`~pyrogram.types.VoiceChatParticipantsInvited`, *optional*):
        #     Service message: new members were invited to the voice chat.
        #
        # phone_call_started (:obj:`~pyrogram.types.PhoneCallStarted`, *optional*):
        #     Service message: phone call started.
        #
        # phone_call_ended (:obj:`~pyrogram.types.PhoneCallEnded`, *optional*):
        #     Service message: phone call ended.
        #
        # web_app_data (:obj:`~pyrogram.types.WebAppData`, *optional*):
        #     Service message: web app data sent to the bot.
        #
        # paid_messages_refunded (:obj:`~pyrogram.types.PaidMessagesRefunded`, *optional*):
        #     Service message: paid messages refunded.
        #
        # paid_messages_price_changed (:obj:`~pyrogram.types.PaidMessagesPriceChanged`, *optional*):
        #     Service message: paid messages price.
        #
        # direct_message_price_changed (:obj:`~pyrogram.types.DirectMessagePriceChanged`, *optional*):
        #     Service message: direct messages price.
        #
        # checklist_tasks_done (:obj:`~pyrogram.types.ChecklistTasksDone`, *optional*):
        #     Service message: checklist tasks done.
        #
        # checklist_tasks_added (:obj:`~pyrogram.types.ChecklistTasksAdded`, *optional*):
        #     Service message: checklist tasks added.
        #
        # gift_code (:obj:`~pyrogram.types.GiftCode`, *optional*):
        #     Service message: gift code information.
        #
        # gifted_premium (:obj:`~pyrogram.types.GiftedPremium`, *optional*):
        #     Service message: gifted premium information.
        #
        # gifted_stars (:obj:`~pyrogram.types.GiftedStars`, *optional*):
        #     Service message: gifted stars information.
        #
        # gift (:obj:`~pyrogram.types.Gift`, *optional*):
        #     Service message: star gift information.
        #
        # suggest_profile_photo (:obj:`~pyrogram.types.Photo`, *optional*):
        #     Service message: suggested profile photo.
        #
        # users_shared (:obj:`~pyrogram.types.UsersShared`, *optional*):
        #     Service message: users shared information.
        #
        # chat_shared (:obj:`~pyrogram.types.ChatShared`, *optional*):
        #     Service message: chat shared information.
        #
        # successful_payment (:obj:`~pyrogram.types.SuccessfulPayment`, *optional*):
        #     Service message: successful payment.
        #
        # refunded_payment (:obj:`~pyrogram.types.RefundedPayment`, *optional*):
        #     Service message: refunded payment.
        #
        # giveaway_created (``bool``, *optional*):
        #     Service message: giveaway launched.
        #
        # giveaway_winners (:obj:`~pyrogram.types.GiveawayWinners`, *optional*):
        #     A giveaway with public winners was completed.
        #
        # giveaway_completed (:obj:`~pyrogram.types.GiveawayCompleted`, *optional*):
        #     Service message: a giveaway without public winners was completed.
        #
        # chat_set_theme (:obj:`~pyrogram.types.ChatTheme`, *optional*):
        #     Service message: The chat theme was changed.
        #
        # chat_set_background (:obj:`~pyrogram.types.ChatBackground`, *optional*):
        #     Service message: The chat background was changed.
        #
        # set_message_auto_delete_time (``int``, *optional*):
        #     Service message: The auto-delete or self-destruct timer for messages in the chat has been changed.
        #
        # chat_boost (``int``, *optional*):
        #     Service message: The chat was boosted by the sender of the message.
        #     Number of times the chat was boosted.
        #
        # write_access_allowed (:obj:`~pyrogram.types.WriteAccessAllowed`, *optional*):
        #     Service message: the user allowed the bot to write messages after adding it to the attachment or side menu, launching a Web App from a link, or accepting an explicit request from a Web App sent by the method `requestWriteAccess <https://core.telegram.org/bots/webapps#initializing-mini-apps>`__

        connected_website (``str``, *optional*):
            The domain name of the website on which the user has logged in. `More about Telegram Login <https://core.telegram.org/widgets/login>`__

        # contact_registered (:obj:`~pyrogram.types.ContactRegistered`, *optional*):
        #     Service message: Contact registered in Telegram.
        #
        # proximity_alert_triggered (:obj:`~pyrogram.types.ProximityAlertTriggered`, *optional*):
        #     Service message: A user in the chat came within proximity alert range.
        #
        # giveaway_prize_stars (:obj:`~pyrogram.types.GiveawayPrizeStars`, *optional*):
        #     Service message: Stars were received by the current user from a giveaway.
        #
        # screenshot_taken (:obj:`~pyrogram.types.ScreenshotTaken`, *optional*):
        #     Service message: screenshot of a message in the chat has been taken.

        business_connection_id (``str``, *optional*):
            Unique identifier of the business connection from which the message was received.
            If non-empty, the message belongs to a chat of the corresponding business account that is independent from any potential bot chat which might share the same identifier.
            This update may at times be triggered by unavailable changes to message fields that are either unavailable or not actively used by the current bot.

        reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
            Additional interface options. An object for an inline keyboard, custom reply keyboard,
            instructions to remove reply keyboard or to force a reply from the user.

        reactions (:obj:`~pyrogram.types.MessageReactions`):
            Reactions of this message.

        send_paid_messages_stars (``int``, *optional*):
            The number of Telegram Stars the sender paid to send the message.

        raw (:obj:`~pyrogram.raw.types.Message`, *optional*):
            The raw message object, as received from the Telegram API.

        link (``str``, *property*):
            Generate a link to this message, only for groups and channels.

        content (``str``, *property*):
            The text or caption content of the message.

        unread_media (``bool``, *optional*):
            True, if there are unread media attachments in this message.

        silent (``bool``, *optional*):
            True, if the message sent without notification.

        legacy (``bool``, *optional*):
            True, if the message is a legacy message.
            This means that the message is based on the old layer and should be refetched with the new layer.

        pinned (``bool``, *optional*):
            True, if the message is pinned.

        restriction_reason (List of :obj:`~pyrogram.types.RestrictionReason`, *optional*):
            Contains a list of human-readable description of the reason why access to this message must be restricted.

        fact_check (:obj:`~pyrogram.types.FactCheck`, *optional*):
            Information about fact-check added to the message.

        channel_post (``bool``, *optional*):
            True, if the message is a channel post.

"""
