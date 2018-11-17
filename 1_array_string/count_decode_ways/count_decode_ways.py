
"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message `111` would give 3, since it could be
decoded as `aaa`, `ka` and `ak`.

You can assume that the messages are decodable, For example `001`
is not allowed.


-  `1111` 4
- ["aaaa", "kaa", "aka", "aak", "kk"] 5

-  `11111` 5
- ["aaaaa", "kaaa", "akaa", "aaka", "aaak", "kka", "kak", "akk"] 8

- `261221`
- ["bfabba", "zabba", "bflba", "bfava", "bfabu", "zlu", ...]
"""

import string
mapping = {}
for i, ch in enumerate(string.ascii_lowercase):
    mapping[str(i+1)] = ch


def count_decode_ways(message: str) -> int:
    if not message:
        return 1

    ret = 0
    for i in mapping:
        if message.startswith(i):
            ret += count_decode_ways(message[len(i):])

    return ret


for msg in ["111", "1111", "11111", "261221"]:
    print(msg, "\t=>", count_decode_ways(msg))
