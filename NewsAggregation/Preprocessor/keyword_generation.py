from keybert import KeyBERT


def load_model():
    return  KeyBERT("distilbert-base-nli-mean-tokens")

def keyword_gen(doc):
    kw_model = load_model()
    keywords = kw_model.extract_keywords(
    doc,
    keyphrase_ngram_range=(1, 1),
    use_mmr=True,
    stop_words="english",
    top_n=10)
    return keywords
