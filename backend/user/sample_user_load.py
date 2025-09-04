from backend.user.user_database import UserDatabase   # Importing the User class

from backend.user.user_class import User   # Importing the User class

db = UserDatabase()

user1 = db.load_user("2")
print(user1.get_weak_words())