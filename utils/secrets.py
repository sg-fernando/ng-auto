import json
from pathlib import Path

def get_secrets():
    p = Path("secrets.json")
    if not p.exists():
        raise SystemExit("secrets.json missing")

    with p.open() as f:
        data = json.load(f)

    return data


def add_already_applied_job(job_id):
    p = Path("secrets.json")
    if not p.exists():
        raise SystemExit("secrets.json missing")

    with p.open() as f:
        data = json.load(f)

    applied_jobs = data.get("applied_jobs", [])
    applied_jobs.append(job_id)

    data["applied_jobs"] = applied_jobs

    with p.open("w") as f:
        json.dump(data, f)