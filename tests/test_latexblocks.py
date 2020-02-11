from latextomd.latexblocks import LatexBlocks
import unittest


class TestProcessExercice(unittest.TestCase):
    def test_without_exercice(self):
        latex = r"""some texte"""
        output = LatexBlocks(latex).process()
        self.assertEqual(output, "some texte")

    def test_without_argument(self):
        latex = "\\begin{exercice}"
        output = LatexBlocks(latex).process()
        self.assertEqual(output, ":::exercice Exercice 1:\n\n")

    def test_with_title(self):
        latex = "\\begin{exercice}[title]"
        output = LatexBlocks(latex).process()
        self.assertEqual(output, ":::exercice Exercice 1: title\n\n")

    def test_with_bareme(self):
        latex = "\\begin{exercice}[][2]"
        output = LatexBlocks(latex).process()
        self.assertEqual(output, ":::exercice Exercice 1: /2 points\n\n")

    def test_with_title_and_bareme(self):
        latex = "\\begin{exercice}[title][2]"
        output = LatexBlocks(latex).process()
        self.assertEqual(output, ":::exercice Exercice 1: title /2 points\n\n")
