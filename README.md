# airflow
Progetto FLC Galasso+Grieco per la realizzazione di un tool di Visual Scripting per progettare simulazioni IoD Sim e missioni.

## Clone
This project uses git submodules, so remember to clone it using the following command:
```
git clone --recurse-submodules ${REPOSITORY_URI}
```
Otherwise, you can init submodules at a later time:
```
git submodule init
```

## Python Setup
Use Python virtualenv to prepare your development environment:
```
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```
