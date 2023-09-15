def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol."

hasil_penjumlahan = tambah(5, 3)
hasil_pengurangan = kurang(7, 2)
hasil_perkalian = kali(4, 6)
hasil_pembagian = bagi(8, 2)

print(f"Hasil penjumlahan: {hasil_penjumlahan}")
print(f"Hasil pengurangan: {hasil_pengurangan}")
print(f"Hasil perkalian: {hasil_perkalian}")
print(f"Hasil pembagian: {hasil_pembagian}")

