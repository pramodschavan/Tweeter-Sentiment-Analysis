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
    accum_dic = {}
    tweet_list = []
    check = 0
    for tweet in tweetlist:
	if "text" in tweet.keys():
		if tweet['lang'] == "en":
			tweet_text = tweet["text"]
            		#print 'Original: ' + tweet_text
			tweet_processed = clean_tweet(tweet_text)
			score = 0
            		for tweet_word in tweet_processed.split(" "):
				#print tweet_word
				if not (tweet_word.encode('utf-8','ignore') == ""):
					if tweet_word.encode('utf-8') in sentdic.keys():
						#print tweet_word + ': ' + str(sentdic[tweet_word])
                   				score += sentdic[tweet_word]
					else:
						if tweet_word.encode('utf-8') not in accum_dic.keys():
							accum_dic[tweet_word] = []
							#tweet_list.append(tweet_word)
			check = check + 1			
			output_file.write(str(score)+'\n')				
			for word in accum_dic.keys():
				#print word + "\n"
				accum_dic[word].append(score)
			
    #print accum_dic.items()	
    check = 0
    for word in accum_dic.keys():
	total_sum = 0
	term_freq = 0
	for score in accum_dic[word]:
		total_sum = total_sum + score
	term_freq = float(total_sum)/float(len(accum_dic[word]))
	print "word: " + word + " total_sum: " + str(total_sum) + " term_freq: " + str(term_freq)
	check += 1
    if check == 5:
        sys.exit(1)
    #print 'tweet ' + ": " + str(sum1)
    #tweet_score.append(score)
			
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
