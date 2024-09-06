import random

from nouns.word_io import load_data
from nouns.settings import CONCRETE_OUT_PATH, ABSTRACT_OUT_PATH


def three_nouns_handler(abstract_path, concrete_path):
    abstract = load_data(abstract_path)
    concrete = load_data(concrete_path)

    words = [
        abstract[random.randint(0, len(abstract))],
        concrete[random.randint(0, len(concrete))],
        concrete[random.randint(0, len(concrete))],
    ]
    print(words)
