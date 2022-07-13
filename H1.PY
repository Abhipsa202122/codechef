def minion_game(s):
    # your code goes heres=input()
    vowel='AEIOU'
    l=len(s)
    consonants=0
    vowels=0
    for i in range(l):
        if s[i] in vowel:
            vowels+=l-i
        else:
            consonants+=l-i
    if consonants>vowels:
        print ('Stuart',consonants)
    elif consonants==vowels:
        print ("Draw")
    else:
        print ('Kevin',vowels)

