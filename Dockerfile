
FROM python:3.6-slim

MAINTAINER huangjie <huangjie@hua-cloud.com.cn>

ENV TZ=Asia/Shanghai

ADD src /code

WORKDIR /code

RUN pip install -r dependencies.config -i https://pypi.tuna.tsinghua.edu.cn/simple  --default-timeout=1000

CMD ["python","/code/helloworld_grpc_server.py"]