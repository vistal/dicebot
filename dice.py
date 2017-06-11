import praw
import pprint
from random import randint
import re
import os

posts = []

if os.path.isfile('posts.txt'):
	with open('posts.txt', 'r') as file:
		posts = [line.rstrip('\n') for line in file]

def process_comment(comment):
        if "rollx" in comment.body.lower():
                if comment.id not in posts:
                        number = randint(1,18)
                        length = len(str(number))
                        if length == 2:
                                comment.reply("Rollbot:\n\n\*\*\*\*\*\*\n\n\*\***" + str(number) + "**\*\*\n\n\*\*\*\*\*\*")
                        else:
                                comment.reply("Rollbot:\n\n\*\*\*\*\*\*\n\n\*\***" + str(number) + "** \*\*\n\n\*\*\*\*\*\*")
                        posts.append(comment.id)
                        with open('posts.txt', 'w') as file:
                                for item in posts:
                                        file.write('{}\n'.format(item))
                else:
                        return

reddit = praw.Reddit('dicebot')

for comment in reddit.subreddit('TheCampaign').stream.comments():
	process_comment(comment)

