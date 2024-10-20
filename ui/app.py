from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess
import os
import shutil
import zipfile
import uuid  
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main():
    return templates.TemplateResponse("index.html", {"request": {}, "download_link": None})

@app.post("/", response_class=HTMLResponse)
async def process_file(source_file: UploadFile = File(...), dag_divider: str = Form(...)):
    download_link = None
    report_data = {}

    if source_file.filename :
        with open(source_file.filename, "wb") as buffer:
            buffer.write(await source_file.read())

        source_path = source_file.filename
        output_path = "output-path"

        # Clear the output directory
        if os.path.exists(output_path):
            shutil.rmtree(output_path)  # This removes the directory and its contents
        os.makedirs(output_path)  # Recreate an empty directory
        current_dir = os.getcwd()
        
        # Run the subprocess from parent directory where DAGify.py is located
        os.chdir('..')

        # source_path is at current directory, this must be specified when running the subprocess
        source_path = os.path.join(current_dir, source_file.filename)
        subprocess.run(["python3", "DAGify.py", "--source-path", source_path,"--dag-divider",dag_divider,"--output-path",output_path,  "-r"])

        if os.listdir(output_path):
            # Generate a unique ID
            unique_id = uuid.uuid4() 
            source_xml_name = source_path.split("/")[-1].split(".")[0]

            # Create a ZIP archive with the unique ID in the filename
            zip_filename = f"dagify_{source_xml_name}_{unique_id}.zip"
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(output_path):
                    for file in files:
                        if file.endswith(".json"):
                            file_path = os.path.join(root, file)
                            with open(file_path, 'r') as f:
                                report_data = json.load(f)

                        zipf.write(os.path.join(root, file), 
                                   os.path.relpath(os.path.join(root, file), output_path))

            download_link = f"/download/{zip_filename}"
        
        # Change directory to current directory after subprocess completes
        os.chdir(current_dir)
        os.remove(source_file.filename)

    return templates.TemplateResponse("index.html", {"request": {}, "download_link": download_link,"report_data": report_data})


@app.get("/download/{filename}")
async def download_file(filename: str):
    # File Path is updated as output is downloaded in parent directory, 
    # where DAGify.py is located. 
    file_path = os.path.join(os.pardir, filename)
    return FileResponse(file_path, media_type='application/zip', filename=filename)