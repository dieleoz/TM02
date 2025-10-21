# T03: ARQUITECTURA CONCEPTUAL - SISTEMA INFORMACIÓN USUARIOS
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Sistema de Información a Usuarios  
**Responsable:** Ingeniero de Sistemas ITS  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual del Sistema de Información a Usuarios que proporcionará comunicación multicanal con usuarios del corredor, integrando emisora de radio, aplicación móvil, redes sociales y portal web.

### 1.2 Alcance
Arquitectura completa para sistema integral de comunicación que incluye emisora de radio FM, aplicación móvil iOS/Android, portal web, redes sociales y coordinación con paneles LED para información coherente a usuarios.

### 1.3 Referencias
- T01_08: Ficha de Sistema - Sistema Información Usuarios
- T02_08: Análisis de Requisitos - Sistema Información Usuarios
- AT2: Sección 3.3.3.2.4
- MinTIC: Normativa radiodifusión

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    ┌─────────────────────────────────────┐
                    │              CCO                    │
                    │  ┌─────────────────────────────┐    │
                    │  │   Plataforma Central        │    │
                    │  │   - CMS contenidos          │    │
                    │  │   - Base datos usuarios     │    │
                    │  │   - API integración         │    │
                    │  └─────────────────────────────┘    │
                    └─────────────┬───────────────────────┘
                                  │ API REST/WebSocket
                    ┌─────────────┴───────────────────────┐
                    │        Hub Comunicaciones           │
                    │     (Distribución Multicanal)      │
                    └─┬─────┬─────┬─────┬─────┬───────────┘
                      │     │     │     │     │
        ┌─────────────┴─┐ ┌─┴───┐ │   ┌─┴───┐ │
        │ Emisora Radio │ │ App │ │   │ Web │ │
        │   FM 24/7     │ │Móvil│ │   │Portal│ │
        │ Cobertura     │ │iOS/ │ │   │Info │ │
        │ 272.1 km      │ │Andr.│ │   │     │ │
        └───────────────┘ └─────┘ │   └─────┘ │
                                  │           │
                        ┌─────────┴─┐   ┌─────┴─────┐
                        │Redes      │   │Paneles    │
                        │Sociales   │   │LED        │
                        │FB/TW/IG   │   │Coordinados│
                        └───────────┘   └───────────┘
```

**Descripción del diagrama:**
Plataforma centralizada en CCO que distribuye información coherente a múltiples canales: emisora de radio, aplicación móvil, portal web, redes sociales y paneles LED, garantizando mensajes consistentes.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Estación Radio FM** | Transmisión 24/7 | 1kW, cobertura 272 km | 1 estación |
| **Servidor CMS** | Gestión contenidos | 32GB RAM, 2TB SSD | 1 servidor |
| **Aplicación Móvil** | Info tiempo real | iOS/Android nativo | 2 apps |
| **Portal Web** | Información completa | Responsive, accesible | 1 sitio |
| **Sistema Redes Sociales** | Comunicación masiva | FB, Twitter, Instagram | 3 cuentas |
| **API Gateway** | Integración sistemas | REST + WebSocket | 1 sistema |
| **Base Datos** | Almacenamiento | PostgreSQL cluster | 1 BD |
| **CDN** | Distribución contenido | Global, baja latencia | 1 servicio |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Comunicaciones

- **Tipo de topología:** Hub centralizado con distribución multicanal
- **Protocolo principal:** API REST + WebSocket para tiempo real
- **Cobertura radio:** 100% corredor + 20 km adicionales
- **Redundancia:** Sí - Servidores en cluster + CDN global

### 3.2 Diagrama de Topología

```
                     CCO (Centro Control)
                    ┌─────────────────────┐
                    │  Servidor Principal │
                    │  + Base Datos       │
                    │  + API Gateway      │
                    └──────────┬──────────┘
                               │ Internet + Radio
                    ┌──────────┴──────────┐
                    │   Distribución      │
                    │   Multicanal        │
                    └─┬─────┬─────┬─────┬─┘
                      │     │     │     │
            ┌─────────┴─┐ ┌─┴───┐ │   ┌─┴─────┐
            │Radio FM   │ │Apps │ │   │ Web   │
            │Antena     │ │Store│ │   │Hosting│
            │Transmisión│ │Dist.│ │   │CDN    │
            └───────────┘ └─────┘ │   └───────┘
                                  │
                        ┌─────────┴─────────┐
                        │  Redes Sociales   │
                        │  APIs Externas    │
                        └───────────────────┘
