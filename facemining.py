import sys
import os
import dotenv
import facebook
import urllib3

dotenv.load_dotenv()

token = os.environ['USER_ACCESS_TOKEN']

graph = facebook.GraphAPI(access_token=token, version=7.0)
post = graph.get_object(id='3282934375160574', fields='posts')
print(post['posts'])
#Meu Id '3282934375160574'