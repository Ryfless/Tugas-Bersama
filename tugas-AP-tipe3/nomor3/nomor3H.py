#program soal ke 3

nama=str(input('masukkan nama: '))
golongan=int(input('masukkan golongan: '))
jam_kerja=int(input('masukkan jam kerja: '))
gaji_pokok=[1500000, 2000000, 2500000, 3000000]
tunjangan=[250000, 300000, 350000, 400000]
jam=173
lembur=jam_kerja-jam
uang_lembur=lembur*20000

gaji_pokok0=gaji_pokok[0]
gaji_pokok1=gaji_pokok[1]
gaji_pokok2=gaji_pokok[2]
gaji_pokok3=gaji_pokok[3]

print('nama              :',nama)
print('golongan          :',golongan)

if jam_kerja>173:
    lembur==0


if golongan==1:
     gaji_pokok0=gaji_pokok[0]
     print('Gaji Pokok        :',gaji_pokok0)
elif golongan==2:
     gaji_pokok1=gaji_pokok[1]
     print('Gaji Pokok        :',gaji_pokok1)
elif golongan==3:
     gaji_pokok2=gaji_pokok[2]
     print('Gaji Pokok        :',gaji_pokok2)
else:
     gaji_pokok3=gaji_pokok[3]
     print('Gaji Pokok        :',gaji_pokok3)


if golongan==1:
     Pajak_pokok0=gaji_pokok0*0.05
     print('Pajak Gaji Pokok :', Pajak_pokok0)
elif golongan==2:
    pajak_pokok1=gaji_pokok1*0.05
    print('Pajak Gaji Pokok  :',pajak_pokok1)
elif golongan==3:
    pajak_pokok2=gaji_pokok2*0.05
    print('Pajak Gaji Pokok  :',pajak_pokok2)
elif golongan==4:
    pajak_pokok3=gaji_pokok3*0.05
    print('Pajak Gaji Pokok  :',pajak_pokok3)


pajak_lembur=uang_lembur*0.05
print('Pajak Lembur      :',pajak_lembur)


if golongan==1:
     total_pajak0=Pajak_pokok0+pajak_lembur
     print('Total Pajak      :',total_pajak0)
elif golongan==2:
    total_pajak1=pajak_pokok1+pajak_lembur
    print('Total Pajak       :',)
elif golongan==3:
    total_pajak2=pajak_pokok2+pajak_lembur
    print('Total Pajak       :',total_pajak2)
elif golongan==4:
    total_pajak3=pajak_pokok3+pajak_lembur
    print('Total Pajak       :',total_pajak3)


if golongan==1:
    tunjangan0=tunjangan[0]
    print('Tunjangan         :',tunjangan0)
elif golongan==2:
    tunjangan1=tunjangan[1]
    print('Tunjangan         :',tunjangan1)
elif golongan==3:
    tunjangan2=tunjangan[2]
    print('Tunjangan         :',tunjangan2)
else:
    tunjangan3=tunjangan[3]
    print('Tunjangan         :',tunjangan3)

if golongan==1:
    totalgaji0=(gaji_pokok0+uang_lembur+tunjangan0)-total_pajak0
    print('Gaji Diterima     :',totalgaji0)
elif golongan==2:
    totalgaji1=(gaji_pokok1+uang_lembur+tunjangan1)-total_pajak1
    print('Gaji Diterima     :',totalgaji1)
elif golongan==3:
    totalgaji2=(gaji_pokok2+uang_lembur+tunjangan2)-total_pajak2
    print('Gaji Diterima     :',totalgaji2)
elif golongan==4:
    totalgaji3=(gaji_pokok3+uang_lembur+tunjangan3)-total_pajak3
    print('Gaji Diterima     :',totalgaji3)
