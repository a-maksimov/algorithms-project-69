import re


def get_term(token: str) -> str:
    processed_token = re.findall(r'\w+', token)
    term = ''.join(processed_token).lower()
    return term


def get_terms(tokens: list[str]) -> list[str]:
    terms = []
    for token in tokens:
        terms.append(get_term(token))
    return terms


def process_docs(docs_dict: dict[str, str]) -> dict[str, list[str]]:
    processed_docs_dict = {}
    for key, value in docs_dict.items():
        terms = []
        for token in value.split():
            terms.append(get_term(token))
        processed_docs_dict[key] = terms

    return processed_docs_dict


def search(docs: list[dict[str, str]], string: str) -> list[str]:
    if not docs:
        return []

    def count_term(_key: str) -> int:
        counter = 0
        for word in processed_docs_dict[_key]:
            if word not in terms:
                continue
            counter += 1
        return counter

    docs_dict = {doc["id"]: doc["text"] for doc in docs}
    processed_docs_dict = process_docs(docs_dict)
    terms = get_terms(string.split())

    results = []
    for key, value in processed_docs_dict.items():
        if not any(term in value for term in terms):
            continue
        results.append(key)

    sorted_results = sorted(results, key=count_term, reverse=True)

    return sorted_results
