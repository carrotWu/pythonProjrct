result =''
bySourceByte = b'\xfc\xa5\xc9\x16\x1eT\xa6\xe9\x1e\xc6\x07G\xec7\xaf\xb2'
len = len(bySourceByte)
for i in range(len):
    tb = bySourceByte[i]
    print(tb)
    tmp = chr(tb >> 4 & 0xF)
    print(tmp)
    if (tmp >= '\n'):
        high = chr(97 + ord(tmp) - 10)
        print(high)
    else:
        high = chr(ord('0') + ord(tmp))
        print(high)
    result += high
    tmp = chr(tb & 0xF)
    print('--------------'+tmp)
    if (tmp >= '\n'):
        low = chr(97 + ord(tmp) - 10)
        print(low)
    else:
        low = chr(ord('0') + ord(tmp))
        print(low)
    result += low

print(result)
