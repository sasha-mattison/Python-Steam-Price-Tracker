from pathlib import Path

env_path = Path(".env")

if not env_path.exists():
    env_path.write_text(
        "APP_PASSWORD=\nEMAIL=\n"
    )
    print(".env file created")
else:
    print(".env already exists")
