import codecs
import os
import re

from latextomd import config

from latextomd.postpandoc import Postpandoc
from latextomd.soup import Latex
from latextomd.text_manipulation import LatexString


def _process_preamble(latex_string: str) -> tuple:
    """Detect Latex Preamble

    Arguments:
        latex_string {string} -- Latex Source

    Returns:
        tupple -- preamble, content
    """
    if r"\begin{document}" in latex_string:
        preamble, content = latex_string.split(r"\begin{document}")
        if r"\end{document}" in content:
            content = content.split(r"\end{document}")[0]
    else:
        preamble = "\\documentclass{article}\n"
        content = latex_string
    return preamble, content


def _strip_lines(latex_string: str) -> str:
    """Strip Lines in Latex Source

    Arguments:
        latex_string {string} -- LateX Source

    Returns:
        string -- Latex with lines striped
    """
    # latex_string = latex_string.replace("\\\\", "\\newline\n")
    lines = latex_string.splitlines()
    result = []
    for line in lines:
        result.append(line.strip())
    return "\n".join(result)


def _clean_lines(latex_string: str) -> str:
    lines = latex_string.splitlines()
    if lines == []:
        return latex_string
    # while lines[0] == "":
    #     lines = lines[1:]
    # while lines[-1] == "":
    #     lines = lines[:-1]
    content = "\n".join(lines)
    while "\n\n\n" in content:
        content = content.replace("\n\n\n", "\n\n")
    return content


def _delete_blocks(latex_string: str) -> str:
    """delete blocks define in config.del_environnements

    Arguments:
        latex_string {string} -- Latex string

    Returns:
        string -- Latex string
    """
    content = latex_string
    for env in config.del_environnements:
        content = content.replace(env, "")
    return content


def _pandoc(preamble: str, content: str) -> str:
    """Convert latex to md with pandoc

    Arguments:
        preamble {string} -- Latex preamble: documentclass{...}...
        content {string} -- Latex content

    Returns:
        string -- Markdown
    """
    total = "\n\\begin{document}\n".join([preamble, content])  # + "\n\\end{document}"
    total = content
    f = codecs.open("temp/temp.tex", "w", "utf-8")
    f.write(total)
    f.close()
    # os.system("pandoc temp.tex -o temp.md --katex --from latex --to gfm")
    os.system(
        "pandoc temp/temp.tex -o temp/temp.md -f latex+raw_tex  --shift-heading-level-by=1"
    )
    with codecs.open("temp/temp.md", "r", "utf-8") as f:
        content = f.read()

    return content
    # os.system(f"dvisvgm temp.dvi")


def to_markdown(
    latex_string: str, export_file_name: str = "", options: dict = None
) -> str:
    content = latex_string
    content = _strip_lines(content)
    content = re.sub("(?<!\\\\)%.*$", "", content, flags=re.M)

    if not os.path.exists("temp"):
        os.mkdir("temp")
    with open("temp/vrac.tex", "w", encoding="utf-8") as f:
        f.write(content)
    os.system(
        "pandoc temp/vrac.tex -o temp/pandoc_raw.tex -f latex+raw_tex -r markdown-auto_identifiers"
    )
    with open("temp/pandoc_raw.tex", "r") as f:
        content = f.read()
    content = content.replace(r"\textbackslash begin\{document\}", r"\begin{document}")
    content = content.replace(r"\textbackslash end\{document\}", r"\end{document}")

    preamble, content = _process_preamble(content)
    content = Postpandoc(content).process()
    # with open("temp/vrac2.tex", "w", encoding="utf-8") as f:
    #     f.write(content)
    #     os.system("pandoc temp/vrac2.tex -o temp/pandoc_2.tex -f latex+raw_tex ")
    # with open("temp/pandoc_2.tex", "r") as f:
    #     content = f.read()
    # content = Postpandoc(content).process()

    content = LatexString(content, preamble, export_file_name, options).process()
    content = _pandoc(preamble, content)
    # content = Latex(content).process()
    content = Postpandoc(content).process()
    content = _delete_blocks(content)
    # content = _strip_lines(content)

    content = _clean_lines(content)
    if options["mkdocs"]:
        content = admonition_mkdocs(content)
    return content


def admonition_mkdocs(content: str):

    lines = content.splitlines()
    in_block = False
    result = []
    for line in lines:
        if ":::" in line:
            in_block = False
            result.append("")
        elif in_block:
            result.append("    " + line)
        elif "!!!" in line:
            in_block = True
            result.append(line)
        else:
            result.append(line)

    return "\n".join(result)


class LatexToMd(object):
    def __init__(self, latex_string, export_file_name="", options={}):
        """Initialisation LatexToMd

        Arguments:
            latex_string {str} -- latex string

        Keyword Arguments:
            export_file_name {str} -- export file name (default: {""})
        """
        self.content = latex_string
        self.options = options
        self._process_options()

    def _process_options(self):
        try:
            self.pandoc_enumerate = self.options["pandoc_enumerate"]
        except:
            self.pandoc_enumerate = False

    def process(self):
        """Convert Latex String in Markdown String

        Returns:
            {str} -- Markdown String
        """
        self.prepandoc()
        return self.content

    def prepandoc(self):
        self._remove_comments()
        self._replace_simple()
        self._strip_lines()
        self.preamble, self.content = _process_preamble(self.content)
        self.content = _clean_lines(self.content)

    def _remove_comments(self):
        """Remove comments in latex_string"""
        self.content = re.sub("(?<!\\\\)%.*$", "", self.content, flags=re.M)

    def _replace_simple(self):
        """Replace without regex
        use config.replace_simple
        """
        for replace_simple in config.replace_simple:
            self.content = self.content.replace(replace_simple[0], replace_simple[1])

    def _strip_lines(self):
        """Strip lines in latex string"""
        lines = self.content.splitlines()
        result = []
        for line in lines:
            result.append(line.strip())
        self.content = "\n".join(result)
