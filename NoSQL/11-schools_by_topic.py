#!/usr/bin/env python3
"""schools_by_topic module"""


def schools_by_topic(mongo_collection, topic):
    """
    returns list with the specifc topic
    """
    documents = list(mongo_collection.find(
        {"topics": topic}
    ))

    return documents
