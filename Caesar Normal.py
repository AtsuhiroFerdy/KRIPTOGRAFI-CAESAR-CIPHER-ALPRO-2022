import string

abjad = string.ascii_letters  # a - Z
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
        else:
            jawaban = abjad.index(pesan[i]) + kunci
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
        else:
            jawaban = abjad.index(pesan[i]) - kunci
            pesan[i] = abjad[jawaban]
    print(''.join(pesan))
