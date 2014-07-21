from __future__ import division
import sys
import re
import json
import operator

def main():
    tweet_file = open(sys.argv[1])
    compute_and_print_top_ten_hashtags(tweet_file)

def compute_and_print_top_ten_hashtags(tweets):
    hash_tags = {}
    for line in tweets:
        tweet = json.loads(line)
        if 'entities' in tweet.keys():
            entities = tweet['entities']
            if 'hashtags' in entities.keys():
                hashtags = entities['hashtags']
                for tag in hashtags:
                    if tag in hash_tags.keys():
                        hash_tags[tag['text']] += 1
                    else:
                        hash_tags[tag['text']] = 1
    sorted_tags = sorted(hash_tags.iteritems(), key=operator.itemgetter(1))
    for tag in sorted_tags.reverse()[:10]:
        print "%s %s" % (tag[0], tag[1])

if __name__ == '__main__':
    main()

