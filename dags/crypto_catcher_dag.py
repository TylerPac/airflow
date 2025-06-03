from airflow import DAG
#from airflow.operators.python import PythonOperator
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
#import subprocess

with DAG(
    dag_id='crypto_catcher_k8s',
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=['crypto'],
) as dag:

    run_k8s_task = KubernetesPodOperator(
        task_id='run_crypto_catcher_k8s',
        name='crypto-catcher',
        namespace='airflow',
        image='sirpacster/crypto-catcher:latest',
        cmds=["python", "fetch_crypto.py"],
        is_delete_operator_pod=True,
    )
    
#def run_fetch_crypto():
#    subprocess.run(["python", "/opt/airflow/dags/fetch_crypto.py"], check=True)

#with DAG(
#    dag_id='crypto_catcher_dag_local',
#    start_date=datetime(2024, 1, 1),
#    schedule="@daily",
#    catchup=False,
#    tags=['crypto'],
#) as dag:
#    run_local_task = PythonOperator(
#        task_id='run_local_crypto_catcher',
#        python_callable=run_fetch_crypto
#    )

