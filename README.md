# flask-db-api
API, which is able to add records to the database, get records by title, get all records, update and delete it.

## Table of Contents
 - [How to run the API](#how-to-run-the-api)
 - [Before the beginning](#before-the-beginning)
 - [What fields does the record have](#what-fields-does-the-record-have)
 - [Get record](#get-record)
 - [Create record](#create-record)
 - [Update record](#update-record)
 - [Delete record](#delete-record)

## How to run the API
To run the API run file manage.py through your IDE or using the follow command in the console in your virtual environment.
```python
python manage.py
```

## Before the beginning
For GET, DELETE requests, only refer to a specific url.
For POST, PUT requests both refer to the specific url and be sure to send the json-object.

You always get a json-object in response. And every time it is full information about the record in the database, i.e. all its fields. Even you update or delete record. This is to ensure that you always see the changes after any request. 
Therefore, when you delete a record from the database, you get it in the json object.
 
All examples here are written using the standard values of Flask: host=127.0.01 and port=5000.

## What fields does the record have

Record contains the following fields:

| field | description |
| ----- | :----- |
| unique_id | Integer, Primary key |
| title | String, Required, No empty string* |
| description | String, default=`` |
| done  |  Boolean, default=False |
*Cannot contain an empty string, a string consisting only of spaces.

## Get record
To **get all** records from the database.
```
[GET request] host:port/api/v1.0/tasks/getAll
```
:pencil2: E.g. http://127.0.0.1:5000/api/v1.0/tasks/getAll 


To **get one** first record, you need to use its title and the following request.  
```
[GET] host:port/api/v1.0/tasks/get?title=your record title
```
:exclamation: Note, that you need to write the title with spaces, uppercase, and punctuation.  
:pencil2: E.g. http://127.0.0.1:5000/api/v1.0/tasks/get?title=New Year 2019

If you have two or more records with the same title, the first record with the smallest unique_id in the database will be returned.

To **get all records by title**
```
[GET] host:port/api/v1.0/tasks/getAll?title=your record title
```
:pencil2: E.g. http://127.0.0.1:5000/api/v1.0/tasks/getAll?title=Hello

---
#### :dart: Result of GET requests.
You'll see something like this.
```json
{
    "tasks": [
        {
            "description": "world!",
            "done": false,
            "title": "hello",
            "unique_id": 4
        },
        {
            "description": "Be happy",
            "done": false,
            "title": "Hello world!",
            "unique_id": 6
        }
    ]
}
```


## Create record
To create the record in the database you need use POST request and send a json-object, which must contain required the title field and optional description field.
```
[POST] host:port/api/v1.0/tasks/create
```
```json
{
	"title": "required record title",
	"description": "optional!"
}
```
:exclamation: Note, that you can create a task without description, but title should be necessarily.

---
:pencil2: E.g. [POST] http://127.0.0.1:5000/api/v1.0/tasks/create  
*Send json*
```json
{
	"title": "Hello world!",
	"description": "Be happy"
}
```
:dart: Result
```json
{
    "task": {
        "description": "Be happy",
        "done": false,
        "title": "Hello world!",
        "unique_id": 6
    }
}
```

## Update record
To update the record, use the PUT request and the following URL. 
```
[PUT] host:port/api/v1.0/tasks/update?title=your record title
```
You also need to send a json-object with the field you want to change. It can be *title*, *description*, *done* and any of their variations.
```json
{
	"title": "new title",
	"description": "new description",
	"done": true
}
```

---
:pencil2: E.g. we have the following record.
```json
{
	"description": "world",
	"done": false,
	"title": "hello",
	"unique_id": 5
}
```
And we want to update the title and description in it.

[PUT] http://127.0.0.1:5000/api/v1.0/tasks/update?title=hello  
*Send json*
```json
{
	"title": "Hello",
	"description": "world!!!"
}
```
:exclamation: Note that in the url we refer to the old title, and in the json-object we send the new title. And we can not send a new title.

:dart: Result
```json
{
    "task": {
        "description": "world!!!",
        "done": false,
        "title": "Hello",
        "unique_id": 5
    }
}
```
Great!

## Delete record
To delete a record, send a DELETE request to the following URL.
```
[DELETE] host:port/api/v1.0/tasks/delete?title=your record title
```

---
:pencil2: E.g. we want to delete the record with title "hello".  
[DELETE] http://127.0.0.1:5000/api/v1.0/tasks/delete?title=hello

:dart: Result
```json
{
    "deleted task": {
        "description": "world!",
        "done": false,
        "title": "hello",
        "unique_id": 4
    },
    "result": "Success"
}
```
As you can see, we got the full record in the json object, but it no exists in the database already. And if you want to get a record from the database with title "hello", you will get an error.

## Links
All questions and suggestions: IamEgorNovik@gmail.com
