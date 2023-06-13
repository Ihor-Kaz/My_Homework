# Task description:
# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurence in text bellow
# ( sum of lower and capital cases)
# and write output as table smth like this
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély...."   and print it


poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

sep_num = 27
print("-" * sep_num)
print(f"| {'vowel':^10} | {'count':^10} |")
print("-" * sep_num)
count_a = poem_text.count('A') + poem_text.count('a')
print(f"| {'a':^10} | {count_a:^10} |")
count_e = poem_text.count('E') + poem_text.count('e')
print(f"| {'e':^10} | {count_e:^10} |")
count_i = poem_text.count('I') + poem_text.count('i')
print(f"| {'i':^10} | {count_i:^10} |")
count_o = poem_text.count('O') + poem_text.count('o')
print(f"| {'o':^10} | {count_o:^10} |")
count_u = poem_text.count('U') + poem_text.count('u')
print(f"| {'u':^10} | {count_u:^10} |")
print("-" * sep_num)

replacement_dict = {
    "A": "À",
    "a": "à",
    "E": "É",
    "e": "é",
    "I": "Í",
    "i": "í",
    "O": "Ó",
    "o": "ó",
    "U": "Ú",
    "u": "ú"
}

def replace_characters(poem_text, replace):
    modified_text = ""
    for char in poem_text:
        if char in replace:
            modified_text += replace[char]
        else:
            modified_text += char
    return modified_text


modified_text = replace_characters(poem_text, replacement_dict)
print(modified_text)
