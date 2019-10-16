# -*- coding: utf-8 -*-
"""5_Python_for_Web_Science__Homework_Group4_LIU.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kdM1CyfAExanIWRb_SuBsizeLJYG5uRm

# Week 5 Homework
"""

import json
from google.colab import files

uploaded = files.upload()

# You don't have to understand this line.  
#  Just know it takes your data file and turns it into a Python nested dictionary
auth_pers = json.loads( list( uploaded.values() ).pop().decode('utf-8') )['twitter']
CONSUMER_KEY = auth_pers['APIKey']
CONSUMER_SECRET = auth_pers['APISecretKey']
ACCESS_TOKEN = auth_pers['AccessToken']
ACCESS_TOKEN_SECRET = auth_pers['AccessTokenSecret']

!git clone git://projects.mako.cc/twitter-api-cdsw

import os 
os.chdir('/content/twitter-api-cdsw')
import pprint

import encoding_fix
import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

a_tweet = api.home_timeline(count=1)
a_tweet = a_tweet[0]._json

print( a_tweet['user']['name'] + ": " + a_tweet['text'])

"""Setting Count"""

max_count = 1
#max_count = 200
public_tweets = api.home_timeline(count=max_count + 1)
#https://stackoverflow.com/questions/46734636/tweepy-api-user-timeline-count-limited-to-200
#max is 200

print( len( public_tweets ))
for tweet in public_tweets:
    pprint.pprint(tweet.text)

"""### 0)

Add your name to the title of this file

### 0.5)

Add your group's number to the title of this file as well, before your name.

### 1)

Produce a list of tweets on the topic "house boat", setting `count = 200`.  Produce code that answers each of the following questions. For both latter questions, be sure to detect variants like "BOAT" and "House".
1.   How many tweets did you retrieve? 
2.   How many mention a boat house instead? 
3.   How many mention neither boat nor house?
"""

#How many tweets did you retrieve?
### Depending on when you run these, the answer is different every time.
public_tweets = api.search("house boat", count=200)
print(len(public_tweets))

#How many mention a boat house instead?
import pprint
public_tweets = api.search("house boat", count=200)
list_bh = []
for boat_tweet in public_tweets:
  new_str = boat_tweet.text.lower() ### take the entire tweet and lowercase all of it so you can check all the variance
  if "boat house" in new_str:
    list_bh.append(new_str)
print(len(list_bh))
pprint.pprint(list_bh)

#How many mention neither boat nor house?
public_tweets2 = api.search("house boat", count=200)
no_house_boat = []
for no_house in public_tweets2:
  new_no = no_house.text.lower()
  if "house" and "boat" not in new_no:
    no_house_boat.append(new_no)
print(len(no_house_boat))
pprint.pprint(no_house_boat)

"""### 2)
Provide code answering the following questions about Sir David Attenborough's Twitter account:
1.   How many accounts follow his account?
2.   How many accounts does his account follow?
Remember: you should be able to check the correctness of your numbers against the site.
"""

user = api.get_user('Sir_Attenboroug')

#How many accounts follow his account?
print(user.screen_name + " has " + str(user.followers_count) + " followers.")
followers = user.followers(count=100)
#.format will replace the double brackets with whatever is in the parentheses

#How many accounts does his account follow?
print(user.screen_name + " follows " + str(user.friends_count) + " users.")
friends = user.friends(count=100)

"""### 3)
Pick a Twitter account that both follows and is followed by between 10 and 1000 accounts.  Within a subset of `count = 200` of this account's followers and "friends" (accounts it follows), determine the accounts that have a reciprocated "follow" relationship with this account.
"""

user = api.get_user('philip_a_liu')

import pprint
print(user.screen_name + " follows " + str(user.friends_count) + " users.")
friends = user.friends(count=200)
#pprint.pprint(list(friends))
#print("They include these {} people:".format(len(friends)))
#for friend in friends:
   #print(friend.screen_name)

