
hours_weekly = input("Enter hours: ")
pay_rate = input("Enter rate: ")
no_ot_net_pay = float(hours_weekly) * float(pay_rate)
ot_pay_rate = float(pay_rate) * 1.5
ot_hours = float(hours_weekly) - 40
ot_pay = float(ot_hours) * float(ot_pay_rate)
ot_net_pay = float(ot_pay) + (float(pay_rate) * 40)


if float(hours_weekly) <= 40:
    print("Gross pay :", no_ot_net_pay)

else:
    print("Gross pay with overtime:", ot_net_pay)
