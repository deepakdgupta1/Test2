FROM python:3.9-slim
RUN --mount=type=secret,id=MYSQL_USER,dst=/run/secrets/MYSQL_USER cat /run/secrets/MYSQL_USER
RUN --mount=type=secret,id=MYSQL_PASSWORD,dst=/run/secrets/MYSQL_PASSWORD cat /run/secrets/MYSQL_PASSWORD
RUN --mount=type=secret,id=MYSQL_DATABASE,dst=/run/secrets/MYSQL_DATABASE cat /run/secrets/MYSQL_DATABASE
RUN --mount=type=secret,id=MYSQL_ROOT_PASSWORD,dst=/run/secrets/MYSQL_ROOT_PASSWORD cat /run/secrets/MYSQL_ROOT_PASSWORD

# Set working directory
WORKDIR /app

# Add a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Switch to non-root user
USER appuser

# Run the application
CMD ["python", "src/main.py"]
