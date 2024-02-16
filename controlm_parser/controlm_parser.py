import xml.etree.ElementTree as ET

class ControlMParser():

  def __init__(self, 
               xml_path: str, 
               folder_name: str, 
               smart_folder_name: str,
               output_path: str):
    self.xml_path = xml_path
    self.folder_name = folder_name
    self.smart_folder_name = smart_folder_name
    self.output_path = output_path

  def parse(self):

    tree = ET.parse(self.xml_path)
    root = tree.getroot()

    if self.folder_name:
      folder = root.find("FOLDER[@FOLDER_NAME=\'" + self.folder_name + "\']")
    else:
      folder = root.find("SMART_FOLDER[@FOLDER_NAME=\'" + self.smart_folder_name + "\']")

    f = open(self.output_path, "a")

    f.write("# Task definitions\n")
    jobs = folder.findall("JOB")
    for job in jobs:
      f.write(job.get("JOBNAME") + "= CustomSSHOperator(task_id=\'" + job.get("JOBNAME") + "\', dag=dag)\n")

    f.write("\n")
    f.write("# Task dependencies\n")

    for job in jobs:

      out_conds = job.findall("OUTCOND")
      out_conds_positive = []
      for out_cond in out_conds:
        if out_cond.get("SIGN") == "+":
          out_conds_positive.append(out_cond)
      
      if len(out_conds_positive) > 0:
        f.write(job.get("JOBNAME") + " >> ")
        
        if len(out_conds_positive) == 1:
          next_job = folder.findall("JOB/INCOND[@NAME=\'" + out_cond.get("NAME") + "\']/..")
          f.write(next_job[0].get("JOBNAME"))
          f.write("\n")
        else:
          f.write("[")

          for i in range(len(out_conds_positive)-1):
            out_cond = out_conds_positive[i]
            next_job = folder.findall("JOB/INCOND[@NAME=\'" + out_cond.get("NAME") + "\']/..")
            f.write(next_job[0].get("JOBNAME") + ", ")

          next_job = folder.findall("JOB/INCOND[@NAME=\'" + out_conds_positive[-1].get("NAME") + "\']/..")
          f.write(next_job[0].get("JOBNAME") + "]")
          f.write("\n")

    f.close()

  def print(self):
    print("Hello...")
