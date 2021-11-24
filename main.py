import sys
import discord
from discord.ext import commands
    
intents = discord.Intents.default()
intents.members = True

token = open("token.txt", 'r').readlines(1)[0].strip()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')
roles_dict = {
"1. Semester": '1️⃣',
"2. Semester": '2️⃣',
"3. Semester": '3️⃣',
"4. Semester": '4️⃣',
"5. Semester": '5️⃣',
"6. Semester": '6️⃣',
"Informatik": '🇮',
"AI": '🇦',
"Bachelor": '🇧',
"Master": '🇲',
"∞.Semester": '♾️',
}

roles = set(map(lambda s: s.encode('unicode-escape').decode('ASCII'), roles.values()))

ROLE_MSG_ID = 756093869187137537

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
    await member.send(f"Welcome to the Informatik & AI Discord Server! Here you can find other students of the JKU Linz who are also studying Informatik or AI from your and other semesters. Although the server is primarily aimed at JKU students, everyone is welcome.\n\n"
                      f"As you can see, there are categories for each semester (sorted by curriculum) and there is a text channel for each course. There you can ask questions to fellow students and discuss the subject. If a course consists of several parts (e.g. exercise and lecture), you can discuss both in the respective channel.\n\n\n"
                      f"So that you don't get annoyed by the other categories, you can mute them by right clicking on them. (You can also hide all muted channel in the dropdown on the top left, dont forget to untick this if you want to see them again!) "
                      f"If you want to appear here with your real name, you can do this with a nickname (click on the arrow next to the server name in the upper left corner and then click on 'Change nickname'). This only changes the name on this server, so you can remain anonymous on other servers.\n\n"
                      f"Link to invite new people: https://discord.gg/wAek576\n\n"
                      f"If you need some help or there are problems with the server (or with someone on the server), don't be afraid to someone from @ÖH.\n\n"
                      f"If you want to assign yourself a role go to this message and click the appropriate reactions: https://discordapp.com/channels/370458917073059841/497699283772899348/756093869187137537 ")

def add_or_remove(payload, mode):
    member = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    emoji = payload.emoji.name.encode('unicode-escape').decode('ASCII')
    if payload.message_id == ROLE_MSG_ID and emoji in roles:
        role = discord.utils.get(guild.roles, name=emoji)
        if mode == "add":
            await member.add_roles(role, atomic=True)
        elif mode == "remove":
            await member.remove_roles(role, atomic=True)


@bot.event
async def on_raw_reaction_add(payload):
    add_or_remove(payload, "add")


@bot.event
async def on_raw_reaction_remove(payload):
    add_or_remove(payload, "remove")


bot.run(token)
