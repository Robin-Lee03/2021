def main():
    """
    TODO: DNA compare to find the best match
    """
    long_sequence = input('Please give me a DNA sequence to search: ').upper()
    short_sequence = input('What DNA sequence you would you like to match? ').upper()

    move = len(long_sequence) - len(short_sequence)
    max = 0
    best_match = ''
    for i in range(move+1):
        count = 0
        for j in range(len(short_sequence)):
            if short_sequence[j] == long_sequence[i+j]:
                count += 1
                if count > max:
                    max = count
                    best_match = long_sequence[i:i+len(short_sequence)]


    print('The best match is', best_match)


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
