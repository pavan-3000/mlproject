import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "mlproject"

list_of_files = {
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/.__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__/py", 
    "config/config.yaml",
    "param.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "reequirments.txt",
    "setup.py",
    "research/trails/ipynb",
    "templates/index.html"
}




for filepath in list_of_files:
    filepath = Path(filepath)
    fildir,filename  = os.path.split(filepath)

    if fildir !="":
        os.makedirs(fildir,exist_ok=True)
        logging.info(f"creating dirctory;{fildir} for file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filename)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exits")