FROM        eb_ubuntu
MAINTAINER  hyeongjin184@gmail.com

# 현재 경로의 모든 파일들을 컨테이너의 /srv/study_foolog 폴더에 복사
COPY        . /srv/eb_docker_study

# cd /srv/study_foolog 와 같은 효과
WORKDIR     /srv/eb_docker_study

# requirements 설치
RUN         /root/.pyenv/versions/eb_docker_study/bin/pip install -r .requirements/deploy.txt

# supervisor 파일 복사
COPY        .config/supervisor/uwsgi.conf /etc/supervisor/conf.d/
COPY        .config/supervisor/nginx.conf /etc/supervisor/conf.d/

# nginx파일 복사
COPY        .config/nginx/nginx.conf /etc/nginx/nginx.conf
COPY        .config/nginx/nginx-app.conf /etc/nginx/sites-available/nginx-app.conf
RUN         rm -rf /etc/nginx/sites-enabled/default
RUN         ln -sf /etc/nginx/sites-available/nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf

## collectstatic 실행
RUN         /root/.pyenv/versions/study_foolog/bin/python /srv/study_foolog/django_app/manage.py collectstatic --settings=config.settings.deploy --noinput

CMD         supervisord -n
EXPOSE      80 8000