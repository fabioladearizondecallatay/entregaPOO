class A: 
    def z(self): 
        return self #devuelve el objeto
 
    def y(self, t): 
        return len(t) #devuelve la longitud del argumento 't'
 
def main():
    a = A() #crea una instancia de la clase A 
    y = a.z #metodo 'z' de instancia 'a' asignado a variable 'z'
    print(y()) #imprime metodo y con argumento a

    aa = A() #otra instancia de la clase A
    print(aa is a) #imprime si las dos instancias son iguales

    z = aa.y #metodo 'y' de instancia 'aa' asignado a varible 'z'

    print(z(())) #imprime el metodo z con argumento de tupla vacia

    print(A().y((A,))) #imprime la longitud de una tupla que contiene la clase A

    print(A.y(aa, (a,z))) #imprime la longitud de una tupla que contiene la clase A y el metodo 'z'

    print(aa.y((z,1,'z'))) #imprime la longitud de una tupla que contiene el metodo 'z', un entero y un string
 
if __name__ == "__main__":
    main()