# Apache Airflow on Kubernetes (DevOps Senior Project)

This guide describes how to build and deploy Apache Airflow using KIND (Kubernetes IN Docker), Helm, and a custom Docker image containing your DAGs and scripts.

---
## 🛠️ Prerequisites

Before you begin, make sure the following tools are installed and properly configured:

### 1. Docker
- Required to run Kubernetes locally via KIND and to build/push Airflow DAGs images.
- [Install Docker Desktop](https://www.docker.com/products/docker-desktop/)
- After install, verify with:
  ```bash
  docker --version
  ```
- Enable Kuberenetes via settings inside docker decktop 


### 2. Kubernetes (via KIND - Kubernetes IN Docker)
- Used to spin up a lightweight local Kubernetes cluster inside Docker.
- [Install KIND](https://kind.sigs.k8s.io/docs/user/quick-start/)
- After install, verify with:
  ```bash
  kind --version
  ```

    Make sure kind is added to path envioroment variables 
    and the .exe is named kind.exe


### 3. kubectl (Kubernetes CLI)
- Required to interact with your Kubernetes cluster.
- [Install kubectl](https://kubernetes.io/docs/tasks/tools/)
- After install, verify with:
  ```bash
  kubectl version --client
  ```

### 4. Helm (Kubernetes Package Manager)
- Used to install and manage Airflow via Helm charts.
- [Install Helm](https://helm.sh/docs/intro/install/)
- After install, verify with:
  ```bash
  helm version
  ```

### 5. Git (optional but recommended)
- Useful for version-controlling your DAGs and configuration files.
- [Install Git](https://git-scm.com/downloads)
- Verify with:
  ```bash
  git --version
  ```

---

### 6. Configuration of files
Edit kind-config.yaml
``` bash
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraMounts:
      - hostPath: C:\Users\User\Desktop\Test_Read
        containerPath: /mnt/localfiles
      - hostPath: C:\Users\User\Desktop\SeniorProject\airflow\dags
        containerPath: /opt/airflow/dags
```

* Need to change these paths
- hostPath: C:\Users\User\Desktop\Test_Read
    This is folder path on host machine that you want to read from 
- hostPath: C:\Users\User\Desktop\SeniorProject\airflow\dags
    This is folder path of dags on host machine



---

### 7. Installing Kind

Open cmd from current pathing
                Used For Debugging Dont run below 
                    kind delete cluster --name airflow-cluster
# 1. Create Kind Cluster
kind create cluster --name airflow-cluster --config kind-config.yaml
    What it does:

    Creates a new Kubernetes cluster using [Kind (Kubernetes IN Docker)].

    --name airflow-cluster: names the cluster so you can manage it later.

    --config kind-config.yaml: applies a custom config file, e.g., to mount host directories into your containers.
# 2. Create Kind namespace
kubectl create namespace airflow

    What it does:

    Creates a new Kubernetes namespace called airflow.

    Why you're doing it:

    Helm charts for Airflow are often installed into a dedicated namespace.

    Namespaces help isolate your Airflow deployment from other apps or future projects running in the same cluster.


# 3. Create Persistant Volume Claims
kubectl apply -f text-read.yaml
kubectl apply -f dag-read.yaml
kubectl apply -f log-read.yaml
    Mount volumes


# Step 4: Pull the image from Docker Hub
docker build --pull --tag sirpacster/airflow-dags:latest .

# Step 5: Tag image locally
docker tag sirpacster/airflow-dags:latest kind.local/sirpacster/airflow-dags:latest



# Step 5: Load it into the kind cluster
kind load docker-image sirpacster/airflow-dags:latest --name airflow-cluster    

# Step 6: add airflow repo to helm
helm repo add apache-airflow https://airflow.apache.org

    What it does:

    Add apache airflow to your helm repo

# Step 7: Install airflow version we use with our values to helm

helm install fair-airflow apache-airflow/airflow --version 1.11.0 -n airflow -f values.yaml

    ^ Use this for initial install

helm upgrade fair-airflow apache-airflow/airflow --version 1.11.0 -n airflow -f values.yaml

    ^ Use this for updates to helm install


    What it does:

    Installs the Apache Airflow Helm chart into your cluster using Helm, a package manager for Kubernetes.c

    fair-airflow: this is your release name — you can change it if you want.

    apache-airflow/airflow: this refers to the Helm chart repository and the specific chart name.

    -n airflow: tells Helm to install this into the airflow namespace.

    -f values.yaml uses the values file

# Step 8: run web server on local host 8080
kubectl port-forward svc/fair-airflow-webserver 8080:8080 --namespace airflowkubectl port-forward svc/fair-airflow-webserver 8080:8080 --namespace airflowkubectl port-forward svc/fair-airflow-webserver 8080:8080 --namespace airflowkubectl port-forward svc/fair-airflow-webserver 8080:8080 --namespace airflow
# Debug & Extras
kubectl delete pods -n airflow --selector=release=fair-airflow







docker build --pull --tag sirpacster/airflow-dags:latest .
kind load docker-image sirpacster/airflow-dags:latest --name airflow-cluster    





docker build -t sirpacster/airflow-dags:latest .
docker push sirpacster/airflow-dags:latest
    Build Docker Image

docker build --pull --tag sirpacster/airflow-dags:latest .

kind load docker-image sirpacster/airflow-dags:latest --name airflow-cluster    
    Load image into Kind






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




