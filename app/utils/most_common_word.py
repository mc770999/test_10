from typing import List
import string
from collections import Counter

from toolz import pipe,partial
from toolz.curried import reduce

from app.psql.models import HostageMessages, ExplosiveMessages

def clean_word(word: str) -> str:
    return word.translate(str.maketrans('', '', string.punctuation))


def most_common_word(list1 : List[HostageMessages], list2 : List[ExplosiveMessages]):
    words_list1 = [
        clean_word(word.lower())
        for sentence in list(map(lambda m: m.content, list1))
        for word in sentence.split()
    ]
    words_list2 = [
        clean_word(word.lower())
        for sentence in list(map(lambda m: m.content, list2))
        for word in sentence.split()
    ]
    word_count = Counter(words_list1 + words_list2)
    return word_count.most_common(1)

