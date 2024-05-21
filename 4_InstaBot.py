from instabot import Bot
bot = Bot() #Create an instance of the Bot class

bot.login(username="hridita_mitra2004",password="#H#R#11092004#") #instagram login

bot.follow("sweet_brier09")  #following a person

bot.upload_photo("") #upload a photo in instagram

bot.unfollow("") #unfollow a person

bot.send_message("I love python",["",""]) #send message to 2 or more members

followers=bot.get_user_followers("") 
for follower in followers:
    print(bot.get_user_info(follower)) #printing followers info
    
following=bot.get_user_following("")
for Following in following:
    print(bot.get_user_info(Following))#printing following persons info
    

bot.logout() #logout instagram