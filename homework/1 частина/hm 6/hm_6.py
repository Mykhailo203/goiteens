text = input('Enter text').rstrip()

is_end = False
space_prev = 0
max_word = ''
max_word_lengh = 0


while not is_end:
    space_current = text.find(' ', space_prev)
    if text.find(' ', space_current) == -1:
        #пробілів бльше немає
        print(max_word)
        is_end = True
    else:
        current_word = text[space_prev : space_current]
        space_prev = space_current +1
        if len(current_word) > max_word_lengh:
            max_word = current_word
            max_word_lengh = len(current_word)