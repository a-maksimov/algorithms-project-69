from search_engine.search_engine import search

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."

docs = [
    {'id': 'doc1', 'text': doc1},
    {'id': 'doc2', 'text': doc2},
    {'id': 'doc3', 'text': doc3},
]


def main(docs: list[dict[str, str]], string: str) -> list[str]:
    return search(docs, string)


if __name__ == "__main__":
    main(docs, 'shoot')
