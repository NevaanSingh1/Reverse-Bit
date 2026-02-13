def rightmost_set_bit(n):
    position = 1
    while n:
        if n & 1:
            return position
        n >>= 1
        position += 1
    return -1

def reverse_bits(n):

    num_bits = n.bit_length()
    reversed_num = 0
    for i in range(num_bits):
       
        reversed_num <<= 1
      
        reversed_num |= (n & 1)
       
        n >>= 1
    return reversed_num

num = int(input("Enter a number: "))
print("Reversed bits:", reverse_bits(num))
