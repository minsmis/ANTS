import os.path
import shutil
from typing import List

import _api_app as api
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


@api.app.post('/load/')
async def load(files: UploadFile):
    temp_dir = os.path.join(os.getcwd(), 'temp')  # path temp
    os.makedirs(temp_dir, exist_ok=True)  # make temp directory

    with open(os.path.join(temp_dir, files.filename), 'wb') as f:  # temporary save contents
        f.write(await files.read())

    loaded_data = api.ants.Ants.load(os.path.join(temp_dir, files.filename))  # load selected data

    shutil.rmtree(temp_dir)  # delete directory and files
    return {"batch size": len(loaded_data)}
