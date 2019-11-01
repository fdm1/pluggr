BUILD_GIT_SHA=$(shell git log -n 1 --pretty=format:"%h")
NAME=fdm1-pluggr
TAG=${NAME}:application-python-flask-dummy-${BUILD_GIT_SHA}

build:
	docker build -t ${TAG} .

interactive: build
	docker run --rm -it -v $(shell pwd):/home -p 5090:5090 ${TAG} bash

build_test: build
	echo "TODO: build test dir on top of build dir to only install once. Use that for interactive"

test: build
	docker run --rm -it -v $(shell pwd):/home -w /home ${TAG} bash -c "pip install -r test-requirements.txt && pytest"

lint: build
	docker run --rm -it -v $(shell pwd):/app ${TAG} ./ci/lint.sh

