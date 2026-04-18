#!/usr/bin/env python3
"""update topics in document"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a document based on the name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
