
from re import T


class kosan:
    def __init__(self, kosan):
       self.kosan = kosan 


p1 =kosan("ruang satu : Rp 350.000")
p2 =kosan("ruang dua : Rp 350.000")

print('selamat datang!`')
while True:
     print('---perlengkapan---')
     print('1.dapaur')
     print('2.ruang tamu')
     print('3.tempat tidur')

     perlengkapan = int(input('pilih perlengkapan: '))
     pilihsalahsatu=int(input('pilih yang diminati : '))

     
if perlengkapan == 1:
    print(p1.ruang)
    harga = 350.000 
    print("total yang hars di bayar  Rp." +str(harga))

elif perlengkapan == 2:
    print(p2.ruang)
    harga = 350.000
    print("total yang harus di bayar Rp." +str(harga))
     

    print("---------------------------------")
    print("sinar jaya")
    print("---------------------------------")
    print("ruangan yang di pilih")
    print("---------------------------------")
    print("ruangan yang di pilih")
    print("---------------------------------")
    pilihan=input("apakah anda ingin ambil yang mana Y/N")