def count_word(text):
    words = text.split()
    return len(words)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__" :
    print("It is working fine.")