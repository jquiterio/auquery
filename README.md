[![PyPI version](https://badge.fury.io/py/auquery.svg)](https://badge.fury.io/py/auquery)


Defaults
--
auditd log dir is /var/log/audit


Requirements
--
- python3
- Make sure that auditd logs to /var/log/audit or set environment variable AUQUERY_LOG_DIR to a directory where logs are located.
- Make sure that user who run auquery is able to read to AUQERY_LOG_DIR


Install
--
pip install auquery

Run
--
auquery
or 
sudo auquery

TODO
--
- Parse audit logs directly from kernel (without log files dependency)

