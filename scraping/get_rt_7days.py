"""
	Jorge Sánchez Pastor
    2022-02-10
	Este script contiene funciones basicas con tweepy
	esta enfocado a conseguir los retweets de un tweet dado por id 
"""
import snscrape.modules.twitter as sntwitter
import tweepy
import json
import sys
# from twitter_api_keys import *


"""
	devulve los ids de los tweets resultantes en la busqueda
    Para tweetws sin limite de resultados poner un numero negativo
"""
def search_id_to_file(search, number):
    filename = 'tweets.json'
    tweets_list2 = []
    anterior_data = ""

    f = open(filename, 'w')
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
        if i > number and number > 0:
            break
        date = str(tweet.__dict__['date']).split(" ")[0]
        if date != anterior_data:
            print(date)
            anterior_data = date
        f.write(json.dumps(tweet.__dict__, default=str) + '\n')
    return True


if __name__ == '__main__':
    search_query = sys.argv[1]
    number = int(sys.argv[2])
    search_id_to_file(search_query, number)
