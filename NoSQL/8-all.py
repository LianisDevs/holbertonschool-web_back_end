#!/usr/bin/env python3
"""list_all module"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    documents = list(mongo_collection.find())

    return documents
