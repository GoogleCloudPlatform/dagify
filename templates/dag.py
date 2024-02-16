from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 5, 19)
}

dag = DAG('dependency_dag', default_args=default_args, schedule_interval=None)

# Define tasks
task_1 = DummyOperator(task_id='task_1', dag=dag)
task_2 = DummyOperator(task_id='task_2', dag=dag)
task_3 = DummyOperator(task_id='task_3', dag=dag)
task_4 = DummyOperator(task_id='task_4', dag=dag)

# Define dependencies
task_1 >> task_2  # task_2 depends on task_1
task_1 >> task_3  # task_3 depends on task_1
task_2 >> task_4  # task_4 depends on task_2
task_3 >> task_4  # task_4 depends on task_3