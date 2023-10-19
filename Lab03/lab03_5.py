def accept_login(users, username, password):
    if username in users and users[username] == password:
        return True
    return False

users = { 
    "user1" : "password1", 
    "user2" : "password2", 
    "user3" : "password3"} 

if accept_login(users, "wronguser", "wrongpassword") : 
# if accept_login(users, "user1", "password1") : 
    print("login successful!") 
else: 
    print("login failed...") 
