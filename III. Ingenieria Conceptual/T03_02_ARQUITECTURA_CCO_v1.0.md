# T03: ARQUITECTURA CONCEPTUAL - CENTRO DE CONTROL DE OPERACIÓN (CCO)
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Centro de Control de Operación (CCO)  
**Responsable:** Ingeniero de Sistemas - Arquitecto de Soluciones  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define la arquitectura conceptual del Centro de Control de Operación (CCO), sistema neurálgico que centraliza la supervisión, control y coordinación de todos los sistemas del proyecto APP Sabana de Torres - Curumaní.

### 1.2 Alcance
Arquitectura completa del CCO incluyendo infraestructura física, sistemas de información, topología de red, integración con 13 sistemas externos, y operación 24/7/365 para supervisión de 272.1 km del corredor.

### 1.3 Referencias
- T01_02: Ficha de Sistema CCO - CAPEX $2.23M USD
- T02_02: Análisis de Requisitos CCO - 52 requisitos
- AT2: Sección 3.1.7, 3.3.3.3 - Plataforma tecnológica

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CENTRO DE CONTROL DE OPERACIÓN                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │   SALA CONTROL  │    │  SALA TÉCNICA   │    │ SALA REUNIONES  │         │
│  │                 │    │                 │    │                 │         │
│  │ • Videowall 4x3 │    │ • Serv SCADA    │    │ • Presentación  │         │
│  │ • 6 Puestos Op  │    │ • Serv BD       │    │ • Videoconf     │         │
│  │ • Audio/Alarmas │    │ • Storage SAN   │    │ • Reportes      │         │
│  │ • Comunicaciones│    │ • UPS/Respaldo  │    │                 │         │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
│           │                       │                       │                │
│  ┌─────────────────────────────────────────────────────────────────────────┤
│  │                        RED BACKBONE CCO                                 │
│  │  Core Switch Redundante + Firewall + Router Principal                  │
│  └─────────────────────────────────────────────────────────────────────────┤
│                                   │                                        │
└───────────────────────────────────┼────────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────────┐
    │                    RED WAN PROYECTO                                │
    │                                                                    │
    ├─ Estaciones Peaje (3) ────────┼─ Paneles LED (25)                 │
    ├─ Bases Operación (2) ─────────┼─ Ambulancias TAM (2)              │
    ├─ Puentes Peatonales (43) ─────┼─ Áreas Servicio                   │
    ├─ Sistema Iluminación ─────────┼─ Equipos Emergencia               │
    ├─ Intercambiadores (3) ────────┼─ Atención Cliente                 │
    ├─ Variantes ───────────────────┼─ Info Usuarios                    │
    └─ Red Telecomunicaciones ──────┴─ Sistemas Externos (ANI, Policía) │
