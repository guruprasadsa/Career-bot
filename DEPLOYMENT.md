# Deployment Guide

This guide provides instructions for deploying the Career-bot application to various platforms.

## 🚀 Production Deployment

### Prerequisites
- Docker (optional)
- PostgreSQL (for production database)
- Redis (for session management)
- SSL Certificate
- Domain name

### Environment Setup

#### 1. Production Environment Variables

**Django Backend** (`.env`):
```env
DJANGO_SECRET_KEY=your_production_secret_key_here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/career_counselling_db
EMAIL_HOST_USER=your_production_email@gmail.com
EMAIL_HOST_PASSWORD=your_production_app_password
SEND_BIRD_APP_ID=your_production_sendbird_app_id
SEND_BIRD_API_TOKEN=your_production_sendbird_api_token
```

**React Frontend** (`.env.production`):
```env
VITE_SENDBIRD_APP_ID=your_production_sendbird_app_id
VITE_SENDBIRD_API_TOKEN=your_production_sendbird_api_token
VITE_API_BASE_URL=https://api.yourdomain.com
```

#### 2. Database Migration

```bash
# PostgreSQL setup
createdb career_counselling_db
python manage.py migrate
python manage.py collectstatic
```

#### 3. Web Server Configuration

**Nginx Configuration** (`/etc/nginx/sites-available/career-bot`):
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;
    
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    # Frontend
    location / {
        root /var/www/career-bot/dist;
        try_files $uri $uri/ /index.html;
    }
    
    # Backend API
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    # Static files
    location /static/ {
        alias /var/www/career-bot/static/;
    }
}
```

## 🐳 Docker Deployment

### 1. Dockerfile for Django Backend

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY Portal/career_counselling_portal/requirements.txt .
RUN pip install -r requirements.txt

COPY Portal/career_counselling_portal/ .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "career_counselling_portal.wsgi:application"]
```

### 2. Dockerfile for React Frontend

```dockerfile
FROM node:18-alpine AS builder

WORKDIR /app
COPY Portal/package*.json ./
RUN npm install

COPY Portal/ .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
```

### 3. Docker Compose

```yaml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: career_counselling_db
      POSTGRES_USER: career_user
      POSTGRES_PASSWORD: career_password
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: 
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://career_user:career_password@db:5432/career_counselling_db
    depends_on:
      - db

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile.streamlit
    ports:
      - "8501:8501"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}

volumes:
  postgres_data:
```

## ☁️ Cloud Platform Deployment

### Heroku Deployment

1. **Create Heroku apps**:
   ```bash
   heroku create career-bot-backend
   heroku create career-bot-frontend
   heroku create career-bot-ai
   ```

2. **Configure environment variables**:
   ```bash
   heroku config:set DJANGO_SECRET_KEY=your_secret_key -a career-bot-backend
   heroku config:set DATABASE_URL=postgresql://... -a career-bot-backend
   ```

3. **Deploy**:
   ```bash
   git subtree push --prefix=Portal/career_counselling_portal heroku main
   ```

### AWS Deployment

1. **EC2 Instance Setup**
2. **RDS for PostgreSQL**
3. **S3 for Static Files**
4. **CloudFront for CDN**
5. **Route 53 for DNS**

### Vercel (Frontend) + Railway (Backend)

1. **Vercel for React app**:
   - Connect GitHub repository
   - Set build command: `cd Portal && npm run build`
   - Set environment variables

2. **Railway for Django**:
   - Connect GitHub repository
   - Set start command: `cd Portal/career_counselling_portal && python manage.py migrate && gunicorn career_counselling_portal.wsgi:application`

## 🔒 Security Checklist

- [ ] Change all default secrets and passwords
- [ ] Enable HTTPS with SSL certificates
- [ ] Configure CORS properly
- [ ] Set up rate limiting
- [ ] Enable database backups
- [ ] Configure monitoring and logging
- [ ] Set up firewall rules
- [ ] Regular security updates

## 📊 Monitoring

### Health Checks
```bash
# Backend health check
curl https://api.yourdomain.com/health/

# Frontend availability
curl https://yourdomain.com/

# Database connection
python manage.py check --database
```

### Logging Configuration
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/career-bot/django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

## 🔄 CI/CD Pipeline

### GitHub Actions Example

```yaml
name: Deploy Career Bot

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Setup Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    - name: Install dependencies
      run: |
        cd Portal/career_counselling_portal
        pip install -r requirements.txt
    - name: Run tests
      run: |
        cd Portal/career_counselling_portal
        python manage.py test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to production
      run: |
        # Your deployment commands here
```

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Check DATABASE_URL format
   - Verify database server is running
   - Check firewall rules

2. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check STATIC_URL and STATIC_ROOT settings
   - Verify web server configuration

3. **CORS Issues**
   - Update CORS_ALLOWED_ORIGINS in settings
   - Check frontend API base URL

4. **Environment Variables**
   - Verify all required variables are set
   - Check for typos in variable names
   - Restart services after changes