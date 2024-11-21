def calculator():
    print("=== เครื่องคิดเลข ===")
    print("ตัวเลือกการคำนวณ:")
    print("1. บวก (+)")
    print("2. ลบ (-)")
    print("3. คูณ (*)")
    print("4. หาร (/)")
    print("5. หารเอาเศษ (%)")
    print("6. ยกกำลัง (**)")

    try:

        num1 = float(input("ป้อนจำนวนที่ 1: "))

        num2 = float(input("ป้อนจำนวนที่ 2: "))

        choice = input("เลือกการคำนวณ (1/2/3/4/5/6): ")


        if choice == '1':
            print(f"ผลลัพธ์: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"ผลลัพธ์: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"ผลลัพธ์: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"ผลลัพธ์: {num1} / {num2} = {num1 / num2}")
            else:
                print("ข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้")
        elif choice == '5':
            print(f"ผลลัพธ์: {num1} % {num2} = {num1 % num2}")
        elif choice == '6':
            print(f"ผลลัพธ์: {num1} ** {num2} = {num1 ** num2}")
        else:
            print("ข้อผิดพลาด: เลือกตัวเลือกไม่ถูกต้อง")

    except ValueError:
        print("ข้อผิดพลาด: กรุณาป้อนตัวเลขที่ถูกต้อง")


calculator()
