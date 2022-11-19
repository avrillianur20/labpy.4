# praktikum.5
## Nama : Avrillia Nur Hidayah
## NIM  : 312210309
## Kelas: TI.22.A3

### Soal

![WhatsApp Image 2022-11-19 at 21 28 53](https://user-images.githubusercontent.com/115686359/202855941-ac6d4707-9a66-490a-9ec3-d7d8ffbb0cef.jpeg)

#### >gunakan fungsi input() untuk memasukkan data.
```
 while True:  
   nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
```

#### >Untuk menambahkan daftar-daftar gunakan ".append()"
```
data.append([nama,nim,tugas,uts,uas,int(akhir)])
```

#### >untuk melakukan perulangan input yang ingin digunakan untuk menambahakan data atau tidak (y/t)
```
tanya = input('Tambahkan Data (y/t) ? ')
```

#### >untuk tampilan daftar datanya
```
print("==================================================================")
print("| No |    Nama      |  NIM  | Tugas |  UTS  |  UAS  |  Akhir |")
print("==================================================================")

i = 0

for nilai in data:
    i += 1
    print("| {no}  | {nama:12s} | {nim:5s} | {tugas:5d} | {uts:5d} | {uas:5d} | {akhir:6.2f} |".format(no=i, nama=nilai[0], nim=nilai[1], tugas=nilai[2],uts=nilai[3],uas=nilai[4],akhir=nilai[5]))

print("==================================================================")
```

#### >outputnya

![Screenshot (619)](https://user-images.githubusercontent.com/115686359/202857437-818146b9-4b8a-4471-ab88-8abe28c37bd5.png)

#### >Flowchart

![WhatsApp Image 2022-11-19 at 22 20 07](https://user-images.githubusercontent.com/115686359/202858191-7ebb62f6-0749-4f31-b9e8-eafd6f696215.jpeg)

# Selesai.
