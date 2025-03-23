from search_engine.search_engine import search


def main():
    # Текст документов
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    # создание документа
    # документ имеет два атрибута "id" и "text"
    docs = [
        {'id': 'doc1', 'text': doc1},
        {'id': 'doc2', 'text': doc2},
        {'id': 'doc3', 'text': doc3},
    ]

    # поисковый движок проводит поиск
    result = search(docs, 'shoot')

    print(result)  # => ['doc1', 'doc2']

    # Документы пусты
    search([], 'shoot')  # []


if __name__ == "__main__":
    main()
