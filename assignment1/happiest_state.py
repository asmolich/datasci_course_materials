import sys
import json
import re
import operator
import unicodedata

us_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    print compute_happiest_state(tweet_file, get_scores(sent_file))

def compute_happiest_state(tweets, scores):
    state_score = {}
    for line in tweets:
        tweet = json.loads(line)
        if 'text' in tweet.keys():
            state = calculate_state(tweet)
            if state not in state_score.keys():
                state_score[state] = 0
            state_score[state] += calculate_score(tweet["text"], scores)
    sorted_states = sorted(state_score.iteritems(), key=operator.itemgetter(1))
    filtered = filter(lambda x: x[0] != None, sorted_states)
    return filtered[-1] if len(filtered) > 0 else None

def calculate_state(tweet):
    state = None
    if 'user' in tweet:
        user = tweet['user']
        if user is not None and user != 'null' and 'location' in user:
            location = user['location']
            if location is not None and location != 'null':
                splt = location.split(',')
                if splt is not None and len(splt) == 2:
                    state = unicodedata.normalize('NFKD', splt[1]).encode('ascii','ignore')
    return state if state in us_states.keys() else None

def calculate_score(st, scores):
    wordList = re.sub("[^\w]", " ", st).split()
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
