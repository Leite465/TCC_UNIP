import sys
import os
import tweepy
import dotenv
import re
import sqlite3
import json
import facebook
import urllib3

dotenv.load_dotenv()

token = os.environ['USER_ACCESS_TOKEN']

graph = facebook.GraphAPI(access_token=token, version = 8.0)
events = graph.request('/search?q=Poetry&type=event&limit=10000')