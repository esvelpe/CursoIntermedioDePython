
#Lista de los primeros 100 números elevados al cuadrado
def run():
    power_numbers=[]
    for i in range(1,101):
        power=i**2
        if power%3!=0:
            power_numbers.append(power)

    print(power_numbers)

if __name__=='__main__':
    run()