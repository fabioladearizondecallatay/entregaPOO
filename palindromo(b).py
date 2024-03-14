class Palindromo:
    #constructor
    def __init__(self, attribute):
        self.attribute = attribute

    #método de clase
    def esPalindromo(self, string):
        string = ''.join(c.lower() for c in string if c.isalnum()) #elimina los caracteres que no son alfanuméricos y convierte la cadena a minúsculas
        return string == string[::-1], string.upper() #comprueba si la cadena es igual a su reverso

    #método para probar si el atributo es un palíndromo
    def test(self):
        result, uppercase_attribute = self.esPalindromo(self.attribute)
        return result, uppercase_attribute

    #método especial para representar el objeto como una cadena
    def __str__(self):
        result, uppercase_attribute = self.esPalindromo(self.attribute)
        return f"{result}\n{uppercase_attribute}" #tambien devuelve el resultado en mayuscula

#un input para ver si cualquiera cadena es un palindromo
user_input = input("Enter a string to check if it's a palindrome: ")
p = Palindromo(user_input)

# llama al método esPalindromo y mostrar el resultado como booleano
result, uppercase_attribute = p.esPalindromo(user_input)
print(f">>>{result}")

#llama el metodo test y muestra la cadena en mayuscula
result, uppercase_attribute = p.test()
print(f">>>{uppercase_attribute}")