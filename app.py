from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
import os
import shutil
import zipfile

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main():
    return templates.TemplateResponse("index.html", {"request": {}, "download_link": None})

@app.post("/", response_class=HTMLResponse)
async def process_file(source_file: UploadFile = File(...)):
    download_link = None
    error_message = None

    # if source_file.filename == "":
        # error_message = "Please upload a file"
    if source_file.filename :
        with open(source_file.filename, "wb") as buffer:
            buffer.write(await source_file.read())

        source_path = source_file.filename
        subprocess.run(["python3", "DAGify.py", "--source-path", source_path])

        output_path = "output"
        if os.listdir(output_path):
            # Create a ZIP archive of the output folder
            zip_filename = "dagify_output.zip"
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(output_path):
                    for file in files:
                        zipf.write(os.path.join(root, file), 
                                   os.path.relpath(os.path.join(root, file), output_path))

            download_link = f"/download/{zip_filename}"

        os.remove(source_file.filename)

    return templates.TemplateResponse("index.html", {"request": {}, "download_link": download_link, "error_message": error_message})


@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = filename 
    return FileResponse(file_path, media_type='application/zip', filename=filename)
