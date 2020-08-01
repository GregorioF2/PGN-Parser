
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
  El `testing.py` es el archivo principal para correr y testear el modulo.
  Los comandos serían:
  * `-ls`, `--live_stream`  Si qres testear el parser con live stream input
  * `-t1`, `--test_1`       Correr parser para full game común Hikaru Magnus
  * `-t2`, `--test_2`       Correr parser para test chico con comentarios anidados
  * `-t3`, `--test_3`       Correr parser para multiples partidas
  * `-a`, `--all`           Correr todos los test juntos
