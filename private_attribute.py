#Nama : Dian Adiarma
#Nim : D0219318

class Biodata:
    def __init__(self, nama, nim):
        self.nama= nama #public
        self.__nim = nim #private

    def who(self):
        print('Nama : ', self.nama)
        print('Nim : ', self.__nim)
