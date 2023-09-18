import requests
import discord
import asyncio
import itertools

client = discord.Client()

COLORS = {
    'RED1': '\033[38;5;196m',
    'RED2': '\033[38;5;197m',
    'RED3': '\033[38;5;198m',
    'ORANGE1': '\033[38;5;208m',
    'ORANGE2': '\033[38;5;209m',
    'ORANGE3': '\033[38;5;214m',
    'YELLOW1': '\033[38;5;220m',
    'YELLOW2': '\033[38;5;221m',
    'YELLOW3': '\033[38;5;222m',
    'GREEN1': '\033[38;5;46m',
    'GREEN2': '\033[38;5;47m',
    'GREEN3': '\033[38;5;48m',
    'BLUE1': '\033[38;5;21m',
    'BLUE2': '\033[38;5;22m',
    'BLUE3': '\033[38;5;23m',
    'CYAN1': '\033[38;5;51m',
    'CYAN2': '\033[38;5;50m',
    'CYAN3': '\033[38;5;49m',
    'MAGENTA1': '\033[38;5;201m',
    'MAGENTA2': '\033[38;5;200m',
    'MAGENTA3': '\033[38;5;199m',
    'PURPLE1': '\033[38;5;93m',
    'PURPLE2': '\033[38;5;92m',
    'PURPLE3': '\033[38;5;91m',
    'PINK1': '\033[38;5;219m',
    'PINK2': '\033[38;5;218m',
    'PINK3': '\033[38;5;217m',
    'TEAL1': '\033[38;5;38m',
    'TEAL2': '\033[38;5;37m',
    'TEAL3': '\033[38;5;36m',
    'INDIGO1': '\033[38;5;55m',
    'INDIGO2': '\033[38;5;54m',
    'INDIGO3': '\033[38;5;53m',
    'LIME1': '\033[38;5;76m',
    'LIME2': '\033[38;5;77m',
    'LIME3': '\033[38;5;78m',
    'OLIVE1': '\033[38;5;106m',
    'OLIVE2': '\033[38;5;107m',
    'OLIVE3': '\033[38;5;108m',
    'BROWN1': '\033[38;5;130m',
    'BROWN2': '\033[38;5;131m',
    'BROWN3': '\033[38;5;132m',
    'GREY1': '\033[38;5;242m',
    'GREY2': '\033[38;5;243m',
    'GREY3': '\033[38;5;244m',
    'END': '\033[0m'
}

## ^^^ REMOVE ANY COLOR YOU DONT WANT BY JUST SIMPLY REMOVING THE LINE ^^^

async def get_discord_username(discord_id, token):
    headers = {
        'Authorization': f'Bot {token}',
    }
    r = requests.get(f'https://discord.com/api/v9/users/{discord_id}', headers=headers)
    if r.status_code == 200:
        return r.json()['username']
    else:
        return "Unknown"

async def main():
    server_ip = input("Enter the server IP (Eg. XX.XXX.XXX.XX:XXXX): ")
    
    r = requests.get(f'http://{server_ip}/players.json')
    
    if r.status_code != 200:
        print("Failed to fetch players.")
        return
    
    players = r.json()
    
    token = "MTE1MzQxNTUwMDU0NjcwMzM2MA.GnO97k.zJ1K1Yg9HhhwWwKpA09Mm1IlET2OLn9ZMTwDwo" ##!!! ADD A DISCORD BOT TOKEN. MAKE A FRESH ONE !!! 

    color_cycle = itertools.cycle(COLORS.values())

    
    print("\nPlayers Information:")
    print("--------------------")
    
    for player in players:
        color = next(color_cycle) 
        
        discord_id = None
        for identifier in player.get("identifiers", []):
            if identifier.startswith("discord:"):
                discord_id = identifier.split(":")[1]
                break
        
        if discord_id:
            username = await get_discord_username(discord_id, token)
            print(f"{color}Player: {player['name']}{COLORS['END']}, "
                  f"{color}Discord ID: {discord_id}{COLORS['END']}, "
                  f"{color}Discord Username: {username}{COLORS['END']}")
            
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

