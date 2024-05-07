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
    dag_id="fx_fld_001",
    start_date=datetime.datetime(2024, 1, 1),
    # schedule="@daily",
    schedule_interval='*/1 * * * *',
) as dag:

    # DAG Tasks
    fx_fld_001_app_001_subapp_001_job_001_ce606 = PythonOperator(
        task_id="fx_fld_001_app_001_subapp_001_job_001_ce606",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_001_subapp_001_job_001_ce606"],
        dag=dag,
    )
    fx_fld_001_app_001_subapp_001_job_002_06adf = PythonOperator(
        task_id="fx_fld_001_app_001_subapp_001_job_002_06adf",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_001_subapp_001_job_002_06adf"],
        dag=dag,
    )
    fx_fld_001_app_001_subapp_001_job_003_a8eda = PythonOperator(
        task_id="fx_fld_001_app_001_subapp_001_job_003_a8eda",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_001_subapp_001_job_003_a8eda"],
        dag=dag,
    )
    fx_fld_001_app_002_subapp_001_job_001_e9b8d = PythonOperator(
        task_id="fx_fld_001_app_002_subapp_001_job_001_e9b8d",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_002_subapp_001_job_001_e9b8d"],
        dag=dag,
    )
    fx_fld_001_app_002_subapp_001_job_002_4ea5d = PythonOperator(
        task_id="fx_fld_001_app_002_subapp_001_job_002_4ea5d",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_002_subapp_001_job_002_4ea5d"],
        dag=dag,
    )
    fx_fld_001_app_002_subapp_001_job_003_d68d5 = PythonOperator(
        task_id="fx_fld_001_app_002_subapp_001_job_003_d68d5",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_002_subapp_001_job_003_d68d5"],
        dag=dag,
    )
    fx_fld_001_app_002_subapp_002_job_001_481f8 = PythonOperator(
        task_id="fx_fld_001_app_002_subapp_002_job_001_481f8",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_002_subapp_002_job_001_481f8"],
        dag=dag,
    )
    fx_fld_001_app_002_subapp_002_job_002_d63da = PythonOperator(
        task_id="fx_fld_001_app_002_subapp_002_job_002_d63da",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_002_subapp_002_job_002_d63da"],
        dag=dag,
    )
    fx_fld_001_app_002_subapp_002_job_003_fd690 = PythonOperator(
        task_id="fx_fld_001_app_002_subapp_002_job_003_fd690",
        python_callable=helloWorld,
        op_args=["fx_fld_001_app_002_subapp_002_job_003_fd690"],
        dag=dag,
    )

    # Airflow Task Dependencies
    fx_fld_001_app_001_subapp_001_job_001_ce606 >> [fx_fld_001_app_001_subapp_001_job_002_06adf, fx_fld_001_app_001_subapp_001_job_003_a8eda]
    fx_fld_001_app_001_subapp_001_job_002_06adf >> [fx_fld_001_app_001_subapp_001_job_003_a8eda]
    fx_fld_001_app_002_subapp_001_job_001_e9b8d >> [fx_fld_001_app_002_subapp_001_job_003_d68d5]
    fx_fld_001_app_002_subapp_001_job_002_4ea5d >> [fx_fld_001_app_002_subapp_001_job_003_d68d5]
    fx_fld_001_app_002_subapp_002_job_001_481f8 >> [fx_fld_001_app_002_subapp_002_job_003_fd690]
    fx_fld_001_app_002_subapp_002_job_002_d63da >> [fx_fld_001_app_002_subapp_002_job_003_fd690]
