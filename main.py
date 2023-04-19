import discord

ds_token = "7DSbOv81IVAVHMA2_R53zh-hAgj07XlG"


class  myClient(discord.Client):
    async def on_ready(self):
        print("Logged in successfully!")

intents = discord.Intents.default()
client = myClient(intents=intents)
client.run(token=ds_token)