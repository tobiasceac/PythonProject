def computepay(hours, rate):
    if hours > 40:
        overtime = hours - 40
        pay = 40 * rate + (overtime * (rate * 1.5))
    else:
        pay = hours * rate
    return pay


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print("Pay: ", computepay(hours, rate))