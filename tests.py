from mongous import SimpleMongoCRUDHandler


def test_simple_handler():
    handler = SimpleMongoCRUDHandler("mytestdb", "tests")
    handler.delete() # in case some test data is still there from a failed test

    the_intro = "Call me Ishmael."

    result = handler.create(title="Moby Dick", intro=the_intro)
    assert result is not None
    doc = handler.read(title="Moby Dick")
    assert doc is not None
    assert doc["intro"] == the_intro

    the_intro = "Rumors about my death have been greatly exaggerated."

    result = handler.update(doc, intro=the_intro)
    assert result is not None
    doc = handler.read(title="Moby Dick")
    assert doc is not None
    assert doc["intro"] == the_intro

    result = handler.delete(title="Moby Dick")
    assert result is not None
    doc = handler.read(title="Moby Dick")
    assert doc is None

    docs = [
        {
        "type": "book",
        "title": "Moby Dick"
        },
        {
        "type": "book",
        "title": "Crime and Punishment"
        },
        {
        "type": "book",
        "title": "B'rit Chadashah",
        "special": 1
        }
    ]

    result = handler.create_many(docs)
    assert result is not None

    reading_list = handler.read_many(type="book")
    assert reading_list is not None
    assert len([book for book in reading_list]) == len(docs)

    handler.delete()
