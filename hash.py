import os
from BitVector import BitVector

def get_file_hash(file_path):
    bv = BitVector(size=32)

    with open(file_path, "rb") as f:
        while (byte := f.read(1)):
            byte_bv = BitVector(rawbytes=byte)

            bv = bv[:4] | bv.shift_left(4)

            bv = bv ^ byte_bv
            
    return str(bv)

def hash_files_in_dir(dir_path):
    hashes = {}
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            hashes[file_path] = get_file_hash(file_path)
    
    with open("hashes.txt", "w") as hash_file:
        for file_path, file_hash in hashes.items():
            hash_file.write(f"{file_path}: {file_hash}\n")

    return hashes