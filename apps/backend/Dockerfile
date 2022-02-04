FROM python:3-alpine

ENV VIRTUAL_ENV=/OPT/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
EXPOSE 5000
ENTRYPOINT ["flask", "run", "-p", "5000", "-h", "0.0.0.0"]
