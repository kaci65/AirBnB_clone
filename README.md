## **AirBnB Clone Project**

## **Command Interpreter**
This is the first step towards building a full web application: the AirBnB clone. The code written in this project will be used for all the other subsequent projects: HTML/CSS templating, database storage, API, front-end integration…

## **How it works**
The console or the command interpreter is similar to the Bash shell. The command interpreter will be able to:
```
- Create a new object e.g: a new User or a new Place
- Retrieve an object from a file, database
- Do operations on objects e.g: count, compute stats
- Update attributes of an object
- Destroy an object
```

## **Console Commands**
The commands that can be used with this command interpreter include:
```
help
quit
EOF - ctrl_D
```

## **Execution**
The interpreter in interactive mode:

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

The interpreter in non-interactive mode:

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
