class Logger:
    def __init__(self):
        self.logfile = open("log.txt", 'a')#abre un archivo de registro con modo de anadir informacion
        self.count = 0
        self.logfile.write("--Start log--\n")#mensaje de inicio 
    
    def log(self, message):
        self.logfile.write(message + '\n')#escribe un mensaje inicial
        self.count += 1

    def close(self):
        self.logfile.write("--End log: {} log(s)--".format(self.count)) #para escriir un mensaje con el numero total de llamadas
        self.logfile.close() #cierra el archivo 


class Test:
    def __init__(self):
        self.logger = Logger() #crea un objeto logger
        
    def llamada(self, message): #registra un mensaje con el objeto logger
        self.logger.log(message)


def main():
    test = Test() #crea un objeto
    for i in range(1, 6): #realiza llamadas de prueba
            if i == 1:
                test.llamada("Primera llamada")
            else:
                test.llamada("{}a llamada".format(i))
    test.logger.close()  #cierra el regsitrado desues de registrar todas las llamadas 

#lee e imprime el contenido del archivo
with open("log.txt", "r") as file:
    print(file.read())

if __name__ == "__main__":
    main()
