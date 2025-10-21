# T02: ANÁLISIS DE REQUISITOS - CENTRO DE CONTROL DE OPERACIÓN (CCO)
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Centro de Control de Operación (CCO)  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales del Centro de Control de Operación (CCO), sistema neurálgico que centraliza la supervisión, control y coordinación de todos los sistemas del proyecto APP Sabana de Torres - Curumaní.

### 1.2 Alcance
Cubre todos los requisitos para el diseño, implementación y operación del CCO, incluyendo hardware, software, interfaces, personal y procedimientos operacionales para supervisión 24/7/365.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **CCO** | Centro de Control de Operación |
| **SCADA** | Supervisory Control and Data Acquisition |
| **HMI** | Human Machine Interface |
| **NVR** | Network Video Recorder |
| **UPS** | Uninterruptible Power Supply |
| **SLA** | Service Level Agreement |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Supervisión y Monitoreo

**ID:** RF-001  
**Descripción:** El CCO debe supervisar en tiempo real el estado operacional de todos los sistemas del proyecto  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Visualización simultánea de todos los sistemas en videowall
- Actualización de estados cada 30 segundos máximo
- Alarmas visuales y sonoras para eventos críticos
- Registro histórico de todos los eventos

### 2.2 Control Remoto de Sistemas

**ID:** RF-002  
**Descripción:** Capacidad de control remoto de sistemas críticos desde el CCO  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Control de paneles LED (mensajes dinámicos)
- Activación/desactivación sistemas de emergencia
- Control de iluminación en ubicaciones críticas
- Confirmación de comandos ejecutados

### 2.3 Gestión de Emergencias

**ID:** RF-003  
**Descripción:** Coordinación centralizada de respuesta a emergencias y accidentes  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.1.1  

**Criterios de Aceptación:**
- Activación automática de protocolos de emergencia
- Comunicación directa con bases de operación
- Notificación a autoridades competentes
- Seguimiento de tiempos de respuesta

### 2.4 Información a Usuarios

**ID:** RF-004  
**Descripción:** Gestión y distribución de información a usuarios del corredor  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.2  

**Criterios de Aceptación:**
- Actualización página web cada hora máximo
- Control de mensajes en paneles LED
- Coordinación con emisora de radio
- Gestión de boletín trimestral

### 2.5 Reportes y Estadísticas

**ID:** RF-005  
**Descripción:** Generación automática de reportes operacionales y estadísticas  
**Prioridad:** Media  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Reportes diarios, semanales y mensuales
- Indicadores de desempeño (KPIs)
- Exportación en múltiples formatos
- Acceso para ANI e Interventoría

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad del CCO | 99.5% mensual | AT4 |
| **RNF-002** | MTBF (Tiempo Medio Entre Fallas) | 8,760 horas | Buenas prácticas |
| **RNF-003** | MTTR (Tiempo Medio de Reparación) | 4 horas | AT2 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Tiempo respuesta alarmas | < 30 segundos | AT4 |
| **RNF-005** | Capacidad procesamiento video | 200 cámaras simultáneas | Estimado |
| **RNF-006** | Ancho de banda backbone | 1 Gbps | Estimado |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Autenticación usuarios | Control acceso con roles definidos | AT2 |
| **RNF-008** | Cifrado comunicaciones | TLS 1.2 mínimo | Buenas prácticas |
| **RNF-009** | Backup datos | Diario, retención 5 años | AT2 |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Interfaz operador | Intuitiva, capacitación < 40 horas | AT2 |
| **RNF-011** | Idioma | Español, soporte inglés | Buenas prácticas |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Actualización software | Remota, sin interrupción servicio | AT2 |
| **RNF-013** | Diagnóstico remoto | Monitoreo SNMP de todos los equipos | AT2 |
| **RNF-014** | Repuestos críticos | Disponibilidad durante 25 años | AT2 |

### 3.6 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Capacidad crecimiento | +50% sistemas sin cambios mayores | Buenas prácticas |
| **RNF-016** | Módulos expandibles | Arquitectura modular SCADA | Buenas prácticas |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con Estaciones de Peaje

**ID:** RI-001  
**Sistemas:** CCO ↔ Estaciones de Peaje (3)  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP, HTTPS  
**Datos Intercambiados:** Recaudación, alarmas, video CCTV, estado operacional  
**Frecuencia:** Tiempo real

### 4.2 Interface con Bases de Operación

**ID:** RI-002  
**Sistemas:** CCO ↔ Bases de Operación (2)  
**Tipo:** Red de Datos + Radio  
**Protocolo:** TCP/IP, VHF  
**Datos Intercambiados:** Emergencias, ubicación vehículos, estado equipos  
**Frecuencia:** Tiempo real

### 4.3 Interface con Paneles LED

**ID:** RI-003  
**Sistemas:** CCO ↔ Paneles LED (25)  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP, NTCIP 1203  
**Datos Intercambiados:** Mensajes dinámicos, estado paneles, alarmas  
**Frecuencia:** Por evento

### 4.4 Interface con Sistema Web

