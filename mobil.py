class Car:
    def __init__(self, name, models): #Init function
        self.name = name
        self.models = models
        self.found = 0  # Initialize a per-instance found variable to 0
    
    def display(self): #Display one instance of a Car object
        print(f"{self.name}")
        for model in self.models: 
            model.display()
        print()
    
    def search_brand(self, brand_name): #Simple loop for a search
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
