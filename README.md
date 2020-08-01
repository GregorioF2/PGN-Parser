
### Install PGN-Parser locally

* Clone this repo
  `git clone https://github.com/GregorioF2/PGN-Parser.git
* Enter repo
  `cd PGN-Parser`  
* Create a Python 3.6 virtual environment  
  ```
  virtualenv --python=/usr/bin/python3.6 venv
  . venv/bin/activate
  ```
* Install Python requirements
  ```
  pip install -r requirements.txt
  ```

### Run parser
  El `testing.py` es el archivo principal para correr y testear el modulo.
  Los comandos serían:
  * `-ls`, `--live_stream`  Si qres testear el parser con live stream input
  * `-t1`, `--test_1`       Correr parser para full game común Hikaru Magnus
  * `-t2`, `--test_2`       Correr parser para test chico con comentarios anidados
  * `-t3`, `--test_3`       Correr parser para multiples partidas
  * `-a`, `--all`           Correr todos los test juntos
