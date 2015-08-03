# rEVOLVEr

A python3 GUI application to manage your gamesdb rules for the Evolve social gaming platform.

## Installation

## Todo

Code Skeleton -> Move xpick files to here
Parsing gamesdb.xml -> read and write (atomically and write only changes)
GUI for displaying, testing and submitting gamedb rules, with easy rule creation
Auto updating with github api -> (delta updating if possible)
Borderless -> Metro UI Default
Customizable UI

pip, wheel, win32 binary without python as a dependancy

## Design

### Folder Structure

/revolver
	/revolver
		/parser
			__init__.py
			eparser.py
			io.py
		/ui
			__init__.py
			ui.py
			autocompleteentry.py
			config.ini
		/evolve-bjects
			__init__.py
			egame.py
		__init__.py # version info
		revolver.py
	README.md
	requirements.txt
    LICENSE.md
    setup.py

## License

revolver stylized as rEVOLVEr is distributed under the terms of the MIT license. See LICENSE.md for details.

R.I.P xfire

