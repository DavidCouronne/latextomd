import unittest
from TexSoup import TexSoup
from latextomd.soup import Latex


class TestProcessSoup(unittest.TestCase):
    def test_init(self):

        self.assertEqual(2 * 2, 4)

    def test_del_command(self):
        latex = r"""some texte\vspace"""
        manip = Latex(latex)
        manip._delete_commands()
        output = manip.get_content()
        self.assertEqual(output, "some texte")

    def test_replace_commands(self):
        latex = r"""\chapter{test}"""
        manip = Latex(latex)
        manip._replace_commands()
        output = manip.get_content()
        self.assertEqual(output, "# test")

    def test_process(self):
        latex = r"""\chapter{test}"""
        manip = Latex(latex)
        output = manip.process()
        self.assertEqual(output, "# test")

    def test_soup(self):
        latex = r"""\psframebox[framesep=.8em,linecolor=black,]{hop
        }"""
        manip = Latex(latex)
        output = manip.process()
        self.assertEqual(output, "hop\n        ")
