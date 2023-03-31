DummyOperator(task_id="start", dag=dag)

EmptyOperator(task_id="start", dag=dag)

BashOperator(task_id="task_2", bash_command="echo 'Task 2'", dag=dag)

PythonOperator(task_id="task_5", python_callable=random_zero_or_one, dag=dag)

BranchPythonOperator(
    task_id="task_6", python_callable=branching_function, provide_context=True, dag=dag
)

EmailOperator(
    to="person@emal.com",
    subjet="Email Subject",
    html_content="<h3>Hello World!</h3><b/><p>This is an email from Airflow</p>",
)

# pip install 'apache-airflow[amazon]'
create_object = S3CreateObjectOperator(
    task_id="create_object",
    s3_bucket=bucket_name,
    s3_key=key,
    data=DATA,
    replace=True,
)
