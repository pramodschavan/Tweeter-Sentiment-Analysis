import sys
import re
from string import punctuation

tweet = "Bonnie and Damon!! #Bamon for #ChoiceTVChemistry #ChoiceSciFiTVActress Kat Graham #ChoiceSciFiTVActor Ian Somerhalder https:\/\/t.co\/D0k4wxg0ou chavan http://google.com"

print 'Original: '+ tweet
# Converting to lower case
tweet_processed=tweet.lower()

# Removing links
tweet_processed = re.sub(r'https?:[^\s]+','',tweet_processed,flags=re.MULTILINE)

# Removing puntuations
for p in list(punctuation):
    tweet_processed=tweet_processed.replace(p,'')

print 'Processed: ' + tweet_processed

