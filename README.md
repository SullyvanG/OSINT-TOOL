Corompus
=

Corompus est un outil de collectes d'informations (OSINT) qui vise à effectuer des recherches sur une personne française, suisse, luxembourgeoise ou belge. Il fournit divers modules qui permettent des recherches efficaces. Corompus ne requiert pas de clé API ni d'identifiant de connexion.


Disclaimer
=
Corompus a été développé pour faire des recherches sur soi-même et pour voir les informations privées et sensibles que l'on peut laisser derrière sur les réseaux sociaux. Je n'encourage en aucun cas l'utilisation de cet outil sur une autre personne que soi-même ou d'utiliser cet outil à mauvais escient.


Installation Linux
=
    sudo apt install git python3
    git clone https://github.com/SullyvanG/OSINT-TOOL
    cd Corompus
    python3 -m pip install -r requirements.txt
    
Execution Linux
=
- Allez dans le dossier Corompus avec la commande `cd`. Ex: 
```
cd Corompus
```
Et executer:
```
python3 Corompus.py
```

Installation Windows
=
- 1. Telecharger [Corompus](https://github.com/Famalo/Corompus)
- 2. Telecharger [python 3](https://www.python.org/downloads/release/python-380/) 
- 3. Installer Python 3 avec l'option "Add to path" et cliquer sur "Install Now" like:
![](https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png)
- 4. Dezipper Corompus (master.zip)
- 5. Ouvrer le CMD, allez dans le dossier ou vous avez extrait **Corompus-master**  avec la commande ```cd```.
     Ex: 
```
cd Desktop\
``` 
Et executer:
```
    cd Corompus-master
    python -m pip install -r requirements.txt
```

Execution Windows:
=
- Allez dans le dossier Corompus avec la commande `cd`. Ex: `cd Desktop\Corompus-master\`. 
Et executer:
```
python Corompus.py
```


Compatible
=
- Windows
- MacOS
- Linux

Python version:
=
- Python3

Python Modules
=
- requests
- bs4
- terminaltables
- colorama

