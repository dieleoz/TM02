# T02: ANÁLISIS DE REQUISITOS - TELECOMUNICACIONES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Telecomunicaciones  
**Responsable:** Ingeniero de Telecomunicaciones  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales del sistema backbone de telecomunicaciones que interconecta todos los sistemas del proyecto, proporcionando comunicaciones de voz, datos y video en tiempo real.

### 1.2 Alcance
Cubre todos los requisitos para el diseño, implementación y operación de la infraestructura de telecomunicaciones, incluyendo fibra óptica, radio comunicaciones, redes IP, telefonía y enlaces de respaldo para 272.1 km del corredor.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **DWDM** | Dense Wavelength Division Multiplexing |
| **MPLS** | Multiprotocol Label Switching |
| **QoS** | Quality of Service |
| **VLAN** | Virtual Local Area Network |
| **STP** | Spanning Tree Protocol |
| **SNMP** | Simple Network Management Protocol |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Red Backbone de Datos

**ID:** RF-001  
**Descripción:** Proporcionar conectividad IP de alta velocidad entre todos los sistemas  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Fibra óptica backbone 48 hilos mínimo
- Capacidad Gigabit Ethernet en enlaces principales
- Redundancia en rutas críticas
- QoS diferenciado por tipo de tráfico
- Monitoreo SNMP de todos los enlaces

### 2.2 Comunicaciones de Voz

**ID:** RF-002  
**Descripción:** Sistema de radio comunicaciones para operaciones y emergencias  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.1.1  

**Criterios de Aceptación:**
- Cobertura radio 100% del corredor
- Comunicación directa CCO-Bases-Vehículos
- Canales dedicados por tipo de operación
- Grabación de comunicaciones críticas
- Interoperabilidad con autoridades

### 2.3 Telefonía Corporativa

**ID:** RF-003  
**Descripción:** Sistema telefónico IP para comunicaciones administrativas  
**Prioridad:** Media  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Central telefónica IP escalable
- Extensiones en todas las ubicaciones
- Comunicación con redes públicas
- Grabación de llamadas críticas
- Integración con sistema atención cliente

### 2.4 Transmisión de Video

**ID:** RF-004  
**Descripción:** Transmisión de video CCTV desde ubicaciones remotas al CCO  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Ancho de banda suficiente para 200+ cámaras
- Calidad HD mínimo para identificación
- Almacenamiento distribuido y centralizado
- Acceso remoto autorizado
- Compresión eficiente H.264/H.265

### 2.5 Acceso a Internet

**ID:** RF-005  
**Descripción:** Conectividad a internet para sistemas web y comunicaciones externas  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.1.7  

**Criterios de Aceptación:**
- Enlaces redundantes a internet
- Ancho de banda mínimo 100 Mbps
- Firewall y seguridad perimetral
- VPN para acceso remoto
- Filtrado de contenido y amenazas

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad red backbone | 99.5% mensual | AT4 |
| **RNF-002** | MTBF equipos críticos | 50,000 horas | Buenas prácticas |
| **RNF-003** | MTTR reparaciones | 4 horas | AT2 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Latencia red backbone | < 50 ms | Buenas prácticas |
| **RNF-005** | Ancho banda backbone | 1 Gbps | Estimado |
| **RNF-006** | Cobertura radio | 100% corredor | AT2 |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Cifrado comunicaciones | AES-256 mínimo | Buenas prácticas |
| **RNF-008** | Autenticación equipos | 802.1X en switches | Buenas prácticas |
| **RNF-009** | Firewall perimetral | Protección multicapa | AT2 |

### 3.4 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Capacidad crecimiento | +100% sin cambios mayores | Buenas prácticas |
| **RNF-011** | Puertos disponibles | 30% reserva en switches | Buenas prácticas |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Gestión centralizada | NMS para todos los equipos | AT2 |
| **RNF-013** | Configuración remota | Acceso SSH/HTTPS seguro | Buenas prácticas |
| **RNF-014** | Monitoreo proactivo | Alertas automáticas | AT2 |

### 3.6 Requisitos Ambientales

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Operación climática | -10°C a +60°C | Condiciones locales |
| **RNF-016** | Protección equipos | IP65 exteriores, IP20 interiores | Buenas prácticas |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con CCO

**ID:** RI-001  
**Sistemas:** Red Telecomunicaciones ↔ CCO  
**Tipo:** Fibra Óptica  
**Protocolo:** Ethernet, MPLS  
**Datos Intercambiados:** Todos los datos de sistemas remotos  
**Frecuencia:** Tiempo real

### 4.2 Interface con Estaciones Peaje

**ID:** RI-002  
**Sistemas:** Red Telecomunicaciones ↔ Estaciones Peaje  
**Tipo:** Fibra Óptica  
**Protocolo:** TCP/IP, HTTPS  
**Datos Intercambiados:** Recaudación, video, alarmas  
**Frecuencia:** Tiempo real

### 4.3 Interface con Bases Operación

**ID:** RI-003  
**Sistemas:** Red Telecomunicaciones ↔ Bases Operación  
**Tipo:** Fibra Óptica + Radio  
**Protocolo:** Ethernet, VHF/UHF  
**Datos Intercambiados:** Datos operacionales, comunicaciones voz  
**Frecuencia:** Tiempo real

