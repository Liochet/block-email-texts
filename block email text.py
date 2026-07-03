import re

def clean_text(text):
    #remove the punctuation
    return  re.sub(r'[^\w\s]', '', text)



def extract_email(text):
    pattern = r"[a-zA-Z0-9_.+-]@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+\.[a-zA-Z]"
    return re.findall(pattern, text)

# username@gmail.co.za

text = input("Enter your text: ")


cleaned = clean_text(text)
emails = extract_email(text)

def count_words(text):
    words = text.split()
    return len(words)

text = input("Enter your text: ")

cleaned = clean_text(text)
total_words = count_words(cleaned)


def count_unique_words(text):
    # remove duplicates and count unique words
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

import re

def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]  # remove empty strings
    return len(sentences)


import zlib

def compress_text(cleaned_text):
    # Convert string to bytes
    text_bytes = cleaned_text.encode('utf-8')

    # compress the text 
    compressed_data = zlib.compress(text_bytes)

    return compressed_data

    
    