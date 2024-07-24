# Apache Airflow Base Imports
from airflow import DAG
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskMarker
from airflow.sensors.external_task import ExternalTaskSensor
import datetime
# Apache Airflow Custom & DAG/Task Specific Imports
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="fast_x_reports",
    start_date=datetime.datetime(2024, 1, 1),
    #schedule="@daily",
    schedule_interval='*/5 * * * *',
    catchup=False,
) as dag:

    # DAG Tasks
    fast_x_job_1 = SSHOperator(
      task_id="fast_x_job_1",
      command="",
      dag=dag,
    )

    fast_x_job_2 = SSHOperator(
      task_id="fast_x_job_2",
      command="",
      dag=dag,
    )

    fast_x_job_3 = SSHOperator(
      task_id="fast_x_job_3",
      command="",
      dag=dag,
    )

    fast_x_job_4 = SSHOperator(
      task_id="fast_x_job_4",
      command="",
      dag=dag,
    )

    fast_x_job_5 = SSHOperator(
      task_id="fast_x_job_5",
      command="",
      dag=dag,
    )

    fast_x_job_6 = SSHOperator(
      task_id="fast_x_job_6",
      command="",
      dag=dag,
    )


    
    # Airflow Task Internal Dependencies
    fast_x_job_1 >> [fast_x_job_2, fast_x_job_3]
    fast_x_job_2 >> [fast_x_job_3, fast_x_job_5]
    fast_x_job_3 >> [fast_x_job_6]
    fast_x_job_4 >> [fast_x_job_6]
    fast_x_job_5 >> [fast_x_job_6]
    

    

    