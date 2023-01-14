from test_framework import generic_test


def reverse_bits(x: int) -> int:
# these are brut force solution with time complexity = O(n).For multiple use, we can make it efficiant by using lookup table.
    """for i in range(32):
        j = 63 - i
        #print(bin(x))
        x = flip_bits(x,i,j)
        #print(x)
    return x

def flip_bits(input,right_bit_position,left_bit_position):
    #print((1 & (input >> right_bit_position)),(1 & (input >> left_bit_position)))
    if (1 & (input >> right_bit_position)) != (1 & (input >> left_bit_position)):
        bit_mask = (1 << right_bit_position) | (1 << left_bit_position)
        input ^= bit_mask
        return input
    return input"""
# short-cut way
    for i in range(32):
            j = 63 - i
            if (1 & (x >> i)) != (1 & (x >> j)):
                bit_mask = (1 << i) | (1 << j)
                x ^= bit_mask
            
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
