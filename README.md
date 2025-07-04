
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

helm install fair-airflow apache-airflow/airflow -n airflow -f values.yaml
helm install fair-airflow apache-airflow/airflow --version 1.11.0 -n airflow -f values.yaml
helm upgrade fair-airflow apache-airflow/airflow --version 1.11.0 -n airflow -f values.yaml

    What it does:

    Installs the Apache Airflow Helm chart into your cluster using Helm, a package manager for Kubernetes.

    fair-airflow: this is your release name — you can change it if you want.

    apache-airflow/airflow: this refers to the Helm chart repository and the specific chart name.

    -n airflow: tells Helm to install this into the airflow namespace.

    -f values.yaml uses the values file


helm repo add apache-airflow https://airflow.apache.org

    What it does:

    Add apache airflow to your helm repo


kubectl port-forward svc/fair-airflow-api-server 8080:8080 --namespace airflow    



helm install dev-release apache-airflow/airflow --namespace airflow

kubectl apply -f text-read.yaml

kubectl port-forward svc/dev-release-api-server 8080:8080 -n airflow

docker build --pull --tag sirpacster/airflow-dags:latest .

kind load docker-image sirpacster/airflow-dags:latest --name airflow-cluster

helm upgrade dev-release apache-airflow/airflow --namespace airflow --set images.airflow.repository=sirpacster/airflow-dags --set images.airflow.tag=latest

kubectl delete pods -n airflow --selector=release=dev-release

helm upgrade dev-release apache-airflow/airflow --namespace airflow -f values.yaml