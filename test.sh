
rm -rf ./htmlcov
# call python -m pytest instead of just pytest because this will add the pwd
# to sys.path
python -m pytest --cov-report html --cov=myutils --cov-branch tests
