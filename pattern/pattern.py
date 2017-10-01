min_seq_length = 4
Seq = list()
length = [0] * 10


def middle(a, b):
    """Return the node between a and b if there is one, or None."""
    if (a + b) % 2 != 0:
        return None
    mid = (a + b) / 2
    if mid == 5 or a % 3 == b % 3 or (a - 1) / 3 == (b - 1) / 3:
        return mid


def next(base):
    if len(base) == 0:
        return list(xrange(1, 10))
    tmp = list()
    for i in xrange(1, 10):
        if not i in base:
            mid = middle(i, base[-1])
            if mid is None or mid in base:
                tmp.append(i)
    return tmp


def generate(base):
    for n in next(base):
        s = base + [n]
        generate(s)
        Seq.append(s)


def count():
    generate([])
    for seq in Seq:
        if len(seq) >= min_seq_length:
            length[len(seq)] += 1

    print "length:", length, "total:", sum(length)


if __name__ == "__main__":
    count()
