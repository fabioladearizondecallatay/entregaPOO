# entregaPOO

Para el ejercicio a) Palindromo - metodo de clase 
Este programa verifica si una cadena de texto es un palíndromo o no.
El programa define una clase llamada `Palindromo`, que contiene un método estático llamado `esPalindromo`. Este método toma una cadena de texto como entrada, elimina los caracteres que no son alfanuméricos y convierte la cadena a minúsculas. Luego, verifica si la cadena es igual a su reverso. 
Para usarlo hay que ingresar una cadena de texto, luego el programa imprimirá `True` si la cadena es un palíndromo y `False` si no lo es.

B) Palindromo - metodo de instancia 
El programa define una clase llamada `Palindromo`, que tiene los siguientes métodos:
- `__init__(self, attribute)`: El constructor de la clase que inicializa un atributo `attribute`.
- `esPalindromo(self, string)`: Un método que toma una cadena de texto como entrada, elimina los caracteres que no son alfanuméricos, convierte la cadena a minúsculas y verifica si es un palíndromo. Retorna una tupla con dos valores: un booleano indicando si la cadena es un palíndromo y la cadena en mayúsculas.
- `test(self)`: Un método que llama al método `esPalindromo()` y retorna el resultado y la cadena en mayúsculas.
- `__str__(self)`: Un método especial que representa el objeto como una cadena, llamando al método `esPalindromo()` para obtener el resultado y la cadena en mayúsculas.

C) Puzzle 
El programa define una clase llamada `A`, que tiene dos métodos:
- `z(self)`: Retorna el objeto mismo.
- `y(self, t)`: Retorna la longitud del argumento `t`.
Luego, en la función `main()`, se crean dos instancias de la clase `A`, `a` y `aa`. Se asignan los métodos `z` e `y` de estas instancias a variables `y` y `z` respectivamente. Se realizan varias llamadas a estos métodos con diferentes argumentos y se imprimen los resultados.

D) Logger
El programa define dos clases principales:
1. `Logger`: Esta clase gestiona la creación y escritura de registros en un archivo de texto (`log.txt`). Al inicializar un objeto de esta clase, se crea un archivo de registro con un mensaje de inicio (`--Start log--`). El método `log(message)` permite agregar mensajes al archivo de registro, y el método `close()` finaliza el registro con un mensaje que incluye el número total de llamadas al método `log()` y cierra el archivo.
2. `Test`: Esta clase simplemente inicializa un objeto de la clase `Logger` y proporciona un método `llamada(message)` para registrar mensajes con el objeto `Logger`.
La función `main()` crea un objeto de la clase `Test`, realiza varias llamadas de prueba al método `llamada()`, y luego cierra el registro. Posteriormente, lee e imprime el contenido del archivo de registro `log.txt`.