```

### 3.3 Distribución de Contenido

**Canales de información:**
- **Radio FM:** Información tráfico cada 15 minutos + noticias
- **App Móvil:** Tiempo real + notificaciones push + GPS
- **Portal Web:** Información completa + mapas + servicios
- **Redes Sociales:** Alertas + comunicados + interacción

---

## 4. FLUJO DE INFORMACIÓN

### 4.1 Flujo de Publicación de Contenido

```
1. [Operador CCO crea contenido]
   ↓ CMS Interface
2. [Sistema valida y procesa]
   ↓ Workflow automático
3. [Distribución multicanal]
   ↓ API Gateway
4. [Radio: Locución automática]
   ↓ TTS + Programación
5. [App: Notificación push]
   ↓ Firebase/APNS
6. [Web: Actualización automática]
   ↓ CDN refresh
7. [Redes: Publicación programada]
```

**Descripción del flujo:**
1. **Creación:** Operador crea contenido en CMS centralizado
2. **Validación:** Sistema valida formato, idioma y coherencia
3. **Distribución:** API Gateway distribuye a todos los canales
4. **Radio:** TTS convierte texto a audio para transmisión
5. **Móvil:** Push notifications a usuarios suscritos
6. **Web:** Actualización automática con CDN
7. **Social:** Publicación automática en redes sociales

### 4.2 Tipos de Contenido

| Tipo de Contenido | Formato | Canales | Frecuencia |
|:------------------|:--------|:--------|:-----------|
| **Información tráfico** | Texto + Audio | Todos | Tiempo real |
| **Alertas emergencia** | Push + Audio | Todos | Inmediato |
| **Estado servicios** | JSON + HTML | App + Web | Cada 5 min |
| **Noticias generales** | Multimedia | Web + Social | Diario |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Servidores** | Activo-Activo | Cluster 2 nodos | Disponibilidad 99% |
| **Base de datos** | Master-Slave | Replicación automática | Continuidad datos |
| **Transmisión radio** | Backup automático | Transmisor secundario | Cobertura continua |
| **Conectividad** | Dual ISP | 2 proveedores internet | Conectividad garantizada |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad emisora:** 99% (según AT4)
- **Disponibilidad app móvil:** 95%
- **Disponibilidad portal web:** 99%
- **Tiempo actualización:** < 5 minutos
- **Tiempo respuesta:** < 3 segundos

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Transmisor radio** | Sí | Transmisor backup automático |
| **Servidor principal** | No | Cluster activo-activo |
| **Base de datos** | No | Replicación master-slave |
| **Conectividad internet** | No | Dual ISP |

---

## 6. SEGURIDAD

### 6.1 Seguridad de Datos

- Cifrado TLS 1.3 para todas las comunicaciones
- Autenticación OAuth 2.0 para APIs
- Base de datos cifrada en reposo
- Backup cifrado con retención 30 días
- Logs de auditoría completos

### 6.2 Seguridad de Contenido

- Validación automática de contenido
- Moderación de comentarios en redes sociales
- Control de acceso por roles (operadores)
- Aprobación de contenido crítico
- Historial de cambios completo

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| Ley 1581/2012 | Protección datos personales |
| MinTIC | Licencia radiodifusión |
| GDPR | Usuarios internacionales |
| ISO 27001 | Seguridad información |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Arquitectura de Microservicios

```
┌─────────────────────────────────┐
│   FRONTEND (React.js)           │ (Interfaces usuario)
├─────────────────────────────────┤
│   API GATEWAY (Kong)            │ (Enrutamiento, auth)
├─────────────────────────────────┤
│   MICROSERVICIOS                │
│   ├─ Contenido (Node.js)        │
│   ├─ Usuarios (Python)          │
│   ├─ Notificaciones (Go)        │
│   └─ Radio (Java)               │
├─────────────────────────────────┤
│   BASE DE DATOS (PostgreSQL)    │ (Almacenamiento)
└─────────────────────────────────┘
```

### 7.2 Tecnologías Seleccionadas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **Frontend** | React.js + PWA | Experiencia moderna multiplataforma |
| **Backend** | Node.js + Python | Escalabilidad y flexibilidad |
| **Base Datos** | PostgreSQL | Robustez y características avanzadas |
| **Cache** | Redis | Performance y sesiones |
| **CDN** | CloudFlare | Distribución global |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | IF-001 | API REST | Alta | Incidentes, estado tráfico |
| **Paneles LED** | IF-002 | NTCIP/API | Media | Mensajes coordinados |
| **Estaciones Peaje** | IF-003 | API REST | Media | Tarifas, estado operativo |
| **Redes Sociales** | IF-004 | APIs nativas | Media | Publicaciones, respuestas |
| **Servicios Push** | IF-005 | Firebase/APNS | Alta | Notificaciones móviles |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Usuarios app móvil** | 10,000 | 50,000 | 100,000 | Arquitectura para 200K |
| **Visitas web/mes** | 100,000 | 500,000 | 1,000,000 | CDN escalable |
| **Seguidores redes** | 5,000 | 25,000 | 50,000 | Sin límite técnico |
| **Contenido/día** | 50 posts | 100 posts | 200 posts | Sistema para 500 |

### 9.2 Estrategia de Crecimiento

Arquitectura de microservicios permite escalamiento horizontal:
- Contenedores Docker orquestados con Kubernetes
- Base de datos con sharding automático
- CDN global con edge computing
- APIs RESTful stateless

---

## 10. ANÁLISIS DE ALTERNATIVAS

### 10.1 Alternativa 1: Sistema Básico

**Descripción:** Solo emisora de radio y portal web básico

**Ventajas:**
- Menor costo inicial
- Implementación más simple
- Menos complejidad técnica

**Desventajas:**
- Limitada interacción con usuarios
- No aprovecha tecnologías móviles
- Menor efectividad comunicacional

**Costo estimado:** $300,000

### 10.2 Alternativa 2: Plataforma Integral ⭐ **RECOMENDADA**

**Descripción:** Sistema multicanal completo con tecnologías modernas

**Ventajas:**
- Comunicación efectiva multicanal
- Interacción en tiempo real
- Mejor experiencia usuario
- Escalabilidad futura
- Métricas y analytics

**Desventajas:**
- Mayor inversión inicial
- Complejidad técnica mayor
- Requiere personal especializado

**Costo estimado:** $550,000

**Justificación de selección:** Mejor comunicación con usuarios, aprovechamiento de tecnologías móviles y mayor efectividad en información de emergencias.

---

## 11. PLAN DE IMPLEMENTACIÓN

### 11.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Licencia radio + infraestructura | 4 meses | Trámites MinTIC |
| **Fase 2** | Desarrollo plataforma central | 3 meses | Especificaciones aprobadas |
| **Fase 3** | Desarrollo app móvil | 3 meses | Plataforma central |
| **Fase 4** | Portal web + redes sociales | 2 meses | Contenido inicial |
| **Fase 5** | Integración y pruebas | 1 mes | Todos los componentes |
| **Fase 6** | Lanzamiento y operación | 1 mes | Pruebas aprobadas |

### 11.2 Hitos Críticos

- **H1:** Licencia radiodifusión aprobada - Mes 4
- **H2:** Emisora operativa - Mes 8
- **H3:** App móvil en stores - Mes 11
- **H4:** Sistema completo operativo - Mes 14

---

## 12. PRÓXIMOS PASOS

- [ ] Iniciar trámite licencia radiodifusión MinTIC
- [ ] Desarrollar especificaciones técnicas detalladas (T04)
- [ ] Definir estrategia de contenidos y comunicación
- [ ] Estimar costos detallados desarrollo software
- [ ] Crear plan de marketing y adopción usuarios
- [ ] Establecer métricas de éxito y KPIs

---

## 13. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Sistemas ITS | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas ITS