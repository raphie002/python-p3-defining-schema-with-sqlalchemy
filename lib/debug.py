#!/usr/bin/env python3
# lib/debug.py
from sqlalchemy import create_engine # type: ignore

from sqlalchemy_sandbox import Student

engine = create_engine('sqlite:///students.db')

if __name__ == '__main__':
    import ipdb; ipdb.set_trace() # type: ignore
