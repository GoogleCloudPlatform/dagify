import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
from .operators import SSHOperator, UnknownOperator, DummyOperator
from .workflows import Workflow
from .folders import Folder 
from .jobs import Job 
from .variable import Variable
from .inCondition import InCondition
from .outCondition import OutCondition
from .shout import Shout
import time


class ControlMParser():

  def __init__(self, 
               xml_path: str, 
               folder_name: str, 
               smart_folder_name: str,
               output_path: str
               ):
    self.xml_path = xml_path
    self.folder_name = folder_name
    self.smart_folder_name = smart_folder_name
    self.output_path = output_path

  def parse(self):

    # Parse XML file
    tree = ET.parse(self.xml_path)
    root = tree.getroot()

    # Create workflow object
    workflow = Workflow(
      filename=self.xml_path
    )
    
    for folderNode in root:
      # Process Folder and Smart Folder objects
      if folderNode.tag in ["FOLDER", "SMART_FOLDER"]:
        
        # Create Folder Object
        folder = Folder(
          datacenter = folderNode.get("DATACENTER"),
          version = folderNode.get("VERSION"),
          platform = folderNode.get("PLATFORM"),
          folder_name = folderNode.get("FOLDER_NAME"),
          modified = folderNode.get("MODIFIED"),
          last_upload = folderNode.get("LAST_UPLOAD"),
          folder_order_method = folderNode.get("FOLDER_ORDER_METHOD"),
          real_folder_id = folderNode.get("REAL_FOLDER_ID"),
          type = folderNode.get("TYPE"),
          used_by_code = folderNode.get("USED_BY_CODE"),
        )
        # Add folder to workflow
        workflow.addFolder(folder)
        # Process Jobs in Folder
        jobCount=0
        for jobNode in folderNode:
          jobCount+=1
          jobAttrCount=0
          jobAttrCountVar=0
          # Create Job Object
          job = Job(
            job_name = jobNode.get("JOBNAME"),
            description = jobNode.get("DESCRIPTION"),
            jobISN = jobNode.get("JOBISN"),
            application = jobNode.get("APPLICATION"),
            sub_application = jobNode.get("SUB_APPLICATION"),
            memname = jobNode.get("MEMNAME"),
            created_by = jobNode.get("CREATED_BY"),
            run_as = jobNode.get("RUN_AS"),
            priority = jobNode.get("PRIORITY"),
            critical = jobNode.get("CRITICAL"),
            tasktype= jobNode.get("TASKTYPE"),
            cyclic= jobNode.get("CYCLIC"),
            node_id = jobNode.get("NODEID"),
            interval = jobNode.get("INTERVAL"),
            cmd_line = jobNode.get("CMDLINE"),
            confirm = jobNode.get("CONFIRM"),
            retro = jobNode.get("RETRO"),
            maxwait = jobNode.get("MAXWAIT"),
            maxrerun = jobNode.get("MAXRERUN"),
            autoarch = jobNode.get("AUTOARCH"),
            maxdays = jobNode.get("MAXDAYS"),
            maxruns = jobNode.get("MAXRUNS"),
            timefrom = jobNode.get("TIMEFROM"),
            weekdays = jobNode.get("WEEKDAYS"),
            jan = jobNode.get("JAN"),
            feb = jobNode.get("FEB"),
            mar = jobNode.get("MAR"),
            apr = jobNode.get("APR"),
            may = jobNode.get("MAY"),
            jun = jobNode.get("JUN"),
            jul = jobNode.get("JUL"),
            aug = jobNode.get("AUG"),
            sep = jobNode.get("SEP"),
            oct = jobNode.get("OCT"),
            nov = jobNode.get("NOV"),
            dec = jobNode.get("DEC"),
            days_and_or = jobNode.get("DAYS_AND_OR"),
            shift = jobNode.get("SHIFT"),
            shiftnum = jobNode.get("SHIFTNUM"),
            sysdb =jobNode.get("SYSDB"),
            jobs_in_group =jobNode.get("JOBS_IN_GROUP"),
            ind_cyclic =jobNode.get("IND_CYCLIC"),
            creation_user = jobNode.get("CREATION_USER"),
            creation_date = jobNode.get("CREATION_DATE"),
            creation_time = jobNode.get("CREATION_TIME"),
            change_userid = jobNode.get("CHANGE_USERID"),
            change_date = jobNode.get("CHANGE_DATE"),
            change_time = jobNode.get("CHANGE_TIME"),
            rule_based_calendar_relationship = jobNode.get("RULE_BASED_CALENDAR_RELATIONSHIP"),
            appl_type = jobNode.get("APPL_TYPE"),
            multy_agent = jobNode.get("MULTY_AGENT"),
            use_instream_jcl = jobNode.get("USE_INSTREAM_JCL"),
            version_opcode = jobNode.get("VERSION_OPCODE"),
            is_current_version = jobNode.get("IS_CURRENT_VERSION"),
            version_serial = jobNode.get("VERSION_SERIAL"),
            version_host = jobNode.get("VERSION_HOST"),
            cyclic_tolerance = jobNode.get("CYCLIC_TOLERANCE"),
            cyclic_type = jobNode.get("CYCLIC_TYPE"),
            parent_folder = jobNode.get("PARENT_FOLDER"),
          )
          
          for jobAttr in jobNode: 
            # Proccess Job Objects
            match jobAttr.tag:
              case "VARIABLE":
                jobAttrCountVar+=1
                # -- Mapping ---
                # Control-M -> Job -> Variable
                job.addVariable(Variable(
                  name = jobAttr.get("NAME"),
                  value = jobAttr.get("VALUE"),
                ))
              case "INCOND":
                # -- Mapping ---
                # Control-M -> Job -> In Condition (INCOND)
                job.addInCondition(InCondition(
                 name = jobAttr.get("NAME"),
                 odate = jobAttr.get("ODATE"),
                 andOr= jobAttr.get("AND_OR"),
                ))
              case "OUTCOND":
                jobAttrCount+=1
                # -- Mapping ---
                # Control-M -> Job -> Out Condition (OUTCOND)
                job.addOutCondition(OutCondition(
                  name = jobAttr.get("NAME"),
                  odate = jobAttr.get("ODATE"),
                  sign = jobAttr.get("SIGN"),
                ))
              case "SHOUT":
                # -- Mapping ---
                # Control-M -> Job -> Shout Condition (SHOUT)
                job.addShout(Shout(
                  when= jobAttr.get("WHEN"), 
                  urgency= jobAttr.get("URGENCY"), 
                  dest= jobAttr.get("DEST"), 
                  message= jobAttr.get("MESSAGE")
                ))
              case _:
                # -- Mapping ---
                # Unmapped Attribute
                print("Job: " + job.getJobName() + " Job Attribute: " + jobAttr.tag + " is not currently supported, Skipping")
         
          print("Job Count: " + str(jobCount))
          print(job)
          print("Job Attribute Out Count: " + str(jobAttrCount))
          print("Job Attribute Out Count: " + str(len(job.getOutConditions())))
          print("Job Attribute Var Count: " + str(jobAttrCountVar))
          print("Job Attribute Var Count: " + str(len(job.getVariables())))
        

          # Create Airflow Operator Object
          op = None
          match job.getJobType():
            case "Command":
              # -- Mapping ---
              # Control-M JobType: Command
              # Airflow Operator: SSHOperator
              op = SSHOperator(
                task_id=job.job_name,
                command=job.cmd_line,
              )
            case "Dummy":
              # -- Mapping ---
              # Control-M JobType: Dummy
              # Airflow Operator: DummyOperator
              op = DummyOperator(
                task_id=job.job_name,
              )
            case _:
              # -- Mapping ---
              # Control-M JobType: ????
              # Airflow Operator: ????
              print("Job Type: " + job.getJobType() + " is not currently supported.")
              op = UnknownOperator()
              #file_handler.write(op.output())
          
          # Validate Operator 
          op.validate()
          # Add Airflow Operator to Job
          job.setOperator(op)
          # Add Job to folder
          folder.addJob(job)
          job = None
          
      else:
        print("WARNING: Unknown node type: " + node.tag + " SKIPPING.")



      
      # Process Dag Output
      for folder in workflow.getFolders():
        
        
        environment = Environment(loader=FileSystemLoader("templates/"))
        template = environment.get_template("dag.tmpl")
      
        filename = "output/{folder_name}.py".format(folder_name=folder.getFolderName())
        content = template.render(
           imports=[],
           tasks=folder.getJobsOperatorAsStringList(),
           dependencies=folder.getJobDependenciesAsStringList()
        )
        with open(filename, mode="w", encoding="utf-8") as dagFile:
            dagFile.write(content)
        
      
      
      


        
  def write_task_dependencies(self, file_handler, folder):
    file_handler.write("# Task dependencies\n")

    jobs = folder.findall("JOB")
    for job in jobs:

      out_conds = job.findall("OUTCOND")
      out_conds_positive = []
      for out_cond in out_conds:
        if out_cond.get("SIGN") == "+":
          out_conds_positive.append(out_cond)
      
      if len(out_conds_positive) > 0:
        file_handler.write(job.get("JOBNAME") + " >> ")
        
        if len(out_conds_positive) == 1:
          next_job = folder.findall("JOB/INCOND[@NAME=\'" + out_cond.get("NAME") + "\']/..")
          file_handler.write(next_job[0].get("JOBNAME"))
          file_handler.write("\n") 
        else:
          file_handler.write("[")

          for i in range(len(out_conds_positive)-1):
            out_cond = out_conds_positive[i]
            next_job = folder.findall("JOB/INCOND[@NAME=\'" + out_cond.get("NAME") + "\']/..")
            file_handler.write(next_job[0].get("JOBNAME") + ", ")

          next_job = folder.findall("JOB/INCOND[@NAME=\'" + out_conds_positive[-1].get("NAME") + "\']/..")
          file_handler.write(next_job[0].get("JOBNAME") + "]")
          file_handler.write("\n")
    
