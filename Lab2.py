def calculate_income_tax():
    print("=== คำนวณภาษีเงินได้บุคคลธรรมดา ===")
    try:
        income = float(input("ป้อนรายได้ต่อปี (บาท): "))

        if income <= 150000:
            tax = 0
        elif income <= 300000:
            tax = (income - 150000) * 0.05
        elif income <= 500000:
            tax = (150000 * 0.05) + ((income - 300000) * 0.10)
        else:
            tax = (150000 * 0.05) + (200000 * 0.10) + ((income - 500000) * 0.20)

        print(f"รายได้ต่อปี: {income:.2f} บาท")
        print(f"ภาษีที่ต้องชำระ: {tax:.2f} บาท")
    except ValueError:
        print("กรุณาป้อนตัวเลขให้ถูกต้อง!")

# เรียกใช้งานฟังก์ชัน
calculate_income_tax()
