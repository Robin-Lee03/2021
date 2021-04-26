def main():
    perfect = open('perfect.txt','r')
    nevernot = open('never not.txt','r')
    # nevernot = n2
    # perfect = n1
    song = str(input('Chose a song: '))


# def lyric(nevernot,perfect):

    if song == 'perfect':
        for line1 in perfect:
            print(line1)

    elif song == 'nevernot':
        for line2 in nevernot:
            print(line2)

    else:
        print('without the ', song)
















if __name__ == '__main__':
    main()