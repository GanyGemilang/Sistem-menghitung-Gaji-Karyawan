import tkinter
from matplotlib.pyplot import text
from tkcalendar import DateEntry
from tkinter import messagebox

try:
    main_window = tkinter.Tk()
    main_window.title("Sistem Menghitung Gaji Karyawan")
    # tidak bisa di atur screen
    main_window.resizable(0,0)

    #Posisi screen di tengah
    widthscreen= main_window.winfo_screenwidth()
    higthscreen= main_window.winfo_screenheight()
    x = int((widthscreen/2) - (500/2))
    y= int((higthscreen/2) - (100/2))
    main_window.geometry(f"660x420+400+110")

    # Label
    tkinter.Label(main_window, text="Sistem Menghitung Gaji Karyawan").grid(row=1, column=1)
    tkinter.Label(main_window, text="Silahkan Input Data Karyawan Anda").grid(row=2, column=1)
    tkinter.Label(main_window, text="Periode").grid(row=3, column=0,padx=0, pady=7)
    tkinter.Label(main_window, text="Sampai").grid(row=3, column=1)
    tkinter.Label(main_window, text="Nama Karyawan", width=20).grid(row=4, column=0)
    tkinter.Label(main_window, text="Jabatan", width=20).grid(row=5, column=0)
    tkinter.Label(main_window, text="Resiko Keja", width=20).grid(row=6, column=0, padx=0, pady=3)
    tkinter.Label(main_window, text="Status Wajib Pajak*", width=20).grid(row=7, column=0, padx=0, pady=3)
    tkinter.Label(main_window, text="Jumlah Anak*", width=20).grid(row=8, column=0, padx=0, pady=3)
    tkinter.Label(main_window, text="Gaji Pokok Karyawan", width=20).grid(row=9, column=0, pady=5)
    tkinter.Label(main_window, text="Tunjangan Karyawan", width=20).grid(row=10, column=0, pady=5)

    #Periode
    start=DateEntry(main_window,selectmode='day', date_pattern='MM-dd-yyyy',width=25, background='darkblue',
                foreground='white', borderwidth=2)
    start.place(x=148, y=50)
    end=DateEntry(main_window,selectmode='day', date_pattern='MM-dd-yyyy',width=25, background='darkblue',
                foreground='white', borderwidth=2)
    end.place(x=395, y=50)

    #nama Karyawan
    nama = tkinter.Entry(main_window, width=70)
    nama.grid(row=4, column=1)

    #Jabatan
    jabatan = tkinter.Entry(main_window, width=70)
    jabatan.grid(row=5, column=1)

    #Resiko Kerja
    ResikoKerja = tkinter.StringVar(main_window)
    ResikoKerja.set("Click Me") # default value
    w = tkinter.OptionMenu(main_window, ResikoKerja, "Resiko Sangat Rendah", "Resiko Rendah", "Resiko Sedang", "Resiko Tinggi", "Resiko Sangat Tinggi")
    w.place(x=144, y=120)

    #Status Perkawinan
    CheckVar1 = tkinter.IntVar()
    CheckVar2 = tkinter.IntVar()
    CheckVar3 = tkinter.IntVar()
    CheckVar4 = tkinter.IntVar()
    CheckVar5 = tkinter.IntVar()
    C1 = tkinter.Checkbutton(main_window, text = "Belum Kawin", variable = CheckVar1, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    C1.place(x=140, y=150)
    C2 = tkinter.Checkbutton(main_window, text = "Kawin", variable = CheckVar2, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    C2.place(x=240, y=150)
    C3 = tkinter.Checkbutton(main_window, text = "Kawin + Istri/Suami", variable = CheckVar3, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    C3.place(x=300, y=150)
    C4 = tkinter.Checkbutton(main_window, text = "Duda", variable = CheckVar4, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    C4.place(x=435, y=150)
    C5 = tkinter.Checkbutton(main_window, text = "Janda", variable = CheckVar5, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    C5.place(x=495, y=150)


    # Jumlah Anak
    anak0 = tkinter.IntVar()
    anak1 = tkinter.IntVar()
    anak2 = tkinter.IntVar()
    anak3 = tkinter.IntVar()
    a1 = tkinter.Checkbutton(main_window, text = "0", variable = anak0, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    a1.place(x=140, y=175)
    a2 = tkinter.Checkbutton(main_window, text = "1", variable = anak1, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    a2.place(x=240, y=175)
    a3 = tkinter.Checkbutton(main_window, text = "2", variable = anak2, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    a3.place(x=300, y=175)
    a4 = tkinter.Checkbutton(main_window, text = "3", variable = anak3, \
                    onvalue = 1, offvalue = 0, height=0, \
                    width = 0)
    a4.place(x=435, y=175)
    a5 = tkinter.Label(main_window, text="*Pilih Salah Satu", width=0)
    a5.place(x=30, y=370)
    a5.config(bg="yellow")

    #gaji Karyawan
    entry_var = tkinter.IntVar()
    gaji = tkinter.Entry(main_window, width=70,textvariable=entry_var)
    gaji.grid(row=9, column=1)

    #Tunjangan Karyawan
    dt1 = tkinter.IntVar()
    dataTunjangan1 = tkinter.Entry(main_window, width=70, textvariable=dt1)
    dataTunjangan1.grid(row=11, column=1)
    label1 = tkinter.Entry(main_window,justify='center', width=20)
    label1.grid(row=11, column=0)
    
    dt2 = tkinter.IntVar()
    dataTunjangan2 = tkinter.Entry(main_window, width=70, textvariable=dt2)
    dataTunjangan2.grid(row=12, column=1)
    label2 = tkinter.Entry(main_window,justify='center', width=20)
    label2.grid(row=12, column=0)

    dt3 = tkinter.IntVar()
    dataTunjangan3 = tkinter.Entry(main_window, width=70, textvariable=dt3)
    dataTunjangan3.grid(row=13, column=1)
    label3 = tkinter.Entry(main_window,justify='center', width=20)
    label3.grid(row=13, column=0)

    dt4 = tkinter.IntVar()
    dataTunjangan4 = tkinter.Entry(main_window, width=70, textvariable=dt4)
    dataTunjangan4.grid(row=14, column=1)
    label4 = tkinter.Entry(main_window,justify='center', width=20)
    label4.grid(row=14, column=0)

    dt5 = tkinter.IntVar()
    dataTunjangan5 = tkinter.Entry(main_window, width=70, textvariable=dt5)
    dataTunjangan5.grid(row=15, column=1)
    label5 = tkinter.Entry(main_window,justify='center', width=20)
    label5.grid(row=15, column=0)

except Exception as e:
    print("Error : ", e)
    messagebox.showerror(title="Error!!!", message="Internal Server Error" )