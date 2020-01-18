import re

from latextomd import config


class LatexString(object):
    def __init__(self, latex_string):
        self.content = latex_string

    def process(self):
        self._remove_comments()
        return self.content

    def _remove_comments(self):
        self.content = re.sub('(?<!\\\\)%.*$', '', self.content, flags=re.M)
