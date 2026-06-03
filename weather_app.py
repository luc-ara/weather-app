import requests
import json
from datetime import datetime
from pathlib import Path

CONFIG_FILE = Path("config.json")


def main():
    config = load_config()
    record = fetch_weather(config)
    filepath = build_filepath(record, config)
    save_record(record, filepath)

    
def load_config():
    with CONFIG_FILE.open(encoding="utf-8") as config_file:
        return json.load(config_file)

    
def fetch_weather(config):
    params = {
        "latitude": config["latitude"],
        "longitude": config["longitude"],
        "current": config["variables"]
    }

    response = requests.get(config["base_url"], params=params, timeout=10)

    response.raise_for_status()

    return response.json()["current"]


def build_filepath(record, config):
    dt = datetime.fromisoformat(record["time"])
    title = f"{config['title_prefix']}{dt.strftime('%Y-%m-%d')}.jsonl"

    reports_dir = Path(config["reports_dir"])
    reports_dir.mkdir(parents=True, exist_ok=True)

    return reports_dir / title


def save_record(record, filepath):
    with filepath.open("a", encoding="utf-8") as report:
        report.write(json.dumps(record, ensure_ascii=False))
        report.write("\n")

                            
if __name__ == "__main__":
    main()