### 4.4 Interface con Paneles LED

**ID:** RI-004  
**Sistemas:** Red Telecomunicaciones ↔ Paneles LED  
**Tipo:** Fibra Óptica  
**Protocolo:** TCP/IP, NTCIP  
**Datos Intercambiados:** Mensajes, estado, alarmas  
**Frecuencia:** Por evento

### 4.5 Interface con Internet

**ID:** RI-005  
**Sistemas:** Red Telecomunicaciones ↔ Proveedores ISP  
**Tipo:** Fibra Óptica  
**Protocolo:** BGP, MPLS  
**Datos Intercambiados:** Tráfico web, VPN, email  
**Frecuencia:** Continua

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Red backbone datos | AT2, Sección 3.1.7 | Fibra óptica, switches | Alta |
| RF-002 | Funcional | Comunicaciones voz | AT2, Sección 3.3.3.1.1 | Sistema radio | Alta |
| RF-003 | Funcional | Telefonía IP | AT2, Sección 3.1.7 | Central telefónica | Media |
| RF-004 | Funcional | Transmisión video | AT2, Sección 3.1.7 | Red IP, encoders | Alta |
| RF-005 | Funcional | Acceso internet | AT2, Sección 3.1.7 | Enlaces ISP, firewall | Alta |
| RNF-001 | No Funcional | Disponibilidad 99.5% | AT4 | Todos los sistemas | Alta |
| RNF-004 | No Funcional | Latencia < 50ms | Buenas prácticas | Red backbone | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Disponibilidad permanente requerida | Redundancia obligatoria | AT2 |
| **REST-002** | Acceso múltiples entidades | Interfaces específicas | AT2 |
| **REST-003** | Cumplimiento normativa MinTIC | Licencias y permisos | Legal |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Permisos MinTIC aprobados | No operación radio | Validar mes 1 |
| **SUP-002** | Fibra óptica instalable en corredor | Retrasos implementación | Validar mes 2 |
| **SUP-003** | ISPs disponibles en región | Falta conectividad internet | Validar mes 1 |

---

## 7. CASOS DE USO

### 7.1 Comunicación de Emergencia

**ID:** CU-001  
**Actor:** Operador Base de Operación  
**Descripción:** Comunicación urgente con CCO por emergencia  
**Precondiciones:** Sistema radio operativo, cobertura disponible  
**Flujo Normal:**
1. Operador activa radio de emergencia
2. Sistema prioriza canal de emergencia
3. Establece comunicación directa con CCO
4. CCO recibe alerta automática
5. Inicia grabación de comunicación
6. Coordina respuesta según protocolo
7. Mantiene canal abierto hasta resolución
8. Registra evento completo

**Postcondiciones:** Emergencia comunicada y registrada  
**Flujos Alternativos:** Si falla radio, usar telefonía IP

### 7.2 Transmisión Video Crítico

**ID:** CU-002  
**Actor:** Sistema CCTV  
**Descripción:** Transmisión de video de incidente al CCO  
**Precondiciones:** Cámaras operativas, red disponible  
**Flujo Normal:**
1. Cámara detecta evento crítico
2. Sistema prioriza ancho de banda
3. Aumenta calidad de transmisión
4. Envía alerta al CCO
5. CCO visualiza video en tiempo real
6. Inicia grabación de alta calidad
7. Distribuye video a autoridades
8. Mantiene transmisión hasta resolución

**Postcondiciones:** Evento documentado y transmitido

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Conectividad IP entre 100% de ubicaciones
- [ ] Cobertura radio 100% del corredor
- [ ] Transmisión video 200+ cámaras simultáneas
- [ ] Telefonía IP en todas las ubicaciones
- [ ] Acceso internet redundante operativo

### 8.2 Criterios de Performance

- [ ] Disponibilidad ≥ 99.5% mensual
- [ ] Latencia red backbone < 50 ms
- [ ] Ancho banda backbone ≥ 1 Gbps
- [ ] Cobertura radio sin zonas muertas

### 8.3 Criterios de Calidad

- [ ] Equipos certificados MinTIC
- [ ] Cumplir estándares IEEE 802.11
- [ ] Personal certificado en operación
- [ ] Documentación técnica completa

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| Permisos MinTIC | Licencias radio requeridas | Alta | ⏳ Pendiente |
| Energía Eléctrica | Suministro estable todos los nodos | Alta | ⏳ Pendiente |
| Infraestructura Civil | Torres, ductos, salas técnicas | Alta | ⏳ Pendiente |
| Proveedores ISP | Enlaces internet redundantes | Alta | ⏳ Pendiente |
| Personal Técnico | Especialistas en telecomunicaciones | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual red (T03)
- [ ] Realizar estudios de cobertura radio
- [ ] Elaborar especificaciones técnicas equipos (T04)
- [ ] Tramitar permisos y licencias MinTIC
- [ ] Cotizar equipos especializados
- [ ] Diseñar plan de implementación por fases

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero de Telecomunicaciones | Análisis inicial requisitos telecomunicaciones |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Telecomunicaciones