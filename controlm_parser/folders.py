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

    def add_job(self, job):
        self.jobs.append(job)

    def get_jobs(self):
        return self.jobs

    def get_job_count(self):
        return len(self.jobs)

    def get_folder_name(self):
        return self.folder_name

    def get_folder_name_safe(self):
        safe_name = self.get_folder_name()
        safe_name = safe_name.replace("-", "_")
        safe_name = safe_name.replace(":", "")
        safe_name = safe_name.replace(".", "")
        safe_name = safe_name.replace(",", "")
        safe_name = safe_name.replace("#", "_")
        safe_name = safe_name.replace(" ", "_")
        safe_name = "JOB_" + safe_name
        return safe_name.upper()

    def get_real_folder_id(self):
        return self.real_folder_id

    def get_jobs_operator_as_string_list(self):
        jobs = []
        for job in self.jobs:
            jobs.append(job.getMetadata())
            jobs.append(job.get_operator()
                        .output(task_name=job.get_job_name_safe()))
        return jobs

    def calculate_imports(self):
        imports = []
        imports.append("#System Imports\nfrom datetime import datetime\n\n# Base Airflow Imports\nimport airflow\nfrom airflow import DAG")
        for job in self.get_jobs():
            if job.get_operator().getImports() != "":
                if job.get_operator().getImports() not in imports:

                    imports.append(job.get_operator().getImports())
        return imports

    def calculate_job_dependencies(self):
        deps = []
        # Calculate Job Dependencies for every job.
        for job in self.get_jobs():
            dep = ""
            out_conds = job.getOutConditions()
            out_conds_positive = []

            for out_cond in out_conds:
                if out_cond.getSign() == "+":
                    out_conds_positive.append(out_cond)

            if len(out_conds_positive) > 0:
                items = ""

                for poutcon in out_conds_positive:
                    for job in self.get_jobs():
                        for incon in job.getInConditions():
                            if incon.get_name() == poutcon.get_name():
                                items += job.get_job_name_safe() + ", "
                if items != "":
                    dep = job.get_job_name_safe() + " >> [" + items + "]"
                    dep = dep.replace(", ]", "]")

            if dep != "":
                deps.append(dep)

        return deps
