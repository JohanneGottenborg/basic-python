import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

# match command:
#     case "encode":
#         # Implement the encoding here
#         y = []
#         for c in x:
#             y.append(str(ord(c)))
#         encoding = '0x'.join(y)
#         print(encoding)

#     case "decode":
#         # Implement the decoding here
#         y = x.split('0x')
#         z = []
#         for i in y:
#             n = int(i)
#             z.append(chr(n))
#         decoding = ''.join(z)
#         print(decoding)


if command == "encode":
    # Implement the encoding here
    y = []
    for c in x:
        y.append(str(ord(c)))
    encoding = '0x'.join(y)
    print(encoding)

if command == "decode":
    # Implement the decoding here
    y = x.split('0x')
    z = []
    for i in y:
        n = int(i)
        z.append(chr(n))
    decoding = ''.join(z)
    print(decoding)



# x = 'abcdabc'
# y = []
# for c in x:
#     y.append(str(ord(c)))

# z = '0x'.join(y)

# print(z)

# x = "970x980x990x1000x970x980x99"

# y = x.split('0x')
# z = []
# for i in y:
#     print(i)
#     n = int(i)
#     z.append(chr(n))
# print(z)
# decoding = ''.join(z)

# print(decoding)