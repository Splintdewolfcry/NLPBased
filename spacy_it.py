import spacy

# # nlp = spacy.load("fr_core_news_sm")
# # nlp = spacy.load("en_core_web_sm")
# nlp = spacy.load("it_core_news_sm")

# with open('song_lyrics.txt', 'r', encoding='utf-8') as file:
#     lyrics = file.read()
#     doc = nlp(lyrics)
#     sentence_spans = list(doc.sents)

# spacy.displacy.serve(sentence_spans, style="dep")

import spacy

nlp = spacy.load("it_core_news_sm")

with open('song_lyrics.txt', 'r', encoding='utf-8') as file:
    lyrics = file.read()
    doc = nlp(lyrics)
    sentence_spans = list(doc.sents)

print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

