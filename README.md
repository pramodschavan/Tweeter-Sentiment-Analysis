This project was done as part of 'Introduction to Data Science' course on Coursera taught by Bill Howe from the University of Washington.

As part of this project, sentiment analysis was performed on live stream tweets to determine which US states were happiest. Live stream of twitter data was collected through Tweeter API using oauth2. Collected tweeter data was further cleaned (converting to lower case, removing hyperlinks and punctuation, English only tweets etc) and analyzed using python program modules. Finally, findings were represented in the form of bar charts and pie charts.

Following steps were followed to determine happiest states:
1. Getting Twitter Data - Live stream of twitter data was collected through Tweeter API using oauth2.
2. Deriving the sentiment of each tweet: Sentiment for each tweet was computed based on the sentiment score of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet. The file AFINN-111.txt containing a list of pre-computed sentiment scores was used to determine term score in each tweet.
3. Deriving the sentiment of new terms: The sentiment for the terms that do not appear in the file AFINN-111.txt was computed based on the overall tweet sentiment deduced in step 2. 
4. Computing term frequency: Frequency of each term was calculated as [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets].
5. Calculating happiest state: Location of each tweet was extracted and a list of state with sentiment scores calculated in earlier steps for each tweet was stored to capture the happiest states in the USA.
6. Representation of findings: Findings were represented in the form of bar charts and pie charts.

In addition, top ten trending hashtags were also captured as part of this project.


 