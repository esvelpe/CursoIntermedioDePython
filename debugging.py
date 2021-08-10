def divisors(num):
        divisors=[i for i in range(1,num+1) if num%i==0]

        return divisors


# def run():
#     try:
#         num=int(input("Ingresa un número: "))
#         if num<0:
#             raise ValueError("Debe ingresar un número positivo")
#         print(divisors(num))
#         print("Terminó mi programa")
#     except ValueError as ve:
#         print(ve)

def run():
    num=input("Ingresa un número: ")
    assert num.isnumeric(),"Debe ingresar un número entero"
    print(divisors(int(num)))
    print("Terminó mi programa")

        



if __name__=='__main__':
    run()