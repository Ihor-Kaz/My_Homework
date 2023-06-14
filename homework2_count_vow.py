"""Home-task02.

Task description:
The English language has five vowels: A, E, I, O, and U
Please count each vowel occurence in text bellow
( sum of lower and capital cases)
and write output as table smth like this
-----------------
| vowel | count |
-----------------
|   a   |  11   |
|   e   |  23   |
...
-----------------
then modify text where each vowel replaced with
A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
ex. "Í wàndéréd lónély...."   and print it
"""
sep_num = 27
a = 'AaEeIiOoUu'
b = 'ÀàÉéÍíÓóÚú'

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

print('-' * sep_num)
print(f"| {'vowel':^10} | {'count':^10} |")
print('-' * sep_num)
poem = poem_text.lower()
count_a = poem.count('a')
print(f"| {'a':^10} | {count_a:^10} |")
count_e = poem.count('e')
print(f"| {'e':^10} | {count_e:^10} |")
count_i = poem.count('i')
print(f"| {'i':^10} | {count_i:^10} |")
count_o = poem.count('o')
print(f"| {'o':^10} | {count_o:^10} |")
count_u = poem.count('u')
print(f"| {'u':^10} | {count_u:^10} |")
print('-' * sep_num)

modified_text = str.maketrans(a, b)
print(poem_text.translate(modified_text))
