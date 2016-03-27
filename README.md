# Mongous
[![Build Status](https://travis-ci.org/nonproftechie/mongous.svg?branch=master)](https://travis-ci.org/nonproftechie/mongous) [![Coverage Status](https://coveralls.io/repos/github/nonproftechie/mongous/badge.svg?branch=master)](https://coveralls.io/github/nonproftechie/mongous?branch=master) [![PyPI version](https://badge.fury.io/py/mongous.svg)](https://badge.fury.io/py/mongous)  ![Downloads per month](http://img.shields.io/pypi/dm/mongous.svg)

A (very) thin wrapper on top of PyMongo CRUD functions in order to use some different query syntax.  Another possible use is that the `SimpleCRUDHandler` class could be used as a base class for database models.  Tested to work on Python 2.6, 2.7, 3.3, 3.4, 3.5, pypy, and pypy3.

## Example
### BEFORE (with PyMongo)
```python
from pymongo import MongoClient as Client

posts = Client().blog.posts
results = posts.find_one({"title": "Moby Dick"})
```

### AFTER (with Mongous)
```python
from mongous import SimpleMongoCRUDHandler as Handler

posts = Handler("blog", "posts")
results = posts.read(title="Moby Dick")
```

## Installation
```
$ pip install mongous
```
Alternatively, you can download the source code and install to your library:
```
$ python setup.py install
```
In some cases you might need to do this:
```
$ sudo python setup.py install
```

## API
#### class `SimpleCRUDHandler`
##### `__init__(self, database_name, collection_name, connection=None)`
Constructor, sets database to `database_name`, collection to `collection_name`, and optionally uses the connection string `connection` if supplied.
##### `create(self, **kwargs)`
returns the return value of `PyMongo.MongoClient.insert_one` with `kwargs` passed as a `dict`
##### `create_many(self, documents)`
returns the return value of `PyMongo.MongoClient.insert_many` with `documents` passed
##### `read(self, **kwargs)`
returns the return value of `PyMongo.MongoClient.find_one` with `kwargs` passed as a `dict`
##### `read_many(self, **kwargs)`
returns the return value of `PyMongo.MongoClient.read_many` with `kwargs` passed as a `dict`
##### `update(self, doc, **kwargs)`
returns the return value of `PyMongo.MongoClient.update_many` with `doc` and `kwargs` passed as `dict`s (the second argument being a blend of both `doc` and `kwargs` minus `_id` so you don't have to add everything manually to an `update` query)
##### `delete(self, **kwargs)`
returns the return value of `PyMongo.MongoClient.delete_many` with `kwargs` passed as a `dict`
