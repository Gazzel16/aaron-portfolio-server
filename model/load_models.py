# model/model_loader.py
import os
import importlib

def load_models():
    models_dir = os.path.dirname(__file__)
    for file in os.listdir(models_dir):
        if file.endswith(".py") and file != "__init__.py" and file != "model_loader.py":
            importlib.import_module(f"model.{file[:-3]}")