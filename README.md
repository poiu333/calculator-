# calculator-
# Kalkulator Sederhana

Program kalkulator sederhana berbasis terminal yang ditulis dalam Python. Kalkulator ini mendukung berbagai operasi matematika dasar hingga fungsi ilmiah.

## Fitur

Kalkulator ini memiliki 14 fitur operasi matematika:

1. **Penambahan** (+) - Menjumlahkan dua angka
2. **Pengurangan** (-) - Mengurangkan dua angka
3. **Perkalian** (×) - Mengalikan dua angka
4. **Pembagian** (÷) - Membagi angka pertama dengan angka kedua
5. **Pangkat** (^) - Memangkatkan angka pertama dengan angka kedua
6. **Akar** (√) - Menghitung akar kuadrat dari sebuah angka
7. **Persen** (%) - Menghitung persentase (angka pertama × (angka kedua/100))
8. **Modulus** (%) - Sisa hasil pembagian
9. **Faktorial** (!) - Menghitung faktorial dari sebuah bilangan bulat
10. **Logaritma** (log) - Logaritma natural (basis e) dari sebuah angka
11. **Sinus** (sin) - Menghitung sinus (dalam derajat)
12. **Cosinus** (cos) - Menghitung cosinus (dalam derajat)
13. **Tangen** (tan) - Menghitung tangen (dalam derajat)
14. **Pembulatan** - Membulatkan angka hingga 2 desimal

## Cara Penggunaan

1. Jalankan program:
```bash
python kalkulator.py
```

2. Pilih menu dengan memasukkan angka 1-14 sesuai operasi yang diinginkan
3. Masukkan angka yang diperlukan sesuai instruksi
4. Program akan menampilkan hasil perhitungan
5. Pilih menu 0 untuk keluar dari program

## Contoh Penggunaan

```
pilih_menu_kalkulator
1.penambahan
2.pengurangan
...
0.berhenti
silahkan memilih diantara 1/2/3/4/5/6/7/8/9/10/11/12/13/14/0: 1
Masukkan angka pertama: 10
masukan angka kedua: 5
hasil: 15.00
```

## Catatan Penting

- Untuk pembagian (menu 4) dan modulus (menu 8), angka kedua tidak boleh 0
- Untuk akar (menu 6), angka harus non-negatif
- Untuk faktorial (menu 9), angka harus bilangan bulat non-negatif
- Untuk logaritma (menu 10), angka harus positif
- Untuk persen (menu 7), angka kedua adalah persentase yang ingin dihitung
- Untuk fungsi trigonometri (menu 11,12,13), input dalam satuan derajat
- Hasil perhitungan akan ditampilkan dengan 2 angka di belakang koma

## Requirements

- Python 3.x
- Module math (built-in)

## Struktur Kode

Program ini terdiri dari:
- Fungsi-fungsi matematika untuk setiap operasi
- Validasi input untuk mencegah error
- Loop utama untuk interaksi dengan pengguna
- Penanganan exception untuk input yang tidak valid

## Kontributor

Dibuat oleh: [izam]

## Lisensi

Program ini dapat digunakan dan dimodifikasi secara bebas untuk keperluan pembelajaran.
