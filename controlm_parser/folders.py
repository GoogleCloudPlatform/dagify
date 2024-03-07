import time

class Folder:
    def __init__(self, datacenter, version, platform, folder_name, modified, last_upload, folder_order_method, real_folder_id, type, used_by_code):
        self.datacenter = datacenter
        self.version = version
        self.platform = platform
        self.folder_name = folder_name
        self.modified = modified
        self.last_upload = last_upload
        self.folder_order_method = folder_order_method
        self.real_folder_id = real_folder_id
        self.type = type
        self.used_by_code = used_by_code
        self.jobs = []
        return
    
    def addJob(self, job):
        self.jobs.append(job)
    
    def getJobs(self):
        return self.jobs
    
    def getJobCount(self):
        return len(self.jobs)
    
    def getFolderName(self):
        return self.folder_name
    
    def getRealFolderId(self):
        return self.real_folder_id
    
    def getJobsOperatorAsStringList(self):
        jobs = []
        for job in self.jobs:
            jobs.append(job.getMetadata())
            jobs.append(job.getOperator().output(task_name=job.getJobNameSafe()))
        return jobs

    def calculateImports(self): 
        imports = []
        imports.append("#System Imports\nimport datetime\n\n# Base Airflow Imports\nimport airflow\nfrom airflow import DAG")
        for job in self.getJobs():
            if job.getOperator().getImports() != "":
                if job.getOperator().getImports() not in imports:
                    
                    imports.append(job.getOperator().getImports())
        return imports

    
    def calculateJobDependencies(self): 
        deps = []
        #Calculate Job Dependencies for every job.
        for job in self.getJobs():
            dep = ""
            out_conds = job.getOutConditions()
            out_conds_positive = []
            
            for out_cond in out_conds:
                if out_cond.getSign() == "+":
                    out_conds_positive.append(out_cond)
            
            if len(out_conds_positive) > 0:
                items = ""
                
                for poutcon in out_conds_positive:                    
                    for job in self.getJobs():
                        for incon in job.getInConditions():
                            if incon.getName() == poutcon.getName():
                                items += job.getJobNameSafe() + ", "
                if items != "":
                    dep = job.getJobNameSafe() + " >> [" + items + "]" 
                    dep = dep.replace(", ]", "]")     
            
            if dep != "":
                deps.append(dep)
        
        return deps
   