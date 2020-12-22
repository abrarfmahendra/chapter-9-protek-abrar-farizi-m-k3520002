mhs = ['K001 : ROSIHAN ARI         : 1979-09-01 : SOLO', 
       'K002 : DWI AMALIA FITRIANI : 1979-09-17 : KUDUS',
       'K003 : FAZA FAUZAN         : 2005-01-28 : KARANGANYAR']
print("===========================================================")
print("NIM".ljust(10), "NAMA MAHASISWA".ljust(20), "TGL LAHIR".ljust(12), " TEMPAT LAHIR".ljust(8))
print("-----------------------------------------------------------")
for data in mhs :
    mahasiswa          = data.split(':')
    nim                = mahasiswa[0]
    nama               = mahasiswa[1]
    tglLahir           = mahasiswa[2]
    dataTglLahir       = tglLahir.split('-')
    formatBaruTglLahir = '{0}/{1}/{2}'.format(dataTglLahir[0],dataTglLahir[1],dataTglLahir[2])
    tempatLahir        = mahasiswa[3]
    print(nim.ljust(10), nama.ljust(20), formatBaruTglLahir.ljust(15), tempatLahir.ljust(8))
print("-----------------------------------------------------------")
