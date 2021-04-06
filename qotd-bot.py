import discord

TOKEN = 
CHANNEL_ID = 


class MyClient(discord.Client):
    async def on_message(self, message):
        if message.channel.id == CHANNEL_ID:
            qotd = message.channel
            effMessage = message.content.lower()
            if 'q:' in effMessage:
                split = effMessage.split('q:')
                question = split[-1].strip()
                if question != "same":
                    print(f'New question: {question}')
                    await qotd.edit(topic=f"The current question is: {question}")
            
            
client = MyClient()
client.run(TOKEN)
