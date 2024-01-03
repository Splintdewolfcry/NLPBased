import spacy
import genius

nlp = spacy.load("fr_core_news_sm")

with open('song_lyrics.txt', 'r', encoding='utf-8') as file:
    lyrics = file.read()
    doc = nlp(lyrics)
    sentence_spans = list(doc.sents)

print(doc.text)
spacy.displacy.serve(sentence_spans, style="dep")

for token in doc:
    print(token.text, token.pos_, token.dep_)