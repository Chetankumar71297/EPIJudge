from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    while x:
        """result ^= x & 1 -- runs n times -- time complexity = O(n) -- n is no of bits in input
        x >>= 1"""
        x &= (x-1)  # runs only k times, where k = no of 1 in binary input -- time complexity =O(k)
        result ^= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
