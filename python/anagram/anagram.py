def find_anagrams(word: str, candidates: list):
    return [c for c in candidates if \
            sort_upper_split(word)==sort_upper_split(c) and \
            word.upper() != c.upper()]

def sort_upper_split(word: str):
    return sorted(l for l in word.upper())