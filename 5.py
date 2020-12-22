nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas'     : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid'     : 40, 'uas'     : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid'   : 100, 'uas'    : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid'    : 20, 'uas'     : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid'  : 70, 'uas'     : 100}]

print ('=============================================')
print ("NIM" , "\t NAMA" , "\t\tN.MID" , "\t\tN.UAS")
print ('---------------------------------------------')
for data in nilai :
    print (data['nim'].ljust(9),data['nama'].ljust(15),str(data['mid']).ljust(13),str(data['uas']).ljust(9))
print ('---------------------------------------------')
