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
        # Slow operation, but done only on initializing app
        self._tagger = SequenceTagger.load('ner_spanish_large/pythorch_model.bin')
        print("Tagger loaded")

    def foo(self, text):
        sentence = Sentence(text, use_tokenizer = True)
        self._tagger.predict(sentence)

        # iterate over entities and print
        for entity in sentence.get_spans('ner'):
            print(entity)

        print(sentence.to_dict(tag_type='ner')['entities'])

        return sentence.to_dict(tag_type='ner')

    def test(self):
        print("testing")
