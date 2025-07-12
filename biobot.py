import asyncio
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()
import discord
from discord.ext import commands

discord.opus.load_opus('/Users/Favio/homebrew/Cellar/opus/1.5.2/lib/libopus.0.dylib')

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True
bot = commands.Bot(command_prefix='*', intents=intents)


@bot.command()
async def bio(ctx, response=None):
    await ctx.send(f"Hola, soy un asistente que te ayuda con la contaminación: {bot.user}!")
    await ctx.send("Para empezar, dime qué tipo de contaminación te interesa: aire, agua, suelo o acustica.")

    def check(message):
        return (
            message.author == ctx.author and
            message.channel == ctx.channel and
            message.content.lower() in ['aire', 'agua', 'suelo', 'acustica']
        )

    try:
        response = await bot.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No recibi respuesta a tiempo, intentalo denuevo.")
        return

    tipo = response.content.lower()
    if response:
        if tipo == 'aire':
            await ctx.send("La contaminacion del aire ocurre cuando sustancias mortales o nocivas, como partículas solidas y gases se dispersan en la atmósfera")
            await ctx.send("stas sustancias provienen principalmente de vehículos, fábricas, quema de combustibles y procesos industriales. Los efectos incluyen problemas respiratorios, enfermedades cardiovasculares y, según estudios recientes, un mayor riesgo de tumores cerebrales como los meningiomas")
            await ctx.send("https://tenor.com/view/roblox-industrialist-industrialist-players-pollution-gif-6673786930248027286")
        elif tipo == 'agua':
            await ctx.send("La contaminación del agua sucede cuando sustancias químicas, microorganismos o residuos alteran la calidad del agua, haciéndola tóxica para el consumo humano, la fauna y la flora. Las principales causas incluyen:")
            await ctx.send("Vertidos industriales y domésticos sin tratar.")
            await ctx.send("Agricultura intensiva que utiliza pesticidas y fertilizantes.")
            await ctx.send("Derrames de petróleo y productos químicos.")
            await ctx.send("https://tenor.com/view/dirty-water-the-simpsons-bart-simpson-lisa-simpson-pollution-gif-12793952")
        elif tipo == 'suelo':
            await ctx.send("La contaminación del suelo implica la alteración de sus características físicas, químicas y biológicas debido a la presencia de sustancias tóxicas.")
            await ctx.send("Las principales causas incluyen:")
            await ctx.send("Uso excesivo de pesticidas y fertilizantes en la agricultura.")
            await ctx.send("Vertidos industriales y residuos sólidos mal gestionados.")
            await ctx.send("Derrames de productos quimicos y metales pesados.")
            await ctx.send("https://tenor.com/view/smog-air-pollution-pollution-bad-air-gif-12428217")
        elif tipo == 'acustica':
            await ctx.send("La contaminación acústica se refiere a la presencia de ruidos excesivos en el ambiente, que pueden afectar la salud y el bienestar de las personas.")
            await ctx.send("Las principales fuentes incluyen:")
            await ctx.send("Tráfico vehicular y ferroviario.")
            await ctx.send("Obras de construcción y maquinaria pesada.")
            await ctx.send("Actividades industriales y comerciales.")
            await ctx.send("https://tenor.com/view/vagrant-queen-vagrants-syfy-vagrant-loud-gif-16912713")
import random

@bot.command()
async def biofact(ctx):
    await ctx.send("Aqui tienes un dato interestante sobre la contaminación")
    await ctx.send(random.choice([
        "La contaminación del aire causa aproximadamente 7 millones de muertes prematuras al año a nivel mundial.",
        "El 80 porciento e la contaminación del agua proviene de fuentes terrestres, como la agricultura y la industria.",
        "Se estima que el 30 porciento e los suelos agrícolas en el mundo están degradados debido a la contaminación y prácticas insostenibles.",
        "La contaminación acústica puede afectar la salud mental y física, aumentando el estrés y el riesgo de enfermedades cardiovasculares.",
        "El plástico representa el 80 porcfiento de la contaminación marina, afectando a la vida marina y a los ecosistemas acuáticos.",
        "El dióxido de carbono (CO2) es el principal gas de efecto invernadero, y su concentración ha aumentado un 40 porciento sde la Revolución Industrial.",
        "La contaminación del aire puede reducir la esperanza de vida en hasta 2 años en algunas regiones del mundo.",
        "El reciclaje de papel puede reducir la contaminación del agua en un 35% y la contaminación del aire en un 74% en comparación con la producción de papel nuevo.",
        "Las emisiones de vehículos son responsables de aproximadamente el 30 porciento e la contaminación del aire en las ciudades.",
        "El ruido del tráfico puede aumentar el riesgo de enfermedades cardiovasculares y problemas de sueño."
    ]))

