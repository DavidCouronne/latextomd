import re

from latextomd import config
from TexSoup import TexSoup


def _remove_comments(latex_string):
    """Remove comments"""
    return re.sub('(?<!\\\\)%.*$', '', latex_string, flags=re.M)


def _process_preamble(latex_string):
    """Detect latex preamble"""
    if r"\begin{document}" in latex_string:
        preamble, content = latex_string.split(r"\begin{document}")
        if r"\end{document}" in content:
            content = content.split(r"\end{document}")[0]
    else:
        preamble = 'default header\n'
        content = latex_string
    return preamble, content

def _strip_lines(latex_string):
    lines = latex_string.splitlines()
    result = []
    for line in lines:
        result.append(line.strip())
    return '\n'.join(result)

def _clean_lines(latex_string):
    lines = latex_string.splitlines()
    while lines[0] == '':
        lines = lines[1:]
    while lines[-1] == '':
        lines = lines[:-1]
    content = '\n'.join(lines)
    while '\n\n\n' in content:        
        content=content.replace('\n\n\n','\n\n')
    return content

def _delete_blocks(latex_string):
    content = latex_string
    for env in config.del_environnements:
        content = content.replace(env,'')
    return content

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


def to_markdown(latex_string, export_file_name=""):
    content = latex_string
    content = _remove_comments(content)
    
    preamble, content = _process_preamble(content)
    content = Latex(content).process()
    content = _delete_blocks(content)
    content = _strip_lines(content)
    
    content = _clean_lines(content)
    return content
