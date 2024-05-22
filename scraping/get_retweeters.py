"""
	Jorge Sánchez Pastor
	2022-02-10
	Este script contiene funciones basicas con tweepy
	esta enfocado a conseguir los retweets de un tweet dado por id 
"""
import snscrape.modules.twitter as sntwitter
import tweepy
import json
from twitter_api_keys import *
import sys


"""
	devulve los ids de los tweets resultantes en la busqueda
	Para tweetws sin limite de resultados poner un numero negativo
"""

def get_retweeters(t_id:int , api):
	result = []
	for retweet in api.get_retweets(t_id):
		result.append(retweet.user.screen_name)
	print(' . ',end="")
	return result



# get the list of retweeters of every tweet in the file
def get_retweeters_from_file(infile, outfile):
	auth = tweepy.OAuthHandler(api_key, api_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)


	f = open(infile, 'r')
	g = open(outfile, 'w')
	l = f.readline()
	count = 0
	rt_count = 0
	retweeters = []
	while l != "":
		# get the ETA every 100 lines
		tweet = json.loads(l)
		if int(tweet["retweetCount"]) > 2 :
			d = tweet
			try:
				retweeters = get_retweeters(int(tweet['id']) , api)
				count += 1
				d['retweeters'] = retweeters
			except:
				print("Excepcion :( : ", count)
			print("count: {:<10}, total RTs: {:<20}".format(count, rt_count))
			rt_count += len(retweeters)
			g.write(json.dumps(d) + "\n")

		else:
			d = tweet
			d['retweeters'] = []
			g.write(json.dumps(d) + "\n")

		l = f.readline()
	f.close()
	g.close()




if __name__ == '__main__':
	infile = sys.argv[1]
	outfile = sys.argv[1].split(".")[0] + "_retweeters.json"
	# launch a python shell with the functions defined in this file
	get_retweeters_from_file(infile, outfile)



