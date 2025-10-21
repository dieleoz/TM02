# T03: ARQUITECTURA CONCEPTUAL - PANELES LED
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Paneles LED (Paneles de Mensaje Variable - PMV)  
**Responsable:** Ingeniero de Sistemas ITS  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual del sistema de Paneles LED (PMV) que proporcionará información dinámica a usuarios del corredor, integrándose con el CCO y otros sistemas ITS para operación coordinada.

### 1.2 Alcance
Arquitectura completa para 31 paneles LED distribuidos en 272.1 km del corredor, incluyendo paneles principales, paneles de peaje, controladores locales, comunicaciones y software de gestión centralizado.

### 1.3 Referencias
- T01_04: Ficha de Sistema - Paneles LED
- T02_04: Análisis de Requisitos - Paneles LED
- AT1: Sección Paneles LED
- AT2: Sección 3.3.3.2.4

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    ┌─────────────────────────────────────┐
                    │              CCO                    │
                    │  ┌─────────────────────────────┐    │
                    │  │   Software Gestión PMV      │    │
                    │  │   - Control mensajes        │    │
                    │  │   - Monitoreo estado        │    │
                    │  │   - Programación automática │    │
                    │  └─────────────────────────────┘    │
                    └─────────────┬───────────────────────┘
                                  │ Red IP/Fibra Óptica
                    ┌─────────────┴───────────────────────┐
                    │        Red Telecomunicaciones       │
                    │     (Backbone Fibra Óptica)        │
                    └─┬─────────┬─────────┬──────────────┘
                      │         │         │
        ┌─────────────┴─┐ ┌─────┴─────┐ ┌─┴──────────────┐
        │   Zona Norte  │ │Zona Centro│ │   Zona Sur     │
        │  (10 paneles) │ │(11 paneles)│ │  (10 paneles) │
        └─┬─────────────┘ └─┬─────────┘ └─┬──────────────┘
          │                 │             │
    ┌─────┴─────┐     ┌─────┴─────┐ ┌─────┴─────┐
    │Panel LED  │     │Panel LED  │ │Panel LED  │
    │+ Control  │     │+ Control  │ │+ Control  │
    │+ UPS      │     │+ UPS      │ │+ UPS      │
    │+ Sensores │     │+ Sensores │ │+ Sensores │
    └───────────┘     └───────────┘ └───────────┘
```

**Descripción del diagrama:**
Sistema distribuido con control centralizado desde CCO, comunicación por fibra óptica y controladores locales inteligentes en cada panel para operación autónoma en caso de falla de comunicaciones.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Paneles LED Principales** | Información dinámica corredor | Matriz LED full color, 4x2m | 25 unidades |
| **Paneles LED Peajes** | Información específica peajes | Matriz LED full color, 3x1.5m | 6 unidades |
| **Controladores Locales** | Control y comunicación panel | CPU ARM, 4GB RAM, Linux | 31 unidades |
| **Sistemas UPS** | Respaldo energético | 2kVA, 30min autonomía | 31 unidades |
| **Sensores Ambientales** | Ajuste automático brillo | Fotoceldas + temperatura | 31 unidades |
| **Software Gestión Central** | Control desde CCO | Plataforma web, base datos | 1 sistema |
| **Estructuras Soporte** | Soporte mecánico paneles | Acero galvanizado, anti-viento | 31 unidades |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Red

- **Tipo de topología:** Estrella distribuida con redundancia
- **Protocolo principal:** NTCIP 1203 sobre TCP/IP
- **Segmentación:** VLAN dedicada para PMV (VLAN 40)
- **Redundancia:** Sí - Enlaces backup por radio 4G

### 3.2 Diagrama de Topología

```
                     CCO (Centro Control)
                    ┌─────────────────────┐
                    │  Switch Core L3     │
                    │  VLAN 40 (PMV)      │
                    └──────────┬──────────┘
                               │ Fibra Principal
                    ┌──────────┴──────────┐
                    │   Backbone Fibra    │
                    │   Redundancia 4G    │
                    └─┬─────────┬─────────┘
                      │         │
            ┌─────────┴─┐   ┌───┴─────────┐
            │Switch L2  │   │  Switch L2  │
            │Zona Norte │   │  Zona Sur   │
            └─┬─────────┘   └─┬───────────┘
              │               │
        ┌─────┴─────┐   ┌─────┴─────┐
        │Panel LED  │   │Panel LED  │
        │IP: x.x.x.1│   │IP: x.x.x.2│
        └───────────┘   └───────────┘
