import math
nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
         {'nim' : 'A02', 'nama' : 'Budi',     'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha',   'mid' : 100,'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna',    'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah',  'mid' : 70, 'uas' : 100}]
print ('==============================================================')
print("NIM".ljust(10), "NAMA".ljust(10),   "N.MID".ljust(10),  "N.UAS".ljust(10),  "N.AKHIR".ljust(10),  "STATUS".ljust(10))
print ('--------------------------------------------------------------')

for data in nilai :
    HitungNilaiAkhir = (data['mid'] + (2 * data['uas'])) / 3
    
    nilaiakhir = math.ceil(HitungNilaiAkhir)
    
    if (nilaiakhir > 60) :
        status = 'LULUS'
    else :
        status = 'GAGAL'
    print (data['nim'].ljust(10),data['nama'].ljust(12),str(data['mid']).ljust(10),str(data['uas']).ljust(10),str(nilaiakhir).ljust(8),str(status).ljust(10))
print ('--------------------------------------------------------------')
