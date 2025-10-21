# T02: ANÁLISIS DE REQUISITOS - SISTEMA INFORMACIÓN USUARIOS
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Sistema de Información a Usuarios  
**Responsable:** Ingeniero de Sistemas ITS  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para el Sistema de Información a Usuarios del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y mejores prácticas de comunicación con usuarios viales.

### 1.2 Alcance
Análisis completo de requisitos para sistema integral de información que incluye emisora de radio, redes sociales, aplicación móvil y coordinación con paneles LED para 272.1 km del corredor.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **ITS** | Intelligent Transportation Systems |
| **API** | Application Programming Interface |
| **CMS** | Content Management System |
| **SLA** | Service Level Agreement |
| **GPS** | Global Positioning System |
| **TMC** | Traffic Message Channel |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Emisora de Radio Especializada

**ID:** RF-001  
**Descripción:** Operar emisora de radio dedicada para información de tráfico y servicios del corredor  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.2.4  

**Criterios de Aceptación:**
- Cobertura 100% del corredor 272.1 km
- Transmisión 24/7/365
- Información tráfico cada 15 minutos
- Coordinación con CCO en tiempo real
- Contenido en español e inglés

### 2.2 Aplicación Móvil Usuarios

**ID:** RF-002  
**Descripción:** Desarrollar aplicación móvil para información en tiempo real a usuarios del corredor  
**Prioridad:** Alta  
**Fuente:** AT2, Mejores prácticas ITS  

**Criterios de Aceptación:**
- Disponible iOS y Android
- Información tráfico tiempo real
- Cálculo rutas alternativas
- Notificaciones push emergencias
- Integración GPS y mapas#
## 2.3 Plataforma Redes Sociales

**ID:** RF-003  
**Descripción:** Gestionar presencia en redes sociales para comunicación masiva con usuarios  
**Prioridad:** Media  
**Fuente:** Mejores prácticas comunicación  

**Criterios de Aceptación:**
- Presencia en Facebook, Twitter, Instagram
- Publicaciones automáticas incidentes
- Respuesta consultas < 2 horas
- Contenido multimedia (fotos, videos)
- Coordinación con CCO para información

### 2.4 Portal Web Informativo

**ID:** RF-004  
**Descripción:** Mantener portal web con información completa del corredor y servicios  
**Prioridad:** Media  
**Fuente:** AT2, Información usuarios  

**Criterios de Aceptación:**
- Información tarifas actualizada
- Mapa interactivo servicios
- Reportes estado vial
- Sección noticias y comunicados
- Accesibilidad web (WCAG 2.1)

### 2.5 Integración con Paneles LED

**ID:** RF-005  
**Descripción:** Coordinar mensajes entre diferentes medios de comunicación  
**Prioridad:** Alta  
**Fuente:** AT2, Integración sistemas  

**Criterios de Aceptación:**
- Sincronización mensajes radio-paneles
- Consistencia información todos los medios
- Actualización simultánea incidentes
- Control centralizado desde CCO
- Priorización mensajes críticos

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad emisora radio | 99% | AT4 |
| **RNF-002** | Disponibilidad aplicación móvil | 95% | SLA estándar |
| **RNF-003** | Disponibilidad portal web | 99% | SLA estándar |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Tiempo actualización información | < 5 minutos | Mejores prácticas |
| **RNF-005** | Tiempo carga aplicación móvil | < 3 segundos | Estándar UX |
| **RNF-006** | Usuarios concurrentes app | 10,000 usuarios | Estimación tráfico |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Cifrado datos usuarios | TLS 1.3 mínimo | Estándar seguridad |
| **RNF-008** | Autenticación administradores | 2FA obligatorio | Mejores prácticas |
| **RNF-009** | Backup contenido | Diario, retención 30 días | Continuidad negocio |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Interface intuitiva | Uso sin capacitación | Estándar UX |
| **RNF-011** | Accesibilidad | Cumplir WCAG 2.1 AA | Legal |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Actualización contenido | CMS fácil uso | Operacional |
| **RNF-013** | Monitoreo automático | Alertas fallas sistema | Mejores prácticas |
| **RNF-014** | Escalabilidad horizontal | Crecimiento sin rediseño | Arquitectura |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con CCO

**ID:** RI-001  
**Sistemas:** Sistema Información ↔ CCO  
**Tipo:** Red de Datos  
**Protocolo:** API REST sobre HTTPS  
**Datos Intercambiados:** Incidentes, estado tráfico, emergencias  
**Frecuencia:** Tiempo real

### 4.2 Interface con Paneles LED

**ID:** RI-002  
**Sistemas:** Sistema Información ↔ Paneles LED  
**Tipo:** Red de Datos  
**Protocolo:** NTCIP 1203  
**Datos Intercambiados:** Mensajes coordinados  
**Frecuencia:** Por evento

### 4.3 Interface con Estaciones de Peaje

**ID:** RI-003  
**Sistemas:** Sistema Información ↔ Estaciones Peaje  
**Tipo:** Red de Datos  
**Protocolo:** API REST  
**Datos Intercambiados:** Tarifas, colas, estado operativo  
**Frecuencia:** Cada 5 minutos

### 4.4 Interface con Servicios Externos

