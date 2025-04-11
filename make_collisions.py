from BitVector import BitVector
from hash import get_file_hash

def find_hash_collsion_bytes(h1: BitVector, h2: BitVector):
    """
    Find the bytes that will make two hashes collide.
    h2 is the hash to be modified to be equal to h1.
    Only 8 bytes are needed to make such transformation.
    """
    h1 = h1.deep_copy().shift_right(4) | h1.deep_copy().shift_left(32-4)
    new_bytes = []
    for i in range(0, 32, 4):
        new_bytes.append(str(h2[32-4:] ^ h1[:4]) + "0000")
        
        h1 = h1[:4] | h1.shift_left(4)
        h2 = h2[:4] | h2.shift_left(4)

    return new_bytes

def make_file_collision(fixed_file_path: str, modified_file_path):
    """
    Make a collision between two files.
    The second file will be modified to have the same hash as the first one.
    """
    hash1 = BitVector(bitstring = get_file_hash(fixed_file_path))
    hash2 = BitVector(bitstring = get_file_hash(modified_file_path))

    new_bytes = find_hash_collsion_bytes(hash1, hash2)

    # add the 8 bytes to the end of the file
    with open(modified_file_path, 'ab') as modified_file:
        for byte in new_bytes:
            BitVector(bitstring=byte).write_to_file(modified_file)
