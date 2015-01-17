import json
from pprint import pprint
import datetime
import sys

laskuri = {}

for tiedosto in sys.argv[1:]:



    with open(tiedosto) as json_data:
        d = json.load(json_data)
        json_data.close()
        for tweet in d:
            aika = datetime.datetime.fromtimestamp(
                    int(tweet['time'])
                ).strftime('%Y-%m-%d')
            if aika not in laskuri:
                laskuri[aika] = 0

            laskuri[aika] += 1

            teema_lista = tweet['text']

            ## print teema_lista

    #pprint (laskuri)



for x in laskuri.keys():

    a = laskuri[x]

    print x,",", a
