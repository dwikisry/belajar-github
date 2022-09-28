import random 

angka = random.randint(1, 100)
jawaban = -1
kesempatan = 5

while jawaban != angka :
    jawaban = int(input('Tebak Angka: '))

    if jawaban > angka :
        print('Oops! Kebesaran! Tebak Lagi!')
        kesempatan = kesempatan -1
    elif jawaban < angka :
        print('Oops! Kekecilan! Tebak Lagi!')
        kesempatan = kesempatan -1

    if kesempatan == 0 :
        print('MAAF KESEMPATAN ANDA TELAH HABIS!')
        break

    print()

if jawaban == angka :
    print('SELAMAT ANDA BENAR!')
