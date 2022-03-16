def binary_conversion():
    value1 = int(input("1 oktet: "))
    binvalue1 = bin(value1)[2:]
    value2 = int(input("2 oktet: "))
    binvalue2 = bin(value2)[2:]
    value3 = int(input("3 oktet: "))
    binvalue3 = bin(value3)[2:]
    value4 = int(input("4 oktet: "))
    binvalue4 = bin(value4)[2:]

    print("___________________________________________________________________")

    binvalue = binvalue1 + ' ' + binvalue2 + ' ' + binvalue3 + ' ' + binvalue4
    first_ip = value4 - value4 + 1
    print("Adres sieci: " + str(value1) + '.' + str(value2) + '.' + str(value3) + '.' + str(0))
    print("Pierwszy adres: " + str(value1) + '.' + str(value2) + '.' + str(value3) + '.' + str(first_ip))
    print("Adres rozgłoszeniowy: " + str(value1) + '.' + str(value2) + '.' + str(value3) + '.' + str(255))
    print("Zapis binarny podanego adresu: " + ' ' + binvalue)


def subnet_mask_conversion():
    subnet_mask1 = int(input("1 oktet: "))
    subnet_mask_value1 = bin(subnet_mask1)[2:]
    subnet_mask2 = int(input("2 oktet: "))
    subnet_mask_value2 = bin(subnet_mask2)[2:]
    subnet_mask3 = int(input("3 oktet: "))
    subnet_mask_value3 = bin(subnet_mask3)[2:]
    subnet_mask4 = int(input("4 oktet: "))
    subnet_mask_value4 = bin(subnet_mask4)[2:]

    subnet_mask_value = subnet_mask_value1 + ' ' + subnet_mask_value2 + ' ' + subnet_mask_value3 + ' ' + subnet_mask_value4
    print(subnet_mask_value)
    print("Maska podsieci: /" + str(subnet_mask_value.count("1")))


choice = input('1. Zamiana adres IP na binarny i jego właściwości.\n'
               '2. Zamiana maski podsieci na binarny.\n')
if choice == '1':
    binary_conversion()
elif choice == '2':
    subnet_mask_conversion()
else:
    print("Zła komenda.")
