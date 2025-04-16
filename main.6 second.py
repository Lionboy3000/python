num_of_units=int(input("enter units consumed: "))
if num_of_units<50:
    amount=num_of_units*2.60
    surcharge=25
elif num_of_units<100:
    amount=130+((num_of_units-50)*3.6)
    surcharge=35
elif (num_of_units<=200):
    amount=130+165+((num_of_units-100)*5.2)
    surcharge=75
else:
    amount=130+165+526+((num_of_units-200)*8.5)
    surcharge=125
total_amount=amount+surcharge 
print(f"total momthly electricity bill is{total_amount}")