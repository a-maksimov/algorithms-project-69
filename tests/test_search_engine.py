from search_engine.search_engine import search


def test_search_engine():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {'id': 'doc1', 'text': doc1},
        {'id': 'doc2', 'text': doc2},
        {'id': 'doc3', 'text': doc3},
    ]

    assert search(docs, 'shoot') == ['doc2', 'doc1']


def test_punctuation():
    doc1 = {
        'id': 'doc1', 'text': "I can't shoot straight unless I've had a pint!"
    }
    docs = [doc1]

    assert search(docs, 'pint!') == ['doc1']


def test_ranging():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {'id': 'doc1', 'text': doc1},
        {'id': 'doc2', 'text': doc2},
        {'id': 'doc3', 'text': doc3},
    ]

    assert search(docs, 'shoot') == ['doc2', 'doc1']


def test_fuzzy_search():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {'id': 'doc1', 'text': doc1},
        {'id': 'doc2', 'text': doc2},
        {'id': 'doc3', 'text': doc3},
    ]

    assert search(docs, 'shoot at me') == ['doc2', 'doc1']


def test_short_strings():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."
    docs = [
        {"id": 'doc1', "text": doc1},
        {"id": 'doc2', "text": doc2},
        {"id": 'doc3', "text": doc3},
    ]

    assert search(docs, 'shoot at me, nerd') == ['doc2', 'doc1']
