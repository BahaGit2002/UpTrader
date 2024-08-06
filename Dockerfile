# We use the official Python 3.11 image
FROM python:3.11.0rc1-slim

# Set the working directory
WORKDIR ./

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
RUN pip install poetry

# Copy project files
COPY ./pyproject.toml ./poetry.lock ./

# Install dependencies via Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the remaining project files
COPY . .

# Copy the .env file
COPY .env ./.env

# Open the port for the application
EXPOSE 8000

# Command to launch the application
CMD ["sh", "-c", "python manage.py migrate && python manage.py create_test_menus && python manage.py runserver 0.0.0.0:8000"]