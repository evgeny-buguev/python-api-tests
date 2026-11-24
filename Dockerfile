FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m playwright install --with-deps chromium \
    && useradd --create-home qa \
    && chown qa:qa /app

COPY --chown=qa:qa . .
USER qa

CMD ["python", "-m", "pytest", "--alluredir=allure-results", "--tracing=retain-on-failure", "--screenshot=only-on-failure"]
