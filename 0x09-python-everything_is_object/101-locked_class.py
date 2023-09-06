#!/usr/bin/python3
"""
locked class that prevents the user from dynamically
creating new instance attributes
"""


class LockedClass:
    """allow only first_name attribute as new instance"""
    __slots__ = ('first_name')
    pass
