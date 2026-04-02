Do not use any tools or programming to solve these problems. Work it out yourself by hand, and fill in the answers.

Do not convert any binary numbers to decimal when solving a question unless the question explicitly tells you to.

The goal of these exercises is for you to gain an intuition for binary numbers. Using tools to solve the problems defeats the point.

Convert the decimal number 14 to binary.
Answer:1110

Convert the binary number 101101 to decimal:
Answer:45

Which is larger: 1000 or 0111?
Answer:1000 has a 1 in a higher position than 0111 → 1000 is larger

Which is larger: 00100 or 01011?
Answer:01011 has a higher leading 1 → 01011 is larger

What is 10101 + 01010?
Answer:11111

What is 10001 + 10001?
Answer:100010

What's the largest number you can store with 4 bits, if you want to be able to represent the number 0?
Answer:All 1s → 1111
= 8 + 4 + 2 + 1 = 15

How many bits would you need in order to store the numbers between 0 and 255 inclusive?
Answer:255 = 11111111 → 8 bits

How many bits would you need in order to store the numbers between 0 and 3 inclusive?
Answer:3 = 11 → 2 bits

How many bits would you need in order to store the numbers between 0 and 1000 inclusive?
Answer:10 bits

How can you test if a binary number is a power of two (e.g. 1, 2, 4, 8, 16, ...)?
Answer:A binary number is a power of two if it has exactly one '1' bit and all other bits are '0'. In other words, a binary number that is a power of two will look like this: 1, 10, 100, 1000, etc.              

Convert the decimal number 14 to hex.
Answer:hexadecimal (hex) uses 16 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F therefore 14 in decimal = E in hex

Convert the decimal number 386 to hex.
Answer:Divide by 16 repeatedly (because hex is base 16).
386 ÷ 16 = 24 remainder 2 → the last digit is 2
24 ÷ 16 = 1 remainder 8 → next digit is 8
1 ÷ 16 = 0 remainder 1 → first digit is 1
Write the remainders from top to bottom:

1 → 8 → 2 = 182

Convert the hex number 386 to decimal.
Answer:Hex is base 16, so each digit represents:
3 × 16² = 3 × 256 = 768
8 × 16¹ = 8 × 16 = 128
6 × 16⁰ = 6 × 1 = 6
Add them: 768 + 128 + 6 = 902

Convert the hex number B to decimal.
Answer:B in hex = 11 in decimal

If reading the byte 0x21 as a number, what decimal number would it mean?
Answer:0x21 = hex 21 → base 16
2 × 16 = 32
1 × 1 = 1
Add: 32 + 1 = 33

If reading the byte 0x21 as an ASCII character, what character would it mean?
Answer: !

If reading the byte 0x21 as a greyscale colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:Greyscale ranges 0x00 (black) → 0xFF (white)
0x21 is low value, so it’s dark grey

If reading the bytes 0xAA00FF as an RGB colour, as described in "Approaches for Representing Colors and Images", what colour would it mean?
Answer:red + blue = purple/magenta

If reading the bytes 0xAA00FF as a sequence of three one-byte decimal numbers, what decimal numbers would they be?
AA → 170
00 → 0
FF → 255
Answer: 170, 0, 255 
