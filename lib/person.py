#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def greet(self):
        return "hello"
import ipdb; ipdb.set_trace()