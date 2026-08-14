 # String method : A method is like tool attached to an object

# name= "kiran"
# print(name.upper())

# 1 . upper() : Converts string into uppercase .

# name = "kiran kumar v"
# print(name.upper())

# 2 . lower() : Converts string into lowercase .

# name2 = "KIRAN KUMAR V"
# print(name2.lower())

# 3 . strip() : Removes the spaces from beginning and ending .

# text = "   Kiran     "
# print(text.strip())

# 4 . split() : Breaks a statement into list of words .

# stat = "I am batman I am manic"
# print(stat.split())

# 5 . replace() : Replaces the word with another word that is defined .

# sentence = "I am spiderman"
# print(sentence.replace("spiderman", "batman"))

# 6 . len() : Returns the number of the characters present in the string .
# also they calculate the space as a character .

# mane = "Kiran Kumar V"
# print(len(mane))

# 7 .title() : Converts the first letter of each word into uppercase .

# name="kiran kumar v"
# print(name.title())

# Combining Methods

# name3 = "         Kiran loves gaming     "
# print(name3.strip().upper().split())
# print(name3.strip().lower().split())

name = "Kiran Kumar V"
print(name.upper())
print(name.lower())

city = "  Bangalore   "
print(city.strip())

sentence = "I love Java"
print(sentence.replace("Java" , "Python"))

skills = "PYTHON AI ML"
print(skills.split())

print(len(name))

# Challenge 01

quote = "It is our choices, Harry, that show what we truly are, far more than our abilities"

print(quote)
print(quote.upper())
print(quote.lower())
print(len(quote))

# Challenge 02

email = "   Kiran@gmail.com   "

print(email)
print(email.strip())
print(email.lower())

# Bonus Challenge

full_name = "Kiran Kumar V "

print(full_name.upper())
print(full_name.lower())
print(len(full_name))