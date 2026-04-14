import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

agents_dir = os.environ.get("AGENTS_DIR", ".")

app = get_fast_api_app(agents_dir=agents_dir, web=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")