# Configuración de APIs - Confluence, Jira y Google Drive

Esta guía explica cómo configurar las credenciales y autenticación para conectar
con las APIs de Confluence, Jira y Google Drive.

## Prerrequisitos

- Python 3.8+ instalado
- Acceso a las instancias de Atlassian (Confluence/Jira)
- Acceso a Google Workspace con permisos para Drive API
- Permisos de administrador o usuario con acceso a APIs

---

## 1. Confluence API

### Opción A: API Token (Recomendado)

1. Ir a: `https://id.atlassian.com/manage-profile/security/api-tokens`
2. Crear un nuevo token API
3. Copiar el token generado

### Opción B: OAuth 2.0

Para aplicaciones más complejas, usar OAuth 2.0.

### Configuración

```python
# Ejemplo de configuración
CONFLUENCE_URL = "https://tu-empresa.atlassian.net"
CONFLUENCE_USERNAME = "tu-email@empresa.com"
CONFLUENCE_API_TOKEN = "tu-api-token"
```

### Librería Recomendada

```bash
pip install atlassian-python-api
```

### Ejemplo de Uso

```python
from atlassian import Confluence

confluence = Confluence(
    url=CONFLUENCE_URL,
    username=CONFLUENCE_USERNAME,
    api_token=CONFLUENCE_API_TOKEN
)

# Obtener espacios
spaces = confluence.get_all_spaces()
```

---

## 2. Jira API

### API Token (Mismo proceso que Confluence)

1. Usar el mismo token API de Atlassian creado para Confluence
2. O crear uno específico para Jira

### Configuración

```python
JIRA_URL = "https://tu-empresa.atlassian.net"
JIRA_USERNAME = "tu-email@empresa.com"
JIRA_API_TOKEN = "tu-api-token"
```

### Librería Recomendada

```bash
pip install jira
# o
pip install atlassian-python-api  # Incluye Jira también
```

### Ejemplo de Uso

```python
from atlassian import Jira

jira = Jira(
    url=JIRA_URL,
    username=JIRA_USERNAME,
    api_token=JIRA_API_TOKEN
)

# Obtener proyectos
projects = jira.projects()
```

---

## 3. Google Drive API

### Configuración OAuth 2.0

1. Ir a [Google Cloud Console](https://console.cloud.google.com/)
2. Crear un nuevo proyecto o seleccionar uno existente
3. Habilitar Google Drive API
4. Crear credenciales OAuth 2.0:
   - Tipo: "Aplicación de escritorio" o "Aplicación web"
   - Descargar archivo JSON de credenciales
5. Configurar pantalla de consentimiento OAuth (si es necesario)

### Configuración

```python
# Ruta al archivo de credenciales descargado
GOOGLE_CREDENTIALS_PATH = "path/to/credentials.json"
GOOGLE_SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.metadata.readonly'
]
```

### Librería Recomendada

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Ejemplo de Uso

```python
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def get_drive_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('drive', 'v3', credentials=creds)

service = get_drive_service()
```

---

## Gestión de Credenciales

### Usar Variables de Entorno (Recomendado)

Crear archivo `.env`:

```bash
# .env
CONFLUENCE_URL=https://tu-empresa.atlassian.net
CONFLUENCE_USERNAME=tu-email@empresa.com
CONFLUENCE_API_TOKEN=tu-token-aqui

JIRA_URL=https://tu-empresa.atlassian.net
JIRA_USERNAME=tu-email@empresa.com
JIRA_API_TOKEN=tu-token-aqui

GOOGLE_CREDENTIALS_PATH=./credentials/google-credentials.json
```

### Cargar Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

CONFLUENCE_URL = os.getenv('CONFLUENCE_URL')
CONFLUENCE_USERNAME = os.getenv('CONFLUENCE_USERNAME')
CONFLUENCE_API_TOKEN = os.getenv('CONFLUENCE_API_TOKEN')
```

### Archivo .gitignore

Asegurarse de que `.gitignore` incluya:

```
.env
*.json
credentials/
token.json
__pycache__/
*.pyc
```

---

## Script de Prueba de Conexión

Crear `test_connections.py`:

```python
#!/usr/bin/env python3
"""Script para probar conexiones a las APIs"""

from dotenv import load_dotenv
import os
from atlassian import Confluence, Jira

load_dotenv()

def test_confluence():
    try:
        confluence = Confluence(
            url=os.getenv('CONFLUENCE_URL'),
            username=os.getenv('CONFLUENCE_USERNAME'),
            api_token=os.getenv('CONFLUENCE_API_TOKEN')
        )
        spaces = confluence.get_all_spaces(start=0, limit=5)
        print("✅ Confluence: Conexión exitosa")
        print(f"   Espacios encontrados: {len(spaces.get('results', []))}")
        return True
    except Exception as e:
        print(f"❌ Confluence: Error - {e}")
        return False

def test_jira():
    try:
        jira = Jira(
            url=os.getenv('JIRA_URL'),
            username=os.getenv('JIRA_USERNAME'),
            api_token=os.getenv('JIRA_API_TOKEN')
        )
        projects = jira.projects()
        print("✅ Jira: Conexión exitosa")
        print(f"   Proyectos encontrados: {len(projects)}")
        return True
    except Exception as e:
        print(f"❌ Jira: Error - {e}")
        return False

if __name__ == "__main__":
    print("Probando conexiones a APIs...\n")
    test_confluence()
    test_jira()
    # Agregar test de Google Drive cuando esté configurado
```

---

## Permisos Necesarios

### Confluence
- Permiso de lectura en espacios relevantes
- Permiso para acceder a API

### Jira
- Permiso de lectura en proyectos relevantes
- Permiso para acceder a API

### Google Drive
- Permiso de lectura en carpetas compartidas
- Scope: `drive.readonly` o `drive.metadata.readonly`

---

## Troubleshooting

### Error 401 (No autorizado)
- Verificar que el token API sea correcto
- Verificar que el usuario tenga permisos necesarios

### Error 403 (Prohibido)
- Verificar permisos en espacios/proyectos/carpetas
- Verificar que la API esté habilitada

### Error de rate limiting
- Implementar retry con backoff exponencial
- Reducir frecuencia de requests

---

## Seguridad

- **NUNCA** commitear credenciales al repositorio
- Usar variables de entorno o archivos de configuración ignorados
- Rotar tokens periódicamente
- Usar permisos mínimos necesarios (principio de menor privilegio)

