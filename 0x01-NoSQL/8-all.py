#!/usr/bin/env python3
"""mongo db module 8-all.py"""

def list_all(mongo_collection):
    """ lists all documents in a collection"""
    return mongo_collection.find()
