'''
Sentiment analysis with finbert Model
This module consist for sentiments_analysis function which extracts sentiments of the text passed and returns it
Author Parth Shah shah.parth3@northeastern.edu'
Created at 27th April 2022
'''
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, AutoModelForTokenClassification


Text = "No Sentiments"
def sentiments_analysis(doc):
    '''
    This Function downloads the finbert model and cleans the document
    Parameters:
    ---------------------
    doc: string
        The document(Sentence, paragraphs) on which sentiment analysis must be performed
        
    '''
    try:
        tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert",max_length=512)
        model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
        nlp = pipeline("sentiment-analysis", model = model, tokenizer=tokenizer)
        clean_text= doc.replace("\n", " ")       
        clean_text= ''.join([c for c in clean_text if c != "'"])
        sentiment = nlp(str(clean_text))
        return sentiment
    except:
        print("Cannot do sentiment analysis")
        return Text

#run when file is directly executed
if __name__ == '__main__':
    doc = 'The words are very positive in this sentence'
    return_sentiment = sentiments_analysis(doc)
    assert(return_sentiment[0]['score'] == 0.6004692316055298)