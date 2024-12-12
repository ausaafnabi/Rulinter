import re
import tokenize
from tokenize import TokenInfo
from typing import Iterable, Iterator, Set
from flake8 import checker

class RussianCommentsChecker:
    name = 'russian-comments-checker'
    version = '1.0'
    _message = 'RU001: Russian comment found'

    REX_WORD = re.compile(r'[а-яА-Я]+')
    REX1 = re.compile(r'(.)([А-Я][а-я]+)')
    REX2 = re.compile(r'([а-я0-9])([А-Я])')

    def __init__(self, tree=None, filename=None, lines=None, file_tokens: Iterable[TokenInfo] = None):
        self.tree = tree
        self.filename = filename
        assert file_tokens
        self._tokens = file_tokens

    def get_words(self, text: str) -> Set[str]:
        text = self.REX1.sub(r'\1 \2', text)
        text = self.REX2.sub(r'\1 \2', text).lower()
        text = text.replace('_', ' ')
        words = set(self.REX_WORD.findall(text))
        words = {w for w in words if len(w) > 1}
        return words

    def get_russian_comments(self, tokens: Iterable[TokenInfo]) -> Iterator[TokenInfo]:
        comment = None
        multiline_comment = True
        for token in tokens:
            if token.type == tokenize.NL:
                continue
            if token.type == tokenize.COMMENT:
                if comment is None:
                    comment = token
                else:
                    comment = None
                continue

            multiline_comment = False
            if comment is None:
                continue
            comment_words = self.get_words(comment.string)
            if comment_words:
                yield comment
            comment = None

    def run(self) -> Iterator[tuple]:
        for comments in self.get_russian_comments(self._tokens):
            yield (
                comments.start[0],
                comments.start[1],
                self._message,
                self.name,
            )





