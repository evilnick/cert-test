source .sphinx/venv/bin/activate
make clean
python .sphinx/build_requirements.py
make html
sphinx-build -M latex "." "_build" -c . -d .sphinx/.doctrees
cd _build/latex
make
