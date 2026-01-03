# Mapeo de Extracción por Área

Este documento define qué información específica extraer de cada fuente (Confluence, Jira, Drive)
para cada área operativa de A Kantar.

## Estructura de Extracción

Para cada área, se debe extraer:

### Confluence
- Espacios relevantes
- Páginas clave (con contenido)
- Metadatos (autor, fecha, etiquetas)
- Comentarios y versiones
- Relaciones entre páginas

### Jira
- Proyectos asociados
- Issues representativos (anonymizados)
- Workflows y estados
- Filtros y etiquetas usadas
- Tipos de issues y campos personalizados

### Google Drive
- Estructura de carpetas
- Documentos clave (tipo, tamaño, última modificación)
- Hojas de cálculo y formularios
- Metadatos y permisos
- Relaciones entre documentos

---

## Área: RRHH

### Confluence
**Espacios a mapear**:
- [ ] Identificar espacios relacionados con RRHH
- [ ] Páginas sobre procesos de contratación
- [ ] Páginas sobre manuales de funciones
- [ ] Páginas sobre políticas de nómina

**Extraer**:
- Contenido de páginas clave
- Estructura jerárquica de páginas
- Etiquetas y categorías usadas

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos relacionados con RRHH
- [ ] Filtros por etiquetas: `rrhh`, `contratacion`, `nomina`
- [ ] Tipos de issues: solicitudes, procesos, tareas

**Extraer**:
- Ejemplos de issues (anonymizados)
- Workflow de procesos de RRHH
- Campos personalizados relevantes

### Google Drive
**Carpetas identificadas** (ya parcialmente mapeadas):
- ✅ Certificados Laborales
- ✅ Colaboradores
- ✅ Contratación
- ✅ Manuales de Funciones
- ✅ Nómina
- ✅ Preasesorías
- ✅ Revisar
- ✅ Sura - Asesorías y Plantillas
- ✅ Hoja de cálculo: "USUARIOS / CONTACTOS / PROVEEDORES"

**Extraer**:
- Estructura completa de subcarpetas
- Tipos de documentos en cada carpeta
- Frecuencia de actualización
- Tamaño y cantidad de archivos

---

## Área: Operación y Administración

### Confluence
**Espacios a mapear**:
- [ ] Espacios de procesos operativos
- [ ] Páginas sobre procedimientos operativos
- [ ] Páginas sobre gestión de restaurantes/establecimientos

**Extraer**:
- Procesos documentados
- Checklists y procedimientos
- Métricas y KPIs operativos

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos de operaciones
- [ ] Filtros por tipo de operación
- [ ] Issues relacionados con incidentes operativos

**Extraer**:
- Tipos de issues operativos
- SLA y tiempos de respuesta
- Categorización de problemas

### Google Drive
**Carpetas a mapear**:
- [ ] Carpeta de Operaciones
- [ ] Documentos de procedimientos
- [ ] Reportes y métricas
- [ ] Plantillas operativas

**Extraer**:
- Estructura de carpetas operativas
- Tipos de documentos más usados
- Frecuencia de actualización

---

## Área: Legal y Privacidad

### Confluence
**Espacios a mapear**:
- [ ] Espacios de Legal
- [ ] Páginas sobre políticas de privacidad
- [ ] Páginas sobre cumplimiento normativo
- [ ] Páginas sobre contratos y acuerdos

**Extraer**:
- Políticas documentadas
- Procesos de revisión legal
- Plantillas de documentos legales

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos de Legal
- [ ] Issues de revisión legal
- [ ] Issues de cumplimiento

**Extraer**:
- Workflow de aprobaciones legales
- Tipos de documentos legales gestionados

### Google Drive
**Carpetas a mapear**:
- [ ] Carpeta de Legal
- [ ] Contratos y acuerdos
- [ ] Políticas y procedimientos legales
- [ ] Documentos de cumplimiento

**Extraer**:
- Estructura de documentos legales
- Versiones y control de cambios
- Clasificación de documentos

---

## Área: Gobernanza y Portafolio

### Confluence
**Espacios a mapear**:
- [ ] Espacios de gobernanza
- [ ] Páginas sobre portafolio de proyectos
- [ ] Páginas sobre decisiones estratégicas
- [ ] Espacio ET (proyectos TI)

