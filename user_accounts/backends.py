from models import User


# create the e-mail authorisation class the over-ride Djangos default login.
class EmailAuth(object):

	def authenticate(self, email=None, password=None):
		# get an instance of the User with the supplied e-mail address and check its password is correct
		try:
			# get the user by e-mail address
			_user = User.objects.get(email=email)

			# if password is correct, return the user
			if _user.check_password(password):
				return _user

		# return error if User Doesn't Exist
		except User.DoesNotExist:
			return None


	# used by the Django authentication system to retrieve an instance of User
	def get_user(self, user_id):
		try:
			# get the user by user id
			_user = User.objects.get(pk=user_id)

			# if user exists and is an active user, return user.
			if _user.is_active:
				return _user

			# otherwise, return nothing.
			return None

		# if User doesn't exist, return nothing
		except User.DoesNotExist:
			return None
