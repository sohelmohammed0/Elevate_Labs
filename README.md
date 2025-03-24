# DevOps Task: Deploy a Web Application Using Docker and Nginx Reverse Proxy

## 📌 Objective
Containerize a **Flask web application** and set up **Nginx as a reverse proxy** for better traffic management.

---

## 🏗️ Project Structure
```
Elevate_Labs/
│── app.py                 # Flask application
│── requirements.txt       # Python dependencies
│── Dockerfile             # Flask app Dockerfile
│── docker-compose.yml     # Docker Compose file
│── nginx/
│   └── nginx.conf         # Nginx configuration
│── logs/
│   └── flask/             # Log directory for Flask
```

---

## 🛠️ Step-by-Step Setup

### 1️⃣ Clone the Repository (or Create Project Directory)
```bash
git clone <repository_url>
cd Elevate_Labs
```

### 2️⃣ Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Define the Flask Application (`app.py`)
```python
import logging
import os
from flask import Flask

app = Flask(__name__)

# Ensure logs directory exists
log_directory = "logs/flask"
os.makedirs(log_directory, exist_ok=True)

# Configure logging
logging.basicConfig(filename=os.path.join(log_directory, "app.log"), level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return "Hello, DevOps with Flask!"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### 5️⃣ Create `requirements.txt`
```
flask
```

### 6️⃣ Write the Dockerfile for Flask App
```dockerfile
# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

### 7️⃣ Configure Nginx (`nginx/nginx.conf`)
```nginx
server {
    listen 80;

    location / {
        proxy_pass http://flask-app:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### 8️⃣ Create `docker-compose.yml`
```yaml
services:
  flask-app:
    build: .
    container_name: flask-app
    ports:
      - "5000:5000"

  nginx-proxy:
    image: nginx:latest
    container_name: nginx-proxy
    ports:
      - "80:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - flask-app
```

### 9️⃣ Create Log Directory (If Not Created Automatically)
```bash
mkdir -p logs/flask
```

### 🔟 Build and Run the Containers
```bash
docker-compose up --build -d
```

### 1️⃣1️⃣ Verify Containers are Running
```bash
docker ps
```
Expected Output:
```
CONTAINER ID   IMAGE                    COMMAND                  STATUS              PORTS                    NAMES
xxxxxxx       nginx:latest             "nginx -g 'daemon off;'"   Up X minutes   0.0.0.0:80->80/tcp       nginx-proxy
xxxxxxx       elevate_labs-flask-app   "python app.py"          Up X minutes   0.0.0.0:5000->5000/tcp   flask-app
```

### 1️⃣2️⃣ Test the Application
Open in browser:
- 🔗 **http://localhost/** → Should return `Hello, DevOps with Flask!`
- 🔗 **http://localhost/health** → Should return `{ "status": "healthy" }`

Or use curl:
```bash
curl -I http://localhost
curl http://localhost/health
```

### 1️⃣3️⃣ Check Logs
```bash
cat logs/flask/app.log
```

---

## 🏆 Conclusion
✅ **Successfully containerized a Flask app**  
✅ **Set up Nginx as a reverse proxy**  
✅ **Ensured logging and best practices**  
✅ **Now ready for production deployment!** 🚀

For any issues, check container logs:
```bash
docker logs flask-app
docker logs nginx-proxy
```

Happy DevOps! 🎉