print(user.screen_name + " has " + str(user.followers_count) + " followers.")
followers = user.followers(count=200)
#.format will replace the double brackets with whatever is in the parentheses
#print("They include these {} people:".format(len(followers)))
#for follower in followers:
   #print(follower.screen_name)

rec_follow = []
rec_follower = []
new_list = []
for friend in friends:
  rec_follow.append(friend.screen_name)
for follower in followers:
  rec_follower.append(follower.screen_name)
for i in rec_follow:
  if i in rec_follower:
    new_list.append(i)
    
print("The user has a reciprocated follow relationship with these {} people:".format(len(new_list)))
for h in new_list:
  print(h)

### solution from hw review 6/5
'''
friends = user1.friends(count=200)
followers = user2.followers(count=200)
### nested dict representation of a person
total=0

for follow in followers:
  for friend in friends:
    if follower.id == friend.id:
      total = total + 1
print(total)
'''

'''

### know the difference between these two. Both are correct 
for follower in followers: #works for the objects
  for friend in friends:
    if follower == friend:
      total = total + 1
print(total)

# vs. 

for follower in followers: #only acceptable if you are looping through a list of strings
  if follower in friends: # if
    total = total + 1
print(total)

'''

"""### 4)
1.   Retrieve all followers of the USA's CDC (@CDCgov)
2.   Retrieve all followers of the USA's NASA (@NASA)
3.   Find any accounts that both are following. Specifically, create  a list of all of the screennames of the accounts followed by both the CDC and NASA.
"""

user1 = api.get_user('CDCgov')
cdc = (user1.screen_name + " has " + str(user1.followers_count) + " followers.")
print(cdc)
followers_cdc = user1.followers(count=100)
#.format will replace the double brackets with whatever is in the parentheses

user2 = api.get_user('NASA')
nasa = (user2.screen_name + " has " + str(user2.followers_count) + " followers.")
print(nasa)
followers_cdc = user2.followers(count=100)

import pprint
print(user1.screen_name + " follows " + str(user1.friends_count) + " users.")
cdc_follows = user1.friends(count=200)
#print("They include these {} people:".format(len(cdc_follows)))
#pprint.pprint(cdc_follows)
#for x in cdc_follows:
   #print(cdc_follows.screen_name)

import pprint
print(user2.screen_name + " follows " + str(user2.friends_count) + " users.")
nasa_follows = user2.friends(count=200)
#print("They include these {} people:".format(len(nasa_follows)))
#pprint.pprint(list(nasa_follows))
#for friend in friends:
   #print(friend.screen_name)

cdc_fol = []
nasa_fol = []
both_follow = []

for fol in cdc_follows:
  cdc_fol.append(fol.screen_name)
for fol2 in nasa_follows:
  nasa_fol.append(fol2.screen_name)
for k in cdc_fol:
  if k in nasa_fol:
    both_follow.append(k)
    
print("NASA and the CDC follow these {} people:".format(len(both_follow)))
for t in both_follow:
  print(t)

"""### 5) 
Florida's Kingsley Lake is a nearly perfectly circular lake almost exactly 2 miles across.  Use Twitter's geolocation to approximately locate a circle over the water of the lake, and retrieve tweets that have been sent by boat.  There may or may not be any; give it a try.
"""

# I pulled lat and lon by searching for https://www.google.com/search?q=Florida%27s+Kingsley+Lake+coordinates&oq=Florida%27s+Kingsley+Lake&aqs=chrome.1.69i57j69i59j0l4.1442j0j7&sourceid=chrome&ie=UTF-8 
#   Note the negation of 122W below
tweets_lake = api.search("", count=50, geocode='29.9680,-82.0026,2mi') ### Florida's Kingsley Lake ### use 1 mi because it's supposed to be a radius

for tw in tweets_lake:
  print( tw.created_at, tw.text  )

