# T03: ARQUITECTURA CONCEPTUAL - ATENCIÓN AL CLIENTE
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Atención al Cliente  
**Responsable:** Ingeniero Industrial - Servicio al Cliente  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual del Sistema de Atención al Cliente que proporcionará servicio integral multicanal para usuarios del corredor, incluyendo call center 24/7, gestión de PQRS, atención presencial y canales digitales.

### 1.2 Alcance
Arquitectura completa para sistema de atención al cliente con call center, oficinas presenciales, plataforma CRM, portal web, aplicación móvil y gestión integral de PQRS según normativa colombiana.

### 1.3 Referencias
- T01_11: Ficha de Sistema - Atención al Cliente
- T02_11: Análisis de Requisitos - Atención al Cliente
- Ley 1755/2015: PQRS
- Ley 1581/2012: Protección datos personales

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    ┌─────────────────────────────────────┐
                    │              CCO                    │
                    │  ┌─────────────────────────────┐    │
                    │  │   Plataforma CRM Central    │    │
                    │  │   - Base datos usuarios     │    │
                    │  │   - Gestión PQRS            │    │
                    │  │   - Reportes y analytics    │    │
                    │  └─────────────────────────────┘    │
                    └─────────────┬───────────────────────┘
                                  │ API REST + WebSocket
                    ┌─────────────┴───────────────────────┐
                    │        Hub Atención Cliente         │
                    │     (Distribución Multicanal)      │
                    └─┬─────┬─────┬─────┬─────┬───────────┘
                      │     │     │     │     │
        ┌─────────────┴─┐ ┌─┴───┐ │   ┌─┴───┐ │
        │ Call Center   │ │ Web │ │   │ App │ │
        │   24/7        │ │Portal│ │   │Móvil│ │
        │ - IVR         │ │PQRS │ │   │PQRS │ │
        │ - Agentes     │ │Auto │ │   │Push │ │
        │ - Grabación   │ │serv.│ │   │Notif│ │
        └───────────────┘ └─────┘ │   └─────┘ │
                                  │           │
                        ┌─────────┴─┐   ┌─────┴─────┐
                        │Oficinas   │   │Redes      │
                        │Presencial │   │Sociales   │
                        │Peajes     │   │FB/TW/IG   │
                        └───────────┘   └───────────┘
```

**Descripción del diagrama:**
Plataforma CRM centralizada que integra múltiples canales de atención: call center 24/7, portal web, aplicación móvil, oficinas presenciales y redes sociales, con gestión unificada de PQRS.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Call Center** | Atención telefónica 24/7 | 10 posiciones, IVR, grabación | 1 centro |
| **Plataforma CRM** | Gestión integral clientes | Salesforce/Dynamics, cloud | 1 sistema |
| **Portal Web** | Autoservicio PQRS | Responsive, accesible WCAG | 1 portal |
| **Aplicación Móvil** | Atención móvil | iOS/Android, push notifications | 2 apps |
| **Oficinas Presenciales** | Atención cara a cara | En estaciones peaje principales | 3 oficinas |
| **Sistema IVR** | Clasificación automática | Reconocimiento voz, 5 niveles | 1 sistema |
| **Base Datos CRM** | Almacenamiento | PostgreSQL cluster, backup | 1 BD |
| **Sistema Grabación** | Cumplimiento legal | 90 días retención, cifrado | 1 sistema |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Comunicaciones

- **Tipo de topología:** Hub centralizado con canales distribuidos
- **Protocolo principal:** API REST + WebSocket para tiempo real
- **Telefonía:** SIP trunks + PSTN tradicional
- **Redundancia:** Sí - Call center backup + servidores cluster

### 3.2 Diagrama de Topología

```
                     CCO (Centro Control)
                    ┌─────────────────────┐
                    │  Servidor CRM       │
                    │  + Base Datos       │
                    │  + Call Center      │
                    └──────────┬──────────┘
                               │ Internet + SIP
                    ┌──────────┴──────────┐
                    │   Distribución      │
                    │   Multicanal        │
                    └─┬─────┬─────┬─────┬─┘
                      │     │     │     │
            ┌─────────┴─┐ ┌─┴───┐ │   ┌─┴─────┐
            │Telefonía  │ │Web  │ │   │ Móvil │
            │PSTN/SIP   │ │Cloud│ │   │ Stores│
            │IVR        │ │Host │ │   │ Push  │
            └───────────┘ └─────┘ │   └───────┘
                                  │
                        ┌─────────┴─────────┐
                        │  Oficinas Físicas │
                        │  Red Corporativa  │
                        └───────────────────┘
