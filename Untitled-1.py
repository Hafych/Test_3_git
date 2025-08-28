def main():
    list_1 = input("Введіть цілі числа через пробіл: ")
    list_1 = [int(i) for i in list_1.split()]
    list_2 = [i for i in list_1 if i % 2 == 0]
    print(f"Парні числа: {list_2}")

if __name__ == "__main__":
    main()
