
#!/bin/bash
set -e

echo "Generando paquete de TaskFlow..."

mkdir -p dist

tar -czf dist/taskflow.tar.gz \
  main.py tasks.py storage.py utils.py \
  requirements.txt scripts/preparar_entorno.sh

echo "Paquete generado: dist/taskflow.tar.gz"
