FROM public.ecr.aws/lambda/python:3.9

# Set the wd to /var/task. This is whre the lambda will look for the code
WORKDIR ${LAMBDA_TASK_ROOT}

COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt --target .

CMD [ "app.handler" ]