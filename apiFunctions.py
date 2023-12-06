import requests

api_key = 'Enter api-key here'


# Function that gets a player account

def get_account(name, region, tag):
    cont = ''

    if region == 'NA1':
        cont = 'americas'
    elif region == 'EUW1' or region == 'EUN1':
        cont = 'europe'
    elif region == 'KR':
        cont = 'asia'

    api_url1 = 'https://'
    api_url2 = '.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
    api_url = api_url1 + cont + api_url2 + name + '/' + tag + '?api_key=' + api_key
    resp = requests.get(api_url)
    account = resp.json()
    return account

# Get summoner profile by puuid


def profile_info(pid, region):
    api_url1 = 'https://'
    api_url2 = '.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'
    api_url = api_url1 + region + api_url2 + pid + '?api_key=' + api_key
    resp = requests.get(api_url)
    info = resp.json()
    return info

# Function that splits user input into summoner name and tag


def find_name(name):
    n = ''
    tag = ''
    hashtag = False
    for c in name:
        if c == '#':
            hashtag = True

        if hashtag == False:
            n += c
        else:
            tag += c
    return [n, tag[1:]]


def recent_matches(player_id):
    pass


def get_icon(icon_id):
    pass
