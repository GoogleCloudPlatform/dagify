# Task definitions
JOB7 = SSHOperator(
    task_id='{task_id}',
    ssh_hook=ComputeEngineSSHHook(
        instance_name={instance_name},
        zone={zone},
        project_id={gcp_project_id},
        use_oslogin={use_oslogin},
        use_iap_tunnel={use_iap_tunnel},
        use_internal_ip={use_internal_ip}),
    command='{command}',
    dag=dag
)
        

JOB8 = SSHOperator(
    task_id='{task_id}',
    ssh_hook=ComputeEngineSSHHook(
        instance_name={instance_name},
        zone={zone},
        project_id={gcp_project_id},
        use_oslogin={use_oslogin},
        use_iap_tunnel={use_iap_tunnel},
        use_internal_ip={use_internal_ip}),
    command='{command}',
    dag=dag
)
        



    #   !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported Control-M Job Type
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    #   !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported Control-M Job Type
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!




    #   !!UnknownOperator!!
    #
    #   The following code block represents of an Unsupported Control-M Job Type
    #   Manual intervention is required here.
    #
    #   !!UnknownOperator!!


JOB12 = SSHOperator(
    task_id='{task_id}',
    ssh_hook=ComputeEngineSSHHook(
        instance_name={instance_name},
        zone={zone},
        project_id={gcp_project_id},
        use_oslogin={use_oslogin},
        use_iap_tunnel={use_iap_tunnel},
        use_internal_ip={use_internal_ip}),
    command='{command}',
    dag=dag
)
        

# Task dependencies
JOB7 >> JOB9
JOB8 >> JOB9
JOB9 >> [JOB10, JOB11]
JOB11 >> JOB12
# Task definitions
