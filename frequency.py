import sys
import json
import re
from string import punctuation

def lines(fp):
    print str(len(fp.readlines()))

def load_sentiments(sf):
    ''' Read the AFINN-111 text file and create dictionary of all sentiment words with their score'''
    sentdic = {}
    sf = open("AFINN-111.txt")
    for line in sf:
        word,score = line.split("\t")
        sentdic[word]=int(score)
    return sentdic

def load_tweet(tf):
    ''' Read tweet file and store tweets in a list ''' 
    
    tweetlist = []
    tweetline = tf.readline()
  
    while len(tweetline) is not 0:
        tweet = json.loads(tweetline)
        tweetlist.append(tweet)
        tweetline = tf.readline()
    
    ''' Display number of tweets been processed '''   
    
    print 'Number of tweets: ' + str(len(tweetlist))
    return tweetlist

def clean_tweet(tweet):
    ''' Cleaning raw tweet data into process data for analysis '''
     	
    ''' Converting tweet text to lower case '''
    tweet_processed=tweet.lower()

    ''' Removing hyperlinks in the tweet text '''
    tweet_processed = re.sub(r'https?:[^\s]+','',tweet_processed,flags=re.MULTILINE)

    ''' Removing puntuations in the tweet text '''
    for p in list(punctuation):
        tweet_processed=tweet_processed.replace(p,'')
    
    ''' Printing processed tweet '''
    #print 'Processed: ' + tweet_processed
    
    return tweet_processed


def parse_tweet(tweetlist,sentdic):
    ''' Processing cleaned tweet for analysis '''
      
    #output_file = open('output_tweetscore.txt','w')
    
    accum_dic = {}
    tweet_list = []
    word_dic = {}
    
    total_words = 0
    #print 'pramod'
    ''' Reading each tweet in the list of tweet list created earlier '''	
    for tweet in tweetlist:
	''' Processing the tweets containing text (ignoring other) and engisht text'''
	if "text" in tweet.keys() and tweet['lang'] == "en":   
		''' Processing english language tweets only '''
		#if tweet['lang'] == "en":       
		tweet_text = tweet["text"]
            	#print 'Original: ' + tweet_text
		''' Call for cleaning tweets '''
		tweet_processed = clean_tweet(tweet_text)  
		score = 0
		''' Reading words in a single tweet '''
            	for tweet_word in tweet_processed.split(" "):
			#print tweet_word
               		''' Assigning sentiment score for AFFINN'''				
			if not (tweet_word.encode('utf-8','ignore') == ""):
				if tweet_word.encode('utf-8') in sentdic.keys():
					#print tweet_word + ': ' + str(sentdic[tweet_word])
               				score += sentdic[tweet_word]
				else:
					if tweet_word.encode('utf-8') not in accum_dic.keys():
						accum_dic[tweet_word] = []
				
			''' Creating word dictionary for calculating term frequency '''	
			if tweet_word not in word_dic:
				word_dic[tweet_word] = 1
			else:
				word_dic[tweet_word] = word_dic[tweet_word] + 1
			total_words += 1
		''' Processing of single tweet done ''' 			

		''' Writing scores for sentiment words to output file '''			
		#output_file.write(str(score)+'\n')		
							
		for word in accum_dic.keys():
			#print word + "\n"
			accum_dic[word].append(score)
    ''' Reading of all tweets done '''			
    
    for word in accum_dic.keys():
	total_sum = 0
	term_sent = 0
	for score in accum_dic[word]:
		total_sum = total_sum + score
	term_sent = float(total_sum)/float(len(accum_dic[word]))
	#print "word: " + word + " total_sum: " + str(total_sum) + " term_freq: " + str(term_freq)
   	#print word + " " term_sent
   
  
    ''' Calculating term frequency for each term '''
    term_freq = {}
    for term in word_dic.keys():
	term_freq[term] = float(word_dic[term])/float(total_words)			
        print term + ' ' + str(term_freq[term])
    
    #output_file.close()    
    #print tweet_score
	
   
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    lines(sent_file)
    sentdic = load_sentiments(sent_file)
    tweetlist = load_tweet(tweet_file)
    parse_tweet(tweetlist,sentdic)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
