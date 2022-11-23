nama = []
nim = []
ntugas = []
nuts = []
nuas = []
stop = False
no = 1

while (not stop):
    nama.append (input ("Nama : "))
    nim.append (input("NIM : "))
    ntugas.append (input("Nilai Tugas : "))
    nuts.append (input("Nilai UTS : "))
    nuas.append (input("Nilai UAS : "))
    jawab = input ("Tambah Data (y/t)?" )
    if(jawab == 't'):
        stop = True

for n in range (no):
    nt = float(ntugas[no])*30/100
    nu = float(nuts[no])*35/100
    na = float(nuas[no])*35/100
    akhir = nt+nu+na

print ("========================================================================")
print (" No |  Nama  |   NIM   |   Tugas   |   UTS   |   UAS   |   Akhir   |")
print ("========================================================================")
print (" ",no,"|  ", nama[n],"  |  ", nim[n],"  |  ", ntugas[n], "  |  ", nuts[n], "  |  ", nuas[n], "  |  ", akhir, "  |")
no += 1
print (" ",no,"|  ", nama[n+1],"  |  ", nim[n+1],"  |  ", ntugas[n+1], "  |  ", nuts[n+1], "  |  ", nuas[n+1], "  |  ", akhir+1, "  |")
