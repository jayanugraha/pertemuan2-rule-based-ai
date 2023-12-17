def bool_converter(option):
    if option.lower() == 'ya':
        return True
    elif option.lower() == 'tidak':
        return False
    else:
        raise Exception('Error.. Tolong pilih YA atau TIDAK!')

# Input
boros = bool_converter(input("Apakah mobil tersebut boros? [YA/TIDAK] "))
bahan_bakar_tinggi = bool_converter(input("Apakah mobil tersebut bahan bakar tinggi? [YA/TIDAK] "))
bentuk_panjang = bool_converter(input("Apakah mobil tersebut bentuk panjang? [YA/TIDAK] "))
bentuk_kecil= bool_converter(input("Apakah mobil tersebut bentuk kecil? [YA/TIDAK] "))
offroad = bool_converter(input("Apakah mobil tersebut offroad? [YA/TIDAK] "))

if bahan_bakar_tinggi and bentuk_kecil:
    print("\nItu adalah ertiga")
elif boros and offroad :
    print("\nItu adalah jeep")
elif bentuk_panjang and bahan_bakar_tinggi:
    print("\nItu adalah camry")
elif boros and bentuk_kecil and bahan_bakar_tinggi :
    print("\nItu adalah kijang innova")
elif boros and bentuk_panjang and bahan_bakar_tinggi :
    print("\nItu adalah fortuner")
elif boros and bahan_bakar_tinggi and bentuk_panjang and offroad:
    print("\nItu adalah pajero")
else:
    print("\nTidak ditemukan!")