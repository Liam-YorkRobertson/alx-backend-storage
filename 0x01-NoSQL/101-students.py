#!/usr/bin/env python3
"""
function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {
                    "$cond": {
                        "if": {"$isArray": "$topics"},
                        "then": {"$avg": "$topics.score"},
                        "else": 0
                    }
                }
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
