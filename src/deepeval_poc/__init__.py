"""DeepEval POC - AI QA & Security Testing Framework"""

from pathlib import Path
from dotenv import load_dotenv

# Auto-load .env from project root
project_root = Path(__file__).parent.parent.parent
env_path = project_root / '.env'
if env_path.exists():
    load_dotenv(env_path)

__version__ = "1.0.0"
