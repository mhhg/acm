min_seq_length = 4

def Middle(a, b):
  """Return the node between a and b if there is one, or None."""
  if (a+b)%2 != 0:
    return None
  mid = (a+b)/2
  if mid == 5:
    return mid
  if a%3 == b%3:
    return mid
  if (a-1)/3 == (b-1)/3:
    return mid
  return None

def NextValid(base):
  """Generate valid moves j+1 given a sequence of moves 1..j."""
  if len(base) >= 9:
    return
  if len(base) == 0:
    for i in xrange(1,10):
      yield i
    return
  for i in xrange(1,10):
    if not i in base:
      mid = Middle(i, base[-1])
      if mid is None or mid in base:
        yield i

def Sequences(base):
  """Generator for valid sequences of moves."""
  if len(base) >= min_seq_length:
    yield list(base)
  for n in NextValid(base):
    for s in Sequences(base + [n]):
      yield s

seqs_of_length = [0]*10

for seq in Sequences([]):
  seqs_of_length[len(seq)] += 1
  
print 'Sequences by length:', seqs_of_length
print 'Total number of sequences:', sum(seqs_of_length)