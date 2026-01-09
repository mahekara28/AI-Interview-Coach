import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

FILLER_WORDS = ["um", "uh", "like", "you know", "basically"]

# Lazy load spaCy
def load_nlp():
    import spacy
    return spacy.load("en_core_web_sm")

def count_filler_words(text):
    text = text.lower()
    return sum(text.count(word) for word in FILLER_WORDS)

def keyword_analysis(text, keywords):
    text = text.lower()
    found = [kw for kw in keywords if kw in text]
    missing = list(set(keywords) - set(found))
    return found, missing

def clarity_score(text):
    try:
        nlp = load_nlp()
        doc = nlp(text)
        sentences = list(doc.sents)
        if len(sentences) == 0:
            return 0
        avg_len = np.mean([len(sent.text.split()) for sent in sentences])
        if avg_len < 5:
            return 4
        elif avg_len < 10:
            return 6
        elif avg_len < 20:
            return 8
        return 9
    except Exception:
        return 7  # fallback if spaCy crashes

def relevance_score(answer, keywords):
    try:
        if not answer.strip() or not keywords:
            return 0
        corpus = [answer, " ".join(keywords)]
        tfidf = TfidfVectorizer()
        vectors = tfidf.fit_transform(corpus)
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        return round(score * 10, 2)
    except Exception:
        return 0

def generate_feedback(answer, keywords):
    fillers = count_filler_words(answer)
    found, missing = keyword_analysis(answer, keywords)
    clarity = clarity_score(answer)
    relevance = relevance_score(answer, keywords)

    feedback = []

    if fillers > 2:
        feedback.append("Reduce filler words to sound more confident.")

    if missing:
        feedback.append(f"Try covering these concepts: {', '.join(missing)}")

    if clarity < 6:
        feedback.append("Your answer could be more structured.")

    if not feedback:
        feedback.append("Great answer! Clear and relevant.")

    return {
        "fillers": fillers,
        "found_keywords": found,
        "clarity_score": clarity,
        "relevance_score": relevance,
        "feedback": feedback
    }
