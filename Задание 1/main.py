def amortizationCounter():
    price=int(input("Введите стоимость оборудования "))
    years=int(input("Введите срок службы оборудования (кол-во лет) "))
    result=price/years/12
    print("Ежемесячный платеж равен", round(result, 2))
   

amortizationCounter()
