# Bot_discord

import discord
from discord import *
from discord.ext import commands
import nextcord
import asyncio
from env import TOKEN
from quizz_data import quizzData
import random

# Les commandes demandés
avancement = 0

score = 0
quizz_started = False

command_list = "/start, /astuce, /help, /reset, /score, /blague, /clear"
quizz = []


def reset_score():
    global score
    score = 0
    return "Score remis à 0 avec succès !"


def display_score():
    global score
    return "Le score actuel est de "+str(score)


async def start_bot(interaction):
    global score, avancement, quizz, quizz_started
    quizz_started = True
    quizz = sorted(quizzData, key=lambda x: random.random())
    score = 0
    avancement = 0
    await send_to_discord(interaction, "Demarrage du quizz en cours...\n")
    await send_to_discord(interaction, "Question "+str(avancement+1)+"/"+str(len(quizz))+" : **"+quizz[avancement]["question"]+"**")


async def stop_bot(interaction):
    global quizz_started
    quizz_started = False
    await send_to_discord(interaction, "Quizz terminé ! Score final : "+str(score))


async def send_to_discord(data, message):
    await data.send(message)


async def display_help(interaction):
    global command_list
    await interaction.send("Liste des commandes possibles : \n"+command_list)


# Traiter les reponses au quizz
async def treat_message(data, bot):
    global score, quizz, avancement
    message = data.content

    if data.author == bot.user or not quizz_started:
        return

    if (message.lower() == quizz[avancement]["reponse"].lower()):
        score = score+10
        await data.channel.send(":white_check_mark: **Bonne réponse !** ")
    else:
        await data.channel.send(":x: **Mauvaise réponse !**")
        await data.channel.send("La bonne réponse était : "+quizz[avancement]["reponse"])
    avancement = avancement+1

    if (avancement >= len(quizz)):
        await data.channel.send("Quizz terminé ! Score final : "+str(score))
    else:
        await data.channel.send("Question "+str(avancement+1)+"/"+str(len(quizz))+" : **"+quizz[avancement]["question"]+"**")


# Initialisation du Bot discord
intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/",
                   description="Bot de Nivek", intents=intents)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Streaming(name="sur Youtube !", platform="Youtube", url="https://www.youtube.com/watch?v=p7YXXieghto"))
    print("Ready !")


@bot.event
async def on_message(message):
    global score
    # user_message = str(message.content)
    await treat_message(message, bot)


@bot.slash_command(description="Help me Please!")
async def help(interaction: nextcord.Interaction):
    await display_help(interaction)


@bot.slash_command(description="Demarrer le quizz!")
async def start(interaction: nextcord.Interaction):
    await start_bot(interaction)


@bot.slash_command(description="Remettre a zero le score")
async def reset(interaction: nextcord.Interaction):
    await interaction.send(reset_score())
    await start_bot(interaction)


@bot.slash_command(description="Afficher le score")
async def score(interaction: nextcord.Interaction):
    await interaction.send(display_score())


@bot.slash_command(description="Demander une astuce pour la question courante du quizz")
async def astuce(interaction: nextcord.Interaction):
    global avancement, quizz
    await interaction.send(quizz[avancement]["indice"])


# Commandes supplementaires :

@bot.slash_command(description="Demander de raconter une blague")
async def blague(interaction: nextcord.Interaction):
    jokes = [" Que dit une mère à son fils geek quand le dîner est servi ? \
                     \n**Alt Tab.**",
             "Quel Pokemon a une mitraillette ? \
                     \n**Ratatatatatatatatatata.**",
             "A quoi sert Internet Explorer ? \
                     \n**A télécharger Google Chrome.**",
             "Qu'est-ce qui est vert et blanc, et navigue sous l'eau \
                     \n**Un Chou-Marin**",
             "Qu'est ce qui est vert, qui monte et qui descend \
                     \n**Un petit pois dans un ascenceur**",

             ]
    await interaction.send(random.choice(jokes)+"\n:rofl:")


@bot.slash_command(description="Effacer l'historique de discution")
async def clear(interaction: nextcord.Interaction):
    await interaction.channel.purge(limit=100)


@bot.slash_command(description="Arrete le quizz!")
async def stop(interaction: nextcord.Interaction):
    await stop_bot(interaction)


# Lancement du bot discord ...
bot.run(TOKEN)
