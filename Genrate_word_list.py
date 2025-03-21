from itertools import product

def generate_wordlist(chars, min_length, max_length, output_file):
    with open(output_file, "w") as f:
        for length in range(min_length, max_length + 1):
            for word in product(chars, repeat=length):
                f.write("".join(word) + "\n")

# Example: Generate 3-6 letter words using lowercase letters
generate_wordlist("abcdefghijklmnopqrstuvwxyz", 3, 6, "custom_file.txt")