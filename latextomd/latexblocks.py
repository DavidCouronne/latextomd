import re

regex_exercice = r"\\begin{exercice}(\[(?P<block_title>.*?)\])?(\[(?P<block_bareme>.*?)\])?"
regex_exercice_compile = re.compile(regex_exercice)

#from latextomd import config


class LatexBlocks(object):
    """class LatexBlocks

    Arguments:
        object {string} -- Latex String Source

    Returns:
        string -- Latex String
    """

    def __init__(self, latex_string):
        self.content = latex_string
        self.exercice = 0

    def process(self):
        self.process_exercice()
        return self.content

    def process_exercice(self):
        """Process block: exercice
        """
        self.content = self.content.replace('\\end{exercice}', '\n\n:::\n\n')
        self.lines = self.content.split('\n')
        newlines = []
        for line in self.lines:
            if "\\begin{exercice}" in line:
                self.exercice = self.exercice + 1
                line = regex_exercice_compile.sub(
                    f':::tip Exercice {self.exercice}: ' + r'\1', self.content)
            newlines.append(line)
        self.lines = newlines
        self.content = '\n'.join(self.lines)
