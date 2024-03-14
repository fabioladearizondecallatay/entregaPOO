class Palindromo:
    #metodo clase
    def esPalindromo(clc, string):
        string = ''.join(c.lower() for c in string if c.isalnum()) #elimina los caracteres que no son alfanuméricos y convierte la cadena a minúsculas
        return string == string[::-1]#comprueba si la cadena es igual a su reverso

#un input para ver si cualquiera cadena es un palindromo
user_input = input("Enter a string to check if it's a palindrome: ")
p = Palindromo() #crea una instancia de la clase

#llama al método esPalindromo y mostrar el resultado como booleano
result = p.esPalindromo(user_input)
print(f">>>{result}")