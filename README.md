
# 🔐 Security Lab 6 – Hash Collision Demonstration

This project is part of a computer systems security lab focused on implementing and exploring the behavior of a **custom 32-bit hashing algorithm**. The main objective is to:

- Understand how file hashing works
- Detect hash collisions
- Manually construct collisions by modifying file contents

---

## 👥 Team Members

- **Omar Mahmoud Abdelwahab**
- **Marshelino Maged**
- **Omar Tarek Abdelwahab**

---

## 📌 Problem Statement

You are tasked with creating a simple 32-bit hash function using Python. The hashing function processes each file byte by byte, applies a circular shift, and XOR operations to produce a final 32-bit hash. After computing hashes for all files in a directory, you must detect collisions and manually construct a collision between two files.

---

## 🛠️ How It Works

### 🔄 Custom Hash Function

```python
def get_file_hash(file_path):
    bv = BitVector(size=32)
    with open(file_path, "rb") as f:
        while (byte := f.read(1)):
            byte_bv = BitVector(rawbytes=byte)
            bv = bv[:4] | bv.shift_left(4)
            bv = bv ^ byte_bv
    return str(bv)
```

- **Initialization**: Start with a 32-bit vector of zeroes.
- **Circular Shift**: Perform a 4-bit left circular shift.
- **Mixing**: XOR the current byte into the hash.

---

### 🗂️ Hash Files in a Directory

The script walks through all files (even nested) in a directory and computes their hashes. Results are saved in `hashes.txt`.

---

### ⚠️ Collision Detection

After computing hashes, the program checks for duplicate hash values indicating a collision.

---

### 🧪 Manual Collision Creation

Given two files, the program:

1. Computes their original hashes.
2. Determines 8 bytes to append to one file to **force** a hash collision with the other.
3. Appends the bytes to the file using `BitVector.write_to_file()`.

---

## 📁 Project Structure

```
.
├── hash.py                  # Hash function and file hashing logic
├── make_collisions.py      # Collision generation logic
├── main.py                 # Entry point: hash checking and collision testing
├── hashes.txt              # Output file with computed hashes
├── test_dir/               # Directory with sample files to test
└── README.md               # This file
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install BitVector
```

### 2. Run the script

```bash
python main.py
```

You can uncomment `check_hashes()` or `create_collision_and_check_hashes()` inside `main.py` depending on your desired functionality.  
You can modify/add  the files in `test_dir`.

---

## 📊 Pseudocode Summary

### 🧩 Hashing

```
1. Initialize 32-bit vector to 0
2. For each byte in file:
   a. Circular left shift by 4 bits
   b. XOR with new byte
```

### 🔁 Manual Collision

```
1. Compute hashes h1 and h2
2. Shift h1 right by 4 bits
3. XOR relevant 4-bit chunks of h1 and h2
4. Pad each result to a byte (8 total bytes)
5. Append to second file
```

---

## 📬 Output Example

```
test_dir/file1.txt: 11101010101000001111000010100000
test_dir/file2.txt: 11101010101000001111000010100000
Collision found: file2.txt and file1.txt have the same hash!
```

---
    
