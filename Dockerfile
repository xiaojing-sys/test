FROM python:3.14-slim

WORKDIR /app

COPY prompt_validation.py test_prompt_validation.py ./

CMD ["python", "-m", "unittest", "discover", "-v"]
