#!/usr/bin/python3


class country:
    name: str
    code: str


    def __init__(self, name, code)
        self.name = name
        self.code = code

    def __repr__(self):
        return f"[country] {self.name}, {self.code}"
