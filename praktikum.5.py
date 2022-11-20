nama = input("masukkan Nama:")
nim = input("masukkan NIM:")
uts = input("masukkan nilai UTS:")
uas = input("masukkan nilai UAS:")
tugas = input("masukkan nilai TUGAS:")

akhir = (int(tugas) * .2) + (int(uts) * .4) + (int(uas) * .4)

print("\nNama                       :",nama)
print("\nNIM                        :",nim)
print("Nilai UTS                    :",uts)
print("Nilai UAS                    :",uas)
print("Nilai Tugas                  :",tugas)
print("Nilai Akhir                  :",akhir)

print (' ')
print ('Tambah Data? (ya/tidak)')
x=input()
