# epi-py
Elements of Programming Interviews in Python

## New Python Project Setup

### 1. Check you have Python 3.7 installed and available
```shell
python3.7 --version
pip3 --version
```

*If you do not have python3.7 then look for Python installer for your OS*

### 2. Clone project
```shell
git https://github.com/andrewboss/epi-py.git
cd epi-py
```

### 3. Install virtualenv python module
```shell
pip3 install --user virtualenv
```

### 4. Create virtual python environment
```shell
python3.7 -m virtualenv venv
```

### 5. Activate virtual environment
```shell
source venv/bin/activate
```

### 6. Install project modules
```shell
pip install --upgrade -r requirements.txt
```

### 7. Run unit tests:
Main integration test Prover with Verifier:
```shell
python -m unittest -v tests/test_h_index.py
```
or all tests:
```shell
python -m unittest discover tests
```

