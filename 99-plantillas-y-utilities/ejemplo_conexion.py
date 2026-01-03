#!/usr/bin/env python3
"""
Script de ejemplo para probar conexiones a Confluence, Jira y Google Drive.
Este script valida que las credenciales estén correctamente configuradas.
"""

import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_confluence():
    """Prueba conexión a Confluence"""
    try:
        from atlassian import Confluence
        
        url = os.getenv('CONFLUENCE_URL')
        username = os.getenv('CONFLUENCE_USERNAME')
        api_token = os.getenv('CONFLUENCE_API_TOKEN')
        
        if not all([url, username, api_token]):
            print("❌ Confluence: Variables de entorno no configuradas")
            return False
        
        confluence = Confluence(
            url=url,
            username=username,
            password=api_token  # En versiones recientes, el token se pasa como password
        )
        
        # Intentar obtener espacios
        spaces = confluence.get_all_spaces(start=0, limit=5)
        print("✅ Confluence: Conexión exitosa")
        print(f"   URL: {url}")
        print(f"   Espacios encontrados: {len(spaces.get('results', []))}")
        
        # Mostrar algunos espacios
        if spaces.get('results'):
            print("   Primeros espacios:")
            for space in spaces['results'][:3]:
                print(f"     - {space.get('key')}: {space.get('name')}")
        
        return True
        
    except ImportError:
        print("❌ Confluence: Librería 'atlassian-python-api' no instalada")
        print("   Ejecuta: pip install atlassian-python-api")
        return False
    except Exception as e:
        print(f"❌ Confluence: Error - {type(e).__name__}: {e}")
        return False


def test_jira():
    """Prueba conexión a Jira"""
    try:
        from atlassian import Jira
        
        url = os.getenv('JIRA_URL')
        username = os.getenv('JIRA_USERNAME')
        api_token = os.getenv('JIRA_API_TOKEN')
        
        if not all([url, username, api_token]):
            print("❌ Jira: Variables de entorno no configuradas")
            return False
        
        jira = Jira(
            url=url,
            username=username,
            password=api_token  # En versiones recientes, el token se pasa como password
        )
        
        # Intentar obtener proyectos
        projects = jira.projects()
        print("✅ Jira: Conexión exitosa")
        print(f"   URL: {url}")
        print(f"   Proyectos encontrados: {len(projects)}")
        
        # Mostrar algunos proyectos
        if projects:
            print("   Primeros proyectos:")
            for project in projects[:3]:
                print(f"     - {project.get('key')}: {project.get('name')}")
        
        return True
        
    except ImportError:
        print("❌ Jira: Librería 'atlassian-python-api' no instalada")
        print("   Ejecuta: pip install atlassian-python-api")
        return False
    except Exception as e:
        print(f"❌ Jira: Error - {type(e).__name__}: {e}")
        return False


def test_google_drive():
    """Prueba conexión a Google Drive"""
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        import os.path
        
        credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')
        if not credentials_path:
            print("❌ Google Drive: GOOGLE_CREDENTIALS_PATH no configurado")
            return False
        
        if not os.path.exists(credentials_path):
            print(f"❌ Google Drive: Archivo de credenciales no encontrado: {credentials_path}")
            return False
        
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
        
        creds = None
        token_path = 'token.json'
        
        # Cargar token existente si existe
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
        # Si no hay credenciales válidas, hacer flujo OAuth
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                from google.auth.transport.requests import Request
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Guardar credenciales para próximas ejecuciones
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
        
        # Construir servicio
        service = build('drive', 'v3', credentials=creds)
        
        # Intentar listar archivos
        results = service.files().list(pageSize=5, fields="files(id, name)").execute()
        files = results.get('files', [])
        
        print("✅ Google Drive: Conexión exitosa")
        print(f"   Archivos encontrados: {len(files)}")
        
        if files:
            print("   Primeros archivos:")
            for file in files[:3]:
                print(f"     - {file.get('name')}")
        
        return True
        
    except ImportError as e:
        print("❌ Google Drive: Librerías no instaladas")
        print("   Ejecuta: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")
        return False
    except Exception as e:
        print(f"❌ Google Drive: Error - {type(e).__name__}: {e}")
        return False


def main():
    """Función principal"""
    print("=" * 60)
    print("Prueba de Conexiones - KOVA A Kantar Discovery")
    print("=" * 60)
    print()
    
    results = {
        'Confluence': test_confluence(),
        'Jira': test_jira(),
        'Google Drive': test_google_drive()
    }
    
    print()
    print("=" * 60)
    print("Resumen:")
    print("=" * 60)
    
    for service, success in results.items():
        status = "✅ OK" if success else "❌ FALLO"
        print(f"{service}: {status}")
    
    all_ok = all(results.values())
    
    if all_ok:
        print("\n🎉 Todas las conexiones funcionan correctamente!")
        return 0
    else:
        print("\n⚠️  Algunas conexiones fallaron. Revisa la configuración.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

