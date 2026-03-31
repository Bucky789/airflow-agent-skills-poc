import os

def detect_breeze_context():
    if os.path.exists("/.dockerenv"):
        return "breeze_container"

    if os.environ.get("AIRFLOW_HOME"):
        return "breeze_container"

    if os.environ.get("BREEZE_ENV") == "true":
        return "breeze_container"

    return "host"


if __name__ == "__main__":
    print("Context:", detect_breeze_context())