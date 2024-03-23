import unittest

from main import CardsFile


class TestCardsFile(unittest.TestCase):

    def test_parse(self):
        md = [
            {"front": "question 1", "back": ["answer 1"]},
            {"front": "question 2", "back": ["answer 2a", "answer 2b"]},
        ]

        cf = CardsFile("test/test.md")
        for i, card in enumerate(cf.cards):
            self.assertEqual(card.front, md[i]["front"])
            self.assertEqual(card.back, md[i]["back"])


if __name__ == "__main__":
    unittest.main()
