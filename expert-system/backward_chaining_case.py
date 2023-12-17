Mobil = ('ertiga', 'jeep', 'camry', 'kijang innova', 'fortuner', 'pajero')

def bool_converter(option):
    if option.lower() == 'ya':
        return True
    elif option.lower() == 'tidak':
        return False
    else:
        raise Exception('Error.. Tolong pilih YA atau TIDAK!')

# Input
nama = str(input("Pilih mobil berikut? ['ertiga', 'jeep', 'camry', 'kijang innova', 'fortuner', 'pajero'] "))

if nama in Mobil:
    boros = bool_converter(input("Apakah mobil tersebut boros? [YA/TIDAK] "))
    bahan_bakar_tinggi = bool_converter(input("Apakah mobil tersebut bahan bakar tinggi? [YA/TIDAK] "))
    bentuk_panjang = bool_converter(input("Apakah mobil tersebut bentuk panjang? [YA/TIDAK] "))
    bentuk_kecil = bool_converter(input("Apakah mobil tersebut bentuk keci? [YA/TIDAK] "))
    offroad = bool_converter(input("Apakah mobil tersebut offroad? [YA/TIDAK] "))

else:
    raise Exception('Error.. Tolong pilih YA atau TIDAK!')

if bahan_bakar_tinggi and bentuk_kecil and nama:
    print("\nBenar.. Itu adalah ertiga")
elif boros and offroad and nama:
    print("\nBenar.. Itu adalah jeep")
elif bentuk_panjang and bahan_bakar_tinggi and nama:
    print("\nBenar.. Itu adalah camry")
elif boros and bentuk_kecil and bahan_bakar_tinggi and nama:
    print("\nBenar.. Itu adalah kijang innova")
elif boros and bentuk_panjang and bahan_bakar_tinggi and nama:
    print("\nBenar.. Itu adalah fortuner")
elif boros and bahan_bakar_tinggi and bentuk_panjang and offroad and nama:
    print("\nBenar.. Itu adalah pajero")
else:
    print("\nTidak ditemukan!")
