install:
	pip install -r requirements.txt

dev:
	uvicorn app:app --reload
