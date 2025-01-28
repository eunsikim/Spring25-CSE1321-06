def main():
    print("1 Hours of Operation")
    print("2 Sales Department")
    print("3 Billing Department")
    print("4 Spanish")

    userOption = int(input("What would you like to order? "))

    match userOption:
        case 1:
            print("Monday - Friday: 9am - 5pm")
        case 2:
            print("Redirecting to Sales Department")
        case 3:
            print("Redirecting to Billing Department")
        case 4:
            print("1 Horas de Operación")
            print("2 Departamento de Ventas")
            print("3 Departamento de Facturación")
        case _:
            print("Invalid option")

if __name__ == "__main__":
    main()