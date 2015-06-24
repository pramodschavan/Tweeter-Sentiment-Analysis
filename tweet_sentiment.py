import sys
import json
import re
from string import punctuation

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiments(sf):
    sentdic = {}
    sf = open("AFINN-111.txt")
    #print sf
    for line in sf:
        word,score = line.split("\t")
        sentdic[word]=int(score)
    #print 'lmao: ' + str(sentdic['lmao'])
    return sentdic

def load_tweet(tf):
    tweetlist = []
    #tweetrawfile = open(tweet_file)
    tweetline = tf.readline()
    
    while len(tweetline) is not 0:
        tweet = json.loads(tweetline)
        tweetlist.append(tweet)
        tweetline = tf.readline()
        
    #print tweetlist[8405]
    #print type(tweet["text"])
    print len(tweetlist)
    return tweetlist

def clean_tweet(tweet):
    # Converting to lower case
    tweet_processed=tweet.lower()

    # Removing links
    tweet_processed = re.sub(r'https?:[^\s]+','',tweet_processed,flags=re.MULTILINE)

    # Removing puntuations
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
    #print 'Processed: ' + tweet_processed
    return tweet_processed


def parse_tweet(tweetlist,sentdic):
    output_file = open('output_tweetscore.txt','w')
    tweet_score = []
    for tweet in tweetlist:
	if "text" in tweet.keys():
		if tweet['lang'] == "en":
			tweet_text = tweet["text"]
            		#print 'Original: ' + tweet_text
			tweet_processed = clean_tweet(tweet_text)
			sum1 = 0
            		for tweet_word in tweet_processed.split(" "):
				#print tweet_word
				if not (tweet_word.encode('utf-8','ignore') == ""):
					if tweet_word.encode('utf-8') in sentdic.keys():
						#print tweet_word + ': ' + str(sentdic[tweet_word])
                   				sum1 += sentdic[tweet_word]
			#print 'tweet ' + ": " + str(sum1)
			output_file.write(str(sum1)+'\n')			
			tweet_score.append(sum1)
			#if t == 6:
			#	sys.exit(0) 
    output_file.close()    
    #print tweet_score
	
   
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    sentdic = load_sentiments(sent_file)
    tweetlist = load_tweet(tweet_file)
    parse_tweet(tweetlist,sentdic)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
