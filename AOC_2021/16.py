# Advent of Code 2021
# Day 16

import os


def parse_data_stream(stream):
    version_size = 3
    type_size    = 3
    header_size = version_size + type_size
    
    packets = []
    stream_index = 0

    while header_size < len(stream[stream_index:]):
        curr_ver = int(stream[stream_index: stream_index + version_size], 2)
        stream_index += version_size
        curr_type = int(stream[stream_index: stream_index + type_size], 2)
        stream_index += type_size
        # Literal value
        if curr_type == 4:
            bin_val = ""
            literal_val = None
            while 5 < len(stream[stream_index:]):
                last_group = not bool(int(stream[stream_index], 2))
                stream_index += 1
                bin_val += stream[stream_index: stream_index + 4]
                stream_index += 4
                if last_group:
                    literal_val = int(bin_val, 2)
                    break    
            packets.append((curr_ver, curr_type, literal_val))
        # Operator
        else:
            if 1 < len(stream[stream_index:]):
                curr_len = int(stream[stream_index])
                stream_index += 1
                len_sub_bits = None
                len_sub = None
                # Next 15 bits
                if curr_len == 0:
                    if 15 <= len(stream[stream_index:]):
                        len_sub_bits = int(stream[stream_index: stream_index + 15], 2)
                        stream_index += 15
                # Next 11 bits
                else:
                    if 11 <= len(stream[stream_index:]):
                        len_sub = int(stream[stream_index: stream_index + 11], 2)
                        stream_index += 11
            packets.append((curr_ver, curr_type, curr_len, len_sub_bits, len_sub))
    
    return packets


def main():
    with open(f"input{os.sep}day16.txt") as puzzle_data:
        puzzle_input = puzzle_data.read().split()
    
    bin_str = ""
    for byte in puzzle_input:
        bin_str += format(int(byte, 16), 'b')

    packets = parse_data_stream(bin_str)
    p1 = 0
    for packet in packets: 
        p1 += packet[0]

    print(f"Part One: {p1}")
   
    p2 = 0
    for packet in packets:
        sub_depth = 0
        curr_ver, curr_type = packet[0:2]
        if curr_type != 4:
            sub_depth += 1
        if curr_type == 0:
            pass    
        if curr_type == 1:
            pass    
        if curr_type == 2:
            pass    
        if curr_type == 3:
            pass    
        if curr_type == 4:
            p2 += packet[2]
        if curr_type == 5:
            pass    
        if curr_type == 6:
            pass    
        if curr_type == 7:
            pass    
                    
    print(f"Part Two: {p2}")


if __name__ == "__main__":
    main()

