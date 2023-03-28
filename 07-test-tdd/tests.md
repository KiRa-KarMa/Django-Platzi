

# TESTS

Los test de nuestro codigo son muy importantes por estas razones:

    - Si tenemos muchas líneas de código, encontrar un error puede ser catastrófico.
    - Nos hace ver más profesionales.
    - Nos permite trabajar mejor en equipo

# TDD (Test-Driven Development)

Es una práctica de programación que consiste en escribir primero las pruebas (generalmente unitarias), despues escribir el codigo fuente
que pase la prueba satisfactoria y por último, refactorizar el codigo escrito.


Pasos a seguir para los tests

    - Identificamos un problema
    - Creamos un test
    - Corremos un test
    - Arreglamos el problema
    - Corremos el test


##################################################################################
Los test de Django crean su propia base de datos replicando los modelos que tiene.
##################################################################################

# Para las comparaciones usaremos:

Método	                                Comparación
-------------------------------------------------------
assertEqual(a, b)	                    a == b
assertNotEqual(a, b)	                a != b
assertTrue(x)	                        bool(x) es True
assertFalse(x)	                        bool(x) es False
assertIs(a, b)	                        a es b
assertIsNot(a, b)                       a no es b
assertIsNone(x)	                        x es None
assertIsNotNone(x)	                    x no es None
assertIn(a, b)	                        a está en b
assertNotIn(a, b)	                    a no está en b
assertIsInstance(a, b)                  isinstance(a, b) es True
assertNotIsInstance(a, b)	            isinstance(a, b) es False
assertContains(a, b)                    a contains b
assertQuerysetEqual([a,b,c], [b])       [b] in [a,b,c]
