

#### [Youtube Tutorial](https://www.youtube.com/watch?v=VSmhitrZ_0w&list=PL5E1F5cTSTtRSP3Qb8-gZ-Hm5AXp3VKvu&index=10)


#### [Django Starter](https://github.com/andyjud/django-starter/blob/main/requirements.txt)



## Setup

#### - Create Virtual Environment
###### # Mac
```
python3 -m venv venv
source venv/bin/activate
```

###### # Windows
```
python3 -m venv venv
.\venv\Scripts\activate.bat
```

<br>

#### - Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

<br>

#### - Migrate to database
```
python manage.py migrate
python manage.py createsuperuser
```

<br>

#### - Run application
```
python manage.py runserver
```

<br>

#### - Generate Secret Key ( ! Important for deployment ! )
```
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()
```

## Docker
**To deploy the project on Server**
```
sudo docker-compose -f docker/docker-compose-db.yml up -d
```

**Extra Commands**
```
sudo docker ps -a
sudo docker images
sudo docker volume ls
sudo docker network ls

sudo docker stop chatapp-backend chatapp-redis
sudo docker rm chatapp-backend chatapp-redis
sudo docker rmi img_chatapp-backend:latest # postgres:13
sudo docker network rm chatapp-network
sudo docker volume rm docker_chatapp-redis
```
