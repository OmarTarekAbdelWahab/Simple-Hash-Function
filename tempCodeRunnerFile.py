from BitVector import BitVector

with open("test_dir/name2.txt", 'ab') as modified_file:
    # BitVector(bitstring='00000000').write_to_file(modified_file)
    modified_file.write(int("10101010", 2).to_bytes(1, byteorder='big'))


    