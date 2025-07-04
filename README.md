
kind delete cluster --name airflow-cluster

kind create cluster --name airflow-cluster --config kind-config.yaml
    What it does:

    Creates a new Kubernetes cluster using [Kind (Kubernetes IN Docker)].

    --name airflow-cluster: names the cluster so you can manage it later.

    --config kind-config.yaml: applies a custom config file, e.g., to mount host directories into your containers.

kubectl create namespace airflow

    What it does:

    Creates a new Kubernetes namespace called airflow.

    Why you're doing it:

    Helm charts for Airflow are often installed into a dedicated namespace.

    Namespaces help isolate your Airflow deployment from other apps or future projects running in the same cluster.



kubectl apply -f text-read.yaml
kubectl apply -f dag-read.yaml
    Mount volumes

docker build -t sirpacster/airflow-dags:latest .
docker push sirpacster/airflow-dags:latest
    Build Docker Image

docker build --pull --tag sirpacster/airflow-dags:latest .

kind load docker-image sirpacster/airflow-dags:latest --name airflow-cluster    
    Load image into Kind



helm repo add apache-airflow https://airflow.apache.org

    What it does:

    Add apache airflow to your helm repo


helm install fair-airflow apache-airflow/airflow -n airflow -f values.yaml
helm install fair-airflow apache-airflow/airflow --version 1.11.0 -n airflow -f values.yaml
    Use Older version for AirFlow


helm upgrade fair-airflow apache-airflow/airflow --version 1.11.0 -n airflow -f values.yaml

    What it does:

    Installs the Apache Airflow Helm chart into your cluster using Helm, a package manager for Kubernetes.c

    fair-airflow: this is your release name — you can change it if you want.

    apache-airflow/airflow: this refers to the Helm chart repository and the specific chart name.

    -n airflow: tells Helm to install this into the airflow namespace.

    -f values.yaml uses the values file




kubectl delete pods -n airflow --selector=release=fair-airflow




