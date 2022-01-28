## Project Structure
```
libs
  |_  __init__.py    (Python specific requirement for package recognition)
  |_  exceptions.py  (Custom exceptions for the program)
  |_  models.py      (Contains dataclasses which model and validate the the data comping from the YAML Parser)
  |_  parser.py      (Contains functions that take parsed data from pyYAML and return dataclasses defined by models.py)
facility.yaml   (YAML file required for parsing)
main.ipynb      (A notebook alternative for program execution)
main.py         (Script execution that provides an infinite runtime loop and prints objects based on user input)
```

## Info

The program runs in a loop and queries for input, then shows tables for the corresponding data queried

Inputs can be
`Pods`, `Gates`, `Airlocks`, `Astronauts`

## Package requirements

### Yaml parsing library

`pip install pyyaml`

### For Table Output

`pip install rich`

## Usage
Double click `main.py`

or

Open a terminal in the program folder and run

`python main.py`

# Todo
## Parsing Documents into objects
  - [X] Pods
  - [X] Gates
  - [X] Airlocks
  - [X] Astronauts

## Validation
  - [X] Accomplished Via dataclasses, more can be added as client demand

## Printing All Values
  - [X] Done, with rich_tables
  
