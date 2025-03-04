# base image
FROM python:3.12-bullseye

#maintainer
LABEL Author="Aaqib Ansari"

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code
COPY ../django_chatapp /app


# RUN apt-get update && \
#     apt-get install -y --no-install-recommends gcc


COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -rf /tmp/requirements.txt \
    && useradd -U app_user \
    && install -d -m 0755 -o app_user -g app_user /app/static



# # Copy the requirements file and install Python dependencies
COPY ../requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
    
# Install Gunicorn if it's not in requirements.txt
RUN pip install gunicorn

# # Expose port 8000 for the Django application
EXPOSE 8000


RUN mkdir -p logs/
RUN chown -R app_user:app_user logs
RUN mkdir -p media/
RUN chown -R app_user:app_user media
RUN mkdir -p gunicorn_logs/
RUN chown -R app_user:app_user gunicorn_logs

# # Command to run the Django application with Gunicorn
CMD ["gunicorn", "django_chatapp.wsgi:application", "--bind", "0.0.0.0:8000"]

# # Copy entrypoint.sh
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]









