import praw

#create a txt file called pw.txt and enter your password on the first line
with open('pw.txt') as file:
    pw_line = file.readline()

#create a reddit app and enter your respective credentials here
reddit = praw.Reddit(client_id='xxx', client_secret='xxx',
                     username='xxx', password=pw_line, user_agent='APITEST_0.0.2')

#creat a for loop for each sort
submissions0 = reddit.subreddit('wallstreetbets').top(limit=5)

print("Top 5 WSB Threads:")
for submission in submissions0:
    i = submission.title
    print("-"+i)

submissions1 = reddit.subreddit('wallstreetbets').hot(limit=5)

print("5 Hottest WSB Threads:")
for submission in submissions1:
    i = submission.title
    print("-"+i)

submissions2 = reddit.subreddit('wallstreetbets').new(limit=5)

print("5 Newest WSB Threads:")
for submission in submissions2:
    i = submission.title
    print("-"+i)

submissions3 = reddit.subreddit('wallstreetbets').controversial(limit=5)

print("5 Most Controversial WSB Threads:")
for submission in submissions3:
    i = submission.title
    print("-"+i)
