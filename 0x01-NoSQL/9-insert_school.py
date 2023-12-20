#!/usr/bin/env python3
"""
function that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in a collection based on kwargs
    """
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id