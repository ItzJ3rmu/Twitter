def twitteri():

    import json
    from pprint import pprint
    import datetime
    import collections

    tiedosto = raw_input("Tiedoston nimi: ")

    laskuri = {}

    teema_laskin = {}

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
            if "luonto" not in teema_laskin:
                teema_laskin[teema_lista] = 0

            teema_laskin[teema_lista] += 1


    avain = laskuri.keys()

    teema_maara = teema_laskin.keys()

    #print avain

    for x in avain:

        a = laskuri[x]

        print x,",", a

    for y in teema_maara:

        b = teema_laskin[y]

    pprint (teema_maara)
