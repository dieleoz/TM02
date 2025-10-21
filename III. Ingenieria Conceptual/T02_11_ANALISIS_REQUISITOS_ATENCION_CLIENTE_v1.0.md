# T02: ANÁLISIS DE REQUISITOS - ATENCIÓN AL CLIENTE
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Atención al Cliente  
**Responsable:** Ingeniero Industrial - Servicio al Cliente  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para el Sistema de Atención al Cliente del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y mejores prácticas de servicio al usuario.

### 1.2 Alcance
Análisis completo de requisitos para sistema integral de atención al cliente que incluye call center, atención presencial, canales digitales y gestión de PQRS para usuarios del corredor de 272.1 km.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **PQRS** | Peticiones, Quejas, Reclamos y Sugerencias |
| **CRM** | Customer Relationship Management |
| **SLA** | Service Level Agreement |
| **IVR** | Interactive Voice Response |
| **ANS** | Acuerdo de Nivel de Servicio |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Call Center Especializado

**ID:** RF-001  
**Descripción:** Operar call center 24/7 para atención telefónica de usuarios del corredor  
**Prioridad:** Alta  
**Fuente:** AT2, Atención usuarios  

**Criterios de Aceptación:**
- Operación 24 horas, 7 días semana
- Tiempo respuesta < 30 segundos
- Atención en español e inglés
- Sistema IVR para clasificación llamadas
- Grabación de todas las llamadas#
## 2.2 Gestión de PQRS

**ID:** RF-002  
**Descripción:** Sistema completo para gestión de Peticiones, Quejas, Reclamos y Sugerencias  
**Prioridad:** Alta  
**Fuente:** Ley 1755/2015, AT2  

**Criterios de Aceptación:**
- Recepción por múltiples canales
- Asignación automática según tipo
- Seguimiento con número único
- Respuesta en tiempos legales
- Reportes estadísticos automáticos

### 2.3 Atención Presencial

**ID:** RF-003  
**Descripción:** Puntos de atención presencial en ubicaciones estratégicas  
**Prioridad:** Media  
**Fuente:** AT2, Servicio usuarios  

**Criterios de Aceptación:**
- Oficinas en estaciones de peaje principales
- Horario comercial extendido
- Personal bilingüe capacitado
- Sistema de turnos y citas
- Accesibilidad para discapacitados

### 2.4 Canales Digitales

**ID:** RF-004  
**Descripción:** Plataformas digitales para autoservicio y atención virtual  
**Prioridad:** Media  
**Fuente:** Transformación digital  

**Criterios de Aceptación:**
- Portal web con autoservicio
- Chat en línea con agentes
- Aplicación móvil integrada
- Redes sociales monitoreadas
- Chatbot para consultas básicas

### 2.5 Sistema CRM Integrado

**ID:** RF-005  
**Descripción:** Plataforma CRM para gestión integral de relación con clientes  
**Prioridad:** Alta  
**Fuente:** Mejores prácticas servicio  

**Criterios de Aceptación:**
- Base datos única de usuarios
- Historial completo interacciones
- Segmentación de clientes
- Campañas de comunicación
- Indicadores de satisfacción

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad call center | 99.5% | SLA estándar |
| **RNF-002** | Disponibilidad portal web | 99% | SLA estándar |
| **RNF-003** | Tiempo respuesta llamadas | < 30 segundos | Estándar industria |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Capacidad llamadas concurrentes | 50 llamadas | Estimación demanda |
| **RNF-005** | Tiempo resolución PQRS | Según Ley 1755 | Legal |
| **RNF-006** | Nivel satisfacción cliente | > 85% | Objetivo calidad |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Protección datos personales | Cumplir Ley 1581/2012 | Legal |
| **RNF-008** | Grabaciones seguras | Cifrado y backup | Regulatorio |
| **RNF-009** | Acceso controlado CRM | Roles y permisos | Seguridad |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Interface intuitiva | Uso sin capacitación | UX estándar |
| **RNF-011** | Accesibilidad web | WCAG 2.1 AA | Legal |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Actualización contenido | CMS fácil uso | Operacional |
| **RNF-013** | Backup datos | Diario automático | Continuidad |
| **RNF-014** | Monitoreo automático | Alertas proactivas | Operacional |

### 3.6 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Crecimiento agentes | +50% sin rediseño | Escalabilidad |
| **RNF-016** | Volumen llamadas | +100% capacidad | Crecimiento |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con Sistema Peajes

**ID:** RI-001  
**Sistemas:** Atención Cliente ↔ Estaciones Peaje  
**Tipo:** Red de Datos  
**Protocolo:** API REST  
**Datos Intercambiados:** Transacciones, reclamos, tarifas  
**Frecuencia:** Tiempo real

### 4.2 Interface con CCO

**ID:** RI-002  
**Sistemas:** Atención Cliente ↔ CCO  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP  
**Datos Intercambiados:** Incidentes, estado vía, emergencias  
**Frecuencia:** Tiempo real

### 4.3 Interface con Sistema Información

**ID:** RI-003  
**Sistemas:** Atención Cliente ↔ Info Usuarios  
**Tipo:** Red de Datos  
**Protocolo:** API REST  
**Datos Intercambiados:** Consultas, información actualizada  
**Frecuencia:** Por consulta

### 4.4 Interface con Sistemas Externos

