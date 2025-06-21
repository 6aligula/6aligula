# Cloud Run LLM Classifier

Este ejemplo muestra una aplicación sencilla en Python que se ejecuta en Google Cloud Run y utiliza un modelo pequeño de lenguaje (LLM) para clasificar una descripción dentro de una de las diez categorías del sector automoción.

## Despliegue rápido

1. Construir la imagen Docker:
   ```sh
   docker build -t gcr.io/PROJECT_ID/cloud-run-llm .
   ```
2. Publicar en Google Container Registry:
   ```sh
   docker push gcr.io/PROJECT_ID/cloud-run-llm
   ```
3. Desplegar en Cloud Run:
   ```sh
   gcloud run deploy cloud-run-llm \
     --image gcr.io/PROJECT_ID/cloud-run-llm \
     --platform managed \
     --region REGION \
     --allow-unauthenticated
   ```

La aplicación expone el endpoint `/classify` que recibe una descripción en formato JSON:

```json
{
  "description": "Necesito cambiar las pastillas de freno de mi coche"
}
```

y devuelve la categoría estimada:

```json
{
  "category": "Frenos"
}
```

## Pruebas locales

Se incluyen tests en `tests/` con conversaciones ficticias para comprobar que
el servicio clasifica correctamente. Para ejecutarlos:

```sh
pip install -r requirements.txt pytest
pytest
```
