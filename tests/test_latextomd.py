from latextomd import __version__
from latextomd import latextomd
import unittest

export_file = "document.md"


class TestVersionMethods(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.2")


class TestLatexToMdProcess(unittest.TestCase):
    def test_text(self):
        latex_string = "some text"
        markdown_string = latextomd.LatexToMd(latex_string, export_file).process()
        self.assertEqual(markdown_string, markdown_string)

    def test_strip_lines(self):
        latex_string = " some text "
        markdown_string = latextomd.LatexToMd(latex_string, export_file).process()
        self.assertEqual(markdown_string, "some text")

    def test_default_preamble(self):
        latex_string = "some text"
        objet = latextomd.LatexToMd(latex_string, export_file)
        markdown_string = objet.process()
        self.assertEqual(markdown_string, "some text")
        self.assertEqual(objet.preamble, "\\documentclass{article}\n")

    def test_remove_comments(self):
        latex_string = r"some text % some comments"
        markdown_string = latextomd.LatexToMd(latex_string, export_file).process()
        self.assertEqual(markdown_string, "some text")


class TestLatexToMdPrepandoc(unittest.TestCase):
    def test_replace_simple(self):
        latex_string = r"\item \begin{enumerate}"
        latextomd_object = latextomd.LatexToMd(latex_string, export_file)
        latextomd_object.prepandoc()
        markdown_string = latextomd_object.content
        self.assertEqual(markdown_string, "\\item\n\\begin{enumerate}")

    def test_preamble(self):
        latex_string = r"""\documentclass{article}
        \usepackage{mypackage}
        \begin{document}
        some text
        \end{document}
        """
        latextomd_object = latextomd.LatexToMd(latex_string, export_file)
        latextomd_object.prepandoc()
        markdown_string = latextomd_object.content
        self.assertEqual(markdown_string, "some text")
        self.assertEqual(
            latextomd_object.preamble,
            "\\documentclass{article}\n\\usepackage{mypackage}\n\n",
        )
