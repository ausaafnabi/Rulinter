import re
from typing import Iterable, Iterator
import tokenize
from tokenize import TokenInfo

class LineEndingsChecker:
    name = 'line-endings-checker'
    version = '1.0'
    _message_crlf = 'LE001: CRLF line ending found'
    _message_cr = 'LE002: CR line ending found'

    def __init__(self, tree=None, filename=None, lines=None, file_tokens: Iterable[TokenInfo] = None):
        self.tree = tree
        self.filename = filename
        self.lines = lines
        assert file_tokens
        self._tokens = file_tokens
    
    def run(self)->Iterator[tuple]:
        if self._tokens is None:
            return

        for token in self._tokens:
            if token.type == tokenize.NL:
                if token.string.endswith('\r\n'):
                    yield (token.start[0], token.start[1], self._message_crlf, self.name)
                elif token.string.endswith('\r'):
                    yield (token.start[0], token.start[1], self._message_cr, self.name)

    # def run(self) -> Iterator[tuple]:
    #     if self.lines is None:
    #         return
    #
    #     for i, line in enumerate(self.lines, start=1):
    #         if line.endswith('\r\n'):
    #             yield (i, 0, self._message_crlf, self.name)
    #         elif line.endswith('\r'):
    #             yield (i, 0, self._message_cr, self.name)
