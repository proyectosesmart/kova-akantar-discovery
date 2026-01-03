# Plan de Extracción de Datos - KOVA A Kantar

Este documento define el plan de trabajo para extraer conocimiento real desde
Confluence, Jira y Google Drive y estructurarlo en los documentos Markdown del repositorio.

## Objetivo

Alimentar todos los documentos `.md` del repositorio con conocimiento real extraído
desde las fuentes oficiales, estructurado por área operativa y validado por expertos.

## Fases del Plan

### Fase 1: Configuración y Autenticación
**Estado**: Pendiente

- [ ] Configurar credenciales para Confluence API
- [ ] Configurar credenciales para Jira API
- [ ] Configurar credenciales para Google Drive API
- [ ] Crear scripts de autenticación y prueba de conexión
- [ ] Documentar proceso de obtención de credenciales

**Entregables**:
- Script de autenticación funcional para cada API
- Documentación de configuración (`configuracion-apis.md`)
- Variables de entorno o archivo de configuración (`.env.example`)

---

### Fase 2: Inventario de Fuentes por Área
**Estado**: Pendiente

Para cada área operativa, identificar y catalogar:

#### 2.1 Confluence
- [ ] Listar espacios relevantes por área
- [ ] Identificar páginas clave por área
- [ ] Mapear jerarquía de páginas y relaciones
- [ ] Extraer metadatos (autor, fecha, etiquetas, comentarios)

#### 2.2 Jira
- [ ] Identificar proyectos Jira por área
- [ ] Definir filtros y etiquetas relevantes
- [ ] Mapear workflows y estados
- [ ] Extraer issues representativos (anonymizados)

#### 2.3 Google Drive
- [ ] Mapear estructura de carpetas por área
- [ ] Identificar documentos clave
- [ ] Extraer metadatos de archivos (tipo, tamaño, última modificación)
- [ ] Catalogar hojas de cálculo y formularios

**Áreas a mapear**:
1. ✅ RRHH (iniciado)
2. ⏳ Operación y Administración
3. ⏳ Legal y Privacidad
4. ⏳ Gobernanza y Portafolio
5. ⏳ Finanzas y Control
6. ⏳ Producto y TI
7. ⏳ Marketing y CRM

**Entregables**:
- Inventario completo de fuentes por área
- Mapeo de estructura de información actual

---

### Fase 3: Extracción Automatizada
**Estado**: Pendiente

#### 3.1 Scripts de Extracción
- [ ] Script para extraer páginas de Confluence por espacio/etiqueta
- [ ] Script para extraer issues de Jira por proyecto/filtro
- [ ] Script para listar y mapear estructura de Google Drive
- [ ] Script para extraer contenido de documentos Drive (texto, metadatos)

#### 3.2 Procesamiento de Contenido
- [ ] Parser de contenido Markdown desde Confluence
- [ ] Extracción de metadatos estructurados
- [ ] Detección de objetos de conocimiento (entidades, procesos)
- [ ] Anonimización de datos sensibles

**Entregables**:
- Scripts de extracción funcionales
- Pipeline de procesamiento de contenido
- Logs de extracción y trazabilidad

---

### Fase 4: Estructuración por Área
**Estado**: Pendiente

Para cada área, completar el documento de mapeo con:

1. **Fuentes analizadas**
   - Links directos a espacios Confluence
   - Links a proyectos/filtros Jira
   - Links a carpetas Drive

2. **Estructura actual de información**
   - Subcarpetas/secciones principales
   - Observaciones sobre orden, duplicidad, calidad

3. **Objetos de conocimiento identificados**
   - Lista de tipos (entidades) clave
   - Dónde vive cada tipo hoy
   - Nivel de estructuración actual

4. **Flujos operativos detectados**
   - Procesos principales soportados
   - Secuencia de pasos identificada

5. **Necesidades donde KOVA puede aportar**
   - Preguntas que KOVA debería poder responder
   - Acciones que KOVA podría orquestar

6. **Dolores y riesgos detectados**
   - Problemas de gobierno
   - Dispersión de información
   - Falta de trazabilidad

**Entregables**:
- Documentos de mapeo completos por área
- Referencias cruzadas entre áreas

---

### Fase 5: Síntesis y Requerimientos
**Estado**: Pendiente

- [ ] Consolidar hallazgos comunes entre áreas
- [ ] Derivar requerimientos específicos KOVA A Kantar
- [ ] Identificar capacidades genéricas para KOVA CORE
- [ ] Priorizar requerimientos por impacto y factibilidad

**Entregables**:
- `requerimientos-kova-akantar.md` completo
- `requerimientos-kova-core-derivados.md` completo

---

### Fase 6: Diseño de Arquitectura
**Estado**: Pendiente

- [ ] Mapear espacios Confluence al tenant KOVA A Kantar
- [ ] Definir proyectos Jira asociados
- [ ] Estructurar carpetas Drive relevantes
- [ ] Diseñar flujos priorizados por fases del roadmap

**Entregables**:
- `arquitectura-logica-tenant-akantar.md` completo

---

## Herramientas y Tecnologías

### APIs a Utilizar
- **Confluence**: REST API v2
- **Jira**: REST API v3
- **Google Drive**: Drive API v3

### Lenguaje de Scripts
- Python (recomendado por librerías disponibles)
- Alternativa: Node.js

### Librerías Sugeridas
- `atlassian-python-api` o `requests` para Confluence/Jira
- `google-api-python-client` para Drive
- `python-dotenv` para gestión de credenciales
- `markdown` para procesamiento de contenido

---

## Cronograma Estimado

| Fase | Duración Estimada | Dependencias |
|------|-------------------|--------------|
| Fase 1: Configuración | 1-2 días | - |
| Fase 2: Inventario | 3-5 días | Fase 1 |
| Fase 3: Extracción | 5-7 días | Fase 2 |
| Fase 4: Estructuración | 7-10 días | Fase 3 |
| Fase 5: Síntesis | 3-5 días | Fase 4 |
| Fase 6: Diseño | 2-3 días | Fase 5 |

**Total estimado**: 21-32 días hábiles

---

## Próximos Pasos Inmediatos

1. **Configurar autenticación** para las tres APIs
2. **Crear scripts de prueba** de conexión
3. **Identificar espacios Confluence clave** (empezar por ET - proyectos TI)
4. **Mapear estructura Drive** de RRHH (ya identificada parcialmente)
5. **Completar mapeo de RRHH** como caso piloto

---

## Notas Importantes

- **Anonimización**: Todos los datos personales deben ser anonimizados antes de incluirse en el repositorio
- **Validación humana**: Cada extracción debe ser revisada por expertos de área
- **Trazabilidad**: Mantener referencias a fuentes originales en cada documento
- **Versionado**: Los documentos generados deben versionarse para rastrear cambios

