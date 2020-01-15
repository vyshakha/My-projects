import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
        def __init__(self):
                consumer_key=''
                consumer_secret=''
                access_token=''
                access_token_secret=''

                try :
                        self.auth=OAuthHandler(consumer_key,consumer_secret)
                        self.auth.set_access_token(access_token,access_token_secret)
                        self.api=tweepy.API(self.auth)
                except:
                        print("error:Authentication Failed")

        def clean_tweet(self,tweet):
                return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w=:\/\/\S+)"," ",tweet).split())

        def get_tweet_sentiment(self,tweet):
                analysis = TextBlob(self.clean_tweet(tweet))
                if analysis.sentiment.polarity >0:
                        return 'positive'
                elif analysis.sentiment.polarity ==0:
                        return 'neutral'
                else :
                        return 'negative'

        def get_tweets(self,query,count=10):
                tweets=[]
                try:
                        fetched_tweets= self.api.search(q=query , count=count)
                        for tweet in fetched_tweets:
                                parsed_tweet ={}
                                parsed_tweet['text']=tweet.text
                                parsed_tweet['sentiment']=self.get_tweet_sentiment(tweet.text)
                                if tweet.retweet_count >0:
                                        if parsed_tweet not in tweets:
                                                tweets.append(parsed_tweet)
                                else:
                                        tweets.append(parsed_tweet)
                        return tweets
                except tweepy.TweepError as e:
                                print("Error :" +str(e))
                
         




def main():
        api=TwitterClient()
        tweets=api.get_tweets(query= 'DONALD TRUMP', count=200)
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        print(" Positive tweet percentage :{}%".format (100*len(ptweets)/len(tweets)))
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        print("Negative tweet percentage  :{}%.".format(100*len(ntweets)/len(tweets)))
        nutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
        print("Nuetral percentage : {}%".format(100*len(nutweets)/len(tweets)))

        print("\n\nPostitve tweets:")
        for tweet in ptweets[:10]:
                print(tweet['text'])

        print("\n\nNegative tweets:")
        for tweet in ntweets[:10]:
                print(tweet['text'])

        print("\n\nNeutral tweets:")
        for tweet in nutweets[:10]:
                print(tweet['text'])
                                                             

if __name__ == "__main__": 
	
	main() 
