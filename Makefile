TEST_PATH=$(shell pwd)/example/tests/*.py

test:
	pytest ${TEST_PATH}

run:
	uvicorn main:app

run_dev:
	uvicorn main:app --reload
