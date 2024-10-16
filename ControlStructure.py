#1. Write a PYTHON program to evaluate the student performance
nilai = int(input("Masukkan nilai siswa : "))
if nilai >= 90:
    print("Kinerja: Excellent")
elif nilai >= 80:
    print("Kinerja: Very Good")
elif nilai >= 70:
    print("Kinerja: Good")
elif nilai >= 60:
    print("Kinerja: Average")


#2. Write a PYTHON program to find largest of three numbers!
aa = float(input("Masukkan angka pertama: "))
ba = float(input("Masukkan angka kedua: "))
ca = float(input("Masukkan angka ketiga: "))

terbesar = max(aa, ba, ca)
print("Angka terbesar adalah:", terbesar)


#3. Write a PYTHON program to print Fibonacci series up to n!
an = int(input("Masukkan jumlah elemen Fibonacci: "))

def fibonacci(an):
    a, b = 0, 1
    for an in range(an):
        print(a, end = " ")
        a, b = b, a + b

print("Fibonacci : ")
fibonacci(an)


#4. Write a PYTHON program to print odd numbers up to n!
ganjil = int(input("Masukkan batas nilai ganjil : "))
print("Angka ganjil sampai", ganjil, ":")
for i in range(1, ganjil + 1,):
    if i % 2 != 0:
        print(i, end = " ")


#5. Write a PYTHON program to produce following design
n = int(input("Masukkan nilai n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end = " ")
    print()