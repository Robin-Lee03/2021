# def change():
#
#
# def main():
#     sentence = str(input('Enter a name: '))


def main():

	s = str(input('Enter a name: '))
	result = change(s)
	print(result)

def change(s):
	ans = ''
	for i in range(len(s)):
		ch = s[i]
		if ch.islower():
			ch = ch.upper()
			ans += ch
		elif ch.isupper():
			ch = ch.lower()
			ans += ch
		else:
			ans += ch

	return ans


if __name__ == '__main__':
	main()