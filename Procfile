web: newrelic-admin run-program gunicorn --pythonpath="$PWD/ctest" wsgi:application
worker: python ctest/manage.py rqworker default