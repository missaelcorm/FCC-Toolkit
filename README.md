# FCC-Toolkit
## Installation steps

### 1.- Clone the repository

`Linux:`
```shell
git clone https://github.com/missaelcorm/FCC-Toolkit.git
```

`Windows:`
```Shell
git clone https://github.com/missaelcorm/FCC-Toolkit.git
```

### 2.- Install requierements.txt

`Linux:`
```shell
python3 -m pip install -r requirements.txt
```

`Windows:`
```shell
python -m pip install -r requirements.txt
```

## Usages
### General
Help Menu

`Linux:`
```shell
python3 main.py -h
```

`Windows:`
```shell
python main.py -h
```

`Output`:
```shell
Uso: python main.py [Modulo] [Opciones]>
TABLAS DE VERDAD:
    Use unicamente estas variables: [p, q, r, s, t, u, w, x, y, z]
    -t <"expresion">: tablas de verdad
        ^: Conjuncion
        v: Disyuncion
        ~: Negacion
        >: Implicacion
        -: Doble Implicacion
    Nota: Es necesario escribir la expresion entre comillas ("")
    Ejemplo: python main.py -t "p^qvr"
CONJUNTOS:
    Declara un conjunto -A, -B o -C, y a su derecha los valores
    -s: Operaciones de Conjuntos
    -A <VALORES>: Declara un conjunto A y sus valores separados por comas
    -B <VALORES>: Declara un conjunto B y sus valores separados por comas
    -C <VALORES>: Declara un conjunto C y sus valores separados por comas
    Ejemplo: python main.py -s -A 1,2,3 -C 2,3,4 -B 3,4,5
SUCESIONES:
    Ingresa una sucesion usando "k" como variable.
    -k: Sucesiones
    --expression <"expression">: La expresion a calcular, usando "k" como variable.
        +: Suma
        -: Resta
        /: Division
        *: Multiplicacion
        ^: Potencia
    --limInf <numero>: Limite Inferior
    --limSup <numero>: Limite Superior
    Opcionales:
    --decimals <numero de decimales>: Ingresa el numero de decimales deseado (2 por default).
    Ejemplo: python main.py -k --expression "1/k^2" --limInf 10 --limSup 30 --decimals 6
RELACIONES Y FUNCIONES:
    Ingresa un conjunto de pares ordenados.
    -rf <CONJUNTO>: Ingresa el conjunto con sus pares ordenados.
    Ejemplo: python main.py -rf {(1,2),(3,4),(5,6)}
```

## Examples

### Truth Tables

`Linux:`
```shell
python main.py "p^q"
```
`Output:`
```
+---+---+-----+
| p | q | p^q |
+---+---+-----+
| T | T |  T  |
| T | F |  F  |
| F | T |  F  |
| F | F |  F  |
+---+---+-----+
```

### Sets

`Linux:` 
```shell
python main.py -s -A 1,2,3 -C 2,3,4 -B 3,4,5
```
`Output:`
```
A ∪ C ∪ B: {'4', '1', '2', '5', '3'}
A ∩ C ∩ B: {'3'}
A - C - B: {'1'}
A △ C △ B: {'1', '5', '3'}
```

### Successions

`Linux:`
```shell
python main.py -k --expression "1/k^2" --limInf 1 --limSup 10 --decimals 6
```
`Output:`
```
+--------+---------+--------------+
| 1/k^2  |  k(n-C) |       Result |
+--------+---------+--------------+
| 1/10^2 | k(10-0) |     0.010000 |
| 1/9^2  | k(10-1) |     0.012346 |
| 1/8^2  | k(10-2) |     0.015625 |
| 1/7^2  | k(10-3) |     0.020408 |
| 1/6^2  | k(10-4) |     0.027778 |
| 1/5^2  | k(10-5) |     0.040000 |
| 1/4^2  | k(10-6) |     0.062500 |
| 1/3^2  | k(10-7) |     0.111111 |
| 1/2^2  | k(10-8) |     0.250000 |
| 1/1^2  | k(10-9) |     1.000000 |
|  ---   |   ---   |          --- |
|        |  SUMA:  |     1.549768 |
|        |  MULT:  | 7.594058e-14 |
+--------+---------+--------------+
```

### Relations and Functions

`Linux:`
```shell
python main.py -rf {(1,2),(3,4),(5,6)}
```
`Output:`
```
Reflectividad: False
Simetría: False
Transitividad: True
Dominio X = {1, 3, 5}
Dominio Y = {2, 4, 6}
Funcion: True
```