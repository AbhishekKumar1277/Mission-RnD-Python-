__author__ = 'Kalyan'

notes='''
Notes:
1. Don't use any additional modules from python library.
2. Don't change the signature of the function.
3. Review the relevant lessons if you are blocked.

Reading:
Python has an itertools modules which gives powerful utilities to work with iterators.It is a good exercise to read up
all the method implementations on this page: https://docs.python.org/3/library/itertools.html

For e.g. https://docs.python.org/3/library/itertools.html#itertools.chain

You can use ideas from there, but you cannot use itertools module itself in your code :)
'''

def generator_zip(seq1, seq2,*more_seqs):
	if more_seqs == ():
		t = min(len(seq1), len(seq2))
		for x in range(t):
			yield (seq1[x], seq2[x])
	elif type(seq2).__name__ =='generator':
		t=min(len(seq1),min([len(i) for i in more_seqs]))
		a=evens()
		for x in range(t):		
			z=(seq1[x],a.__next__())+ tuple([more_seqs[i][x] for i in range(len(more_seqs))])
			yield z
		
	else:
		t = min(len(seq1), len(seq2), min([len(i) for i in more_seqs]))
		for x in range(t):
			z = (seq1[x], seq2[x]) + tuple([more_seqs[i][x] for i in range(len(more_seqs))])
			yield z


def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass

# an infinite generator of even numbers.
def evens():
    num = 0
    while True:
        yield num
        num += 2

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1, 5), "abc", [1, 2])
    assert [(1, 'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1, 2), "abcd")
    assert [(1, 'a'), (2, 'b')] == list(gen)

    # test with an infinite sequence
    gen = generator_zip("abc", evens(), (1,2))
    assert [('a',0,1), ('b',2,2)] == list(gen)
test_generator_zip()    