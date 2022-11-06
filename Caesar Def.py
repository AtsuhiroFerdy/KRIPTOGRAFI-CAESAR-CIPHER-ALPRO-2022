import string


def operasi(teks, kunci, geser):
    hasil = ''

    for i in range(len(teks)):
        kata = teks[i]
        if geser == 'e':
            if kata.isupper():
                hasil += chr((ord(kata) + kunci - 65) % 26 + 65)

            elif kata.islower():
                hasil += chr((ord(kata) + kunci - 97) % 26 + 97)

            elif kata in string.punctuation or string.digits:
                hasil += teks[i]

        elif geser == 'd':
            if kata.isupper():
                hasil += chr((ord(kata) - kunci - 65) % 26 + 65)

            elif kata.islower():
                hasil += chr((ord(kata) - kunci - 97) % 26 + 97)

            elif kata in string.punctuation or string.digits:
                hasil += teks[i]

    return hasil


teks = input("Masukkan Teks : ")
kunci = int(input('Masukkan kunci : '))
geser = input('enkrip or dekrip (e / d) : ').lower()
print("\nPesan: ", teks)
print("Kunci: ", kunci)
print("Hasil: ", operasi(teks, kunci, geser))
