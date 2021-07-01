import praw

reddit = praw.Reddit(client_id='TAsJn7Y4ArZC1A', client_secret='Pkf19s972-lShAi5CELfpjLu36JcNQ',
                     username='xxx', password='xxx', user_agent='APITEST_0.0.1')

submissions = reddit.subreddit('wallstreetbets').top(limit=5)
for submission in submissions:
    i = submission.title
    print(i)
