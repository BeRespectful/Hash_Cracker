import hashlib
import time

def hash_password(password, hash_type):
    """Generate hash of a password using the specified hash type."""
    if hash_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        return None

def crack_hash(hash_value, hash_type, dictionary_file):
    """Attempt to crack the hash using a dictionary attack with response time calculation."""
    try:
        with open(dictionary_file, "r", encoding="utf-8") as file:
            total_start_time = time.time()  # Start total execution time

            for word in file:
                word = word.strip()
                start_time = time.time()  # Start time for each attempt

                generated_hash = hash_password(word, hash_type)

                end_time = time.time()  # End time for each attempt
                response_time = end_time - start_time  # Time taken per attempt

                print(f"Trying: {word} (Time: {response_time:.6f} seconds)")

                if generated_hash == hash_value:
                    total_end_time = time.time()  # End total execution time
                    print(f"\n[+] Password found: {word}")
                    print(f"Total Execution Time: {total_end_time - total_start_time:.6f} seconds")
                    return

            total_end_time = time.time()  # End total execution time
            print("\n[-] Password not found in the dictionary.")
            print(f"Total Execution Time: {total_end_time - total_start_time:.6f} seconds")

    except FileNotFoundError:
        print("Error: Dictionary file not found.")
if __name__ == "__main__":
    print("=== Hash Cracker ===")
    hash_type = input("Enter hash type (md5/sha256): ").lower()
    hash_value = input("Enter hash to crack: ")
    dictionary_file = input("Enter dictionary file path: ")

    if hash_type not in ["md5", "sha256"]:
        print("Error: Unsupported hash type. Use 'md5' or 'sha256'.")
    else:
        crack_hash(hash_value, hash_type, dictionary_file)