```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
docker build -t django_api_image .
```
```bash
docker run -d --name django_api -p 8000:8000 django_api_image
```

