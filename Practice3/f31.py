import struct
import pprint

B_SIZE = 3
D_SIZE = 4 + 8 * 3 + 1 + 1
C_SIZE = 1 + 4 + 2 + 4 + 4 + 8 + 1
A_SIZE = 1 + 1 * 8 + B_SIZE + 4 + 4 * 2 + 2 + 2 + 2


# int8 = b
# int16 = h
# int32 = i
# int64 = q

# float =
# uint8 = B
# uint16 = H
# uint32, размер 4 = I
# uint64, Размер 2 = Q

def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>hB', b_bytes)
    return {
        'B1': b_parsed[0],
        'B2': b_parsed[1]
    }


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>fdddBb', d_bytes)
    return {
        'D1': d_parsed[0],
        'D2': list(d_parsed[1:4]),
        'D3': d_parsed[4],
        'D4': d_parsed[5]
    }


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>BihIIqb', c_bytes)
    return {'C1': c_parsed[0],
            'C2': c_parsed[1],
            'C3': c_parsed[2],
            'C4': c_parsed[3],
            'C5': c_parsed[4],
            'C6': c_parsed[5],
            'C7': c_parsed[6]}


def parse_a(offset, byte_string):
    a12_bytes = byte_string[offset:offset + 9]
    a12_parsed = struct.unpack('>bcccccccc', a12_bytes)

    a3_parsed = parse_b(offset + 9, byte_string)

    a4567_bytes = byte_string[offset + 9 + B_SIZE: offset + 9 + B_SIZE + 18]
    a4567_parsed = struct.unpack('>IIIHHH', a4567_bytes)

    a6_bytes = byte_string[a4567_parsed[4]:a4567_parsed[4] + a4567_parsed[3] * 1]
    a6_parsed = struct.unpack('>' + 'c' * a4567_parsed[3], a6_bytes)
    return {
        'A1': a12_parsed[0],
        'A2': b''.join(a12_parsed[1:]).decode('utf-8'),
        'A3': a3_parsed,
        'A4': a4567_parsed[0],
        'A5': [parse_c(a4567_parsed[1], byte_string),
               parse_c(a4567_parsed[2], byte_string)],
        'A6': b''.join(list(a6_parsed)).decode('utf-8'),
        'A7': parse_d(a4567_parsed[5], byte_string)
    }


def f31(byte_string):
    return parse_a(5, byte_string)


pprint.pprint(f31(b'KXTY>\x80gubccjht\xc6\xa1\xe6\xc9\xdc\x1d\xba\x00\x00\x00#\x00\x00\x00'
                  b';\x00\x02\x00S\x00U\xac\xce\xf4\xe0\xd1~i\x98}\x0cd\x14\xac k\x81\x91'
                  b'\xe5@\x0fj\xaf8dV\xd1\xc5\xd0\xee*\x15\xb7f\x00\xaf\xea\xea0\xed\xd6C'
                  b'\xe2M\xe3\x12\xf61Yse?\x03\xe8\xf5?\xee\xb1}\x1a\xf6\xea\xac\xbf\xe4\xb7'
                  b'\xe8.\xc2\x04\xa8?\xcd\xbe\x8f!\xc3\xb5\x08]"'))



