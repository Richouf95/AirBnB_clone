# AirBnB_clone

The goal of the project is to deploy on your server a simple copy of the <a href="https://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw" target="_blank">AirBnB website</a>

The goal is to build a web application composed by:
* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A website (the front-end) that shows the final product to everybody: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The console
create your data model
manage (create, update, destroy, etc) objects via a console / command interpreter
store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

### Tasks

0. README, AUTHORS
1. Be pycodestyle compliant!
2. Unittests
3. BaseModel
4. Create BaseModel from dictionary
5. Store first object
6. Console 0.0.1
7. Console 0.1
8. First User
9. More classes!
10. Console 1.0
11. All instances by class name
12. Count instances
13. Show
14. Destroy
15. Update
16. Update from dictionary
17. Unittests for the Console!

