from transformers import pipeline
import random

def evaluate_sentiment():

    sentiment_analysis = pipeline("sentiment-analysis")

    f = open('transcript.txt', 'r')
    sentences = f.readlines()[0].strip().split('.')

    num_sentences = len(sentences)

    num_samples = (2*num_sentences)/3

    random_sentences = random.sample(sentences, num_sentences)

    total_sentiment = 0.0

    for sentence in random_sentences:

        result = sentiment_analysis(sentence)[0]

        if(result['label']=="POSITIVE"):
            total_sentiment+=result['score']

    return total_sentiment/num_samples