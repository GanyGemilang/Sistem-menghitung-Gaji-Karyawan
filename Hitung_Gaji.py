class Hitung_Gaji:
    def __init__(self, gaji_karyawan, tunjangan_karyawan,PTKP,resikokerja_karyawan) -> None:
        self.gaji = gaji_karyawan # Gaji Pokok Karyawan
        self.tunjangan = tunjangan_karyawan # Jumlah Tunjangan Yang diterima
        self.PTKP = PTKP #Penghasilan Tidak Kena Pajak
        self.ResikoKerja = resikokerja_karyawan #Resiko
    
    #Method