import telebot
import time
import tweepy
import os

# Twitter App keys
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
# Twitter access keys
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
# Authorize and initiate the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Bot keys and initialize the bot
api_token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['user'])
def tweet_archive(message):
	'''
	Listener to extract information from Twitter
	The command message needs to be => "/user <TWITTER_USERNAME>"
	'''
	msg = message.text.split(' ')
	if len(msg) > 1 and len(msg) < 3:
		username = msg[1]
		try:
			# Use tweepy cursor to extract data
			user_tweets = tweepy.Cursor(api.user_timeline, id=username).items()
			i = 0
			for tweet in user_tweets:
				bot.send_message(message.chat.id, tweet.text)
				i += 1
				# Ensuring to not get HTTP 429 error by Telegram
				# The bot rests in every 75 tweets
				if i % 75 == 0:
					time.sleep(15)
		except Exception as e:
			print(e)
			bot.send_message(message.chat.id, 'Error happened.')
			# Sending an exception log to my account
			bot.send_message(86306879, str(e))
		finally:
			bot.send_message(message.chat.id, 'Archive completed.')
	else:
		bot.send_message(
			message.chat.id, 'The format of this function is like this: "/user <TWITTER_USERNAME>".')


bot.polling()
