
### Instalar PGN-Parser localmente

* Clonar repo
  `git clone https://github.com/GregorioF2/PGN-Parser.git`
* Entrar en la carpeta
  `cd PGN-Parser`  
* Crear ambiente virtual para python Python 3.6
  ```
  virtualenv --python=/usr/bin/python3.6 venv
  . venv/bin/activate
  ```
* Instalar requerimientos
  ```
  pip install -r requirements.txt
  ```

### Correr parser
  El archivo `testing.py` es el principal para correr y testear el modulo.
  Tiene multiples flags para testear diferentes cosas. Estos serían:
  * `-h`, `--help`          Muestra opciones de ayuda para correr el parser
  * `-ls`, `--live_stream`  Si qres testear el parser con live stream input
  * `-t1`, `--test_1`       Correr parser para full game común Hikaru Magnus
  * `-t2`, `--test_2`       Correr parser para test chico con comentarios anidados
  * `-t3`, `--test_3`       Correr parser para multiples partidas
  * `-t4`, `--test_4`       Correr parser para partida de analsis con varios comentarios de chess.com
  * `-t5`, `--test_5`       Correr parser para historial de partidas chess.com
  * `-t6`, `--test_6`       Brackets de metadata desbalanceados
  * `-a`, `--all`           Correr todos los test juntos
  
### Ejemplo:
`python testing.py -t1`

### Usar custom input
  En caso de que se quiera con probar con input custom, y no quieran lidiar con escribirlo en el modo de `live stream`. Se puede ejecutar el parser de la siguiente forma
  ```
    [] [] 1.d4 [] 1.d5 [] 1.d5 | python testing.py -ls
  ```
