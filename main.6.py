total_classes=300
attend=int(input("enter classes attended this term: "))
requred_attendance=(75/100)*attend  
fees=10000
fee_paid=int(input("enter amount of fee paid: "))
if attend>=requred_attendance:
    print("you are eligible")
    if fee_paid==fees:
        print("you are eligible for the exam and you fee is paid")
    else:
        print("you are not eligible for the exam due to low fee payment")
else:
    print("you cant do the exams du to low attendance")