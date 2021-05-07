ulang = "yes"

while ulang == "yes":
   pilih = input("input data trunk interface baru? [yes/no]: ")
   if pilih == "yes":
     hostname = input("masukkan hostname switch : ")
     nama = input("masukkan nama interface : ")
     file = open("db-interfaces.txt", 'a')
     file.write("\n"+"hostname switch : " + hostname + ",     " + "name : " + nama)
   else:
    file = open("db-interfaces.txt","r")
    print(file.read())
    break;