**ID:** RI-004  
**Sistemas:** CCO ↔ Sistema Web  
**Tipo:** API REST  
**Protocolo:** HTTPS, JSON  
**Datos Intercambiados:** Estado vía, incidentes, tarifas  
**Frecuencia:** Cada hora

### 4.5 Interface con ANI/Interventoría

**ID:** RI-005  
**Sistemas:** CCO ↔ Sistemas ANI  
**Tipo:** VPN/Web  
**Protocolo:** HTTPS, VPN  
**Datos Intercambiados:** Reportes, indicadores, acceso remoto  
**Frecuencia:** Continua

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Supervisión tiempo real | AT2, Sección 3.1.7 | SCADA, Videowall | Alta |
| RF-002 | Funcional | Control remoto | AT2, Sección 3.1.7 | SCADA, HMI | Alta |
| RF-003 | Funcional | Gestión emergencias | AT2, Sección 3.3.3.1.1 | Radio, SCADA | Alta |
| RF-004 | Funcional | Información usuarios | AT2, Sección 3.3.3.2 | Web, SCADA | Alta |
| RF-005 | Funcional | Reportes | AT2, Sección 3.1.7 | Base datos, SCADA | Media |
| RNF-001 | No Funcional | Disponibilidad 99.5% | AT4 | Todos | Alta |
| RNF-004 | No Funcional | Tiempo respuesta < 30s | AT4 | SCADA, Red | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Operación 24/7/365 sin interrupciones | Requiere redundancia total | Contractual |
| **REST-002** | Acceso permanente ANI/Interventoría | Interfaces específicas requeridas | Contractual |
| **REST-003** | Información disponible < 1 hora | Sistemas tiempo real obligatorios | AT2 |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Fibra óptica disponible todo el corredor | Falta comunicaciones críticas | Validar mes 2 |
| **SUP-002** | Personal operativo calificado disponible | Operación deficiente | Validar mes 1 |
| **SUP-003** | Energía eléctrica estable en ubicación CCO | Interrupciones servicio | Validar mes 1 |

---

## 7. CASOS DE USO

### 7.1 Gestión de Emergencia Vial

**ID:** CU-001  
**Actor:** Operador CCO  
**Descripción:** Respuesta a accidente reportado en el corredor  
**Precondiciones:** CCO operativo, personal en bases disponible  
**Flujo Normal:**
1. Recepción alarma/llamada de emergencia
2. Verificación ubicación y tipo de emergencia
3. Activación protocolo respuesta según tipo
4. Despacho recursos desde base más cercana
5. Coordinación con ambulancia TAM si hay heridos
6. Actualización paneles LED con información
7. Notificación autoridades competentes
8. Seguimiento hasta resolución
9. Registro completo del evento

**Postcondiciones:** Emergencia resuelta, vía despejada, registro completo  
**Flujos Alternativos:** Si no hay respuesta de base, activar base alterna

### 7.2 Control de Información a Usuarios

**ID:** CU-002  
**Actor:** Operador CCO  
**Descripción:** Actualización de información para usuarios  
**Precondiciones:** CCO operativo, sistemas comunicación funcionando  
**Flujo Normal:**
1. Identificación de evento que requiere información
2. Preparación mensaje apropiado
3. Actualización página web
4. Envío mensaje a paneles LED relevantes
5. Coordinación con emisora radio
6. Verificación recepción mensajes
7. Monitoreo efectividad información

**Postcondiciones:** Usuarios informados oportunamente

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] El CCO debe supervisar 100% de los sistemas del proyecto
- [ ] Tiempo respuesta a alarmas críticas < 30 segundos
- [ ] Control remoto efectivo de paneles LED y sistemas críticos
- [ ] Comunicación bidireccional con bases de operación
- [ ] Generación automática de reportes diarios

### 8.2 Criterios de Performance

- [ ] Disponibilidad ≥ 99.5% mensual
- [ ] Procesamiento simultáneo 200+ cámaras CCTV
- [ ] Tiempo respuesta sistema < 2 segundos
- [ ] Capacidad 50+ usuarios concurrentes

### 8.3 Criterios de Calidad

- [ ] Cumplir ISO 27001 para seguridad información
- [ ] Certificación equipos según normativa colombiana
- [ ] Personal certificado en operación SCADA
- [ ] Procedimientos documentados y aprobados

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| Telecomunicaciones | Debe estar operativo antes | Alta | ⏳ Pendiente |
| Energía Eléctrica | Suministro estable requerido | Alta | ⏳ Pendiente |
| Edificación CCO | Construcción completada | Alta | ⏳ Pendiente |
| Personal Operativo | Contratado y capacitado | Alta | ⏳ Pendiente |
| Estaciones Peaje | Interfaces de comunicación | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual CCO (T03)
- [ ] Definir ubicación óptima del CCO
- [ ] Validar requisitos con stakeholders
- [ ] Elaborar especificaciones técnicas SCADA (T04)
- [ ] Diseñar procedimientos operacionales
- [ ] Planificar capacitación personal operativo

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Sistemas | Análisis inicial de requisitos CCO |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas