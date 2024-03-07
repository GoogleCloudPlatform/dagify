


class BaseOperator:
    task_id = None

    def getTaskName(self):
        if self.task_id is None:
            return "UNKNOWN"
        return self.task_id


# SSH Operator 
class SSHOperator(BaseOperator):
    gce_instance_name = None
    gce_instance_zone = None
    gcp_project_id = None
    use_oslogin = True
    use_iap_tunnel = False
    use_internal_ip = True
    command = None

    def __init__(self, task_id, command):
        self.name = "SSHOperator"
        self.task_id = task_id
        self.command = command
    
    def getGCEInstanceName(self):
        if self.gce_instance_name is None:
            return "UNKNOWN"
        return self.gce_instance_name
    
    def getGCEInstanceZone(self):
        if self.gce_instance_zone is None:
           return "UNKNOWN"
        return self.gce_instance_zone
    
    def getGCPProjectID(self):
        if self.gcp_project_id is None:
            return "UNKNOWN"
        return self.gcp_project_id

    def getUseOsLogin(self):
        if self.use_oslogin is None:
            return True
        return self.use_oslogin

    def getUseIapTunnel(self):
        if self.use_iap_tunnel is None:
            return False
        return self.use_iap_tunnel  

    def getUseInternalIp(self):
        if self.use_internal_ip is None:
            return True
        return self.use_internal_ip  

    def getCommand(self):
        if self.command is None:
            return "UNKNOWN"
        return self.command    


    def validate(self):
        return True

    def output(self):
        return """SSHOperator(
        task_id='{task_id}',
        ssh_hook=ComputeEngineSSHHook(
            instance_name={instance_name},
            zone={zone},
            project_id={gcp_project_id},
            use_oslogin={use_oslogin},
            use_iap_tunnel={use_iap_tunnel},
            use_internal_ip={use_internal_ip}),
        command=\"{command}\",
        dag=dag
    )
        """.format(
            task_id=self.getTaskName(), 
            instance_name = self.getGCEInstanceName(),
            zone=self.getGCEInstanceZone(),
            gcp_project_id=self.getGCPProjectID(),
            use_oslogin=self.getUseOsLogin(),
            use_iap_tunnel=self.getUseIapTunnel(),
            use_internal_ip=self.getUseInternalIp(),
            command=self.getCommand()
        )
        

class DummyOperator(BaseOperator):

    def __init__(self, task_id):
        self.name = "DummyOperator"
        self.task_id = task_id

    def validate(self):
        return True

    def output(self):
        return """DummyOperator(
        task_id='{task_id}',
        dag=dag
    )
        """.format(
            task_id=self.getTaskName(), 
        )


class UnknownOperator(BaseOperator):
    def __init__(self):
        self.name = "UnknownOperator"


    def validate(self):
        return True

    def output(self):
        return """

    #   !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported Control-M Job Type
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!
\n\n"""