"""### 6) CHALLENGE

Soccer  is the most international sport in the world, and teams can have very international followings. What language groups are most engaged with different teams? We'll answer this for just two prominent teams (a.k.a. "clubs"), both in Spain.

For #ForçaBarça and #RealMadrid, the customary hashtags of two prominent Spanish teams, pull several tweets using the hashtag, determine the language of each tweet in the sample, and build a dictionary  that counts the number of tweets in your sample by language. 

Some hints / ground rules:
*   Ask for `count = 200` tweets; don't worry if you actually end up with fewer. That's just how Twitter works.
*   Perform a separate query for each hashtag (don't combine both into one search).
*   For your dictionary, it may  end up being simpler if the keys are a language's [standard](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) two-letter code, instead of being the full names of that language  ( `'en'` and `'es'` instead of `'english'` and `'spanish'`).
*   Include in your answer not only code blocks with your solution, but text blocks providing 
   each hashtag's top two languages, 
   the number of languages tweeting each, 
   and a short narrative outlining the steps you went through to find out how tweet's store the language they're in. 

A part of solving this is doing the detective work to find the language of a tweet (or at least the language Twitter assigns to each tweet). You might start by   using a search engine,   inspecting the JSON representation of a tweet,   inspecting the "object" representation of a tweet,    digging through the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index.html) documentation, or    digging through the documentation of the [tweepy Python library](http://docs.tweepy.org/en/v3.5.0/). 

This task may look forbidding, but your answer will probably be shorter than the  text of this question.
"""

### Not right.

### Pull tweets ForçaBarça from hashtag.
### lang = language 
### list of different languages and their codes http://support.gnip.com/apis/powertrack2.0/rules.html#Operators

def ForcaBarca():
  forca_tweets = api.search("ForçaBarça", count=200)
  counter = 0
  lang_list = []
  for tweet in forca_tweets:
    if tweet.lang not in lang_list:
      lang_list.append(tweet.lang)
  # print(lang_list) ### get the keys for lang_dict

  lang_dict = {}

  en_count = 0
  es_count = 0
  ar_count = 0
  und_count = 0 #und is undefined
  pt_count = 0
  ht_count = 0
  ca_count = 0

  for tweet in forca_tweets:
    if tweet.lang == 'en':
      en_count += 1
    lang_dict['en'] = en_count
    if tweet.lang == 'es':
      es_count += 1
    lang_dict['es'] = es_count
    if tweet.lang == 'ar':
      ar_count += 1
    lang_dict['ar'] = ar_count
    if tweet.lang == 'und':
      und_count += 1
    lang_dict['und'] = und_count
    if tweet.lang == 'pt':
      pt_count += 1
    lang_dict['pt'] = pt_count
    if tweet.lang == 'ht':
      ht_count += 1
    lang_dict['ht'] = ht_count
    if tweet.lang == 'ca':
      ca_count += 1
    lang_dict['ca'] = ca_count

  return lang_dict

ForcaBarca()

### Pull tweets RealMadrid from hashtag.

real_tweets = api.search("RealMadrid", count=200)
m_counter = 0
m_lang = []
for m_tweet in real_tweets:
  if m_tweet.lang not in m_lang:
    m_lang.append(m_tweet.lang)

print(m_lang) ### get the keys for lang_dict

'''
lang_dict = {}

en_count = 0
es_count = 0
ar_count = 0
und_count = 0
pt_count = 0
ht_count = 0
ca_count = 0

for tweet in forca_tweets:
  if tweet.lang == 'en':
    en_count += 1
  lang_dict['en'] = en_count
  if tweet.lang == 'es':
    es_count += 1
  lang_dict['es'] = es_count
  if tweet.lang == 'ar':
    ar_count += 1
  lang_dict['ar'] = ar_count
  if tweet.lang == 'und':
    und_count += 1
  lang_dict['und'] = und_count
  if tweet.lang == 'pt':
    pt_count += 1
  lang_dict['pt'] = pt_count
  if tweet.lang == 'ht':
    ht_count += 1
  lang_dict['ht'] = ht_count
  if tweet.lang == 'ca':
    ca_count += 1
  lang_dict['ca'] = ca_count

print(lang_dict)
'''

#Franklin Shih, group 4