# Task definitions
JOB1= CustomSSHOperator(task_id='JOB1', dag=dag)
JOB2= CustomSSHOperator(task_id='JOB2', dag=dag)
JOB3= CustomSSHOperator(task_id='JOB3', dag=dag)
JOB4= CustomSSHOperator(task_id='JOB4', dag=dag)
JOB5= CustomSSHOperator(task_id='JOB5', dag=dag)
JOB6= CustomSSHOperator(task_id='JOB6', dag=dag)

# Task dependencies
JOB1 >> JOB2
JOB2 >> [JOB3, JOB4]
JOB3 >> JOB5
JOB4 >> JOB5
JOB5 >> JOB6
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
