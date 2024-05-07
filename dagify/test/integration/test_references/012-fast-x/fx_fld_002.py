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
    dag_id="fx_fld_002",
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
    fx_fld_002_app_001_subapp_001_job_001_150b1 = PythonOperator(
        task_id="fx_fld_002_app_001_subapp_001_job_001_150b1",
        python_callable=helloWorld,
        op_args=["fx_fld_002_app_001_subapp_001_job_001_150b1"],
        dag=dag,
    )
    fx_fld_002_app_001_subapp_001_job_002_ee1a2 = PythonOperator(
        task_id="fx_fld_002_app_001_subapp_001_job_002_ee1a2",
        python_callable=helloWorld,
        op_args=["fx_fld_002_app_001_subapp_001_job_002_ee1a2"],
        dag=dag,
    )
    fx_fld_002_app_001_subapp_001_job_003_b0450 = PythonOperator(
        task_id="fx_fld_002_app_001_subapp_001_job_003_b0450",
        python_callable=helloWorld,
        op_args=["fx_fld_002_app_001_subapp_001_job_003_b0450"],
        dag=dag,
    )

    # Airflow Task Dependencies
    fx_fld_002_app_001_subapp_001_job_001_150b1 >> [fx_fld_002_app_001_subapp_001_job_002_ee1a2, fx_fld_002_app_001_subapp_001_job_003_b0450]
    fx_fld_002_app_001_subapp_001_job_002_ee1a2 >> [fx_fld_002_app_001_subapp_001_job_003_b0450]
