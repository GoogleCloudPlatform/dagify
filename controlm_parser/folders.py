import time

class Folder: 
    jobs = []

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
    
    def getJobCount(self):
        return len(self.jobs)
    
    def getFolderName(self):
        return self.folder_name
    
    def getRealFolderId(self):
        return self.real_folder_id
    
    def getJobsOperatorAsStringList(self):
        jobs = []
        for job in self.jobs:
            jobs.append(job.getJobNameSafe() + " = " + job.getOperator().output())
        return jobs

    def getJobDependenciesAsStringList(self):
        print(len(self.jobs))
        
        for job in self.jobs:
            
            print(str(len(job.getOutConditions())))
            
            out_conds_positive = []
            for out_cond in job.getOutConditions():
                if out_cond.getSign() == "+": 
                    out_conds_positive.append(out_cond)
        
            #print(out_conds_positive)
            #print("\n")
            time.sleep(10)
                
           
        
        
        
        
        deps = []
        for job in self.jobs:
            dep = job.getJobDependencies()
            
            if dep != "":
                deps.append(dep)
                print(dep)      
                time.sleep(10)      
                    
        #print(deps)
        #print("\n")
        return deps

            

   