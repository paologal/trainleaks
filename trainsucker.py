import time
import requests
import json
from pprint import pprint

baseUrl = 'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/'
action = 'soluzioniViaggioNew'
station0 = '1480'
station1 = '1485'

def addTrains(trains, url):
    response = requests.get(url)
    solutions=response.json()['soluzioni']
    if response.ok:
        for i in range(0, len(solutions)):
            trainList.append(int(solutions[i]['vehicles'][0]['numeroTreno']))
    else:
        response.raise_for_status()      

def getTrains(trains, start, end):
    url = [baseUrl + action + '/' + start + '/' + end + '/' + time.strftime("%Y-%m-%d") + 'T00:00:00',
           baseUrl + action + '/' + end + '/' + start + '/' + time.strftime("%Y-%m-%d") + 'T00:00:00']
    addTrains(trains, url[0])
    addTrains(trains, url[1])


trainList = []

getTrains(trainList, station0, station1)

pprint(trainList)
