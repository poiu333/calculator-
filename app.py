import math
import random
#fungsi matematika
def tambah(x,y): return x+y
def kurang(x,y):return x-y
def kali(x,y):return x*y
def bagi(x,y):
  if y==0: return "Error: tidak bisa dibagi 0"
  return x/y
def pangkat(x,y): return x**y
def akar(x): 
  if x<0: return "Error: tidak bisa akar dari bilangan negatif"
  return x**0.5
def persen (x,y): return x*(y/100)
def modulus(x,y):
  if y==0: return "Error: tidak bisa dibagi 0"
  return x%y
def faktor (x):
  if x<0 or int(x) !=x:
    return "eror: inpur harus bilangan bulat non-negatif/ >0"
  return math.factorial(int(x))
def logaritma(x):
  if x<=0:
    return "error: input harus bilangan positif"
  return math.log(x)
def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))
def tan(x): return math.tan(math.radians(x))
def pembulatan(hasil):
  if isinstance(hasil, (int, float)):
    return round(hasil,2)
  return hasil
single_arg = ['6','9','10','11','12','13','14']
print("pilih_menu_kalkulator")

#menu utama
while True:
  print("1.penambahan")
  print("2.pengurangan")
  print("3.perkalian")
  print("4.pembagian")
  print("5.pangkat")
  print("6.akar")
  print("7.persen")
  print("8.modulus")
  print("9.faktor")
  print("10.logaritma")
  print("11.sinus")
  print("12.cosinus")
  print("13.tangen")
  print("14.pembulatan")
  print("0.berhenti")
  
 
  
 #input

  pilih=input("silahkan memilih diantara 1/2/3/4/5/6/7/8/9/10/11/12/13/14/0: ")
  if pilih == '0':
      print("selamat tinggal")
      break
  if pilih not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14']:
    print("ini bukan pilihan coba ketik 1/2/3/4/5/6/7/8/9/10/11/12/13/14")
    continue
  if pilih not in single_arg:  # operasi yang butuh 2 angka
    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("masukan angka kedua: "))
    except ValueError:
        print("Input tidak valid, coba lagi")
        continue
    if pilih == '4' and num2 == 0:
        print("Error: angka kedua tidak boleh 0 untuk pembagian")
        continue
    if pilih == '8' and num2 == 0:
        print("Error: angka kedua tidak boleh 0 untuk modulus")
        continue
  if pilih == '7':
    print("ingat! untuk persen, angka kedua adalah persentase yang ingin dihitung")
  if pilih == '5':
    print("ingat! untuk pangkat, angka kedua adalah pangkat yang ingin dihitung")
  if pilih in ['6','9','10','11','12','13','14']:
     try:
        num1 = float(input("masukan angka: "))
     except ValueError:
        print("input tidak valid, coba lagi")
        continue
  else:
   try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("masukan angka kedua: "))
   except ValueError:
    print("input tidak valid, coba lagi")
    continue
  #cabang
  menu={
      '1': tambah,
      '2': kurang,
      '3': kali,
      '4': bagi,
      '5': pangkat,
      '6': akar,
      '7': persen,
      '8': modulus,
      '9': faktor,
      '10': logaritma,
      '11': sin,
      '12': cos,
      '13': tan,
      '14': pembulatan
  }
  hasil=menu[pilih](num1,num2) if pilih != '6' and pilih != '9' and pilih != '10' and pilih != '11' and pilih != '12' and pilih != '13' and pilih != '14' else menu[pilih](num1)
  if isinstance(hasil, (int, float)):
    print("hasil: {:.2f}".format(hasil)) 
  else:
    print("hasil: {}".format(hasil))