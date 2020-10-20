from dictionary import alphabet


def translate(string):
    latin_string = ''
    for i in string:
        if i == 'я':
            if temp == 'и':
                latin_string += 'a'
        elif i == 'ю':
            if temp == 'и':
                latin_string += 'u'
        else:
            latin_string += alphabet[i]
        temp = i
    return latin_string
