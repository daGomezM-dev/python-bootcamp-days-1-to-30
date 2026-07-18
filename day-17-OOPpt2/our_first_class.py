# the first letter of our classes name has to be capitalized (PascalCase). For example:
# class CarCamshaftPulley

# in python, we don't use camelCase, we use PascalCase for class names and snake_case for almost everything else

class User:

	def __init__ (self, user_id, username):
		self.user_id = user_id 
		self.username = username
		self.followers = 0
		self.following = 0 
		
	def follow (self, user):
		user.followers += 1
		self.following += 1


# Keyword pass: in order to keep something empty


