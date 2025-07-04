FROM apache/airflow:2.9.2-python3.11


USER root
# Install dependencies

RUN apt-get update && apt-get install -y --no-install-recommends libre2-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow

ENV AIRFLOW_INSTALL_EDITABLE="false"

RUN pip install --no-cache-dir "apache-airflow-providers-cncf-kubernetes==7.4.1" "google-re2>=1.1.2" mysql-connector-python requests
# Copy DAG and script into Airflow DAGs folders
# COPY dags/ /opt/airflow/dags/
# COPY TextParser_to_MySQL.py /opt/airflow/dags/
