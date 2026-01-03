# KOVA A Kantar – Discovery & Diseño

Este repositorio consolida el entendimiento operativo y de TI de A Kantar
para derivar requerimientos claros de KOVA A Kantar (tenant específico)
y de KOVA CORE (producto genérico Horeca).

## ¿Qué es KOVA?

**KOVA** es una plataforma multiagente diseñada para el sector Horeca que:
- Integra conocimiento estructurado desde Confluence, Jira y Google Drive
- Proporciona respuestas inteligentes basadas en el conocimiento organizacional
- Orquesta acciones y flujos de trabajo automatizados
- Separa estrictamente datos de cliente (tenant) de capacidades genéricas (CORE)

Este repositorio sirve como **fuente de conocimiento estructurado** que alimentará
los agentes de KOVA, permitiéndoles entender la realidad operativa de A Kantar
y responder preguntas, ejecutar tareas y generar insights de manera contextualizada.

## Objetivos

### Objetivos Principales
- **Mapear** qué existe hoy en Operación, Administración y TI para A Kantar
- **Extraer** conocimiento real desde Drive, Jira y Confluence mediante APIs
- **Estructurar** el conocimiento en documentos Markdown organizados por área
- **Destilar** requerimientos funcionales y técnicos para KOVA A Kantar y KOVA CORE
- **Servir** como base de conocimiento para la plataforma multiagente KOVA

### Objetivos Técnicos
- Conectar con APIs de Confluence, Jira y Google Drive
- Automatizar la generación de documentos Markdown desde fuentes oficiales
- Mantener trazabilidad entre conocimiento fuente y documentos generados
- Validar y enriquecer conocimiento con intervención humana (human-in-the-loop)

## Estructura del Repositorio

```
00-programa/              # Visión, alcance, governance del proyecto
01-contexto-negocio/      # Modelo de negocio y mapa de áreas
02-mapeo-operativo/       # Análisis detallado por área operativa
03-mapeo-ti/              # Proyectos y arquitectura de TI
04-sintesis-y-requerimientos/  # Hallazgos y requerimientos KOVA
05-diseno-kova-akantar/   # Diseño lógico del tenant A Kantar
99-plantillas-y-utilities/      # Plantillas y scripts de automatización
```

### Descripción de Carpetas

- **`00-programa/`**: Visión del proyecto, alcance, limitaciones y governance
- **`01-contexto-negocio/`**: Modelo de negocio A Kantar y mapa de áreas/responsabilidades
- **`02-mapeo-operativo/`**: Análisis profundo por área (Operaciones, RRHH, Legal, Finanzas, etc.)
- **`03-mapeo-ti/`**: Inventario de proyectos TI y arquitectura tecnológica
- **`04-sintesis-y-requerimientos/`**: Requerimientos específicos de KOVA A Kantar y genéricos de KOVA CORE
- **`05-diseno-kova-akantar/`**: Arquitectura lógica del tenant, espacios Confluence, proyectos Jira, estructura Drive
- **`99-plantillas-y-utilities/`**: Plantillas para mapeo de áreas y scripts para extracción automática

## Proceso de Alimentación de Conocimiento

### 1. Extracción desde Fuentes Oficiales
- **Confluence**: Páginas, espacios, comentarios y metadatos
- **Jira**: Proyectos, issues, workflows, filtros y etiquetas
- **Google Drive**: Estructura de carpetas, documentos, hojas de cálculo y metadatos

### 2. Estructuración por Área
Cada área operativa se mapea siguiendo la plantilla estándar:
- Fuentes analizadas (links a Drive, Confluence, Jira)
- Estructura actual de información
- Objetos de conocimiento identificados
- Flujos operativos detectados
- Necesidades donde KOVA puede aportar
- Dolores y riesgos detectados

### 3. Validación y Enriquecimiento
- Revisión humana de contenido extraído
- Anonimización de datos sensibles
- Validación con expertos de área
- Enriquecimiento con conocimiento tácito

## Configuración y Uso

### Prerrequisitos
- Acceso a APIs de Atlassian (Confluence, Jira)
- Acceso a Google Drive API
- Credenciales configuradas (ver `99-plantillas-y-utilities/`)

### Extracción de Datos
Ver documentación en `99-plantillas-y-utilities/` para scripts y guías de extracción.

## Principios de Gobierno

- **Separación estricta**: Datos de cliente (A Kantar) vs. KOVA CORE (genérico)
- **Human-in-the-loop**: Validación obligatoria antes de considerar conocimiento oficial
- **Trazabilidad**: Cada documento referencia sus fuentes originales

