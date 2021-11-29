import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('punkt', quiet=True)
nltk.download('vader_lexicon', quiet=True)

def global_sentiment(sentence, optimism_rate=0.75):

    sid = SentimentIntensityAnalyzer()
    polarity = sid.polarity_scores(sentence)             
    
    if polarity["compound"] >= (1-optimism_rate):
        return "Positive"
    elif polarity["compound"] <= -(1-optimism_rate):
        return "Negative"
    else:
        return "Neutral"


def sentiment_word_list(sentence, optimism_rate=0.75):
    
    tokens = nltk.word_tokenize(sentence)

    sid = SentimentIntensityAnalyzer()

    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]

    for word in tokens:
        if (sid.polarity_scores(word)['compound']) >= (1-optimism_rate):
            pos_word_list.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -(1-optimism_rate):
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)

    result = {"negative": neg_word_list, "neutral": neu_word_list, "positive": pos_word_list}           

    return result