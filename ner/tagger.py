import flair
from flair.models import TextClassifier
from flair.data import Sentence
from flair.models import SequenceTagger
from flair.visual.ner_html import render_ner_html
from flair.data import Corpus
from flair.embeddings import TokenEmbeddings, WordEmbeddings, StackedEmbeddings, FlairEmbeddings

# https://github.com/flairNLP/flair

# To train:
# https://huggingface.co/flair/ner-spanish-large

class Tagger():
    def __init__(self):
        pass

    def foo(self, text):
        sentence = Sentence(text, use_tokenizer = True)
        # tagger = SequenceTagger.load('resources/taggers/example-ner/best-model.pt')
        # import os
        # print(os.getcwd())
        tagger = SequenceTagger.load('ner_spanish_large/pythorch_model.bin')
        # tagger = SequenceTagger.load('ner-multi')
        tagger.predict(sentence)

        # iterate over entities and print
        for entity in sentence.get_spans('ner'):
            print(entity)

    def test(self):
        print("testing")
