
export AIRFLOW_HOME=~/airflow

echo "installing dependencies ..."
#install dependencies
function update_apt_get() {
    for ((i = 0; i < 10; i++)) ; do
        if apt-get update; then
            return 0
        fi
        sleep 5
    done
    return 1
}


update_apt_get
apt-get install -y libmysqlclient-dev libssl-dev libkrb5-dev libsasl2-dev

echo "installing airflow ..."
pip install apache-airflow

echo "airflow initialization ..."
airflow initdb

echo "copying the dags ..."
gsutil cp gs://amir_tavasoli/scripts/Helloworld.py /root/airflow/dags

echo "airflow bringing up ..."
airflow webserver -p 8080 &
airflow scheduler &
airflow worker &




