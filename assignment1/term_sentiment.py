from __future__ import division
import sys
import re
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    compute_and_print_sentiment(tweet_file, get_scores(sent_file))

def compute_and_print_sentiment(tweets, scores):
    new_terms = {}
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            word_list = re.sub("[^\w]", " ", tweet['text']).split()
            tweet_sentiment = calculate_tweet_sentiment(word_list, scores)
            for term in filter(lambda x: x not in scores , word_list):
                compute_sentiment_for_term(term, tweet_sentiment / len(word_list), new_terms)
    for term in new_terms:
        print "%s %s" % (term, new_terms[term])

def compute_sentiment_for_term(term, term_weight, new_terms):
    val = term_weight
    if term in new_terms.keys():
        val += new_terms[term]
    new_terms[term] = val

def calculate_tweet_sentiment(word_list, scores):
    sum = 0
    for word in word_list:
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