```

**Descripción del diagrama:**
El CCO centraliza la supervisión de 14 sistemas distribuidos en 272.1 km, con arquitectura redundante que garantiza operación continua 24/7/365.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Videowall 4x3** | Visualización múltiple sistemas | 12 pantallas LED 55" ultra-estrecho | 1 sistema |
| **Puestos Operador** | Control y supervisión | Estación dual-monitor + HMI | 6 puestos |
| **Servidor SCADA Principal** | Control supervisorio | Dell PowerEdge R750, 64GB RAM | 1 unidad |
| **Servidor SCADA Respaldo** | Redundancia SCADA | Dell PowerEdge R750, 64GB RAM | 1 unidad |
| **Servidor Base Datos** | Almacenamiento histórico | Dell PowerEdge R750, 128GB RAM | 2 unidades |
| **Storage SAN** | Almacenamiento centralizado | Dell PowerVault, 100TB útiles | 1 sistema |
| **Core Switch Redundante** | Conectividad backbone | Cisco Catalyst 9500, 48 puertos | 2 unidades |
| **Firewall Corporativo** | Seguridad perimetral | Fortinet FortiGate 600E | 2 unidades |
| **UPS Centralizado** | Respaldo energético | APC Symmetra PX 40kVA | 1 sistema |
| **Generador Emergencia** | Respaldo prolongado | Caterpillar 100kVA, diesel | 1 unidad |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Red

- **Tipo de topología:** Estrella jerárquica con redundancia
- **Protocolo principal:** TCP/IP sobre Ethernet/Fibra óptica
- **Segmentación:** VLANs por sistema (SCADA, Videovigilancia, Gestión, DMZ)
- **Redundancia:** Sí - Dual-homing en todos los componentes críticos

### 3.2 Diagrama de Topología

```
                    ┌─────────────────────────────────────┐
                    │              INTERNET               │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────┴───────────────────┐
                    │          FIREWALL CLUSTER           │
                    │     (FortiGate 600E x2 - HA)       │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────┴───────────────────┐
                    │         CORE SWITCH STACK           │
                    │    (Cisco 9500 x2 - VSS/Stack)     │
                    └─┬─────────┬─────────┬─────────┬─────┘
                      │         │         │         │
            ┌─────────┴─┐ ┌─────┴─┐ ┌─────┴─┐ ┌─────┴─────┐
            │  VLAN 10  │ │VLAN 20│ │VLAN 30│ │  VLAN 40  │
            │   SCADA   │ │ CCTV  │ │ MGMT  │ │    DMZ    │
            └───────────┘ └───────┘ └───────┘ └───────────┘
                  │           │         │           │
            ┌─────┴─────┐ ┌───┴───┐ ┌───┴───┐ ┌─────┴─────┐
            │Servidores │ │ NVR   │ │Gestión│ │Servicios  │
            │SCADA x2   │ │Sistema│ │Red    │ │Web/API    │
            └───────────┘ └───────┘ └───────┘ └───────────┘
```

### 3.3 Distribución Física

**Ubicaciones principales:**
- **Sala de Control (80 m²):** Videowall, puestos operador, audio/alarmas
- **Sala Técnica (60 m²):** Servidores, storage, UPS, equipos red
- **Sala Reuniones (40 m²):** Presentaciones, videoconferencia
- **Área Soporte (30 m²):** Oficinas técnicos, almacén repuestos
- **Generador Exterior:** Caterpillar 100kVA con tanque 1000L

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo de Datos Principal

```
1. SISTEMAS CAMPO (14 sistemas distribuidos)
   ↓ (Fibra óptica / IP)
2. CONCENTRADORES LOCALES (Switches campo)
   ↓ (WAN/MPLS)
3. FIREWALL CCO (Filtrado y seguridad)
   ↓ (LAN interna)
4. SERVIDORES SCADA (Procesamiento tiempo real)
   ↓ (Base datos)
5. STORAGE SAN (Almacenamiento histórico)
   ↓ (Consultas)
6. PUESTOS OPERADOR (Visualización HMI)
   ↓ (Comandos)
