# The AirBnB Clone Project
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Project Description
In the initial phase of the AirBnB clone project, our focus was on developing the backend system. We integrated it with a console application using Python's cmd module.

The data, represented as Python objects, is generated and then stored in a JSON file. Utilizing the Python json module, this stored data can be easily accessed.

## Description of the command interpreter:
The application interface resembles the Bash shell, albeit with a restricted set of commands tailored specifically for the functionality of the AirBnB website.
The command-line interpreter functions as the frontend of the web application, enabling users to interact with the backend developed using Python's object-oriented programming principles.ng.

Some of the commands available are:
- show
- create
- update
- destroy
- count

In the integration of the command-line interpreter with the backend and file storage system, the following actions are facilitated:
- Initiating the creation of new objects (e.g., a fresh User or Place)
- Fetching an object from various sources like files or databases
- Executing operations on objects (e.g., counting, computing statistics)
- Modifying attributes of an object
- Removing an object entirely

## How to start it
To get a copy of the project up and running on your local machine (Linux distribution) for development and testing purposes, follow these instructions:

## Installing

To begin, you must clone the project repository from GitHub. It houses the basic shell program along with all necessary dependencies. Once the repository is cloned, you'll find a folder named AirBnB_clone, containing various files essential for the program's functionality.

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application
> 
> models/base_model.py: Class that defines all common attributes/methods for other classes.
> 
> models/user.py: User class that inherits from BaseModel
> 
>models/state.py: State class that inherits from BaseModel
>
>models/city.py: City class that inherits from BaseModel
>
>models/amenity.py: Amenity class that inherits from BaseModel
>
>models/place.py: Place class that inherits from BaseModel
>
>models/review.py: Review class that inherits from BaseModel



## How to use it
It can work in two different modes:


**Interactive** and **Non-interactive**.


During **Interactive mode**, the console presents a prompt (hbnb), signaling that the user can input and execute commands. Following command execution, the prompt reappears, awaiting further commands. This cycle continues indefinitely until the user chooses to exit the program.

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

In **Non-interactive mode**, the shell requires execution alongside a piped command input, causing the command to be immediately executed upon Shell initiation. This mode lacks a prompt and does not anticipate additional input from the user.


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

## Examples
For the other classes like city, place,..etc. We can use the function the same way, all other functions like update, show,..etc. are listed below

![console](https://github.com/mariamabdelgalil/AirBnB_clone/assets/88682947/b5302f30-f27a-4126-a168-cdcd8c663ef9)


## Available commands and their functionality

The commands are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Authors

- **Khaled Mansour** - <[Khaled](https://github.com/KhaledAbdelgalil)>
- **Mariam Abdelgalil** - <[Mariam](https://github.com/mariamabdelgalil)>
