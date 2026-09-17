from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="employee_etl",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id="run_employee_etl",
        bash_command="""
        python -m jobs.spark_job configs/employee_etl.yaml
        """
    )