from latextomd import config
from TexSoup import TexSoup


class Latex(object):
    def __init__(self, latex_string):
        self.soup = TexSoup(latex_string)

    def _delete_commands(self):
        for command in config.del_commands:
            try:
                for include in self.soup.find_all(command):
                    include.delete()
            except ValueError:
                pass

    def process(self):
        self._delete_commands()
        return repr(self.soup)
