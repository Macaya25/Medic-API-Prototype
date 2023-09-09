from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from retrying import retry
import requests
import json
import os

AIRFLOW_URL = os.getenv('AIRFLOW_URL')


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def airflow_dag_trigger(dag_name, param):
    endpoint = 'api/experimental/dags'
    try:
        query = (
            '{}/{}/{}/dag_runs'.format(AIRFLOW_URL, endpoint, dag_name)
        )
        header = {
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache'
        }
        body = json.dumps(
            {
                'conf': param
            }
        )

        retry_strategy = Retry(total=10, backoff_factor=1, status_forcelist=[500, 400], method_whitelist=["POST"])
        http = requests.Session()

        http.mount('https://', HTTPAdapter(max_retries=retry_strategy))
        response = http.post(query, data=body, headers=header, timeout=500)
        return response.json()
    except Exception as e:
        print("Error initializing DAG: {}".format(dag_name))
        print(e.text)
        raise
