from mobil import Car
from model import Model

# region PEMBUATAN OBJEK MODEL
avanzaModel = [
    Model("1.3 MT", 233100000),
    Model("1.3 CVT", 247800000),
    Model("1.5 G MT", 255100000),
    Model("1.5 G CVT", 269800000),
    Model("1.5 G CVT TSS", 295800000),
]
calyaModel = [
    Model("1.2 E MT STD", 160900000),
    Model("1.2 E MT", 163800000),
    Model("1.2 G MT", 169400000),
    Model("1.2 G AT", 183600000),
]
velozModel = [
    Model("1.5 MT", 286000000),
    Model("1.5 Q CVT", 309100000),
    Model("1.5 Q CVT TSS", 331100000),
]
agyaModel = [
    Model("1.2 G MT STD", 159700000),
    Model("1.2 G AT STD", 173300000),
    Model("1.2 GR MT", 165500000),
    Model("1.2 GR AT", 181500000),
]
innovaModel = [
    Model("2.0 G MT", 369600000),
    Model("2.4 G MT", 397100000),
]
innova_zenixModel = [
    Model("Zenix 2.0 G CVT", 419000000, premium_color_price=3000000),
    Model("Zenix 2.0 V CVT", 467000000, premium_color_price=3000000),
    Model("Zenix 2.0 G HV CVT", 458000000, premium_color_price=3000000),
    Model("Zenix 2.0 V HV CVT", 532000000, premium_color_price=3000000),
    Model("Zenix 2.0 Q HV CVT", 611000000, premium_color_price=3000000),
]
raizeModel = [
    Model("1.2 G MT", 232400000, two_tone_color_price=2700000),
    Model("1.2 G CVT", 247300000, two_tone_color_price=2700000),
    Model("1.0 GMT", 251900000, two_tone_color_price=2700000),
    Model("1.0 G CVT", 266900000, two_tone_color_price=2700000),
    Model("1.0 GR CVT", 280800000, two_tone_color_price=2700000),
    Model("1.0 GR CVT TSS", 302500000, two_tone_color_price=2700000),
]
fortunerModel = [
    Model("2.8 VRZ (4X2)", 606200000),
    Model("2.8 VRZ GR (4X2)", 624950000),
    Model("2.8 VRZ GR (4X4)", 715350000),
]
hiaceModel = [
    Model("Comutter MT", 545000000),
    Model("Premio MT", 630000000),
]
gr_86Model = [
    Model("GR 86 2.4L M/T", 922000000),
    Model("GR 86 2.4L A/T", 938500000),
]
supraModel = [
    Model("SUPRA 3.0L A/T", 2051000000),
]
calyaModel = [
    Model("1.2 E MT STD", 160900000),
    Model("1.2 E MT", 163800000),
    Model("1.2 G MT", 169400000),
    Model("1.2 G AT", 183600000),
]
velfireModel = [
    Model("2.5 VELFIRE", 1359600000, premium_color_price=3100000),
]
corolla_crossModel = [
    Model("1.8 HYBRID AT", 540900000, premium_color_price=3800000),
]
corolla_altisModel = [
    Model("1.8 VAT", 514200000, premium_color_price=3000000),
    Model("1.8 HYBRID AT", 565600000, premium_color_price=3000000),
]
camryModel = [
    Model("2.5 V AT", 874600000, premium_color_price=3000000),
    Model("1.5 LAT", 741700000, premium_color_price=3000000),
]
viosModel = [
    Model("1.5 E MT", 314900000, premium_color_price=1500000),
    Model("1.5 G CVT", 355200000, premium_color_price=1500000),
    Model("1.5 G CVT TSS", 368400000, premium_color_price=1500000),
]
hiluxModel = [
    Model("SC 2.0 MT BSN", 269900000),
    Model("SC 2.4 MT DSL", 290900000),
    Model("SC 2.4 MT 4X4 DSL", 393800000),
    Model("DC E MT 4X4 DSL", 431000000),
    Model("DC G MT 4X4 DSL", 464000000),
    Model("DC V AT 4X4 DSL", 513600000),
]
yarisModel = [
    Model("1.2 G CVT 3 AB", 295800000),
    Model("1.5 S MT GR 3 AB", 308100000),
    Model("1.5 S CVT GR 3 AB", 320300000),
    Model("1.5 S CVT GR 7 AB", 325700000),
]
#endregion


