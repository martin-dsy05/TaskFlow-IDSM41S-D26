
#!/bin/bash
set -e

echo "Preparando entorno de TaskFlow..."

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Entorno preparado correctamente."
