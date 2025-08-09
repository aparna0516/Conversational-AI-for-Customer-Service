import spacy
import json
from math import inf

nlp = None
intents = None
EXAMPLE_DOCS = []

def load_resources(intents_path='intents.json'):
    global nlp, intents, EXAMPLE_DOCS
    if nlp is None:
        nlp = spacy.load('en_core_web_sm')
    if intents is None:
        with open(intents_path, 'r', encoding='utf-8') as f:
            intents = json.load(f)['intents']
    # prepare example docs for similarity matching
    EXAMPLE_DOCS = []
    for intent in intents:
        for ex in intent.get('examples', []):
            EXAMPLE_DOCS.append((intent['tag'], nlp(ex)))
    return intents

def predict_intent(user_text):
    """Return best intent and confidence using spaCy similarity to example phrases."""
    if nlp is None or intents is None:
        load_resources()
    doc = nlp(user_text)
    best_tag = None
    best_score = -inf
    # compute similarity with examples
    for tag, ex_doc in EXAMPLE_DOCS:
        try:
            score = doc.similarity(ex_doc)
        except Exception:
            score = 0.0
        if score > best_score:
            best_score = score
            best_tag = tag
    # normalize confidence to 0-1 (spaCy similarity is roughly 0-1)
    confidence = max(0.0, min(1.0, float(best_score)))
    # find response for the tag
    response = next((it['response'] for it in intents if it['tag'] == best_tag), "Sorry, I didn't understand that.")
    return {'tag': best_tag, 'confidence': confidence, 'response': response}
