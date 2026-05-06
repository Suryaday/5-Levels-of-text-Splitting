text = "A Quick brown fox jumps over the lazy dog. This sentence contains all the letters of the alphabet"
chunks = []
chunk_size = 25

for i in range(4, len(text), chunk_size):
    chunk = text[i-4: i+chunk_size]
    chunks.append(chunk)

print(chunks)