# 1) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

for key, value in my_dictionary.items():
    if "c" in str(value) or "c" in str(key):
        print(f"{key} : {value}")

# 2) Aşağıdaki listedeki sayılardan sadece çift sayı olanları başka bir listeye kaydeden bir kod yazınız.

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

ciftler = []
for number in my_numbers:
    if number % 2 == 0:
        ciftler.append(number)
print(ciftler)

# 3) Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]
cevre_list =[]

for r in r_list:
    cevre_list.append(r*2*3.14)
print(cevre_list)

# 4) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur. Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.

age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
yaslar = []
for name,age in age_name_list:
    yaslar.append(age)
print(yaslar)

# 5) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız

import random
metal_list = ["Metallica", "Iron Maiden", "Dream Theater", "Megadeth", "AC/DC"]
random.seed(tuple(metal_list))
print(random.choice(metal_list))


# 6) Aşağıdaki kodun çıktısı ne olacaktır?

number_list = [5,7,18,21,20,10,405,24]
print([num % 2 == 0 for num in number_list])
#[False, False, True, False, True, True, False, True]

#7) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz

barcodeList = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
xyz_list = []
for barcode in barcodeList:
    if "XYZ" in barcode:
        xyz_list.append(barcode)
print(xyz_list)


#8) Aşağıda yazdırılan sınıfı incelediğinizde my_cat.multiply_age() kodunun çıktısı ne olacaktır?


class Cat:
    def __init__(self, name, age=5):
        self.name = name
        self.age = age

    def multiply_age(self):
        return self.age * 3

my_cat = Cat("Whiskers")
print(my_cat.multiply_age())  #15