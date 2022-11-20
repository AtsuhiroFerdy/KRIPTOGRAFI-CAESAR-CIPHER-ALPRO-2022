import string

abjad = string.ascii_letters
pesan = list(input('Masukkan pesan : '))
enkrip_dekrip = input('e = enkripsi / d = deksripsi : ').lower()
kunci = 3
if enkrip_dekrip == 'e':
    for i in range(len(pesan)):
        if pesan[i] == ' ':
            pesan[i] = ' '
        elif pesan[i] in string.punctuation:
            jawaban = pesan[i]
        elif pesan[i] in string.digits:
            jawaban = pesan[i]
        elif pesan[i] in string.ascii_uppercase:
            jawaban = (abjad.index(pesan[i]) + kunci) % 26
            pesan[i] = abjad[jawaban].upper()
        else:
            jawaban = (abjad.index(pesan[i]) + kunci) % 26
            pesan[i] = abjad[jawaban]
    print(''.join(pesan))

elif enkrip_dekrip == 'd':
    for i in range(len(pesan)):
        if pesan[i] == ' ':
            pesan[i] = ' '
        elif pesan[i] in string.punctuation:
            jawaban = pesan[i]
        elif pesan[i] in string.digits:
            jawaban = pesan[i]
        elif pesan[i] in string.ascii_uppercase:
            jawaban = (abjad.index(pesan[i]) - kunci) % 26
            pesan[i] = abjad[jawaban].upper()
        else:
            jawaban = (abjad.index(pesan[i]) - kunci) % 26
            pesan[i] = abjad[jawaban]
    print(''.join(pesan))
