import math

def add(a, b):
    return a +b 

def sub(a, b):
    return a -b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b


operations = {
    '1' : {
        'name' : "Penjumlahan",
        'func' : add 
    },
    '2' : {
        'name' : "Pengurangan",
        'func' : sub 
    },
    '3' : {
        'name' : "Perkalian",
        'func' : add 
    },
    '4' : {
        'name' : "Pembagian",
        'func' : div 
    },
    '5' : {
        'name' : 'Pangkat',
        'func' : math.pow
    }
}

print("List operasi matematika :")

for key, val in operations.items():
    print(key + " " + val['name'])

userChoice = input("Pilihanmu : ")
num1 = float(input("Masukan angka 1 : "))
num2 = float(input("Masukan angka 2 : "))

res = operations[userChoice]['func'](num1, num2)
print("Hasil dari " + operations[userChoice]['name'] + " = " + str(res))
