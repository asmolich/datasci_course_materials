from __future__ import division
import sys
import re
import json

def main():
    tweet_file = open(sys.argv[1])
    compute_and_print_frequencies(tweet_file)

def compute_and_print_frequencies(tweets):
    occurencies = {}
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            word_list = re.sub("[^\w]", " ", tweet['text']).split()
            for word in word_list:
                if word in occurencies.keys():
                    occurencies[word] += 1
                else:
                    occurencies[word] = 1
    length = len(occurencies)
    for term in occurencies:
        print "%s %s" % (term, occurencies[term] / length)

if __name__ == '__main__':
    main()

