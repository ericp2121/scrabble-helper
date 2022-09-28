# Course: ITI 1120
# Assignment number: 4
# Name: Zhisheng Peng
# Student number: 300194928
def is_valid_file_name():
    '''()->str or None'''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def get_file_name():
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >> clean_word("co-operate.")
    'cooperate'
    >> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >> clean_word("1982")
    ''
    >> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    # YOUR CODE GOES HERE
    new_word = ''
    for i in word.lower():
        if not (i in "!.?:,'\"-_\\()[]{}%0123456789\t\n"):
            new_word += i
    return new_word


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >> test_letters("listen", "enlist")
    True
    >> test_letters("eekn", "knee")
    True
    >> test_letters("teen", "need")
    False
    '''

    # YOUR CODE GOES HERE
    if len(w1) == len(w2) and ''.join(sorted(w1)) == ''.join(sorted(w2)):
        return True
    else:
        return False


def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.

    >> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''

    # YOUR CODE GOES HERE
    word = clean_word(s)
    word = sorted(word.split())

    n_list = []
    for item in word:
        if item not in n_list:
            n_list.append(item)

    return n_list


def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >> word_anagrams("race", wordbook)
    ['acre', 'care']
    >> word_anagrams("care", wordbook)
    ['acre', 'race']
    >> word_anagrams("year", wordbook)
    []
    >> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''

    # YOUR CODE GOES HERE
    new_list = []
    for item in wordbook:
        item = ''.join(item)
        if test_letters(word, item) and word != item:
            new_list.append(item)

    return new_list


def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''

    # YOUR CODE GOES HERE
    counts = []

    for item in l:
        counts.append(len(word_anagrams(item, wordbook)))

    return counts


def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''

    # YOUR CODE GOES HERE
    new_list = []
    for i in range(len(anagcount)):
        if anagcount[i] == k:
            new_list.append(l[i])

    new_list = sorted(new_list)

    return new_list


def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)

    >> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''

    # YOUR CODE GOES HERE
    k = max(anagcount)
    return k_anagram(l, anagcount, k)


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)

    >> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    # YOUR CODE GOES HERE
    return k_anagram(l, anagcount, 0)


##############################
# main
##############################
wordbook = open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analyze anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice = input()

if choice == '1':
    file_name = get_file_name()
    rawtx = open(file_name).read()
    l = create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l, wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")

    # YOUR CODE GOES HERE
    # when asking for k from the user you may assume that they will enter non-negative integer
    large_list = max_anagram(l, anagcount)
    print(large_list)
    print('')

    anagram_list = []

    for word in large_list:
        print('Anagrams of ',word,'are:',end=' ')
        print(word_anagrams(word, wordbook))
    print('')
    print("Here are the words from your file that have no anagrams: ")
    print(zero_anagram(l, anagcount))
    print('')

    print("Say you are interested if there is a word in your file that has exactly k anagrams:")
    k = int(input("Enter an integer for k:"))
    print("Here is a word(s) in your file with exactly ",k," anagrams:")
    print(k_anagram(l, anagcount, k))

elif choice == '2':

    # YOUR CODE GOES HERE
    letters = input("Enter the letters that you have, one after another with no space:")
    while letters.__contains__(" "):
        print("Error: You entered space(s)")
        letters = input("Enter the letters that you have, one after another with no space:")

    print("Would you like help forming a word with")
    print("1. all these letters")
    print("2. all but one of these letters?")
    choice_2 = input()

    while choice_2 != '1' and choice_2 != '2':
        print("You must choose 1 or 2. Try again.")
        print("Would you like help forming a word with")
        print("1. all these letters")
        print("2. all but one of these letters?")
        choice_2 = input()

    word_1 = word_anagrams(letters, wordbook)

    if letters in wordbook:
        word_1.append(letters)

    if choice_2 == '1':
        if len(word_1) == 0:
            print("There is no word comprised of exactly these letters.")
        else:
            print("Here are the words that are comprised of exactly these letters:")
            print(word_1)

    elif choice_2 == '2':
        print("The letters you gave us were: "+letters)
        print("Let's see what we can get if we omit one of these letters:")
        new_letters = list(letters)

        for i in range(len(letters)):
            new_letters[i] = ""
            new_letters = ''.join(new_letters)
            print("Without the letter in position ",(i+1)," we have: "+new_letters)
            anagram = word_anagrams(new_letters, wordbook)

            if not anagram and new_letters not in wordbook:
                print("There are no word comprised of the letters: "+new_letters)
            elif not anagram and new_letters in wordbook:
                anagram.append(new_letters)
                print(anagram)
            else:
                print(word_anagrams(new_letters, wordbook))

            new_letters = list(new_letters)
            new_letters.insert(i,letters[i])

        else:
            print("Good bye")

else:
    print("Good bye")


