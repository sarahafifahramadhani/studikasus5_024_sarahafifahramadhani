def harga_parkir(kendaraan, waktu):
    if kendaraan == "mobil":
        harga_perjam = 5000
    elif kendaraan == "motor":
        harga_perjam = 3000
    else:
        harga_perjam = 0
# menghitung total
    total_biaya = harga_perjam * waktu
    return total_biaya
# input dari user
jenis = input("Masukkan Jenis Kendaraan: ")
masuk = float(input("Masukkan Jam Masuk: "))
keluar = float(input("Masukkan Jam keluar: "))
# durasi parkir dari jam masuk dan jam keluar
waktu = keluar - masuk

total_biaya = harga_parkir(jenis, waktu)

print("\n           Biaya Parkir            ")
print("Jenis Kendaraan :",  jenis)
print("Jam masuk :", masuk)
print("Jam Keluar :", keluar)
print("Durasi waktu :", waktu, "jam")
print("Total harga :Rp", total_biaya )