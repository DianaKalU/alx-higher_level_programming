#!/usr/bin/python3

import os
import importlib.util

def import_from_pyc(pyc_path):
    if not os.path.exists(pyc_path):
        raise FileNotFoundError(f"No file found at {pyc_path}")

    spec = importlib.util.spec_from_file_location("hidden_4", pyc_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def print_module_names(module):
    names = [name for name in dir(module) if not name.startswith("__")]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    pyc_path = "C:\Users\SPECTRE\Downloads\hidden_4.pyc"
    try:
        hidden_4 = import_from_pyc(pyc_path)
        print_module_names(hidden_4)
    except Exception as e:
        print(f"Error: {e}")
