def read(ruta):
    numbers=[]
    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    return numbers
    #print(numbers)


def write():
    names=["Facundo","Miguel", "Pepe", "Christian","Rocío"]
    with open("./archivos/names.txt","w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()



if __name__=='__main__':
    run()