**Extraer**:
- Estructura de portafolio
- Procesos de decisión
- Roadmaps y planes estratégicos

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos de portafolio
- [ ] Epics y features estratégicas
- [ ] Filtros por iniciativa

**Extraer**:
- Estructura de portafolio en Jira
- Priorización y scoring
- Dependencias entre proyectos

### Google Drive
**Carpetas a mapear**:
- [ ] Carpeta de Gobernanza
- [ ] Documentos estratégicos
- [ ] Presentaciones ejecutivas
- [ ] Reportes de portafolio

**Extraer**:
- Documentos de planificación estratégica
- Métricas de portafolio
- Decisiones documentadas

---

## Área: Finanzas y Control

### Confluence
**Espacios a mapear**:
- [ ] Espacios de Finanzas
- [ ] Páginas sobre procesos financieros
- [ ] Páginas sobre presupuestos y reportes

**Extraer**:
- Procesos financieros documentados
- Estructura de reportes
- Ciclos de cierre

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos financieros
- [ ] Issues de aprobaciones presupuestarias
- [ ] Issues de reportes financieros

**Extraer**:
- Workflow de aprobaciones
- Tipos de transacciones gestionadas

### Google Drive
**Carpetas a mapear**:
- [ ] Carpeta de Finanzas
- [ ] Presupuestos
- [ ] Reportes financieros
- [ ] Facturas y comprobantes

**Extraer**:
- Estructura de información financiera
- Tipos de documentos financieros
- Frecuencia de reportes

---

## Área: Producto y TI

### Confluence
**Espacios a mapear**:
- [ ] Espacio ET (proyectos TI) - **PRIORITARIO**
- [ ] Páginas sobre arquitectura
- [ ] Páginas sobre productos y features
- [ ] Documentación técnica

**Extraer**:
- Inventario de proyectos TI (ver `03-mapeo-ti/inventario-proyectos-ti-actuales.md`)
- Arquitectura documentada
- Roadmap de productos

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos de desarrollo
- [ ] Proyectos de infraestructura
- [ ] Proyectos de producto
- [ ] Filtros por tecnología o stack

**Extraer**:
- Tipos de proyectos TI
- Estados y workflows técnicos
- Métricas de desarrollo

### Google Drive
**Carpetas a mapear**:
- [ ] Carpeta de TI
- [ ] Documentación técnica
- [ ] Diagramas y arquitectura
- [ ] Especificaciones de producto

**Extraer**:
- Estructura de documentación técnica
- Tipos de documentos técnicos
- Versionado de especificaciones

---

## Área: Marketing y CRM

### Confluence
**Espacios a mapear**:
- [ ] Espacios de Marketing
- [ ] Páginas sobre estrategias de marketing
- [ ] Páginas sobre CRM y clientes

**Extraer**:
- Procesos de marketing
- Estrategias documentadas
- Métricas de marketing

### Jira
**Proyectos/Filtros**:
- [ ] Proyectos de Marketing
- [ ] Issues de campañas
- [ ] Issues de contenido

**Extraer**:
- Tipos de iniciativas de marketing
- Workflow de aprobación de contenido

### Google Drive
**Carpetas a mapear**:
- [ ] Carpeta de Marketing
- [ ] Campañas y materiales
- [ ] Reportes de marketing
- [ ] Base de datos de clientes (estructura, no datos)

**Extraer**:
- Estructura de materiales de marketing
- Tipos de contenido generado
- Frecuencia de campañas

---

## Priorización de Extracción

### Fase 1 (Inmediata)
1. **RRHH** - Ya iniciado, completar
2. **Producto y TI** - Crítico para entender arquitectura

### Fase 2
3. **Operación y Administración** - Core del negocio
4. **Gobernanza y Portafolio** - Visión estratégica

### Fase 3
5. **Finanzas y Control** - Procesos de soporte
6. **Legal y Privacidad** - Cumplimiento
7. **Marketing y CRM** - Crecimiento

---

## Notas de Extracción

- **Anonimización**: Todos los datos personales deben ser anonimizados
- **Muestreo**: Para áreas con mucho contenido, extraer muestras representativas
- **Metadatos**: Priorizar metadatos que ayuden a entender estructura y uso
- **Relaciones**: Identificar y documentar relaciones entre objetos de conocimiento
- **Validación**: Cada extracción debe ser validada por expertos de área

