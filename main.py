import sys
import discord
from discord.ext import commands

def read_token():
    with open("token.txt", 'r') as f:
        lines = f.readlines()
        return lines[0].strip()
    
intents = discord.Intents.default()
intents.members = True

token = read_token()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')
roles_dict = {"1. Semester": '1️⃣'.encode('unicode-escape').decode('ASCII'),
              "2. Semester": '2️⃣'.encode('unicode-escape').decode('ASCII'),
              "3. Semester": '3️⃣'.encode('unicode-escape').decode('ASCII'),
              "4. Semester": '4️⃣'.encode('unicode-escape').decode('ASCII'),
              "5. Semester": '5️⃣'.encode('unicode-escape').decode('ASCII'),
              "6. Semester": '6️⃣'.encode('unicode-escape').decode('ASCII'),
              "Informatik": '🇮'.encode('unicode-escape').decode('ASCII'),
              "AI": '🇦'.encode('unicode-escape').decode('ASCII'),
              "Bachelor": '🇧'.encode('unicode-escape').decode('ASCII'),
              "Master": '🇲'.encode('unicode-escape').decode('ASCII'),
              "∞.Semester": '♾️'.encode('unicode-escape').decode('ASCII'),
              "PhD": '🥼'.encode('unicode-escape').decode('ASCII'),
              "Alumni": '🎓'.encode('unicode-escape').decode('ASCII'),
              "Informatik-Cafe": '🫖'.encode('unicode-escape').decode('ASCII'),
              "AI-Cafe": '☕'.encode('unicode-escape').decode('ASCII')}

role_msg_id = 756093869187137537

#######################################################################################################################
# EVENTS #
#######################################################################################################################

@bot.event
async def on_ready():
    print("Ready")
    sys.stdout.flush()
    game = discord.Game("with roles")
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the Informatik & AI Discord Server! Here you can find other students of the JKU Linz who are also studying Informatik or AI. Although the server is primarily aimed at JKU students, everyone is welcome.\n\n"
                      f"Check out our #welcome-Channel to find out more about the structure of the server, and to assign yourself a role: https://discord.com/channels/370458917073059841/497699283772899348/632232644570251264 \n\n"
                      f"Before posting, make sure you have read the server-rules in #rules! They include rules against discriminatory jokes, spamming and advertising: https://discord.com/channels/370458917073059841/911658031828328448/911940999666880572 \n\n"
                      f"This server is hosted by the Student Union (ÖH) for Informatics and AI. If you need help or there are problems with the server (or with someone on the server), don't be afraid to tell someone from @ÖH. Enjoy your time here!\n\n\n"
                      f"Willkommen am Informatik & AI Discord Server! Hier kannst du dich mit anderen Studierenden der JKU Linz austauschen, die ebenfalls Informatik oder AI studieren. Obwohl der Server sich primär an Studierende richtet, sind alle willkommen.\n\n"
                      f"Sieh dir den #welcome-Channel an, um mehr über die Struktur des Servers zu lernen, und dir eine Rolle zuzuteilen: https://discord.com/channels/370458917073059841/497699283772899348/632232644570251264 \n\n"
                      f"Bitte lies dir vor dem Posten die Server-Richtlinien in #rules durch! Sie beinhalten Regeln gegen diskriminierende Witze, Spamming und Werbung: https://discord.com/channels/370458917073059841/911658031828328448/911940999666880572 \n\n"
                      f"Der Server wird von der Studienvertretung für Informatik & AI (ÖH) betrieben. Falls du Probleme mit dem Server (oder mit jemandem auf dem Server) hast, bitte melde dich einfach bei jemandem mit der @ÖH-Rolle. Wir wünschen dir viel Spaß am Server!")

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    msg_id = payload.message_id
    a_emoji = payload.emoji.name.encode('unicode-escape').decode('ASCII')
    if msg_id == role_msg_id:
        for role_name, emoji in roles_dict.items():
            if emoji == a_emoji:
                role = discord.utils.get(guild.roles, name=role_name)
                await member.add_roles(role, atomic=True)

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    msg_id = payload.message_id
    a_emoji = payload.emoji.name.encode('unicode-escape').decode('ASCII')
    if msg_id == role_msg_id:
        for role_name, emoji in roles_dict.items():
            if emoji == a_emoji:
                role = discord.utils.get(guild.roles, name=role_name)
                await member.remove_roles(role, atomic=True)

bot.run(token)


