from hash import hash_files_in_dir
from make_collisions import make_file_collision

DIR_NAME = "test_dir"
OUTPUT_FILE_NAME = "hashes.txt"

def save_hash_of_dir(hashes: dir, output_path: str):
    with open(output_path, "w") as hash_file:
        for file_path, file_hash in hashes.items():
            hash_file.write(f"{file_path}: {file_hash}\n")

def check_collsions(hashes_file_path: str):
    collsions = False
    with open(hashes_file_path, "r") as hash_file:
        hashes = {}
        for line in hash_file:
            file_path, file_hash = line.strip().split(": ")
            if file_hash in hashes:
                print(f"Collision found: {file_path} and {hashes[file_hash]} have the same hash {file_hash}")
                collsions = True
            else:
                hashes[file_hash] = file_path

    if not collsions:
        print("No collisions found.")



def check_hashes():
    hashes = hash_files_in_dir(DIR_NAME)
    save_hash_of_dir(hashes, OUTPUT_FILE_NAME)
    check_collsions(OUTPUT_FILE_NAME)
    
def create_collision_and_check_hashes():
    make_file_collision(DIR_NAME + "/assignment.txt", DIR_NAME + "/bitvector_doc.txt")
    check_hashes()


# check_hashes()
create_collision_and_check_hashes()