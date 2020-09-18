import discord
from discord.ext import commands

def read_token():
    with open("token.txt", 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()
bot = commands.Bot(command_prefix='.')
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
              "∞.Semester": '♾️'.encode('unicode-escape').decode('ASCII')}

role_msg_id = 756093869187137537

#######################################################################################################################
# EVENTS #
#######################################################################################################################

@bot.event
async def on_ready():
    print("Ready")
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