**ID:** RI-004  
**Sistemas:** Sistema Información ↔ Redes Sociales  
**Tipo:** Internet  
**Protocolo:** APIs redes sociales  
**Datos Intercambiados:** Publicaciones, respuestas  
**Frecuencia:** Por evento

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Emisora radio | AT2, 3.3.3.2.4 | Estación radio | Alta |
| RF-002 | Funcional | Aplicación móvil | Mejores prácticas | App móvil | Alta |
| RF-003 | Funcional | Redes sociales | Mejores prácticas | Plataforma social | Media |
| RF-004 | Funcional | Portal web | AT2 | Sitio web | Media |
| RF-005 | Funcional | Integración paneles | AT2 | Sistema integración | Alta |
| RNF-001 | No Funcional | Disponibilidad 99% | AT4 | Infraestructura | Alta |
| RNF-004 | No Funcional | Actualización < 5 min | Mejores prácticas | Sistema completo | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Licencia radiodifusión requerida | Trámites regulatorios | MinTIC |
| **REST-002** | Contenido en español obligatorio | Idioma principal | Legal |
| **REST-003** | Cumplimiento ley protección datos | Manejo información usuarios | Legal |
| **REST-004** | Coordinación con autoridades | Información oficial | Contractual |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Licencia radio aprobada | Alto (no hay emisora) | Trámite MinTIC |
| **SUP-002** | Cobertura celular adecuada | Medio (app limitada) | Estudio cobertura |
| **SUP-003** | Personal comunicaciones disponible | Medio (operación limitada) | Plan contratación |
| **SUP-004** | Integración sistemas exitosa | Alto (información fragmentada) | Pruebas integración |

---

## 7. CASOS DE USO

### 7.1 Difusión Información Incidente

**ID:** CU-001  
**Actor:** Operador CCO  
**Descripción:** Difundir información de incidente por todos los medios  
**Precondiciones:** Incidente confirmado, sistemas operativos  
**Flujo Normal:**
1. CCO confirma incidente en corredor
2. Operador crea mensaje informativo
3. Sistema envía a emisora radio automáticamente
4. Actualiza paneles LED en zona afectada
5. Publica en redes sociales
6. Envía notificación push a app móvil
7. Actualiza portal web

**Postcondiciones:** Información difundida por todos los canales  
**Flujos Alternativos:** Si falla un canal, continúa con otros disponibles

### 7.2 Consulta Usuario App Móvil

**ID:** CU-002  
**Actor:** Usuario Vial  
**Descripción:** Usuario consulta estado del corredor desde app móvil  
**Precondiciones:** App instalada, conexión internet  
**Flujo Normal:**
1. Usuario abre aplicación móvil
2. App obtiene ubicación GPS
3. Consulta estado tráfico tiempo real
4. Muestra información relevante zona
5. Ofrece rutas alternativas si hay incidentes
6. Usuario selecciona ruta preferida
7. App inicia navegación

**Postcondiciones:** Usuario informado y navegando  
**Flujos Alternativos:** Si no hay GPS, permite búsqueda manual

### 7.3 Actualización Tarifas Peaje

**ID:** CU-003  
**Actor:** Sistema Automático  
**Descripción:** Actualizar información tarifas en todos los medios  
**Precondiciones:** Cambio tarifas autorizado  
**Flujo Normal:**
1. Sistema recibe actualización tarifas
2. Valida información con estaciones peaje
3. Actualiza base de datos central
4. Modifica portal web automáticamente
5. Programa anuncio en emisora radio
6. Actualiza información en app móvil
7. Publica comunicado redes sociales

**Postcondiciones:** Tarifas actualizadas en todos los medios  
**Flujos Alternativos:** Si hay inconsistencias, genera alerta

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Emisora radio operativa con cobertura 100% corredor
- [ ] Aplicación móvil disponible iOS y Android
- [ ] Portal web con toda la información actualizada
- [ ] Integración exitosa con paneles LED
- [ ] Presencia activa en redes sociales principales

### 8.2 Criterios de Performance

- [ ] Disponibilidad emisora ≥ 99%
- [ ] Tiempo actualización información < 5 minutos
- [ ] App móvil soporta 10,000 usuarios concurrentes
- [ ] Portal web carga en < 3 segundos

### 8.3 Criterios de Calidad

- [ ] Cumplimiento WCAG 2.1 AA para accesibilidad
- [ ] Licencia radiodifusión aprobada MinTIC
- [ ] Cifrado TLS 1.3 para seguridad datos
- [ ] Backup diario de todo el contenido

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Licencia Radiodifusión** | Requerida para emisora | Alta | ⏳ Pendiente |
| **CCO Operativo** | Para integración información | Alta | ⏳ Pendiente |
| **Paneles LED** | Para coordinación mensajes | Media | ⏳ Pendiente |
| **Personal Comunicaciones** | Para operación diaria | Media | ⏳ Pendiente |
| **Infraestructura IT** | Para hosting aplicaciones | Alta | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Iniciar trámite licencia radiodifusión MinTIC
- [ ] Validar requisitos con equipo comunicaciones
- [ ] Diseñar arquitectura aplicación móvil
- [ ] Elaborar especificaciones técnicas desarrollo (T04)
- [ ] Definir estrategia contenidos y comunicación

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Sistemas ITS | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas ITS