def run():
    power_numbers=[]
    for i in range(1,101):
        power=i**2
        power_numbers.append(power)

    print(power_numbers)

if __name__=='__main__':
    run()