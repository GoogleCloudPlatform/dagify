class Job:
    # Holds the Airflow Operator Object
    def __init__(self,
        job_name = None,
        description = None,
        jobISN = None,
        application = None,
        sub_application = None,
        memname = None,
        created_by = None,
        run_as = None,
        priority = None,
        critical = None,
        tasktype= None,
        cyclic= None,
        node_id = None,
        interval = None,
        cmd_line = None,
        confirm = None,
        retro = None,
        maxwait = None,
        maxrerun = None,
        autoarch = None,
        maxdays = None,
        maxruns = None,
        timefrom = None,
        weekdays = None,
        jan = None,
        feb = None,
        mar = None,
        apr = None,
        may = None,
        jun = None,
        jul = None,
        aug = None,
        sep = None,
        oct = None,
        nov = None,
        dec = None,
        days_and_or = None,
        shift = None,
        shiftnum = None,
        sysdb = None,
        jobs_in_group = None,
        ind_cyclic = None,
        creation_user = None,
        creation_date = None,
        creation_time = None,
        change_userid = None,
        change_date = None,
        change_time = None,rule_based_calendar_relationship = None,
        appl_type = None,
        multy_agent = None,
        use_instream_jcl = None,
        version_opcode = None,
        is_current_version = None,
        version_serial = None,
        version_host = None,
        cyclic_tolerance = None,
        cyclic_type = None,
        parent_folder = None):
        self.job_name = job_name
        self.description = description
        self.jobISN = jobISN
        self.application = application
        self.sub_application = sub_application 
        self.memname = memname 
        self.created_by = created_by
        self.run_as = run_as 
        self.priority = priority
        self.critical = critical 
        self.tasktype = tasktype
        self.cyclic = cyclic
        self.node_id = node_id
        self.interval = interval
        self.cmd_line = cmd_line
        self.confirm = confirm
        self.retro = retro
        self.maxwait = maxwait
        self.maxrerun = maxrerun
        self.autoarch = autoarch
        self.maxdays = maxdays
        self.maxruns = maxruns
        self.timefrom = timefrom
        self.weekdays = weekdays
        self.jan = jan
        self.feb = feb
        self.mar = mar
        self.apr = apr
        self.may = may
        self.jun = jun
        self.jul = jul
        self.aug = aug
        self.sep = sep
        self.oct = oct
        self.nov = nov
        self.dec = dec
        self.days_and_or = days_and_or
        self.shift = shift
        self.shiftnum = shiftnum
        self.sysdb = sysdb
        self.jobs_in_group = jobs_in_group
        self.ind_cyclic = ind_cyclic
        self.creation_user = creation_user
        self.creation_date = creation_date
        self.creation_time = creation_time
        self.change_userid = change_userid
        self.change_date = change_date
        self.change_time = change_time
        self.rule_based_calendar_relationship = rule_based_calendar_relationship
        self.appl_type = appl_type
        self.multy_agent = multy_agent
        self.use_instream_jcl = use_instream_jcl
        self.version_opcode = version_opcode
        self.is_current_version = is_current_version
        self.version_serial = version_serial
        self.version_host = version_host
        self.cyclic_tolerance = cyclic_tolerance
        self.cyclic_type = cyclic_type
        self.parent_folder = parent_folder
        self.inCondition = []
        self.outCondition = []
        self.shout = []
        self.variables = []
        self.dependencies = []
        self.operator = None
        return

    def setOperator(self, op): 
        self.operator = op
        return

    def getOperator(self): 
        return self.operator

    def getJobType(self):
        if self.tasktype is None: 
            return "UNKNOWN"
        return self.tasktype

    def getJobName(self):
        if self.job_name is None: 
            return "UNKNOWN"
        return self.job_name

    def getJobNameSafe(self):
        safeName = self.getJobName()
        safeName = safeName.replace("-", "_")
        safeName = safeName.replace(":", "")
        safeName = safeName.replace("#", "_")
        safeName = safeName.replace(" ", "_")
        safeName = "JOB_" + safeName
        return safeName.upper()

    def getCmdLine(self):
        return self.cmd_line
        
    def getCmdLineSafe(self):
        safeName = self.getCmdLine()
        safeName = safeName.replace("\"", "'")
        return safeName
    
    def addInCondition(self, cond):
        self.inCondition.append(cond)
        return

    def addOutCondition(self, cond):
        self.outCondition.append(cond)
        return

    def addShout(self, shout):
        self.shout.append(shout)
        return

    def addVariable(self, var):
        self.variables.append(var)
        return

    def getInConditions(self):
        return self.inCondition

    def getOutConditions(self):
        return self.outCondition

    def getShouts(self):
        return self.shout
    
    def getVariables(self):
        return self.variables

    def getDependencies(self):
        return self.dependencies

    def getMetadata(self):
        return "\
# ---- Task Metadata ---- {job_name} ------\n\
\t#\n\
\t# Control-M Job Name: {control_m_job_name} \t-->\t Airflow Job Name: {airflow_job_name}\n\
\t# Control-M Job Type: {control_m_job_type} \t-->\t  Airflow Operator Type: {airflow_operator_type}\n\
\t#\n\
\t# ---- End Task Metadata -------------------------------------------".format(
    job_name = self.getJobNameSafe(),
    control_m_job_name = self.getJobName(),
    airflow_job_name = self.getJobNameSafe(),
    control_m_job_type = self.getJobType(),
    airflow_operator_type = self.getOperator().getType(),
    
)