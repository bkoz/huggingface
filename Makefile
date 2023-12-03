install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=cli --cov=mlib --cov=utilscli --cov=app test_mlib.py

format:
	black *.py

lint:
	pylint --disable=R,C,W1203,E1101 sentiment_analysis.py
	#lint Dockerfile
	#docker run --rm -i hadolint/hadolint < Dockerfile

build:
	#push to ECR for deploy
	docker build -t pyexample .
	docker tag pyexample:latest quay.io/bkozdemb/pyexample:latest
	docker login quay.io
	docker push quay.io/bkozdemb/pyexample:latest

all: install lint test format build
