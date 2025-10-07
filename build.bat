pushd %~dp0
python setup.py sdist
pip install dist/cdebug-0.0.1.tar.gz
pause
