import discord
from discord import * 
import os
import random
from env import token
from discord.ext import commands
from discord.utils import get

client = discord.Intents().all()
bot = commands.Bot(command_prefix="!", description="Noot Bot")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('NootNoot.com'))
    print("Ready !")


@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = "monde des noot noot"
    user_message = str(message.content)

    
    if message.author == bot.user:
        return

    if channel == "monde des noot noot ":
        if user_message.lower() == "!noot ?":
            await message.channel.send('Bonjour Professeur {0.author.mention} ! Allez-vous bien ? Si oui tapez !bien sinon tapez !mal'.format(message) )
        elif user_message.lower() == "!bien":
            await message.channel.send(f'Parfait, Bonne Chance pour vos expériences !')
        elif user_message.lower() == "!mal":
            await message.channel.send(f'Mince :/ , voulez-vous une blague pour vous remonter le morale ? Tapez !oui si oui sinon tapez !non')
        elif user_message.lower() == "!oui":
            jokes = [" Que dit une mère à son fils geek quand le dîner est servi ? \
                     Alt Tab. \
                     N'oubliez pas de taper !merci , la politesse avant tout",
                     "Quel Pokemon a une mitraillette ? \
                     Ratatatatatatatatata.\
                     N'oubliez pas de taper !merci , la politesse avant tout",
                     "A quoi sert Internet Explorer ? \
                     A télécharger Google Chrome. \
                        N'oubliez pas de taper !merci , la politesse avant tout" , ]
            await message.channel.send(random.choice(jokes))
        elif user_message.lower() == "!merci":
            await message.channel.send(f'Mais de rien ! Maintenant, bonne chance pour vos expériences ;)')
        elif user_message.lower() == "!non":
            await message.channel.send(f'Pas de souci et bien Bonne chance pour vos expériences !')
        elif user_message.lower() == "!.":
            await message.channel.send(f'$')
        elif user_message.lower() == "!bye":   
            await message.channel.send('Au plaisir de vous revoir Professeur {0.author.mention}'.format(message))
        elif user_message.lower() == "!joke":
            jokes = [" Que dit une mère à son fils geek quand le dîner est servi ? \
                     Alt Tab. ",
                     "Quel Pokemon a une mitraillette ? \
                     Ratatatatatatatatata.",
                     "A quoi sert Internet Explorer ? \
                     A télécharger Google Chrome. ", ]
            await message.channel.send(random.choice(jokes))
        elif user_message.lower() == "!tell me a number":
            nomber = ["1 ",
                      "2 ",
                      "3 ",
                      "4 "]
            await message.channel.send(random.choice(nomber))

    
    if message.content.startswith("!clear"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()


@bot.command()
async def InfoServeur(ctx):
    if serveur.lower() == "!InfoServeur":

        serveur = ctx.guild
        nombreDeChainesTexte = len(serveur.text_channels)
        nombreDeChainesVocale = len(serveur.voice_channels)
        Description_du_serveur = serveur.description
        Nombre_de_personnes = serveur.member_count
        Nom_du_serveur = serveur.name
        message = f"Le serveur **{Nom_du_serveur}** contient *{Nombre_de_personnes}* personnes ! \nLa description du serveur est {Description_du_serveur}. \nCe serveur possède {nombreDeChainesTexte} salons écrit et {nombreDeChainesVocale} salon vocaux."
        await ctx.send(message)




bot.run(token)