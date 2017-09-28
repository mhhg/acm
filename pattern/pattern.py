min_seq_length = 4

def middle(a, b):
    """Return the node between a and b if there is one, or None."""
    if (a + b) % 2 != 0:
        return None
    mid = (a + b) / 2
    if mid == 5 or a % 3 == b % 3 or (a - 1) / 3 == (b - 1) / 3:
        return mid
    return None


def next(base):
    """Generate valid moves j+1 given a sequence of moves 1..j."""
    if len(base) >= 9:
        return
    if len(base) == 0:
        for i in range(1, 10):
            yield i
        return
    for i in range(1, 10):
        if not i in base:
            mid = middle(i, base[-1])
            if mid is None or mid in base:
                yield i


def next2(base):
    if len(base) >= 9:
        return
    if len(base) == 0:
        return range(1, 10)
    tmp = []
    for i in range(1, 10):
        if not i in base:
            mid = middle(i, base[-1])
            if mid is None or mid in base:
              tmp.append(i)
    return tmp


def Sequences(base):
    print("base:", base)
    """Generator for valid sequences of moves."""
    if len(base) >= min_seq_length:
        yield list(base)
    x = next2(base)
    print("x:", x)
    for n in x:
        for s in Sequences(base + [n]):
            print("n:", n, "s:", s)
            yield s

def seq2(base):
    if len(base) >= min_seq_length:
      return list(base)
    # tmp = list()
    # for n in next2(base):
    #   for s in seq2(base + [n]):
    #     tmp.append(s)
    # return tmp

def main():
    seqs_of_length = [0] * 10
    for seq in Sequences([]):
        print(seq)
        seqs_of_length[len(seq)] += 1
        return  
    print(seqs_of_length)

if __name__ == "__main__":
    main()