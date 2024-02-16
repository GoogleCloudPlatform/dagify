# Task definitions
JOB7= CustomSSHOperator(task_id='JOB7', dag=dag)
JOB8= CustomSSHOperator(task_id='JOB8', dag=dag)
JOB9= CustomSSHOperator(task_id='JOB9', dag=dag)
JOB10= CustomSSHOperator(task_id='JOB10', dag=dag)
JOB11= CustomSSHOperator(task_id='JOB11', dag=dag)
JOB12= CustomSSHOperator(task_id='JOB12', dag=dag)

# Task dependencies
JOB7 >> JOB9
JOB8 >> JOB9
JOB9 >> [JOB10, JOB11]
JOB11 >> JOB12