```

### 3.3 Distribución Física

**Ubicaciones principales:**
- **Zona Norte (km 0-90):** 10 paneles principales + 2 paneles peaje La Gómez
- **Zona Centro (km 90-180):** 11 paneles principales + 2 paneles peaje Morrison  
- **Zona Sur (km 180-272):** 10 paneles principales + 2 paneles peaje Pailitas

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo de Datos Principal

```
1. [Operador CCO crea mensaje]
   ↓ Interface Web
2. [Software valida mensaje]
   ↓ Base de datos
3. [Sistema envía a paneles]
   ↓ NTCIP 1203/TCP-IP
4. [Controlador local recibe]
   ↓ Procesamiento local
5. [Panel muestra mensaje]
   ↓ Confirmación
6. [Estado reportado a CCO]
```

**Descripción del flujo:**
1. **Creación:** Operador crea mensaje en interface web del CCO
2. **Validación:** Sistema valida sintaxis, legibilidad y duración
3. **Distribución:** Mensaje enviado a paneles seleccionados vía NTCIP
4. **Procesamiento:** Controlador local procesa y almacena mensaje
5. **Visualización:** Panel LED muestra mensaje con ajuste automático brillo
6. **Confirmación:** Estado y estadísticas reportadas al CCO

### 4.2 Tipos de Datos

| Tipo de Dato | Formato | Volumen Estimado | Retención |
|:-------------|:--------|:-----------------|:----------|
| **Mensajes texto** | NTCIP 1203 | 50 KB/día | 30 días |
| **Estados paneles** | JSON | 100 MB/día | 90 días |
| **Estadísticas uso** | CSV | 10 MB/día | 1 año |
| **Logs sistema** | Texto plano | 500 MB/día | 6 meses |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Comunicaciones** | Dual path | Fibra + 4G backup | Cumplir disponibilidad 95% |
| **Energía** | UPS local | 30 min autonomía | Continuidad durante cortes |
| **Controlador** | Almacenamiento local | Mensajes en memoria | Operación autónoma |
| **Software CCO** | Activo-Pasivo | Servidor backup | Continuidad operacional |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad:** 95% mensual mínimo (según AT4, PMV01)
- **MTBF:** 8,760 horas (1 año)
- **MTTR:** 4 horas
- **RTO (Recovery Time Objective):** < 2 horas
- **RPO (Recovery Point Objective):** < 15 minutos

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Panel LED** | Sí | Mensajes en paneles adyacentes |
| **Controlador local** | Sí | Almacenamiento local de mensajes |
| **Comunicaciones** | No | Fibra + 4G backup |
| **Software CCO** | No | Servidor backup |

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- Carcasas antivandalismo IK10 para paneles
- Controladores en gabinetes con cerradura
- Cámaras CCTV en ubicaciones críticas
- Estructuras ancladas con concreto
- Acceso controlado a equipos

### 6.2 Seguridad Lógica / Ciberseguridad

- Autenticación de operadores con roles definidos
- Cifrado TLS 1.2 para comunicaciones
- VLAN segregada para tráfico PMV
- Firewall entre red PMV y otras redes
- Logs de auditoría de todos los cambios
- Validación de mensajes antes de envío

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| NTCIP 1201 | Protocolo seguro para PMV |
| IEC 62471 | Seguridad fotobiológica LED |
| Manual Señalización 2015 | Contenido y ubicación mensajes |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Capas de la Aplicación

```
┌─────────────────────────────────┐
│   CAPA DE PRESENTACIÓN          │ (Interface Web CCO)
├─────────────────────────────────┤
│   CAPA DE LÓGICA DE NEGOCIO     │ (Validación, programación)
├─────────────────────────────────┤
│   CAPA DE COMUNICACIONES        │ (NTCIP 1203, TCP/IP)
├─────────────────────────────────┤
│   CAPA DE DATOS                 │ (Base datos mensajes/estado)
└─────────────────────────────────┘
```

### 7.2 Tecnologías Propuestas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **Frontend** | React.js + Bootstrap | Interface moderna y responsiva |
| **Backend** | Node.js + Express | Escalable y eficiente |
| **Base de Datos** | PostgreSQL | Robusta para datos críticos |
| **API** | REST + NTCIP 1203 | Estándar industria PMV |
| **Controlador** | Linux Embedded | Estable y confiable |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | IF-001 | NTCIP/TCP-IP | Alta | Mensajes, estado, alarmas |
| **Estaciones Peaje** | IF-002 | API REST | Media | Estado peajes, tarifas |
| **Bases Operación** | IF-003 | TCP/IP | Media | Información incidentes |
| **Sistema Info Usuarios** | IF-004 | API REST | Media | Mensajes coordinados |
| **Red Telecomunicaciones** | IF-005 | Fibra/4G | Alta | Conectividad |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Paneles LED** | 31 | 35 | 40 | Capacidad para 50 |
| **Mensajes/día** | 100 | 200 | 300 | Sistema para 500 |
| **Ancho banda** | 10 Mbps | 15 Mbps | 20 Mbps | Dimensionado 50 Mbps |
| **Almacenamiento** | 100 GB | 500 GB | 1 TB | Capacidad 2 TB |

### 9.2 Estrategia de Crecimiento

El sistema está diseñado para agregar paneles adicionales sin cambios en la arquitectura central. Cada nuevo panel requiere únicamente:
- Conexión a la red de fibra óptica existente
- Configuración en el software de gestión
- Asignación de dirección IP en VLAN 40

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Paneles LED** | Tecnología LED SMD | P10-P16 | Visibilidad y durabilidad |
| **Protocolo** | NTCIP 1203 | v3.0 | Estándar internacional PMV |
| **Comunicaciones** | Ethernet | 100/1000 Mbps | Confiable y estándar |
| **Controlador** | ARM Cortex | A72 quad-core | Procesamiento suficiente |

### 10.2 Interoperabilidad

- **Con sistemas ANI:** Cumplimiento NTCIP para integración futura
- **Con otros concesionarios:** Protocolo estándar permite integración
- **Con sistemas legados:** API REST para compatibilidad

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Paneles con Controlador Integrado

**Descripción:** Paneles LED con controlador integrado en la misma unidad

**Ventajas:**
- Menor costo inicial
- Instalación más simple
- Menos puntos de falla

**Desventajas:**
- Menor flexibilidad
- Dificultad mantenimiento
- Limitaciones procesamiento

**Costo estimado:** $1,500,000

### 11.2 Alternativa 2: Arquitectura Distribuida ⭐ **RECOMENDADA**

**Descripción:** Controladores separados con capacidad de procesamiento local

**Ventajas:**
- Mayor flexibilidad operacional
- Facilidad mantenimiento
- Operación autónoma
- Escalabilidad superior

**Desventajas:**
- Mayor costo inicial
- Más componentes

**Costo estimado:** $1,728,500

**Justificación de selección:** Mejor balance entre funcionalidad, mantenibilidad y cumplimiento de requisitos de disponibilidad.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Diseño detallado y especificaciones | 2 meses | T02 completado |
| **Fase 2** | Adquisición paneles y controladores | 3 meses | Diseño aprobado |
| **Fase 3** | Instalación infraestructura | 4 meses | Fibra óptica disponible |
| **Fase 4** | Instalación paneles zona piloto | 2 meses | Infraestructura lista |
| **Fase 5** | Pruebas y comisionamiento | 1 mes | Instalación completa |
| **Fase 6** | Despliegue completo | 3 meses | Zona piloto aprobada |

### 12.2 Hitos Críticos

- **H1:** Especificaciones técnicas aprobadas - Mes 2
- **H2:** Primer panel operativo (piloto) - Mes 7
- **H3:** Sistema completo operativo - Mes 12

---

## 13. PRÓXIMOS PASOS

- [ ] Validar arquitectura con fabricantes PMV certificados NTCIP
- [ ] Desarrollar especificaciones técnicas detalladas (T04)
- [ ] Realizar estudios de visibilidad en ubicaciones específicas
- [ ] Estimar costos detallados con cotizaciones reales
- [ ] Crear plan de pruebas de integración con CCO
- [ ] Obtener aprobación diseño con autoridades viales

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Sistemas ITS | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas ITS