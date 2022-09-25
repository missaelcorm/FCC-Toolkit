# FCC-Toolkit
## Installation steps

### 1.- Clone the repository

Linux:
```shell
git clone https://github.com/missaelcorm/FCC-Toolkit.git
```

Windows:
```Shell
git clone https://github.com/missaelcorm/FCC-Toolkit.git
```

### 2.- Install requierements.txt

Linux:
```shell
python3 -m pip install -r requirements.txt
```

Windows:
```shell
python -m pip install -r requirements.txt
```

## Usage

Linux:
```shell
python3 main.py "[Expression]"
```

Windows:
```shell
python main.py "[Expression]"
```

## Example

Linux:
```shell
python main.py "p^q"
```
Output:
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