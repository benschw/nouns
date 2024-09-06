import numpy as np
import spacy
from sklearn.linear_model import LogisticRegression

from nouns.word_io import load_data, save_data

NOUN_TYPE_ABSTRACT = 'abstract'
NOUN_TYPE_CONCRETE = 'concrete'


def processing_handler(nouns_path, abstract_path, concrete_path, abstract_out_path, concrete_out_path):
    nlp = spacy.load("en_core_web_lg")
    all_words = load_data(nouns_path)

    data = [{
        'type': NOUN_TYPE_ABSTRACT,
        'training_data': load_data(abstract_path),
    }, {
        'type': NOUN_TYPE_CONCRETE,
        'training_data': load_data(concrete_path),
    }]

    out = _process_nouns(nlp, data, all_words)

    save_data(abstract_out_path, out[NOUN_TYPE_ABSTRACT])
    save_data(concrete_out_path, out[NOUN_TYPE_CONCRETE])


    data = [{
        'type': 'place',
        'training_data': load_data('data/training/place_src.txt'),
    }, {
        'type': 'non-place',
        'training_data': load_data('data/training/non_place_src.txt'),
    }]

    out = _process_nouns(nlp, data, all_words)

    save_data('data/processed/place.txt', out['place'])
    save_data('data/processed/non_place.txt', out['non-place'])


def _process_nouns(nlp, data, all_words):
    # extract training data as ordered list
    training_set = []
    for d in data:
        training_set.append(d['training_data'])
    classifier = _generate_classifier(nlp, training_set)

    # extract classes as ordered list
    classes = []
    for d in data:
        classes.append(d['type'])
    out = _predict_noun_type(classes, classifier, nlp, all_words)

    return out


def _predict_noun_type(classes, classifier, nlp, words):
    out = {}
    for c in classes:
        out[c] = []

    for word in words:
        tokens = nlp(word)
        token = tokens[0]
        noun_type = classes[classifier.predict([token.vector])[0]]

        out[noun_type].append(word)

        # word_type = token.pos_
        # if word_type != 'NOUN':
        #     print("not noun -", word_type, '-', noun_type, '-', word)

    return out


def _generate_classifier(nlp, train_set):

    x = np.stack([list(nlp(w))[0].vector for part in train_set for w in part])
    y = [label for label, part in enumerate(train_set) for _ in part]
    classifier = LogisticRegression(C=0.1, class_weight='balanced').fit(x, y)
    return classifier
