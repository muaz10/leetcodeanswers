from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    ldef get_key(log):
        _id, rest = log.split(" ", maxsplit=1)
        return (0, rest, _id) if rest[0].isalpha() else (1, )

    return sorted(logs, key=get_key)

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 art can","let3 art can"]
print(reorderLogFiles(logs))