import requests
import json

game_url = "https://www.speedrun.com/api/v1/games?orderby=released&max=100"
platform_url = "https://www.speedrun.com/api/v1/platforms"

game_response = requests.get(game_url).json()
platform_response = requests.get(platform_url).json()

game_response_data = game_response['data']
platform_response_data = platform_response['data']


nameList = []

gameDict_unfiltered = {
    "nameList" : [],
    "platformList" : [],
    "yearList" : []
}

for game in game_response_data:
    if (game['names']['international'] is not None) and (len(game['platforms']) != 0) and (game['released'] is not None): 
        gameDict_unfiltered['nameList'].append(game['names']['international'])
        gameDict_unfiltered['platformList'].append(game['platforms'][0])
        gameDict_unfiltered['yearList'].append(game['released'])
    else:
        print("Game missing condition")
        pass

gameDict_filtered = {
    "nameList" : [],
    "platformIdList" : [],
    "yearList" : [],
    "platformName" : []
}

assert(len(gameDict_unfiltered['nameList']) == len(gameDict_unfiltered['platformList']) == len(gameDict_unfiltered['yearList']))


for platform in platform_response_data:
    if platform['id'] in gameDict_unfiltered['platformList']:
        i = gameDict_unfiltered['platformList'].index(platform['id'])
        print(platform['id'])
        gameDict_filtered['nameList'].append(gameDict_unfiltered['nameList'][i])
        gameDict_filtered['platformIdList'].append(gameDict_unfiltered['platformList'][i])
        gameDict_filtered['yearList'].append(gameDict_unfiltered['yearList'][i])
        gameDict_filtered['platformName'].append(platform['name'])
        
        
print(gameDict_unfiltered)
print("---------------------------------")
print(gameDict_filtered)


for i in range(0, len(gameDict_filtered['nameList'])):
    print(gameDict_filtered['nameList'][i] + " ==> " + str(gameDict_filtered['yearList'][i]) + " ==> " + gameDict_filtered['platformName'][i])

  




    
    # "nameList" : 'Stunt Cycle', 'Drag Strip', 'Basic Math (a.k.a. Fun with Numbers)', kjsdflkj lkjdsf
    # "platformList" : 'o0644863', 'gde31w9k', 'o0644863', v1pxpq46, ____ , lkjdsfl
    # "yearList" : 1976, 098234, 098234 , 098234
    # v1pxpq46 908234098 n098234098324 0982343
