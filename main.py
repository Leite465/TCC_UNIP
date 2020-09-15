import sys
import os
import tweepy
import dotenv
from datetime import datetime
import dataset
import re
import sqlite3
import json
#import pyspark
#import findspark
#import hbase

#findspark.init()

#db2 = dataset.connect('sqlite:///hashtags.db')
db = dataset.connect('sqlite:///tweets.db')

#carrega o arquivo .env
dotenv.load_dotenv()



#arquivo com as keywords para o comando track
stopwords_file = 'stopwords.txt'
stopwords = []
with open(stopwords_file,'r') as f:
    for line in f:
        stopwords.append(line.strip())

#coleta a informação do arquivo
consumer_key = os.environ['CONSUMER_API_KEY']
consumer_secret = os.environ['CONSUMER_API_SECRET_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

#faz a autenticação
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#cria a classe de streaming com uma função pra printar
#class MyStreamListener(tweepy.StreamListener):
#class CustomStreamListener(tweepy.StreamListener):

#    def on_status(self, status):
#        words = status.text.replace('\n', ' ')
#        words = words.split(' ')
#        hashtags = [w for w in words if '#' in w]
#        hashtags = [re.sub(r'[^\w\s]', '', h) for h in hashtags]
#        for h in hashtags:
#            now = datetime.now()
#            timestamp = datetime.timestamp(now)
#            table = db['hashtags']
#            table.insert(dict(word=h, timestamp=timestamp))
#            print(status.text)

 #       def on_error(self, status_code):
 #           print(status_code)
 #           return True  # Don't kill the stream

#       def on_timeout(self):
#            print('timeout')
#            return True  # Don't kill the stream

#        def on_exception(self, exception):
#            print(exception)

class AStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        table = db['tweets']
        table.insert(dict(status=status.text, timestamp=timestamp))
        print(status.text)

        def on_error(self, status_code):
            print(status_code)
            return True  # Don't kill the stream

        def on_timeout(self):
            print('timeout')
            return True  # Don't kill the stream

        def on_exception(self, exception):
            print(exception)



        #print(status.text)

myStreamListener = AStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#myStream = tweepy.streaming.Stream(auth, CustomStreamListener())
myStream.filter(track=stopwords, is_async=True)

#cria o listener
#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#filtros

#usa as palavras chave do arquivo stopwords.txt
#myStream.filter(track=stopwords)

#filtro por individuo
#ID_Bolsonaro=128372940
#Stream do meu feed(@Leltch), meu ID=1019374982621691904
#myStream.filter(follow=["id"])
#myStream.filter(follow=["128372940"])

#filtro por palavras, é possível dar track em mais de uma palavra
#myStream.filter(track=['Comida'])
#myStream.filter(track=['1','2'])

#(language=[en]) serve para definir a lingua dos tweets "captados", tenho que ver a sintaxe certa ainda

#pega meu feed
#public_tweets = api.home_timeline(  )
#for tweet in public_tweets:
#    print(tweet.text)
