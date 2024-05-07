# Apache Airflow Base Imports
from airflow import DAG
from airflow.decorators import task
import datetime
# Apache Airflow Custom & DAG/Task Specific Imports
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airflow',
}

with DAG(
    dag_id="fast_x",
    start_date=datetime.datetime(2024, 1, 1),
    # schedule="@daily",
    schedule_interval='*/1 * * * *',
) as dag:

    # DAG Tasks
    fast_x_job_1_95096 = PythonOperator(
        task_id="fast_x_job_1_95096",
        python_callable=helloWorld,
        op_args=["fast_x_job_1_95096"],
        dag=dag,
    )
    fast_x_job_2_7431b = PythonOperator(
        task_id="fast_x_job_2_7431b",
        python_callable=helloWorld,
        op_args=["fast_x_job_2_7431b"],
        dag=dag,
    )
    fast_x_job_3_a87ed = PythonOperator(
        task_id="fast_x_job_3_a87ed",
        python_callable=helloWorld,
        op_args=["fast_x_job_3_a87ed"],
        dag=dag,
    )
    fast_x_job_4_20442 = PythonOperator(
        task_id="fast_x_job_4_20442",
        python_callable=helloWorld,
        op_args=["fast_x_job_4_20442"],
        dag=dag,
    )
    fast_x_job_5_5fbd0 = PythonOperator(
        task_id="fast_x_job_5_5fbd0",
        python_callable=helloWorld,
        op_args=["fast_x_job_5_5fbd0"],
        dag=dag,
    )
    fast_x_job_6_65c50 = PythonOperator(
        task_id="fast_x_job_6_65c50",
        python_callable=helloWorld,
        op_args=["fast_x_job_6_65c50"],
        dag=dag,
    )

    # Airflow Task Dependencies
    fast_x_job_1_95096 >> [fast_x_job_2_7431b, fast_x_job_3_a87ed]
    fast_x_job_2_7431b >> [fast_x_job_3_a87ed, fast_x_job_5_5fbd0]
    fast_x_job_3_a87ed >> [fast_x_job_6_65c50]
    fast_x_job_4_20442 >> [fast_x_job_6_65c50]
    fast_x_job_5_5fbd0 >> [fast_x_job_6_65c50]
