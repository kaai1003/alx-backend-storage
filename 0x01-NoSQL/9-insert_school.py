#!/usr/bin/env python3
"""mongodb insert with python"""

def insert_school(mongo_collection, **kwargs):
    """insert new document in a collection"""
    new = mongo_collection.insert_one(kwargs)
    return new.inserted_id
