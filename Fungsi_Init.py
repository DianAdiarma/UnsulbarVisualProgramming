class Motor:
    def __init__(self, inputMerek, inputBahanBakar, inputWarna):
        self.merek = inputMerek
        self.bahan_bakar = inputBahanBakar
        self.warna = inputWarna

Motor1 = Motor("Honda Win 100","Bensin","Hitam")
Motor2 = Motor("Jupiter Z","Bensin","Merah")

print(Motor1.__dict__)
