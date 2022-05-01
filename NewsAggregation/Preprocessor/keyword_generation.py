from keybert import KeyBERT
from pandas import DataFrame


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

    df = (DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"])
        .sort_values(by="Relevancy", ascending=False)
        .reset_index(drop=True))

    return df['Keyword/Keyphrase'].to_list()
