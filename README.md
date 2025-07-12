# Splunk Logging & Monitoring Lab

This is a home lab project simulating a real-world logging and monitoring workflow using **Splunk**, **Python**, and **custom log generation**. It mimics how TechOps or DevOps teams ingest and respond to logs in enterprise systems.

## 🧪 Features

- Custom Python script to generate realistic application logs
- Simulated incident script (error storm generator)
- Splunk ingestion, parsing, and live dashboard creation
- Real-time alert setup for error thresholds
- Logs structured in `log_level - message` format

## 🛠️ Tools Used

- Splunk Enterprise (local)
- Python (log generation)
- macOS (host environment)
- Git & GitHub (version control & sharing)

## 🗂️ Files

- `log_generator.py` – continuously writes mixed-level logs (INFO, ERROR, etc.)
- `error_storm.py` – simulates a spike of ERROR logs to trigger Splunk alerts
- `.gitignore` – excludes log files from the repo
- `README.md` – documentation of the project

## 📊 Next Steps

- Create multiple log sources (e.g., Nginx, audit logs)
- Send alerts to Slack/email
- Deploy this lab to AWS for cloud-based monitoring

