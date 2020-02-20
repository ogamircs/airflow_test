#!/bin/env python

import sys
import subprocess


print("starting airflow docker ...")

r = subprocess.call("docker pull puckel/docker-airflow", shell=True)
print(r)

print("list of images .....")
r = subprocess.call("docker images", shell=True)
print(r)

print("downloading dags from GS")
r = subprocess.call("makdir /usr/local/airflow/dags", shell=True)

r = subprocess.call("gsutil cp gs://amir_tavasoli/scripts/Helloworld.py /usr/local/airflow/dags/", shell=True)
print(r)

print("running airflow .....")
r = subprocess.call("docker run -d -p 8080:8080 -v /usr/local/airflow/dags/:/usr/local/airflow/dags  puckel/docker-airflow webserver", shell=True)
print(r)

r = subprocess.call("docker ps", shell=True)
print(r)

r = subprocess.call('docker exec nostalgic_visvesvaraya airflow test Helloworld task_1 2015-06-01', shell=True)



print("done.")

