import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads the yaml file and returns a ConfigBox"""
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    """creates a directory
    Args:
    path_to_directory (list): path to the directory
    ignore_log(bool, optional): ignore if muultiple dirs is to be created"""

    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")

@ensure_annotations
def get_size(path:Path) -> str:
    """gets size in KB
    Args:
    path (Path): path to the file
    
    Returns:
    str: size in KB"""
    size = round(os.path.getsize(path)/1024)
    return f"~ {size} KB"