#region PEMBUATAN OBJEK CAR
avanza = Car("AVANZA", avanzaModel)
calya = Car("CALYA", calyaModel)
veloz = Car("VELOZ", velozModel)
agya = Car("AGYA", agyaModel)
innova = Car("INNOVA", innovaModel)
innova_zenix = Car("INNOVA ZENIX", innova_zenixModel)
raize = Car("RAIZE", raizeModel)
fortuner = Car("FORTUNER", fortunerModel)
hiace = Car("HIACE", hiaceModel)
gr_86 = Car("GR 86", gr_86Model)
supra = Car("SUPRA", supraModel)
velfire = Car("VELFIRE", velfireModel)
corolla_cross = Car("COROLLA CROSS", corolla_crossModel)
corolla_altis = Car("COROLLA ALTIS", corolla_altisModel)
camry = Car("CAMRY", camryModel)
vios = Car("VIOS", viosModel)
hilux = Car("HILUX", hiluxModel)
# endregion

@staticmethod
def create_car():
        brand_name = input("Masukkan nama merek mobil: ").upper()
        models = []
        while True:
            model_name = input("Masukkan nama model mobil (klik enter untuk selesai): ")
            if not model_name:
                break
            price = int(input("Masukkan harga model: "))
            new_model = Model(model_name, price)  
            models.append(new_model)
        new_car = Car(brand_name, models)
        AllCars.append(new_car)
        print(f"Merek mobil '{brand_name}' dan model-modelnya telah ditambahkan.")


@staticmethod
def update_car_name():
        old_name = input("Masukkan nama merek mobil yang akan diubah: ").upper()
        for car in AllCars:
            if car.name == old_name:
                new_name = input("Masukkan nama baru untuk merek mobil: ").upper()
                car.update_brand_name(new_name)
                print(f"Nama merek mobil '{old_name}' telah diubah menjadi '{new_name}'.")
                return
        print(f"Merek mobil '{old_name}' tidak ditemukan.")

@staticmethod
def delete_model_from_car():
        car_name = input("Masukkan nama merek mobil: ")
        for car in AllCars:
            if car.name == car_name:
                model_name = input("Masukkan nama model yang akan dihapus: ")
                car.delete_model(model_name)
                print(f"Model mobil '{model_name}' dari merek '{car_name}' telah dihapus.")
                return
        print(f"Merek mobil '{car_name}' tidak ditemukan.")

AllCars = [
    avanza, calya, veloz, agya, innova, innova_zenix,
    raize, fortuner, hiace, gr_86, supra, velfire,
    corolla_cross, corolla_altis, camry, vios, hilux
]


while True:
    print("Menu:")
    print("1. Cari merk mobil")
    print("2. Display semua mobil")
    print("3. Ajukan Kredit")
    print("4. Tambah Mobil Baru")
    print("5. Update Nama Merek Mobil")
    print("6. Hapus Model Mobil")
    print("7. Exit")
    choice = input("Masukan pilihan (1/2/3/4/5/6/7): ")

   

    if choice == "1":
            search = input("Masukkan Nama Brand yang Ingin Anda Cari: ").upper()
            found_flag = False
            for car in AllCars:
                car.search_brand(search)
                if car.found == 1:
                    found_flag = True
            if not found_flag:
                print(f"Pencarian {search} tidak membuahi hasil.")

    elif choice == "2":
            Car.display_all_cars(AllCars)

    elif choice == "3":
            jenis_kredit = input("Pilih tipe pemohon (perorangan/perusahaan): ").lower()
            result = Car.ajukan_kredit(jenis_kredit)
            print(result)

    elif choice == "4":
            create_car()

    elif choice == "5":
            update_car_name()

    elif choice == "6":
            delete_model_from_car()

    elif choice == "7":
            print("Menutup aplikasi. Terimakasih!")
            break

    else:
            print("Pilahan Invalid. Coba lagi (1/2/3/4/5/6/7).")

    another_action = input("Apakah ingin melakukan operasi lain? (yes/no): ")
    if another_action.lower() != "yes":
            print("Menutup aplikasi. Terimakasih!")
            break