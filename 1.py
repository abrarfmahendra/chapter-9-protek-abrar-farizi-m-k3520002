def ubahHuruf(teks, a, b) :
    daftarTeks = list(teks)

    akhir = ''
    for karakterhuruf in daftarTeks :
        if(karakterhuruf == a):
            karakterhuruf = b
        akhir = ''. join ([akhir,karakterhuruf])
    return akhir

print(ubahHuruf('MATEMATIKA', 'T', 'S'))
