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

    # Airflow Task Dependencies
    fx_fld_001_app_001_subapp_001_job_001_ce606 >> [fx_fld_001_app_001_subapp_001_job_002_06adf, fx_fld_001_app_001_subapp_001_job_003_a8eda]
    fx_fld_001_app_001_subapp_001_job_002_06adf >> [fx_fld_001_app_001_subapp_001_job_003_a8eda]