```

### 3.3 Distribución de Canales

**Canales de atención:**
- **Call Center:** 24/7, 50 llamadas concurrentes, tiempo respuesta <30s
- **Portal Web:** Autoservicio PQRS, consultas, información
- **App Móvil:** PQRS móviles, notificaciones, seguimiento
- **Oficinas:** Atención presencial en peajes principales

---

## 4. FLUJO DE ATENCIÓN

### 4.1 Flujo de Gestión PQRS

```
1. [Usuario presenta PQRS]
   ↓ Cualquier canal
2. [Sistema asigna número único]
   ↓ Generación automática
3. [Clasificación automática]
   ↓ IA + reglas negocio
4. [Asignación a especialista]
   ↓ Según tipo y complejidad
5. [Gestión y seguimiento]
   ↓ Tiempos Ley 1755
6. [Respuesta al usuario]
   ↓ Canal preferido
7. [Encuesta satisfacción]
   ↓ Medición calidad
8. [Cierre y archivo]
```

**Descripción del flujo:**
1. **Recepción:** Usuario presenta PQRS por cualquier canal
2. **Registro:** Sistema asigna número único de seguimiento
3. **Clasificación:** IA clasifica tipo y prioridad automáticamente
4. **Asignación:** Especialista según expertise y carga trabajo
5. **Gestión:** Seguimiento según tiempos legales Ley 1755
6. **Respuesta:** Comunicación por canal preferido del usuario
7. **Medición:** Encuesta satisfacción automática
8. **Cierre:** Archivo con trazabilidad completa

### 4.2 Tipos de Atención

| Tipo PQRS | Canal Preferido | Tiempo Respuesta | Especialista |
|:----------|:----------------|:-----------------|:-------------|
| **Petición** | Web/App | 15 días hábiles | Atención general |
| **Queja** | Call center | 15 días hábiles | Especialista quejas |
| **Reclamo** | Presencial/Call | 15 días hábiles | Especialista técnico |
| **Sugerencia** | Web/Social | 15 días hábiles | Mejora continua |
| **Emergencia** | Call center | Inmediato | Supervisor |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Call Center** | Sitio backup | Centro secundario | Disponibilidad 99.5% |
| **Servidores CRM** | Activo-Activo | Cluster 2 nodos | Continuidad servicio |
| **Base de datos** | Master-Slave | Replicación tiempo real | Integridad datos |
| **Conectividad** | Dual ISP + 4G | 3 proveedores | Comunicación garantizada |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad call center:** 99.5%
- **Tiempo respuesta llamadas:** <30 segundos
- **Disponibilidad portal web:** 99%
- **Tiempo respuesta PQRS:** Según Ley 1755/2015
- **Nivel satisfacción:** >85%

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Call center principal** | Sí | Centro backup automático |
| **Servidor CRM** | No | Cluster activo-activo |
| **Base de datos** | No | Replicación master-slave |
| **Conectividad internet** | No | Triple redundancia |

---

## 6. SEGURIDAD

### 6.1 Seguridad de Datos

- Cifrado TLS 1.3 para todas las comunicaciones
- Base de datos cifrada según Ley 1581/2012
- Grabaciones telefónicas cifradas y con acceso controlado
- Backup cifrado con retención según normativa
- Logs de auditoría completos por 5 años

### 6.2 Seguridad de Acceso

- Autenticación multifactor para agentes
- Control de acceso basado en roles (RBAC)
- Sesiones con timeout automático
- Monitoreo de accesos sospechosos
- Capacitación en protección de datos

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| Ley 1755/2015 | Gestión PQRS |
| Ley 1581/2012 | Protección datos personales |
| ISO 27001 | Seguridad información |
| PCI DSS | Si maneja pagos |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Arquitectura de Microservicios

```
┌─────────────────────────────────┐
│   FRONTEND (React + Angular)    │ (Interfaces multicanal)
├─────────────────────────────────┤
│   API GATEWAY (Kong)            │ (Enrutamiento, auth)
├─────────────────────────────────┤
│   MICROSERVICIOS                │
│   ├─ PQRS (Java Spring)         │
│   ├─ Usuarios (Node.js)         │
│   ├─ Notificaciones (Python)    │
│   ├─ Reportes (Python)          │
│   └─ Call Center (C#)           │
├─────────────────────────────────┤
│   BASE DE DATOS (PostgreSQL)    │ (Almacenamiento)
└─────────────────────────────────┘
```

### 7.2 Tecnologías Seleccionadas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **CRM** | Salesforce/Dynamics | Funcionalidad completa probada |
| **Call Center** | Asterisk/FreePBX | Open source, escalable |
| **Frontend** | React.js + Angular | Experiencia usuario moderna |
| **Backend** | Java Spring + Node.js | Escalabilidad y performance |
| **Base Datos** | PostgreSQL | Robustez y cumplimiento ACID |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | IF-001 | API REST | Media | Incidentes, información operativa |
| **Estaciones Peaje** | IF-002 | API REST | Alta | Transacciones, reclamos |
| **Sistema Info Usuarios** | IF-003 | API REST | Media | Información coordinada |
| **Redes Sociales** | IF-004 | APIs nativas | Baja | Consultas públicas |
| **Bancos/Pagos** | IF-005 | API segura | Media | Validación transacciones |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Llamadas/día** | 500 | 1,000 | 1,500 | Sistema para 2,000 |
| **PQRS/mes** | 200 | 500 | 800 | Arquitectura para 1,000 |
| **Agentes call center** | 10 | 15 | 20 | Infraestructura para 25 |
| **Usuarios registrados** | 5,000 | 25,000 | 50,000 | Base datos escalable |

### 9.2 Estrategia de Crecimiento

Arquitectura cloud-native permite escalamiento automático:
- Microservicios en contenedores Docker
- Auto-scaling basado en demanda
- Base de datos con sharding automático
- Call center con adición de agentes on-demand

---

## 10. ANÁLISIS DE ALTERNATIVAS

### 10.1 Alternativa 1: Sistema Básico

**Descripción:** Solo call center básico y email para PQRS

**Ventajas:**
- Menor costo inicial
- Implementación rápida
- Menos complejidad técnica

**Desventajas:**
- No cumple expectativas usuarios modernos
- Limitada trazabilidad PQRS
- No aprovecha canales digitales

**Costo estimado:** $150,000

### 10.2 Alternativa 2: Plataforma Integral ⭐ **RECOMENDADA**

**Descripción:** Sistema multicanal completo con CRM y automatización

**Ventajas:**
- Experiencia usuario superior
- Cumplimiento normativo completo
- Trazabilidad total PQRS
- Métricas y analytics avanzados
- Escalabilidad futura

**Desventajas:**
- Mayor inversión inicial
- Complejidad técnica mayor
- Requiere personal especializado

**Costo estimado:** $270,000

**Justificación de selección:** Mejor experiencia usuario, cumplimiento normativo y eficiencia operacional justifican la inversión.

---

## 11. PLAN DE IMPLEMENTACIÓN

### 11.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Selección e implementación CRM | 3 meses | Especificaciones aprobadas |
| **Fase 2** | Configuración call center | 2 meses | CRM operativo |
| **Fase 3** | Desarrollo portal web + app | 3 meses | CRM integrado |
| **Fase 4** | Capacitación personal | 1 mes | Sistemas operativos |
| **Fase 5** | Pruebas integrales | 1 mes | Personal capacitado |
| **Fase 6** | Lanzamiento y operación | 1 mes | Pruebas aprobadas |

### 11.2 Hitos Críticos

- **H1:** CRM operativo con PQRS básicas - Mes 3
- **H2:** Call center 24/7 funcionando - Mes 5
- **H3:** Portal web y app móvil lanzados - Mes 8
- **H4:** Sistema completo certificado - Mes 11

---

## 12. PRÓXIMOS PASOS

- [ ] Seleccionar plataforma CRM (Salesforce vs Dynamics)
- [ ] Desarrollar especificaciones técnicas detalladas (T04)
- [ ] Definir estructura organizacional atención cliente
- [ ] Crear procedimientos PQRS según Ley 1755
- [ ] Estimar costos detallados implementación
- [ ] Establecer SLAs y métricas de calidad

---

## 13. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Industrial | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Industrial - Servicio al Cliente