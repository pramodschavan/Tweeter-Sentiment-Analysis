import sys
import json

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

def parse_tweet(tweetlist):
   
    accum_dic = {}
    tweet_list = []
    word_dic = {}
    happiness_dic = {}
    total_words = 0
    output_file = open('output_tophashtags.txt','w')
    hash_dic = {}
	
    ''' Reading each tweet in the list of tweet list created earlier '''	
    for tweet in tweetlist:
	
	''' Reading hashtag from tweet '''
	if "entities" in tweet.keys() and tweet['entities']['hashtags']:
		hashtag_list = tweet['entities']['hashtags']
		#print hashtag_list		
		for hashtag in hashtag_list:
			if hashtag['text'] not in hash_dic:
				hash_dic[hashtag['text']] = 1
			else:
				hash_dic[hashtag['text']] = hash_dic[hashtag['text']] + 1	

    top_counter = 0			
    for hashtag in sorted(hash_dic, key = hash_dic.get, reverse= True):
    	print hashtag.encode('utf-8') + ' ' + str(hash_dic[hashtag])		
    	output_file.write(hashtag.encode('utf-8') + ' ' + str(hash_dic[hashtag]) +'\n')
    	top_counter += 1
    	if top_counter == 10:
    		break
	 	
				
    ''' Reading of all tweets done '''			
    output_file.close() 
    
def main():
    tweet_file = open(sys.argv[1])
    tweetlist = load_tweet(tweet_file)
    parse_tweet(tweetlist)
    
if __name__ == '__main__':
    main()
