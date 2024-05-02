pemasukan = []

pengeluaran = []

# Fungsi menampilkan list uang masuk
def masuk(input_val):
    pemasukan.append(input_val)

# Fungsi menampilkan list uang keluar
def keluar(input_val):
    pengeluaran.append(input_val)

# Fungsi menampilkan jumlah uang masuk
def sum_masuk():
    sum = 0
    for x in pemasukan:
        sum += x
    return sum

# Fungsi menampilkan jumlah uang keluar
def sum_keluar():
    sum = 0
    for x in pengeluaran:
        sum += x
    return sum

# Fungsi menampilkan uang masuk - uang keluar
def sum_all():
    sum_masuk = 0
    for x in pemasukan:
        sum_masuk += x
    
    sum_keluar = 0
    for x in pengeluaran:
        sum_keluar += x

    return sum_masuk-sum_keluar

while True:
    # Take input from the user
    print("Select menu.")
    print("1.masuk")
    print("2.keluar")
    print("3.sum masuk")
    print("4.sum keluar")
    print("5.sum all")

    choice = input("Pilih menu(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            try:
                input_val = int(input("uang masuk: "))
                masuk(input_val)
                print("list uang masuk:", pemasukan)

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            

        elif choice == '2':
            try:
                input_val = int(input("uang keluar: "))
                keluar(input_val)
                print("list uang keluar:", pengeluaran)

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        elif choice == '3':
            print("jumlah uang masuk:", sum_masuk())

        elif choice == '4':
            print("jumlah uang keluar:", sum_keluar())
        
        elif choice == '5':
            print("jumlah uang masuk - uang keluar:", sum_all())
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Enter anything except 'no' to continue ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")