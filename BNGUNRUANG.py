trisia = print
hitung = 'kubus','balok','bola' 
for x in hitung :
  hitung = str(input('mau menghitung apa ?  (kubus/balok/bola) '))
  if hitung == 'kubus':
   sisi = int(input('sisinya berapa ? '))
   trisia()
   trisia('-------- KUBUS ---------')
   luas = 6*sisi*sisi
   keliling = 12*sisi
   volume = sisi*sisi*sisi
   trisia('luas kubus        = ', luas)
   trisia('keliling kubus    = ', keliling)
   trisia('keliling volume   = ', volume)
   trisia('--------------------------')
   tanya = str(input('Ingin coba menghitung lagi?  (iya/tidak) '))
   if tanya == 'iya':
    continue
   else :
     trisia('======================================================')
     trisia('       PROGRAM MENGHIUTNG BANGUN RUANG SELESAI        ')
     trisia('======================================================')
     break
  if hitung == 'balok':
   panjang  = int(input('panjangnya berapa ? '))
   lebar    = int(input('lebarnya berapa ? '))
   tinggi   = int(input('tingginya berapa ? '))
   trisia()
   trisia('----------- BALOK -----------')
   Luas     = 2*(panjang*lebar)+(panjang*tinggi)+(lebar*tinggi)
   Keliling = 4*(panjang+lebar+tinggi)
   volume   = panjang*lebar*tinggi
   trisia('luas balok     = ', Luas)
   trisia('Keliling balok = ', Keliling)
   trisia('volume balok   = ', volume)
   trisia('-----------------------------')
   tanya = str(input('Ingin coba menghitung lagi? (iya/tidak) '))
   if tanya == 'iya':
     continue
   else :
     trisia('======================================================')
     trisia('       PROGRAM MENGHIUTNG BANGUN RUANG SELESAI        ')
     trisia('======================================================')
     break
  if hitung == 'bola':
    r = int(input('jari-jarinya berapa ? '))
    trisia()
    trisia('----------- BOLA -----------')
    phi = 3.14
    luas = 4*phi*r*r
    keliling = 4/3*phi*r*r
    volume = 4/3*phi*r*r*r
    trisia('Luas balok     = ', luas)
    trisia('Keliling balok = ', keliling)
    trisia('Volume bola  fe= ', volume)
    trisia('----------------------------')
    tanya = str(input('Ingin coba menghitung lagi?  (iya/tidak) '))
    if tanya == 'iya':
     continue
    else :
     trisia('======================================================')
     trisia('       PROGRAM MENGHIUTNG BANGUN RUANG SELESAI        ')
     trisia('======================================================')
     break
