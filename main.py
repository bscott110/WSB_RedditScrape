import praw

with open('pw.txt') as file:
    pw_line = file.readline()

reddit = praw.Reddit(client_id='DL-0oLtcYyalnDxjY5hOcw', client_secret='odOqD6s1ser0-vkMTHGhyli_ABM99w',
                     username='BScott110', password=pw_line, user_agent='APITEST_0.0.2')

submissions0 = reddit.subreddit('wallstreetbets').top(limit=5)

print("Top 5 WSB Threads:")
for submission in submissions0:
    i = submission.title
    print("-"+i)

submissions1 = reddit.subreddit('wallstreetbets').hot(limit=5)

print("Hottest 5 WSB Threads:")
for submission in submissions1:
    i = submission.title
    print("-"+i)

submissions2 = reddit.subreddit('wallstreetbets').new(limit=5)

print("Newest 5 WSB Threads:")
for submission in submissions2:
    i = submission.title
    print("-"+i)

submissions3 = reddit.subreddit('wallstreetbets').controversial(limit=5)

print("5 Most Controversial WSB Threads:")
for submission in submissions3:
    i = submission.title
    print("-"+i)
