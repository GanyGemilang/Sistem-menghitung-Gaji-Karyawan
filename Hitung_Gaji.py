class Hitung_Gaji:
    def __init__(self, gaji_karyawan, tunjangan_karyawan, PTKP, resikokerja_karyawan) -> None:
        self.gaji = gaji_karyawan # Gaji Pokok Karyawan
        self.tunjangan = tunjangan_karyawan # Jumlah Tunjangan Yang diterima
        self.PTKP = PTKP #Penghasilan Tidak Kena Pajak
        self.ResikoKerja = resikokerja_karyawan #Resiko
    
    #Method hitung BPJS TK (JKK+JKM)
    def Hitung_BPJS_TK1 (self) :
        JKK = self.ResikoKerja
        if JKK == "Resiko Sangat Rendah" :
            hasil1 = (0.3/100 + 0.24/100) * self.gaji
        elif JKK == "Resiko Rendah" :
            hasil1 = (0.3/100 + 0.54/100) * self.gaji
        elif JKK == "Resiko Sedang" :
            hasil1 = (0.3/100 + 0.89/100) * self.gaji
        elif JKK == "Resiko Tinggi" :
            hasil1 = (0.3/100 + 1.27/100) * self.gaji
        else :
            hasil1 = (0.3/100 + 1.74/100) * self.gaji
            
        return hasil1

    #Method hitung BPJS TK (JHT+JP) Perusahaan
    def Hitung_BPJS_TK2 (self) :
        hasil2 = (5.7/100) * self.gaji

        return hasil2

    #Method hitung BPJS Kesehatan Perusahaan
    def Hitung_BPJS_Kes1 (self) :
        hasil3 = (4/100) * self.gaji

        return hasil3

    #Method hitung Total Penghasilan
    def Total_Penghasilan (self, hasil1, hasil2, hasil3) :
        total = self.gaji + self.tunjangan + hasil1 + hasil2 + hasil3

        return total

    #Method hitung Potongan BPJS Kesehatan Karyawan
    def Hitung_BPJS_Kes2 (self) :
        pot1 = (1/100) * self.gaji

        return pot1

    #Method hitung Potongan BPJS TK (JHT+JP) Karyawan
    def Hitung_BPJS_TK3 (self) :
        pot2 = (3/100) * self.gaji

        return pot2

    #Method hitung PPh21
    def Hitung_PPh21 (self, pot1, pot2) :
        if self.gaji < 4500000:
            PPh21 = 0
        else:        
            PPh21 = ((self.gaji + self.tunjangan - pot1 - pot2) - self.PTKP) 
            if(PPh21 <= 60000000):
                PPh21 = PPh21 * (5/100)
            elif(PPh21 > 60000000 and PPh21 <= 250000000 ):
                PPh21 = (60000000 * (5/100)) + ((PPh21-60000000) * (15/100))
            elif(PPh21 > 250000000 and PPh21 <= 500000000 ):
                PPh21 = (60000000 * (5/100)) + ((250000000) * (15/100) + (PPh21-310000000)*(25/100))
            elif(PPh21 > 500000000 and PPh21 <= 500000000000 ):
                PPh21 = (60000000 * (5/100)) + ((250000000) * (15/100) + (500000000)*(25/100) + (PPh21-810000000)*(30/100))
            elif(PPh21 > 500000000 ):
                PPh21 = (60000000 * (5/100)) + ((250000000) * (15/100) + (500000000)*(25/100) + (5000000000)*(30/100) + (PPh21-5810000000)*(30/100))

        return PPh21

    #Method hitung Total Potongan
    def Total_Potongan (self, pot1, pot2, PPh21,tk1,tk2, kes_p) :
        totalpot = pot1 + pot2 + PPh21 + tk1 + tk2 + kes_p

        return totalpot
    
    #Method hitung Total Gaji Karyawan
    def Total_Gaji (self, total, totalpot) :
        totalgaji = total - totalpot

        return totalgaji