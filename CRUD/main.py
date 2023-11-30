def decide():
    print("1. create\n2. read\n3. update\n4. delete")
    option = int(input("Masukan pilihanmu: "))
    return option

def create(data):
    print(f"<File {data} dibuat>")
    i = open(f"{data}.txt", "x")
    i.close()

def read(data):
    print("<Operasi read dijalankan>")
    i = open(f"{data}.txt", "r")
    display = i.read()
    i.close()
    return display

def update(data):
    print("1. Ubah seluruh file\n2. Tambah data")
    option = int(input("Masukan pilihanmu: "))

    if option == 1:
        print("<Operasi ubah dijalankan>")
        i = open(f"{data}.txt", "w")
        inp = input("Masukan input: ")
        i.write(inp)
        i.close()
    elif option == 2:
        print("<Operasi tambah dijalankan>")
        j = open(f"{data}.txt", "a")
        inp = input("Masukan input: ")
        j.write("\n" + inp)
        j.close()
    else:
        print("error")

def delete(data):
    print(f"Data dalam {data}.txt akan dihapus")
    i = open(f"{data}.txt", "w")
    i.write(" ")

def main():
    print("===Program CRUD===")
    print("==================")

    option = decide()
    match option:
        case 1:
            nameDat = input("Masukan nama file baru: ")
            create(nameDat)
        case 2:
            nameDat = input("Masukan nama data yang ingin diakses: ")
            display = read(nameDat)
            print(display)
        case 3:
            nameDat = input("Masukan nama data yang ingin diakses: ")
            update(nameDat)
        case 4:
            nameDat = input("Masukan nama data yang ingin diakses: ")
            delete(nameDat)
    
    print("===Program selesai===")
    
main()
