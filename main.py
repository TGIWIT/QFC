name = input("What's your name ? ")

while not name == "Mozart":
    print("Error : You have to put the good name")
    name = input("What's your name ? ")


age = input("How old are you ? ")

while not age == "23":
    print("Error : You have to put the good age") 
    age = input("How old are you ? ")  
else:
    print("Your name is " + name + ","" you have " + str(age) + " yers old")


password = input("Whats your password ? ")

while not password == "Mbouzi":
    print("Error : please take the good password")
    password = input("Whats your password ? ")
else:
    print("Password correct you have access to your account")
