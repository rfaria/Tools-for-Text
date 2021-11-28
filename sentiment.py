import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('punkt')
nltk.download('vader_lexicon')

def test(test_subset):

    tokens = nltk.word_tokenize(test_subset)

    sid = SentimentIntensityAnalyzer()
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]

    for word in tokens:
        if (sid.polarity_scores(word)['compound']) >= 0.25:
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.25:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)                

    print('Positive :',pos_word_list)        
    print('Neutral :',neu_word_list)    
    print('Negative :',neg_word_list)  
    
    print(sid.polarity_scores(test_subset))