
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
    dag_id="JOB_BOX2",
    start_date=datetime(2021, 1, 1),
    schedule="@daily",
) as dag:

# DAG Tasks


    # ---- Task Metadata ---- JOB_JOB7 ------
	#
	# Control-M Job Name: JOB7 
	# -->	 Airflow Job Name: JOB_JOB7
	# Control-M Job Type: Command
	# -->	 Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_JOB7 = SSHOperator(
        task_id='JOB_JOB7',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="c:\test6.bat",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_JOB8 ------
	#
	# Control-M Job Name: JOB8 
	# -->	 Airflow Job Name: JOB_JOB8
	# Control-M Job Type: Command
	# -->	 Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_JOB8 = SSHOperator(
        task_id='JOB_JOB8',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="c:\test7.bat",
        dag=dag
    )

    # ---- Task Metadata ---- JOB_JOB9 ------
	#
	# Control-M Job Name: JOB9 
	# -->	 Airflow Job Name: JOB_JOB9
	# Control-M Job Type: Job
	# -->	 Airflow Operator Type: UnknownOperator
	#
	# ---- End Task Metadata -------------------------------------------

    
    #   JOB_JOB9 = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported
    #   Control-M Job Type
    #
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    # ---- Task Metadata ---- JOB_JOB10 ------
	#
	# Control-M Job Name: JOB10 
	# -->	 Airflow Job Name: JOB_JOB10
	# Control-M Job Type: Job
	# -->	 Airflow Operator Type: UnknownOperator
	#
	# ---- End Task Metadata -------------------------------------------

    
    #   JOB_JOB10 = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported
    #   Control-M Job Type
    #
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    # ---- Task Metadata ---- JOB_JOB11 ------
	#
	# Control-M Job Name: JOB11 
	# -->	 Airflow Job Name: JOB_JOB11
	# Control-M Job Type: Job
	# -->	 Airflow Operator Type: UnknownOperator
	#
	# ---- End Task Metadata -------------------------------------------

    
    #   JOB_JOB11 = !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported
    #   Control-M Job Type
    #
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    # ---- Task Metadata ---- JOB_JOB12 ------
	#
	# Control-M Job Name: JOB12 
	# -->	 Airflow Job Name: JOB_JOB12
	# Control-M Job Type: Command
	# -->	 Airflow Operator Type: SSHOperator
	#
	# ---- End Task Metadata -------------------------------------------

    JOB_JOB12 = SSHOperator(
        task_id='JOB_JOB12',
        ssh_hook=ComputeEngineSSHHook(
            instance_name=UNKNOWN,
            zone=UNKNOWN,
            project_id=UNKNOWN,
            use_oslogin=True,
            use_iap_tunnel=False,
            use_internal_ip=True),
        command="c:\test11.bat",
        dag=dag
    )


# Task Dependencies


    JOB_JOB12 >> [JOB_JOB9]

    JOB_JOB12 >> [JOB_JOB9]

    JOB_JOB12 >> [JOB_JOB10, JOB_JOB11]

    JOB_JOB12 >> [JOB_JOB12]
