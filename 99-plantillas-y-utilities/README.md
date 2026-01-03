# Plantillas y Utilidades - KOVA A Kantar Discovery

Esta carpeta contiene plantillas, scripts y documentación para la extracción
y procesamiento de datos desde Confluence, Jira y Google Drive.

## Contenido

### Documentación
- **`plan-extraccion-datos.md`**: Plan de trabajo completo para extracción de datos
- **`configuracion-apis.md`**: Guía de configuración de APIs y autenticación
- **`mapeo-extraccion-por-area.md`**: Qué extraer de cada fuente por área operativa
- **`plantilla-mapeo-area.md`**: Plantilla para documentar mapeo de cada área

### Scripts
- **`ejemplo_conexion.py`**: Script para probar conexiones a las tres APIs
- **`requirements.txt`**: Dependencias Python necesarias

## Inicio Rápido

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar Credenciales

Crear archivo `.env` en la raíz del proyecto con:

```bash
# Confluence
CONFLUENCE_URL=https://tu-empresa.atlassian.net
CONFLUENCE_USERNAME=tu-email@empresa.com
CONFLUENCE_API_TOKEN=tu-token-api

# Jira
JIRA_URL=https://tu-empresa.atlassian.net
JIRA_USERNAME=tu-email@empresa.com
JIRA_API_TOKEN=tu-token-api

# Google Drive
GOOGLE_CREDENTIALS_PATH=./credentials/google-credentials.json
```

### 3. Probar Conexiones

```bash
python 99-plantillas-y-utilities/ejemplo_conexion.py
```

## Próximos Pasos

1. **Configurar APIs**: Seguir guía en `configuracion-apis.md`
2. **Revisar plan**: Leer `plan-extraccion-datos.md` para entender el proceso completo
3. **Identificar fuentes**: Usar `mapeo-extraccion-por-area.md` para saber qué extraer
4. **Comenzar extracción**: Empezar por RRHH (ya parcialmente mapeado) o Producto y TI

## Estructura de Scripts Futuros

Los scripts de extracción se organizarán así:

```
99-plantillas-y-utilities/
├── extractors/
│   ├── confluence_extractor.py
│   ├── jira_extractor.py
│   └── drive_extractor.py
├── processors/
│   ├── content_processor.py
│   └── anonymizer.py
└── generators/
    └── markdown_generator.py
```

## Notas Importantes

- **Seguridad**: Nunca commitear credenciales. Usar `.env` y `.gitignore`
- **Anonimización**: Todos los datos personales deben ser anonimizados
- **Validación**: Todo contenido extraído debe ser validado por expertos
- **Trazabilidad**: Mantener referencias a fuentes originales

