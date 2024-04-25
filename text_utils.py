def clean_text(text):
    """Remove unwanted characters and whitespace."""
    return ' '.join(text.strip().replace('\n', ' ').split())

def split_sentences(text):
    """Split text into a list of sentences."""
    from nltk import tokenize
    return tokenize.sent_tokenize(text)