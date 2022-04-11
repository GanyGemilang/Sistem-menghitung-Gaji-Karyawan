import tkinter
import locale
from fpdf import FPDF
from tkinter import messagebox
from datetime import date, datetime
from GUI_Gaji import*
from Hitung_Gaji import*

try:
    def rupiah_format(angka, with_prefix=False, desimal=2):
        locale.setlocale(locale.LC_NUMERIC, 'IND')
        rupiah = locale.format("%.*f", (desimal, angka), True)
        if with_prefix:
            return "Rp. {}".format(rupiah)
        return rupiah

    def pdf():
        try:
            # Get Periode
            a = start.get_date()
            date1= a.strftime("%d %B %Y")
            b = end.get_date()
            date2= b.strftime("%d %B %Y")

            #Get Nama Karyawan
            nama_karyawan = nama.get()
            if(nama_karyawan == str("")):
                messagebox.showwarning(title="Warning!!!", message="Nama Karyawan Tidak Boleh Kosong" )
                return
            #Get Jabatan
            jabatan_karyawan = jabatan.get()
            if(jabatan_karyawan == str("")):
                messagebox.showwarning(title="Warning!!!", message="Jabatan Tidak Boleh Kosong" )
                return
            #Get Resiko
            resikokerja_karyawan = ResikoKerja.get()
            if(resikokerja_karyawan == str("Click Me")):
                messagebox.showwarning(title="Warning!!!", message="Resiko Kerja Tidak Boleh Kosong" )
                return
            
            # Get Status Kawin
            belum_kawin = CheckVar1.get()
            kawin = CheckVar2.get()
            kawin_istri_suami = CheckVar3.get()
            duda = CheckVar4.get()
            janda = CheckVar5.get()
            if(belum_kawin == 0 and kawin == 0 and kawin_istri_suami == 0 and duda == 0 and janda == 0):
                messagebox.showwarning(title="Warning!!!", message="Status Wajib Pajak Tidak Boleh Kosong" )
                return
            elif(belum_kawin + kawin + kawin_istri_suami + duda + janda > 1):
                messagebox.showwarning(title="Warning!!!", message="Pilih Salah Satu Opsi Status Perkawinan" )
                return

            #Get anak
            ank0 = anak0.get()
            ank1 = anak1.get()
            ank2 = anak2.get()
            ank3 = anak3.get()
            if(ank0 == 0 and ank1 == 0 and ank2 == 0 and ank3 == 0):
                messagebox.showwarning(title="Warning!!!", message="Jumlah Anak Tidak Boleh Kosong" )
                return
            elif(ank0 + ank1 + ank2 + ank3 > 1):
                messagebox.showwarning(title="Warning!!!", message="Pilih Salah Satu Opsi Jumlah Anak" )
                return
            
            #Get Gaji
            gaji_karyawan = entry_var.get()
            if(gaji_karyawan == int(0)):
                messagebox.showwarning(title="Warning!!!", message="Gaji Karyawan Tidak Boleh Kosong" )
                return
            #getTunjangan
            tunjangan_karyawan = 0
            if(label1.get() != ""):
                tunjangan_karyawan += int(dataTunjangan1.get())
            elif(label2.get() != ""):
                tunjangan_karyawan += int(dataTunjangan2.get())
            elif(label3.get() != ""):
                tunjangan_karyawan += int(dataTunjangan3.get())
            elif(label4.get() != ""):
                tunjangan_karyawan += int(dataTunjangan4.get())
            elif(label5.get() != ""):
                tunjangan_karyawan += int(dataTunjangan5.get())
            
            # Menghitung PTKP
            PTKP = 0
            if(belum_kawin == 1 or duda == 1 or janda ==1 ):
                PTKP += 4500000
            elif(kawin ==1):
                PTKP += 4500000 + 375000
            elif(kawin_istri_suami ==1):
                PTKP += 4500000 *2
            if(ank0 == 1):
                PTKP = PTKP
            elif(ank1 == 1):
                PTKP += 375000
            elif(ank2 == 1):
                PTKP += 375000*2
            elif(ank3 == 1):
                PTKP += 375000*3

            # Logic Menghitung Gaji
            print(gaji_karyawan, tunjangan_karyawan, PTKP, resikokerja_karyawan)
            #return


            periode         = "Periode " + date1 + " - " + date2
            namakaryawan    = "Nama karyawan    : " + nama_karyawan
            jabatankaryawan = "Jabatan          : " + jabatan_karyawan
            resiko          = "Resiko Kerja     : " + resikokerja_karyawan
            matauang        = "Mata Uang        : IDR"
            Gaji_pokok      = "         Gaji Pokok                       " + rupiah_format(float(gaji_karyawan))
            #Tunjangan_text  = "         Tunjangan {}                     "
            JKK_JKM         = "         Tunjangan BPJS TK (JKK+JKM)      "
            JHT_JP          = "         Tunjangan BPJS TK (JHT+JP)       "
            BPJS_Kes        = "         Tunjangan BPJS Kesehatan         "
            Tot_penghasilan = "         Total Penghasilan                "
            JKK_JKM_2       = "         Potongan BPJS TK (JKK+JKM)       "
            JHT_JP_2        = "         Potongan BPJS TK (JHT+JP)        "
            BPJS_Kes_2      = "         Potongan BPJS Kesehatan          "
            pph21           = "         Potongan PPH21                   "
            Tot_potongan    = "         Total Potongan                   "
            Tot_gaji        = "Total Gaji                                "

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Courier", size=10)
            pdf.cell(200, 10, txt="SLIP PEMBAYARAN GAJI", ln=1, align="C")
            pdf.cell(0, 5, txt=periode, ln=1, align="C")
            pdf.cell(200, 5, txt="", ln=1, align="L")
            pdf.cell(200, 5, txt=namakaryawan, ln=1, align="L")
            pdf.cell(100, 5, txt=jabatankaryawan, ln=1, align="L")
            pdf.cell(100, 5, txt=resiko, ln=1, align="L")
            pdf.cell(100, 5, txt=matauang, ln=1, align="L")
            pdf.cell(100, 5, txt="-----------------------------------------------------------------------------------------", ln=1, align="L")
            pdf.cell(200, 5, txt="", ln=1, align="L")
            pdf.cell(200, 5, txt="Penghasilan", ln=1, align="L")
            pdf.cell(200, 5, txt="", ln=1, align="L")
            pdf.cell(200, 5, txt= Gaji_pokok, ln=1, align="L")
            if(label1.get() != ""):
                Tunjangan1  = "         Tunjangan {}                  ".format(label1.get()) + rupiah_format(float(dataTunjangan1.get()))
                pdf.cell(200, 5, txt= Tunjangan1, ln=1, align="L")
            if(label2.get() != ""):
                Tunjangan2  = "         Tunjangan {}                   ".format(label2.get()) + rupiah_format(float(dataTunjangan2.get()))
                pdf.cell(200, 5, txt= Tunjangan2, ln=1, align="L")
            if(label3.get() != ""):
                Tunjangan3  = "         Tunjangan {}                 ".format(label3.get()) + rupiah_format(float(dataTunjangan3.get()))
                pdf.cell(200, 5, txt= Tunjangan3, ln=1, align="L")
            if(label4.get() != ""):
                Tunjangan4  = "         Tunjangan {}                 ".format(label4.get()) + rupiah_format(float(dataTunjangan4.get()))
                pdf.cell(200, 5, txt= Tunjangan4, ln=1, align="L")
            if(label5.get() != ""):
                Tunjangan5  = "         Tunjangan {}                 ".format(label5.get()) + rupiah_format(float(dataTunjangan5.get()))
                pdf.cell(200, 5, txt= Tunjangan5, ln=1, align="L")

            pdf.cell(200, 5, txt= JKK_JKM, ln=1, align="L")
            pdf.cell(200, 5, txt= JHT_JP, ln=1, align="L")
            pdf.cell(200, 5, txt= BPJS_Kes, ln=1, align="L")
            pdf.cell(200, 5, txt= "", ln=1, align="L")
            pdf.cell(200, 5, txt= Tot_penghasilan, ln=1, align="L")
            pdf.cell(200, 5, txt="", ln=1, align="L")
            pdf.cell(200, 5, txt="Potongan", ln=1, align="L")
            pdf.cell(200, 5, txt="", ln=1, align="L")
            pdf.cell(200, 5, txt= JKK_JKM_2, ln=1, align="L")
            pdf.cell(200, 5, txt= JHT_JP_2, ln=1, align="L")
            pdf.cell(200, 5, txt= BPJS_Kes_2, ln=1, align="L")
            pdf.cell(200, 5, txt= JKK_JKM, ln=1, align="L")
            pdf.cell(200, 5, txt= JHT_JP, ln=1, align="L")
            pdf.cell(200, 5, txt= BPJS_Kes, ln=1, align="L")
            pdf.cell(200, 5, txt= "", ln=1, align="L")
            pdf.cell(200, 5, txt= Tot_potongan, ln=1, align="L")
            pdf.cell(200, 5, txt= "", ln=1, align="L")
            pdf.cell(200, 5, txt= Tot_gaji, ln=1, align="L")


            today = date.today()
            file            = "E:\Belajar Coding\Python PRO\Tugas Akhir\Data\Slip_Gaji_"+ nama_karyawan.replace(" ", "_")+today.strftime("_%d_%m_%Y") +".pdf"
            pdf.output(file, 'F')
            messagebox.showinfo(title="Selamat!!!", message="Anda Berhasil Cetak Slip Gaji Karyawan" )
            # Refresh Form
            start.set_date(datetime.now())
            end.set_date(datetime.now())
            nama.delete('0',tkinter.END)
            jabatan.delete('0',tkinter.END)
            ResikoKerja.set("Click Me")
            CheckVar1.set(0)
            CheckVar2.set(0)
            CheckVar3.set(0)
            CheckVar4.set(0)
            CheckVar5.set(0)
            anak0.set(0)
            anak1.set(0)
            anak2.set(0)
            anak3.set(0)
            entry_var.set(0)
            dt1.set(0)
            dt2.set(0)
            dt3.set(0)
            dt4.set(0)
            dt5.set(0)
            label1.delete('0',tkinter.END)
            label2.delete('0',tkinter.END)
            label3.delete('0',tkinter.END)
            label4.delete('0',tkinter.END)
            label5.delete('0',tkinter.END)
        except Exception as e:
            print("Error : ", e)
            messagebox.showerror(title="Error!!!", message="Internal Server Error" )

    #-----------------------------------Start GUI Tkinter Call GUI_Gaji.py--------------------------------------
    #Cetak Slip Gaji
    Cetak = tkinter.Button(main_window, text="Cetak Slip Gaji", bg="blue" ,fg='white',command= pdf)
    Cetak.place(x= 480,y=370)
    # Method Menampilkan GUI
    main_window.mainloop()

except Exception as e:
    print("Error : ", e)
    messagebox.showerror(title="Error!!!", message="Internal Server Error" )


    
