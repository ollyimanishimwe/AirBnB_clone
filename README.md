![](https://camo.githubusercontent.com/9ebbf60e208b031d4dcf7db6ffc19fe0339d0ff3/68747470733a2f2f692e6962622e636f2f64354e38354e682f68626e622e706e67)

<h1 align="center">AirBnB clone </h1>
<p align="center"></p>


### The command interpreter

With command interpreter you can:

- Destroy an object
- Update attributes of an object
- Retrieve an object from a file, a database etc
- Create a new object (ex: a new User or a new Place)
- Do operations on objects (count, compute stats, etc)



#### Installation
```
git clone https://github.com/ollyimanishimwe/AirBnB_clone
cd AirBnB_clone
```
#### Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Usage
The following are the commands' usage and their OutPuts.

### Command => Snytax => Usage:

Command | Syntax | Output
------- | ------ | ------
create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id
count | `count [class_name]` or `[class_name].count()`| Counts all the instances with class name specified
help | `help [option]` | Displays all available commands
quit | `quit` | Exit command interpreter
EOF | `EOF` | Exit command interpreter



### Environment
* OS: MacOs Catalina
* Language: Python3
* Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html)

### Authors
* Olly | [GitHub](https://github.com/ollyimanishimwe) | [Twitter](https://twitter.com/ollyImanishimwe)
* Chris | [GitHub](https://github.com/crispy-rw/) | [Twitter](https://twitter.com/rw_crispy)
