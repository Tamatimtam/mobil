class Car:
    def __init__(self, name, models):
        self.name = name
        self.models = models
        self.found = 0  # Initialize a per-instance found variable to 0
    
    def display(self):
        print(f"{self.name}")
        for model in self.models: 
            model.display()
        print()
    
    def search_brand(self, brand_name):
        # Reset the found variable for each search
        self.found = 0

        # Check if the current car's brand matches the input brand_name
        if self.name == brand_name:
            print(f"{self.name}")
            for model in self.models:
                model.display()
            print()
            self.found = 1

    def display_all_cars(cars):
        for car in cars:
            car.display()

    def ajukan_kredit(jenis_kredit):
        dokumen_wajib = []

        if jenis_kredit == "perorangan":
            dokumen_wajib = [
                "KTP Suami + Istri",
                "Kartu Keluarga",
                "NPWP",
                "PBB / AJB Rumah",
                "Rekening tabungan 3 bln terakhir",
                "Slip gaji bila bekerja, SKU bila pelaku usaha"
            ]
        elif jenis_kredit == "perusahaan":
            dokumen_wajib = [
                "Fotocopy akte pendirian & perubahannya",
                "Fotocopy pengesahan kehakiman",
                "Fotocopy SIUP, NPWP, SITU / Domisili, TDP",
                "Fotocopy Rek. Koran 3 bulan terakhir",
                "Fotocopy KTP direksi & komisaris"
            ]
        else:
            print("Invalid input. mohon pilih 'perorangan' or 'perusahaan'.")
            return "Pengajuan Kredit Gagal"

        print("Mohon konfirmasi pengumpulan dokumen berikut:")
        dokumen_kurang = []

        for dokumen in dokumen_wajib:
            response = input(f"Sudah mengumpulkan {dokumen}? (yes/no): ").lower()
            if response != "yes":
                dokumen_kurang.append(dokumen)

        if not dokumen_kurang:
            return "Kredit Berhasil!"
        else:
            return f"Kredit Gagal, Dokumen yang kurang: {', '.join(dokumen_kurang)}"


class Model:
    def __init__(self, name, price, premium_color_price=0, two_tone_color_price=0):
        self.name = name
        self.price = price
        self.premium_color_price = premium_color_price
        self.two_tone_color_price = two_tone_color_price

    def display(self):
        price_str = f"Rp. {self.price}"
        if self.premium_color_price:
            price_str += f" + {self.premium_color_price} (Premium Color)"
        if self.two_tone_color_price:
            price_str += f" + {self.two_tone_color_price} (Two-Tone Color)"
        print(f"- {self.name}: {price_str}")


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
    print("4. Exit")
    choice = input("Masukan pilihan (1/2/3/4): ")

    if choice == "1":
        search = input("Masukan Nama Brand yang Ingin Anda Cari: ").upper()
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
        print("Menutup aplikasi. Terimakasih!")
        break
    else:
        print("Pilahan Invalid. Coba lagi (1/2/3/4).")

    another_action = input("Apakah ingin melakukan operasi lain? (yes/no): ")
    if another_action.lower() != "yes":
        print("Menutup aplikasi. Terimakasih!")
        break