import sys
import json
import re

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = get_scores(sent_file)
    compute_and_print_scores(tweet_file, scores)

def compute_and_print_scores(tweets, scores):
    for line in tweets:
        tweet = json.loads(line)
        if 'text' not in tweet.keys():
            print 0
        else:
            print calculate_score(tweet["text"], scores)

def calculate_score(str, scores):
    wordList = re.sub("[^\w]", " ", str).split()
    sum = 0
    for word in wordList:
        if word in scores.keys():
            sum += scores[word]
    return sum

def get_scores(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    return scores

if __name__ == '__main__':
    main()
