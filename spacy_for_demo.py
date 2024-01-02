import spacy
import streamlit as st

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a sentence.")
spacy.displacy.serve(doc, style="dep")


