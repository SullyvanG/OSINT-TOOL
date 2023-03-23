import sys, os, time, random
from core.Profiler import *
from colorama import Fore
import settings
from datetime import date
from txt.text import text
from txt.header import lb_header


def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Veuillez lancer la version 3 de python.")

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def menu():
	pr = Profiler()
	pr.loadDatabase(settings.pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """                                                                
                                                                                                   
`8.`888b           ,8' .8.          8 8888                  .8.           ,o888888o.              
 `8.`888b         ,8' .888.         8 8888                 .888.         8888     `88.            
  `8.`888b       ,8' :88888.        8 8888                :88888.     ,8 8888       `8.           
   `8.`888b     ,8' . `88888.       8 8888               . `88888.    88 8888                     
    `8.`888b   ,8' .8. `88888.      8 8888              .8. `88888.   88 8888                     
     `8.`888b ,8' .8`8. `88888.     8 8888             .8`8. `88888.  88 8888                     
      `8.`888b8' .8' `8. `88888.    8 8888            .8' `8. `88888. 88 8888   8888888           
       `8.`888' .8'   `8. `88888.   8 8888           .8'   `8. `88888.`8 8888       .8'           
        `8.`8' .888888888. `88888.  8 8888          .888888888. `88888.  8888     ,88'            
         `8.` .8'       `8. `88888. 8 888888888888 .8'       `8. `88888.  `8888888P'              


                                                                                                                               
	""" 

	print(lb_header())
	print(menu)
