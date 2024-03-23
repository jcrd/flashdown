import argparse

import mistune


class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __str__(self):
        return f"Q: {self.front}\nA: {self.back}"


class CardsFile:
    def __init__(self, filename):
        self.cards = []

        markdown = mistune.create_markdown(renderer=None)

        with open(filename) as f:
            content = markdown(f.read())
            self._parse(content[0])

    def _parse(self, content):
        if content["type"] != "list":
            raise ValueError("Expected list")
        for item in content["children"]:
            if len(item["children"]) != 2:
                raise ValueError("Expected list item with 2 children")

            front_child, back_child = item["children"]

            if front_child["type"] != "block_text":
                raise ValueError("Expected front child to be block text")
            if back_child["type"] != "list":
                raise ValueError("Expected back child to be a list")

            back = []
            for back_item in back_child["children"]:
                back.append(back_item["children"][0]["children"][0]["raw"])

            self.cards.append(Card(front_child["children"][0]["raw"], back))

    def prompt(self):
        for card in self.cards:
            print("Q:", card.front, end="")
            input()
            print("A:")
            for item in card.back:
                print(" " * 2, item)
            print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="flashdown", description="Transform markdown lists into flashcards"
    )
    parser.add_argument("filename")

    args = parser.parse_args()

    CardsFile(args.filename).prompt()
