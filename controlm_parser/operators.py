class BaseOperator:

    def __init__(self, task_id=None):
        self.task_id = task_id
        self.name = None
        self.import_statement = None

    def get_task_name(self):
        if self.task_id is None:
            return "UNKNOWN"
        return self.task_id

    def get_name(self):
        return self.name

    def getType(self):
        return self.name

    def getImports(self):
        return self.import_statement


# SSH Operator
class SSHOperator(BaseOperator):
    def __init__(
        self,
        task_id,
        command,
        gce_instance_name=None,
        gce_instance_zone=None,
        gcp_project_id=None,
        use_oslogin=True,
        use_iap_tunnel=False,
        use_internal_ip=True
    ):
        self.import_statement = '# Imports for Handling SSHOperator\nfrom airflow.contrib.operators.ssh_operator import SSHOperator\nfrom airflow.providers.google.cloud.hooks.compute_ssh import ComputeEngineSSHHook'
        self.name = "SSHOperator"
        self.task_id = task_id
        self.gce_instance_name = gce_instance_name
        self.gce_instance_zone = gce_instance_zone
        self.gcp_project_id = gcp_project_id
        self.use_oslogin = use_oslogin
        self.use_iap_tunnel = use_iap_tunnel
        self.use_internal_ip = use_internal_ip
        self.command = command

    def get_gce_instance_name(self):
        if self.gce_instance_name is None:
            return "UNKNOWN"
        return self.gce_instance_name

    def get_gce_instance_zone(self):
        if self.gce_instance_zone is None:
            return "UNKNOWN"
        return self.gce_instance_zone

    def get_gcp_project_id(self):
        if self.gcp_project_id is None:
            return "UNKNOWN"
        return self.gcp_project_id

    def get_use_os_login(self):
        if self.use_oslogin is None:
            return True
        return self.use_oslogin

    def get_use_iap_tunnel(self):
        if self.use_iap_tunnel is None:
            return False
        return self.use_iap_tunnel

    def get_use_internal_ip(self):
        if self.use_internal_ip is None:
            return True
        return self.use_internal_ip

    def get_command(self):
        if self.command is None:
            return "UNKNOWN"
        return self.command

    def validate(self):
        return True

    def output(self, task_name="UNKNOWN"):
        return f"{task_name} = SSHOperator(\n\
        task_id='{self.get_task_name()}',\n\
        ssh_hook=ComputeEngineSSHHook(\n\
            instance_name={self.get_gce_instance_name()},\n\
            zone={self.get_gce_instance_zone()},\n\
            project_id={self.get_gcp_project_id()},\n\
            use_oslogin={self.get_use_os_login()},\n\
            use_iap_tunnel={self.get_use_iap_tunnel()},\n\
            use_internal_ip={self.get_use_internal_ip()}),\n\
        command=\"{self.get_command()}\",\n\
        dag=dag\n\
    )"


class DummyOperator(BaseOperator):

    def __init__(self, task_id):
        self.import_statement = "# Imports for DummyOperator\nfrom airflow.operators.dummy import DummyOperator"
        self.name = "DummyOperator"
        self.task_id = task_id

    def validate(self):
        return True

    def output(self, task_name="UNKNOWN"):
        return f"{task_name} = DummyOperator(\
        task_id='{self.get_task_name()}',\
        dag=dag\
    )"


class UnknownOperator(BaseOperator):
    def __init__(self):
        self.name = "UnknownOperator"

    def validate(self):
        return True

    def output(self, task_name="UNKNOWN"):
        return """
    #   {task_name} = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported Control-M Job Type
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!
\n\n""".format(
            task_name=task_name
        )
