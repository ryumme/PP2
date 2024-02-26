def rev(string):
    x = string.split(' ')
    words = ' '.join(x[::-1])
    print(words)

x = input()
rev(x)