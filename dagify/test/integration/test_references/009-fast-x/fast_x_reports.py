# Apache Airflow Base Imports
from airflow import DAG
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskMarker
from airflow.sensors.external_task import ExternalTaskSensor
import datetime
# Apache Airflow Custom & DAG/Task Specific Imports
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="fast_x_reports",
    schedule_interval="@daily",  # TIMEFROM not found, default schedule set to @daily,
    catchup=False,
) as dag:

    # DAG Tasks
    fast_x_job_1 = BashOperator(
        task_id="fast_x_job_1",
        bash_command="",
        dag=dag,
    )

    fast_x_job_2 = BashOperator(
        task_id="fast_x_job_2",
        bash_command="",
        dag=dag,
    )

    fast_x_job_3 = BashOperator(
        task_id="fast_x_job_3",
        bash_command="",
        dag=dag,
    )

    fast_x_job_4 = BashOperator(
        task_id="fast_x_job_4",
        bash_command="",
        dag=dag,
    )

    fast_x_job_5 = BashOperator(
        task_id="fast_x_job_5",
        bash_command="",
        dag=dag,
    )

    fast_x_job_6 = BashOperator(
        task_id="fast_x_job_6",
        bash_command="",
        dag=dag,
    )

    # Airflow Task Internal Dependencies
    fast_x_job_1 >> [fast_x_job_2, fast_x_job_3]
    fast_x_job_2 >> [fast_x_job_3, fast_x_job_5]
    fast_x_job_3 >> [fast_x_job_6]
    fast_x_job_4 >> [fast_x_job_6]
    fast_x_job_5 >> [fast_x_job_6]
