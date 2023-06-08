from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

# Define the functions that will be executed as tasks
def extract_data():
    print("Extracting data...")

def transform_data():
    print("Transforming data...")

def load_data():
    print("Loading data...")

# Define the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 6, 8)
}

dag = DAG('simple_pipeline', default_args=default_args, schedule_interval=None)

# Define the tasks
extract_task = PythonOperator(
    task_id='extract_task',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_task',
    python_callable=transform_data,
    dag=dag
)

load_task = BashOperator(
    task_id='load_task',
    bash_command='echo "Loading data..."',
    dag=dag
)

# Define the task dependencies
extract_task >> transform_task >> load_task
