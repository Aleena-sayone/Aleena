fname = "demo.docx"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
print("number of lines  :", num_lines)
print("Number of Words  :", num_words)
print("Number of Charactors :", num_chars)