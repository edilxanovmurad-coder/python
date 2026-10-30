import sys

word1 = input("please type first word : ")
word2 = input("please type second word : ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("They are anagrams!", sorted(word1), sorted(word2))
else:
    print("They are not anagrams.", sorted(word1), sorted(word2))
