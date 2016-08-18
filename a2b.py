

def char2brainfuck(char):
    num = ord(char)
    remainder = num % 10
    times = num / 10

    return '++++++++++[>' + '+' * times + '<-]>' + '+' * remainder + '.>'


with open('logo.txt') as f:
    with open('brainfuck_logo.txt', 'w') as g:
        for line in f:
            l = line.rstrip()
            bf = ''
            for i in l:
                bf += char2brainfuck(i)

            g.write(bf + '++++++++++.\n')