**ID:** RI-004  
**Sistemas:** Atención Cliente ↔ Bancos/Entidades  
**Tipo:** Internet  
**Protocolo:** APIs seguras  
**Datos Intercambiados:** Validaciones, pagos, consultas  
**Frecuencia:** Por transacción

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Call center 24/7 | AT2 | Centro llamadas | Alta |
| RF-002 | Funcional | Gestión PQRS | Ley 1755/2015 | Sistema PQRS | Alta |
| RF-003 | Funcional | Atención presencial | AT2 | Oficinas | Media |
| RF-004 | Funcional | Canales digitales | Transformación digital | Plataformas web | Media |
| RF-005 | Funcional | Sistema CRM | Mejores prácticas | CRM | Alta |
| RNF-001 | No Funcional | Disponibilidad 99.5% | SLA | Infraestructura | Alta |
| RNF-005 | No Funcional | Tiempos Ley 1755 | Legal | Procesos | Alta |
| RNF-007 | No Funcional | Protección datos | Ley 1581/2012 | Seguridad | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Cumplimiento Ley 1755/2015 | Tiempos respuesta fijos | Legal |
| **REST-002** | Protección datos Ley 1581/2012 | Manejo información específico | Legal |
| **REST-003** | Operación 24/7 call center | Personal y costos | Contractual |
| **REST-004** | Atención bilingüe requerida | Personal especializado | Servicio |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Personal bilingüe disponible | Medio (servicio limitado) | Estudio mercado laboral |
| **SUP-002** | Demanda llamadas estimada | Medio (sobredimensionamiento) | Estudios similares |
| **SUP-003** | Integración sistemas exitosa | Alto (información fragmentada) | Pruebas integración |
| **SUP-004** | Usuarios adoptan canales digitales | Bajo (mayor carga telefónica) | Plan promoción |

---

## 7. CASOS DE USO

### 7.1 Usuario Presenta Reclamo Telefónico

**ID:** CU-001  
**Actor:** Usuario Vial  
**Descripción:** Usuario llama para presentar reclamo sobre cobro peaje  
**Precondiciones:** Call center operativo, agente disponible  
**Flujo Normal:**
1. Usuario marca número atención
2. IVR clasifica llamada como reclamo
3. Sistema asigna a agente especializado
4. Agente atiende en < 30 segundos
5. Registra reclamo en sistema CRM
6. Asigna número único seguimiento
7. Informa tiempos de respuesta
8. Envía confirmación por email/SMS

**Postcondiciones:** Reclamo registrado y en proceso  
**Flujos Alternativos:** Si líneas ocupadas, ofrece callback

### 7.2 Gestión PQRS Digital

**ID:** CU-002  
**Actor:** Usuario Web  
**Descripción:** Usuario presenta PQRS a través del portal web  
**Precondiciones:** Portal operativo, usuario registrado  
**Flujo Normal:**
1. Usuario accede al portal web
2. Selecciona opción PQRS
3. Completa formulario digital
4. Adjunta documentos si necesario
5. Sistema valida información
6. Asigna número único automáticamente
7. Envía confirmación inmediata
8. Notifica a área responsable

**Postcondiciones:** PQRS en sistema para gestión  
**Flujos Alternativos:** Si formulario incompleto, solicita información

### 7.3 Seguimiento Satisfacción Cliente

**ID:** CU-003  
**Actor:** Sistema Automático  
**Descripción:** Realizar encuesta satisfacción post-atención  
**Precondiciones:** Caso cerrado, contacto disponible  
**Flujo Normal:**
1. Sistema identifica caso cerrado
2. Espera 24 horas post-cierre
3. Envía encuesta por email/SMS
4. Usuario responde calificación
5. Sistema registra en CRM
6. Genera alertas si calificación baja
7. Actualiza indicadores satisfacción
8. Programa seguimiento si necesario

**Postcondiciones:** Satisfacción medida y registrada  
**Flujos Alternativos:** Si no responde, reenvía una vez más

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Call center operativo 24/7 con tiempo respuesta < 30 segundos
- [ ] Sistema PQRS cumpliendo tiempos Ley 1755/2015
- [ ] Oficinas de atención presencial funcionando
- [ ] Canales digitales integrados y operativos
- [ ] CRM con historial completo de usuarios

### 8.2 Criterios de Performance

- [ ] Disponibilidad call center ≥ 99.5%
- [ ] Capacidad 50 llamadas concurrentes
- [ ] Nivel satisfacción cliente > 85%
- [ ] Resolución PQRS en tiempos legales

### 8.3 Criterios de Calidad

- [ ] Cumplimiento Ley 1755/2015 para PQRS
- [ ] Protección datos según Ley 1581/2012
- [ ] Personal bilingüe certificado
- [ ] Accesibilidad web WCAG 2.1 AA

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Personal Bilingüe** | Requerido para operación | Alta | ⏳ Pendiente |
| **Infraestructura IT** | Para plataformas digitales | Alta | ⏳ Pendiente |
| **Integración Sistemas** | Para información completa | Alta | ⏳ Pendiente |
| **Oficinas Físicas** | Para atención presencial | Media | ⏳ Pendiente |
| **Licencias Software** | Para CRM y call center | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Definir estructura organizacional atención cliente
- [ ] Validar requisitos legales con área jurídica
- [ ] Diseñar procesos PQRS según normativa
- [ ] Elaborar especificaciones técnicas plataformas (T04)
- [ ] Establecer SLAs y métricas de calidad

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Industrial | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Industrial - Servicio al Cliente