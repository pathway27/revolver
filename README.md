# rEVOLVEr

[![Build Status](https://travis-ci.org/pathway27/revolver.svg?branch=master)](https://travis-ci.org/pathway27/revolver)
[![Coverage Status](https://coveralls.io/repos/pathway27/revolver/badge.svg?branch=master&service=github)](https://coveralls.io/github/pathway27/revolver?branch=master)

A python3 GUI application to manage your gamesdb rules for the Evolve social gaming platform. Made for learning python and GUI programming.

## Installation

1. Windows Binary
2. pip
3. Clone this repo and run

## Development

Requirements if dev/testing

```
pip install -r test-requirements.txt
```

Virtual Env : TODO: virtualenvwrapper for multiple py/os
Include instructions for ttk include and fix
Run

## Todo

1. Code Skeleton -> Move xpick here
2. Parsing gamesdb.xml -> read and write (atomically and write only changes)
3. Design of GUI
4. GUI for displaying, testing and submitting gamedb rules, with easy rule creation
8. Unit Tests
9. Optimization - Python, Cython then C (:speak_no_evil:)
10. pip, wheel, win32 binary without python as a dependancy
5. Auto updating with github api -> (delta updating if possible)
6. Borderless -> Metro UI Default
7. Customizable UI

11. Check evolve's terms and policies for this app
12. Control evolve's console (for reloading/resyncing rules)

## Testing

```bash
coverage run -m unittest
coverage report -m #or
coverage html
```

## License

rEVOLVEr is distributed under the terms of the MIT license. See [LICENSE.md](https://github.com/pathway27/revolver/blob/master/LICENSE.md) for details.

<small> :fist: R.I.P xfire :fist: </small>