7. VIDEOWALL (Presentación múltiple)
```

**Descripción del flujo:**
1. **Captura:** Sensores y equipos campo envían datos cada 30 segundos
2. **Concentración:** Switches locales agregan información por zona
3. **Transmisión:** WAN transporta datos al CCO via fibra óptica
4. **Procesamiento:** SCADA procesa alarmas y ejecuta lógicas
5. **Almacenamiento:** Base datos histórica con retención 5 años
6. **Visualización:** HMI presenta información procesada a operadores

### 4.2 Tipos de Datos

| Tipo de Dato | Formato | Volumen Estimado | Retención |
|:-------------|:--------|:-----------------|:----------|
| **Alarmas/Eventos** | JSON/XML | 50 MB/día | 5 años |
| **Video CCTV** | H.264/H.265 | 2 TB/día | 30 días |
| **Datos SCADA** | Modbus/OPC | 100 MB/día | 5 años |
| **Transacciones Peaje** | SQL Records | 200 MB/día | 25 años |
| **Reportes Gestión** | PDF/Excel | 10 MB/día | 10 años |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Servidores SCADA** | Activo-Pasivo | Cluster con failover automático | Cumplir disponibilidad 99.5% |
| **Core Switches** | Activo-Activo | VSS/Stack con LACP | Eliminar SPOF red |
| **Firewall** | Activo-Pasivo | HA con sincronización estado | Seguridad sin interrupción |
| **Alimentación** | N+1 | UPS + Generador + Bypass | Operación continua 24/7 |
| **Enlaces WAN** | Activo-Backup | Fibra principal + 4G backup | Conectividad garantizada |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad:** 99.5% mensual mínimo (según AT4)
- **MTBF:** 8,760 horas (1 año)
- **MTTR:** 4 horas máximo
- **RTO (Recovery Time Objective):** < 15 minutos
- **RPO (Recovery Point Objective):** < 5 minutos

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Servidores SCADA** | No | Cluster activo-pasivo |
| **Core Network** | No | Switches redundantes VSS |
| **Alimentación** | No | UPS + Generador + Bypass |
| **Conectividad WAN** | No | Fibra + 4G backup |
| **Personal Operador** | Sí | Múltiples turnos + guardia |

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- **Control acceso biométrico** a todas las salas CCO
- **CCTV perimetral** con grabación 30 días
- **Detección intrusión** con alarma a central monitoreo
- **Racks cerrados** con llaves individuales por sistema
- **Aire acondicionado redundante** para sala servidores

### 6.2 Seguridad Lógica / Ciberseguridad

- **Firewall perimetral** con IPS/IDS integrado
- **Segmentación VLANs** por tipo de tráfico
- **Autenticación multifactor** para acceso sistemas críticos
- **Logs centralizados** con SIEM para correlación eventos
- **Backup cifrado** con almacenamiento offsite
- **Actualizaciones seguridad** programadas mensualmente

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| **ISO 27001** | Sistema gestión seguridad información |
| **IEC 62443** | Ciberseguridad sistemas industriales SCADA |
| **NIST Cybersecurity Framework** | Marco referencia ciberseguridad |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Capas de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│   CAPA PRESENTACIÓN (HMI/Dashboard)                        │
│   • Wonderware InTouch / Ignition                          │
│   • Dashboards web responsivos                             │
│   • Aplicación móvil operadores                            │
├─────────────────────────────────────────────────────────────┤
│   CAPA LÓGICA NEGOCIO (SCADA Engine)                       │
│   • Wonderware System Platform / Ignition Gateway         │
│   • Lógicas control y alarmas                              │
│   • APIs REST para integración                             │
├─────────────────────────────────────────────────────────────┤
│   CAPA DATOS (Historian + RDBMS)                           │
│   • Wonderware Historian / InfluxDB                        │
│   • SQL Server / PostgreSQL                                │
│   • Almacenamiento distribuido                             │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Tecnologías Propuestas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **HMI/SCADA** | Wonderware/Ignition | Estándar industria, soporte local |
| **Base Datos** | SQL Server/PostgreSQL | Robustez, escalabilidad |
| **Historian** | Wonderware Historian | Optimizado para datos tiempo real |
| **API Integration** | REST/OPC-UA | Interoperabilidad sistemas |
| **Web Services** | .NET Core/Node.js | Performance y mantenibilidad |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **Estaciones Peaje** | IF-001 | TCP/IP | Alta | Transacciones, alarmas, video |
| **Bases Operación** | IF-002 | TCP/IP | Alta | Despacho emergencias, recursos |
| **Paneles LED** | IF-003 | NTCIP 1203 | Alta | Mensajes, estado paneles |
| **Telecomunicaciones** | IF-004 | SNMP | Alta | Estado red, ancho banda |
| **Ambulancias TAM** | IF-005 | Radio/4G | Alta | Ubicación GPS, estado |
| **Puentes Peatonales** | IF-006 | TCP/IP | Media | Estado estructural, iluminación |
| **Sistema Iluminación** | IF-007 | DALI/TCP | Media | Control, estado luminarias |
| **Áreas Servicio** | IF-008 | TCP/IP | Media | Ocupación, servicios |
| **Equipos Emergencia** | IF-009 | Radio | Alta | Disponibilidad, ubicación |
| **Atención Cliente** | IF-010 | TCP/IP | Media | PQRS, estadísticas |
| **Info Usuarios** | IF-011 | TCP/IP | Media | Mensajes, redes sociales |
| **Intercambiadores** | IF-012 | TCP/IP | Media | Estado vial, incidentes |
| **Variantes** | IF-013 | TCP/IP | Media | Condiciones tráfico |
| **ANI (SIINCO)** | IF-014 | VPN/HTTPS | Alta | Reportes, indicadores |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Puntos SCADA** | 2,000 | 3,000 | 4,000 | 5,000 (+25% margen) |
| **Cámaras CCTV** | 150 | 200 | 250 | 300 (+20% margen) |
| **Usuarios concurrentes** | 20 | 30 | 40 | 50 (+25% margen) |
| **Storage datos** | 10 TB | 50 TB | 100 TB | 150 TB (+50% margen) |
| **Ancho banda WAN** | 1 Gbps | 2 Gbps | 4 Gbps | 10 Gbps (fibra) |

### 9.2 Estrategia de Crecimiento

**Escalabilidad horizontal:** Adición de servidores SCADA en cluster  
**Escalabilidad vertical:** Upgrade RAM/CPU en servidores existentes  
**Escalabilidad almacenamiento:** Expansión SAN con discos adicionales  
**Escalabilidad red:** Upgrade switches a mayor capacidad sin cambio topología

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **SCADA Software** | Wonderware System Platform | 2023 | Estándar industria, soporte local |
| **Servidores** | Dell PowerEdge R750 | Gen 15 | Confiabilidad, soporte 24/7 |
| **Switches Core** | Cisco Catalyst 9500 | IOS-XE 17.x | Robustez, funcionalidades avanzadas |
| **Firewall** | Fortinet FortiGate 600E | FortiOS 7.x | Seguridad integral, performance |
| **UPS** | APC Symmetra PX | 40kVA | Confiabilidad, gestión remota |

### 10.2 Interoperabilidad

- **Con sistemas ANI:** Cumplimiento protocolos SIINCO y ANIscopio
- **Con Policía Carreteras:** Interface radio y datos según protocolos oficiales
- **Con sistemas legados:** Gateways OPC/Modbus para integración

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: SCADA Propietario Nacional

**Descripción:** Desarrollo SCADA con empresa colombiana

**Ventajas:**
- Menor costo inicial
- Soporte local garantizado
- Personalización total

**Desventajas:**
- Mayor riesgo técnico
- Menor madurez tecnológica
- Dependencia único proveedor

**Costo estimado:** $1,800,000 USD

### 11.2 Alternativa 2: SCADA Internacional ⭐ **RECOMENDADA**

**Descripción:** Wonderware/Ignition con integrador local certificado

**Ventajas:**
- Tecnología probada mundialmente
- Soporte técnico robusto
- Escalabilidad garantizada
- Interoperabilidad estándar

**Desventajas:**
- Mayor costo inicial
- Dependencia licenciamiento

**Costo estimado:** $2,230,000 USD

**Justificación de selección:** Balance óptimo entre confiabilidad, funcionalidad y soporte técnico para operación crítica 24/7/365.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Diseño detallado y especificaciones | 3 meses | T02 completado |
| **Fase 2** | Construcción infraestructura física | 4 meses | Diseño aprobado |
| **Fase 3** | Adquisición e instalación equipos | 6 meses | Infraestructura lista |
| **Fase 4** | Desarrollo e integración software | 8 meses | Equipos instalados |
| **Fase 5** | Pruebas y comisionamiento | 3 meses | Software integrado |
| **Fase 6** | Capacitación y puesta en operación | 2 meses | Pruebas aprobadas |

### 12.2 Hitos Críticos

- **H1:** Aprobación diseño arquitectónico - Mes 3
- **H2:** Infraestructura física completada - Mes 7
- **H3:** Equipos principales instalados - Mes 13
- **H4:** Integración sistemas críticos - Mes 18
- **H5:** CCO operativo 24/7 - Mes 24

---

## 13. PRÓXIMOS PASOS

- [ ] Validar arquitectura con fabricantes SCADA (Wonderware, Ignition)
- [ ] Desarrollar especificaciones técnicas detalladas servidores (T04)
- [ ] Estimar costos detallados con integradores certificados
- [ ] Crear plan de pruebas de integración con 14 sistemas
- [ ] Obtener aprobación arquitectónica de stakeholders
- [ ] Iniciar proceso de selección ubicación física CCO

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Sistemas - Arquitecto | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas - Arquitecto de Soluciones