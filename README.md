# Mongous
A (very) thin wrapper on top of PyMongo CRUD functions on Python 2 that makes some query syntax more Pythonic.

## Example
### BEFORE (with PyMongo)
```python
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts.insert_one(post)
```

### AFTER (with Mongous)
```python
now = datetime.datetime.utcnow()

posts.create(
    author="Mike",
    text="My first blog post!",
    tags=["mongodb", "python", "pymongo"],
    date=now
)
```

## Installation
Download source code and install to your library:
```
$ python setup.py install
```
In some cases you might need to do this:
```
$ sudo python setup.py install
```
*pip support coming soon*
