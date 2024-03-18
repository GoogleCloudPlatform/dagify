
#System Imports
from datetime import datetime

# Base Airflow Imports
import airflow
from airflow import DAG

#Imports for Handling SSHOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.providers.google.cloud.hooks.compute_ssh import ComputeEngineSSHHook

None


# Global Variabls
UNKNOWN = None

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="JOB_BOX1",
    start_date=datetime(2021, 1, 1),
    schedule="@daily",
) as dag:

# DAG Tasks


    # ---- Task Metadata ---- JOB_JOB1 ------
	#
	# Control-M Job Name: JOB1 
	# -->	 Airflow Job Name: JOB_JOB1
	# Control-M Job Type: Command
	# -->	 Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_JOB1 = SSHOperator(
        task_id='JOB_JOB1',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="c:\test1.bat",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_JOB2 ------
	#
	# Control-M Job Name: JOB2 
	# -->	 Airflow Job Name: JOB_JOB2
	# Control-M Job Type: Command
	# -->	 Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_JOB2 = SSHOperator(
        task_id='JOB_JOB2',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="c:\test2.bat",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_JOB3 ------
	#
	# Control-M Job Name: JOB3 
	# -->	 Airflow Job Name: JOB_JOB3
	# Control-M Job Type: Command
	# -->	 Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_JOB3 = SSHOperator(
        task_id='JOB_JOB3',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="c:\test3.bat",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_JOB4 ------
	#
	# Control-M Job Name: JOB4 
	# -->	 Airflow Job Name: JOB_JOB4
	# Control-M Job Type: Job
	# -->	 Airflow Operator Type: UnknownOperator
	#
	# ---- End Task Metadata -------------------------------------------

    
    #   JOB_JOB4 = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported
    #   Control-M Job Type
    #
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    # ---- Task Metadata ---- JOB_JOB5 ------
	#
	# Control-M Job Name: JOB5 
	# -->	 Airflow Job Name: JOB_JOB5
	# Control-M Job Type: Job
	# -->	 Airflow Operator Type: UnknownOperator
	#
	# ---- End Task Metadata -------------------------------------------

    
    #   JOB_JOB5 = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported
    #   Control-M Job Type
    #
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    # ---- Task Metadata ---- JOB_JOB6 ------
	#
	# Control-M Job Name: JOB6 
	# -->	 Airflow Job Name: JOB_JOB6
	# Control-M Job Type: Job
	# -->	 Airflow Operator Type: UnknownOperator
	#
	# ---- End Task Metadata -------------------------------------------

    
    #   JOB_JOB6 = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported
    #   Control-M Job Type
    #
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!





# Task Dependencies


    JOB_JOB6 >> [JOB_JOB2]

    JOB_JOB6 >> [JOB_JOB3, JOB_JOB4]

    JOB_JOB6 >> [JOB_JOB5]

    JOB_JOB6 >> [JOB_JOB5]

    JOB_JOB6 >> [JOB_JOB6]
