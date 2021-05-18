"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    """
    dna = str(input('Please give a DNA strand and I\'ll find the complement: '))
    dna = dna.upper()
    new_one = build_complement(dna)
    print(new_one)

def build_complement(dna):
    ans = ''
    for x in dna:
        if x == 'A':
            ans+='T'
        elif x == 'T':
            ans+='A'
        elif x == 'C':
            ans+='G'
        elif x == 'G':
            ans+='C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
