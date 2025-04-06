import math
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


def build_index(docs_dict: dict[str, list[str]]) -> dict[str, set[str]]:
    docs_index = {}
    for key, value in docs_dict.items():
        for term in value:
            docs_index.setdefault(term, set()).add(key)

    return docs_index


def search(docs: list[dict[str, str]], string: str) -> list[str]:
    if not docs:
        return []

    def count_term(_key: str) -> float:
        total_score = 0.0
        for _term in terms:
            if _term not in processed_docs_dict[_key]:
                continue
            tf = processed_docs_dict[_key].count(_term) / len(processed_docs_dict[_key])
            total_score += tf * get_idf(_term)
        return total_score

    def get_idf(_term: str):
        idf = math.log2(
            1 + (len(docs) - len(docs_index[_term]) + 1)
            / (len(docs_index[_term]) + 0.5)
        )
        return idf

    docs_dict = {doc["id"]: doc["text"] for doc in docs}
    processed_docs_dict = process_docs(docs_dict)
    docs_index = build_index(processed_docs_dict)

    terms = get_terms(string.split())

    results = set()
    for term in terms:
        if term not in docs_index:
            continue

        results.update(docs_index[term])

    sorted_results = sorted(results, key=count_term, reverse=True)

    return sorted_results
