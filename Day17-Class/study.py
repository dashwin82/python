class User:
    def __init__(self, user_id, user_name) -> None:
        print ("constructor")
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0


user1 = User("001", "Ashwin")
print (user1.user_id)
