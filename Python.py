# DÖNGÜLER

# 1-100 arası 7'ye bölünebilen sayılar
for sayi in range(1,100):
    if sayi % 7 == 0:
        print(sayi)

sayi = 0
while sayi < 101:
    if sayi % 7 == 0:
        print(sayi)
    sayi += 1

# BREAK & CONTINUE

# 1-100 sayıları arasında 35,63 sayıları hariç 7' bölünen sayılar

for sayi in range(1,100):
    if sayi % 7 == 0:
        if sayi in [35,63]:
            continue
        print(sayi)

# Sıfır girilene kadar sayının negatif mi pozitif mi olduğunu yazdırır.

while True:
    sayi = int(input("Sayi: "))
    if sayi == 0:
        print("Program sonlandı.")
        break
    elif sayi < 0:
        print("negatif")
    else:
        print("pozitif")

# 2-10 arası sayı çarpanları
# for-else statement break ifadesinin çalışmadığı durumlarda else ifadesini çalıştırır.
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'=', x, '*', int(n/x))
            break
        else:
            print(n, 'asal sayı')

# while-else
print("1 ile 30 arası bir sayi tahmin ediniz:")
sayi = 24
hak = 2
while hak !=0:
    print("Son", hak, "hak")
    tahmin = int(input("Sayi:"))
    if tahmin == sayi:
        print("Bildiniz!")
        break
    hak -= 1
else:
    print("haklarınız tükendi")

# Comprehensions

# List Comprehensions
# 0-19 arası değerleri listede yazmak
liste = []
for sayi in range(0,20):
    liste.append(sayi)

[sayi for sayi in range(0,20)]

# 0-19 arası tek değerleri listede yazmak
liste = []
for sayi in range(0,20):
    if sayi % 2 != 0:
        liste.append(sayi)

[sayi for sayi in range(0,20) if sayi % 2 != 0]

# [-1,2,3,4,-6,-3] listesindeki sayıları pozitif ve negatif old. yazdırma
liste = []
for sayi in [-1,2,3,4,-6,-3]:
    if sayi < 0:
        liste.append("negatif")
    else:
        liste.append("pozitif")

["negatif" if sayi < 0 else "pozitif" for sayi in [-1,2,3,4,-6,-3] ]

# [-1,2,3,4,0,-6,-3] listesindeki sayıları sıfır, pozitif ve negatif old. yazdırma
liste = []
for sayi in [-1,2,3,4,0,-6,-3]:
    if sayi < 0:
        liste.append("negatif")
    elif sayi == 0:
        liste.append("sıfır")
    else:
        liste.append("pozitif")

["negatif" if sayi < 0 else ("sıfır" if sayi == 0 else "pozitif") for sayi in [-1,2,3,4,0,-6,-3]]

# [[1,2,3],[4,5,6],[7,8,9]] matrisinin transpozu
matrix = [[1,2,3],[4,5,6],[7,8,9]]

tr = []
for i in range(len(matrix)):
    n_row = []
    for row in matrix:
        n_row.append(row[i])
    tr.append(n_row)

for i in range(len(tr)):
    print(tr[i])

[[row[i] for row in matrix] for i in range(len(matrix))]

# Dictionary compherensions
# ["aa","bb","cc","dd"] listesine 1 den başlayan id değerleri atamak
liste = ["aa","bb","cc","dd"]
my_dict = {}
for id,name in enumerate(liste,start=1):
    my_dict[id] = name

{id:name for id,name in enumerate(liste,start=1)}

# car_crashes dataset
agg_list = ['mean','min','max','var']
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
df.dtypes
cols = [col for col in df.columns if df[col].dtype != "O"]
{col:agg_list for col in cols}

# tips dataset
df = sns.load_dataset("tips")
df.dtypes
cols = [col for col in df.select_dtypes(include=["float64","int64"])]
agg_list = ['mean','min','max','sum']
{col: [str(col)+"_"+agg for agg in agg_list] for col in cols}

# 0 girilene kadar sayı girilen ortalama çıktısı veren yapı
toplam = 0
n = 0
while True:
    sayi = input("Bir sayi giriniz")
    if sayi != "0":
        if sayi.isnumeric():
            sayi = int(sayi)
            toplam += sayi
            n += 1
        else:
            print("Hatalı değer girdiniz")
    else:
        print("Çıkış yapıldı")
        break

if toplam == 0:
    print("Nothing")
else:
    print(f"ortalama: {toplam / n}")


# Üçgen Çeşiti Yazdırma
a = input("1.kenarı giriniz:")
b = input("2.kenarı giriniz:")
c = input("3.kenarı giriniz:")

if a.isnumeric() and b.isnumeric() and c.isnumeric():
    a, b, c = int(a), int(b), int(c)
    a_sart = abs(b - c) < a < b + c
    b_sart = abs(a - c) < b < a + c
    c_sart = abs(a - b) < c < a + c
    if a_sart and b_sart and c_sart:
        if a == b and b == c:
            print("Eşkenar üçgen")
        elif a == b or b == c or c == a:
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Girilen değerler ile üçgen oluşturulamaz")
else:
    print("Kenar değeri tam sayı olmalı")

# Girilen sayının en büyük pozitif tam böleni
n = input("Bir sayi giriniz:")
if n.isnumeric():
    n = int(n)
    ebb = 0
    for bolen in range(2,n):
        if n % bolen == 0:
            if bolen > ebb:
                ebb = bolen
    print(f"{n} sayisinin ebb değeri {ebb}")
else:
    print("Tam sayı giriniz")

# Bir sayı tek ise 3 ile çarpılıp 1 ekleniyor, çift ise 2 ile bölünüyor. İşlem sayi bir olana kadar devam edecektir.

n = int(input(("Bir sayi giriniz:")))
while n != 1:
    print(n, end=" --> ")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3*n+1
print(1)

