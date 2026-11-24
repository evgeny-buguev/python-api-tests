import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(PROJECT_ROOT / ".env.example")

JSONPLACEHOLDER_BASE_URL = os.environ["JSONPLACEHOLDER_BASE_URL"].rstrip("/")
DUMMYJSON_BASE_URL = os.environ["DUMMYJSON_BASE_URL"].rstrip("/")
DUMMYJSON_USERNAME = os.environ["DUMMYJSON_USERNAME"]
DUMMYJSON_PASSWORD = os.environ["DUMMYJSON_PASSWORD"]
EXPANDTESTING_BASE_URL = os.environ["EXPANDTESTING_BASE_URL"].rstrip("/")
EXPANDTESTING_USERNAME = os.environ["EXPANDTESTING_USERNAME"]
EXPANDTESTING_PASSWORD = os.environ["EXPANDTESTING_PASSWORD"]
PRACTICE_TEST_BASE_URL = os.environ["PRACTICE_TEST_BASE_URL"].rstrip("/")
PRACTICE_TEST_USERNAME = os.environ["PRACTICE_TEST_USERNAME"]
PRACTICE_TEST_PASSWORD = os.environ["PRACTICE_TEST_PASSWORD"]
TODOMVC_BASE_URL = os.environ["TODOMVC_BASE_URL"].rstrip("/")
SELENIUM_BASE_URL = os.environ["SELENIUM_BASE_URL"].rstrip("/")
TESTPAGES_BASE_URL = os.environ["TESTPAGES_BASE_URL"].rstrip("/")
EXAMPLE_BASE_URL = os.environ["EXAMPLE_BASE_URL"].rstrip("/")
