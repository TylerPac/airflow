from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime
from kubernetes.client import models as k8s


with DAG(
    dag_id='DAG_TextParser_to_MySQL',
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=['TP_toMySQL'],
) as dag:

    run_k8s_task = KubernetesPodOperator(
        task_id='run_DAG_TextParser_to_MySQL',
        name='TextParser_to_MySQL',
        namespace='airflow',
        image='docker.io/sirpacster/airflow-dags:latest',  
        cmds=["python", "/opt/airflow/dags/TextParser_to_MySQL.py"],
        is_delete_operator_pod=False,  # Keep the pod after completion for logs TEST
        volumes=[
            k8s.V1Volume(
                name="dag-read-pvc",
                persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                    claim_name="dag-read-pvc"
                )
            ),
            k8s.V1Volume(
                name="text-read-pvc",
                persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                    claim_name="text-read-pvc"
                )
            )
        ],
        volume_mounts=[
            k8s.V1VolumeMount(
                mount_path="/opt/airflow/dags",
                name="dag-read-pvc",
                read_only=False
            ),
            k8s.V1VolumeMount(
                mount_path="/mnt/data",
                name="text-read-pvc",
                read_only=False
            )
        ],
    )
    