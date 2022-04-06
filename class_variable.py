#Nama : Dian Adiarma
#Nim : D0219318

class transportasi():
    motor = "Honda Blade"

    def __init__(self, input_nama):
        self.nama = input_nama #public
kendaraan = transportasi("Motor Honda Blade")

print(transportasi.motor)
print(kendaraan.motor)
