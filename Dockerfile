FROM python:3.9-alpine

# Set the working directory in the Docker container
WORKDIR /usr/src/abc_rest

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code to the working directory
COPY . .

# Configration
EXPOSE 8088

# Execute
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]