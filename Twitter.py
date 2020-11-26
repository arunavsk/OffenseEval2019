from tweepy import OAuthHandler
import tweepy


class TwitterAccess:

	def __init__(self, consumer_key, consumer_secret,
				access_token, access_secret):

		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.access_token = access_token
		self.access_secret = access_secret
		
		self.api = self.load_api()


	def load_api(self):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)

		# Load the twitter API via Tweepy
		return tweepy.API(auth, wait_on_rate_limit = True)


	# Status Methods
	def tweet_text_from_tweet_id(self, idx):
		tweet = self.api.get_status(idx)
		return tweet.text


	# User Methods
	def get_followers(self, screen_name):
		user_ids = []
		for page in tweepy.Cursor(self.api.followers_ids,
								  screen_name=screen_name).pages():
			user_ids.extend(page)
			time.sleep(60)

		return user_ids


	def user_from_tweet_id(self, idx):
		status = self.api.get_status(idx)
		return (status.user.id_str, status.user.screen_name)


	def get_follow_info(self, x, y):
		return self.api.show_friendship(source_id=x, target_id=y)


	def username_from_user_id(self, idx):
		user = self.api.get_user(user_id=idx)
		return user.screen_name


	def timeline_from_username(self, screen_name):
		timeline = self.api.user_timeline(screen_name=screen_name)
		return timeline