FROM python:3.10-slim

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . /code

# 
CMD ["sh", "-c", "sleep 30 && uvicorn server:app --host 0.0.0.0 --port 5000"]
