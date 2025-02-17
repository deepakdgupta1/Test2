FROM python:3.9-slim

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
