import chardet

data = ""

result = chardet.detect(data)
encoding = result['encoding']
print(f"Detected encoding: {encoding}")

if encoding:
    try:
        decoded_text = data.decode(encoding)
        print(f"Decoded text: {decoded_text}")
    except UnicodeDecodeError:
        print("Decoding failed.")

encodings_to_try = ['latin-1', 'windows-1252', 'utf-8', 'cp437']

for enc in encodings_to_try:
    try:
        decoded_text = data.decode(enc)
        print(f"Decoding with {enc}: {decoded_text}")
    except UnicodeDecodeError:
        print(f"Decoding with {enc} failed.")
