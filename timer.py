"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""


# This program is timer that counts down


# import time # The time library has a sleep function that will pause the script for a specifized amount of time
# from PIL import Image # the pillow library makes it easy to display images 

# im = Image.open("times-up.jpeg")

# # ask user to enter desired countdown time
# set_time = int(input("Please set your timer in seconds: "))

# time.sleep(set_time)

# im.show()

# 1) print players stand 2) while random timmer running player sit one by one if 

# class Player:
#   def __init__(self, name, score):
#   self.name = name
#   self.score = score

import time 


def create_players(num_players):
    players = []
    
    for i in range(1, num_players +1):
        
        name = f"Player {i}"
        players.append(name) 
        #print(name)
        
    return players

num_players = int(input(" How many players in game: "))

create_players(num_players)

print("Players stand")


#testtt




