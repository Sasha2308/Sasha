alphabet = ('A', 'B', 'W', 'G', 'D', 'E', 'V', 'Z', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'H', 'C', 'Q', 'Y', 'X')
morze = ('.-', '-...', '.--', '--.', '-..', '.', '...-', '--..', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '.-.', '...', '-', '..-', '..-.', '....', '-.-.', '--.-', '-.--', '-..-')
alphabet_morze = dict(zip(morze, alphabet))

string_word = tuple(input('Input string: ').split('   '))

string_sym = []
for i in string_word:    
    st = str(i).split(' ')
    for j in st:
        value = alphabet_morze.get(j)
        print(value, end = '')
    print(' ', end = '')
        


#.... .  -.-. .- -- .
#HE CAME 


#.. - ...   .-   --. --- --- -..   .-- . .- - .... . .-.   - --- -.. .- -.--
#ITS A GOOD WEATHER TODAY 
