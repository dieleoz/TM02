# T03: ARQUITECTURA CONCEPTUAL - ESTACIONES DE PEAJE
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Estaciones de Peaje  
**Responsable:** Ingeniero de Sistemas de Peaje  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define la arquitectura conceptual de las 3 Estaciones de Peaje del proyecto, sistemas críticos para la generación de ingresos y control de acceso al corredor concesionado.

### 1.2 Alcance
Arquitectura completa de las estaciones de peaje La Gómez (con reubicación), Morrison y Pailitas, incluyendo sistemas TAG/DSRC, videovigilancia, control de acceso, infraestructura civil y integración con CCO.

### 1.3 Referencias
- T01_01: Ficha Sistema Estaciones Peaje - CAPEX $4.0M USD
- T02_01: Análisis Requisitos Estaciones Peaje - 45 requisitos
- AT1: Ubicaciones obligatorias de peajes

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ESTACIONES DE PEAJE (3 UBICACIONES)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │   LA GÓMEZ      │    │    MORRISON     │    │    PAILITAS     │         │
│  │ (Reubicación)   │    │   (Existente)   │    │   (Nueva)       │         │
│  │                 │    │                 │    │                 │         │
│  │ • 6 Carriles    │    │ • 4 Carriles    │    │ • 4 Carriles    │         │
│  │ • 2 Casetas     │    │ • 2 Casetas     │    │ • 2 Casetas     │         │
│  │ • TAG/Manual    │    │ • TAG/Manual    │    │ • TAG/Manual    │         │
│  │ • CCTV/Foto     │    │ • CCTV/Foto     │    │ • CCTV/Foto     │         │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
│           │                       │                       │                │
│  ┌─────────────────────────────────────────────────────────────────────────┤
│  │                        SISTEMAS COMUNES                                 │
│  │                                                                         │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │
│  │ │   SISTEMA   │ │   SISTEMA   │ │   SISTEMA   │ │   SISTEMA   │        │
│  │ │    TAG      │ │    CCTV     │ │  CONTROL    │ │ COMUNICAC.  │        │
│  │ │             │ │             │ │   ACCESO    │ │             │        │
│  │ │ • Antenas   │ │ • Cámaras   │ │ • Barreras  │ │ • Fibra     │        │
│  │ │ • Lectores  │ │ • NVR       │ │ • Semáforos │ │ • Switches  │        │
│  │ │ • Clasific. │ │ • Analytics │ │ • Sensores  │ │ • Routers   │        │
│  │ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘        │
│  └─────────────────────────────────────────────────────────────────────────┤
│                                   │                                        │
└───────────────────────────────────┼────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │          INTEGRACIÓN         │
                    │                              │
                    ├─ CCO (Supervisión) ─────────┼─ ANI (Reportes)          │
                    ├─ Bancos (Recaudo) ──────────┼─ Policía (Infracciones)  │
                    ├─ Usuarios (Consultas) ──────┼─ Proveedores TAG         │
                    └─ Interventoría (Auditoría) ─┴─ Sistemas Externos       │
```

**Descripción del diagrama:**
Tres estaciones de peaje con arquitectura estandarizada, sistemas TAG/DSRC para cobro automático, videovigilancia para control y evidencia, integración completa con CCO y sistemas externos.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Casetas de Peaje** | Recaudo manual/mixto | Estructura prefabricada climatizada | 6 unidades |
| **Pórticos TAG** | Soporte antenas DSRC | Estructura metálica galvanizada | 3 unidades |
| **Antenas DSRC** | Lectura tags 5.9GHz | Kapsch/TransCore, alcance 30m | 14 unidades |
| **Cámaras CCTV** | Videovigilancia/OCR | IP 4K, analytics integrado | 36 unidades |
| **Barreras Automáticas** | Control acceso vehicular | Brazo 6m, tiempo apertura 3s | 14 unidades |
| **Clasificadores Vehículos** | Detección tipo/ejes | Lazos inductivos + sensores | 14 sistemas |
| **Servidores Locales** | Procesamiento local | Dell PowerEdge R450 | 6 unidades |
| **UPS Sistemas** | Respaldo energético | APC Smart-UPS 10kVA | 6 unidades |
| **Switches Red** | Conectividad local | Cisco IE-3400-8T2S | 12 unidades |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Red por Estación

- **Tipo de topología:** Estrella con redundancia en equipos críticos
- **Protocolo principal:** Ethernet TCP/IP + protocolos propietarios TAG
- **Segmentación:** VLANs por función (TAG, CCTV, Gestión, Usuarios)
- **Redundancia:** Enlaces duales a CCO + backup 4G

### 3.2 Diagrama de Topología

```
                    ┌─────────────────────────────────┐
                    │              CCO                │
                    │        (Supervisión)            │
                    └─────────────┬───────────────────┘
                                  │
                    ┌─────────────┴───────────────────┐
                    │         RED WAN PROYECTO        │
                    │      (Fibra Óptica MPLS)       │
                    └─┬─────────────┬─────────────┬───┘
                      │             │             │
        ┌─────────────▼─┐ ┌─────────▼─┐ ┌─────────▼─┐
        │  PEAJE        │ │  PEAJE    │ │  PEAJE    │
        │  LA GÓMEZ     │ │ MORRISON  │ │ PAILITAS  │
        └─┬─────────────┘ └─┬─────────┘ └─┬─────────┘
          │                 │             │
    ┌─────▼─────┐     ┌─────▼─────┐ ┌─────▼─────┐
    │Switch Core│     │Switch Core│ │Switch Core│
    │Redundante │     │Redundante │ │Redundante │
    └─┬─┬─┬─┬───┘     └─┬─┬─┬─┬───┘ └─┬─┬─┬─┬───┘
      │ │ │ │           │ │ │ │       │ │ │ │
   ┌──▼─▼─▼─▼──┐    ┌──▼─▼─▼─▼──┐ ┌──▼─▼─▼─▼──┐
   │VLAN 10:TAG│    │VLAN 10:TAG│ │VLAN 10:TAG│
   │VLAN 20:CCTV│   │VLAN 20:CCTV│ │VLAN 20:CCTV│
   │VLAN 30:MGMT│   │VLAN 30:MGMT│ │VLAN 30:MGMT│
   │VLAN 40:USER│   │VLAN 40:USER│ │VLAN 40:USER│
   └────────────┘   └────────────┘ └────────────┘
```

### 3.3 Distribución Física por Estación

**Áreas principales:**
- **Plaza de Peaje:** Casetas, pórticos, barreras (área operativa)
- **Edificio Técnico:** Servidores, UPS, equipos red (30 m²)
- **Oficina Administrativa:** Supervisor, archivo, reuniones (20 m²)
- **Área Mantenimiento:** Taller, repuestos, herramientas (15 m²)
- **Estacionamiento:** Personal y usuarios (200 m²)

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo de Datos Principal

```
1. VEHÍCULO INGRESA (Detección automática)
   ↓
2. CLASIFICACIÓN (Tipo vehículo, número ejes)
   ↓
3. LECTURA TAG (Antena DSRC 5.9GHz)
   ↓ (Si tiene TAG válido)
4. VALIDACIÓN (Base datos local + CCO)
   ↓
5. CÁLCULO TARIFA (Según clasificación)
   ↓
6. CAPTURA EVIDENCIA (Foto/video vehículo)
   ↓
7. APERTURA BARRERA (Automática)
   ↓
8. REGISTRO TRANSACCIÓN (Local + CCO)
   ↓
9. REPORTE SISTEMAS (ANI, Bancos, Auditoría)
```

**Descripción del flujo:**
Proceso completamente automatizado para vehículos con TAG, con fallback a proceso manual para vehículos sin TAG o con problemas de lectura.

### 4.2 Tipos de Datos

| Tipo de Dato | Formato | Volumen Estimado | Retención |
|:-------------|:--------|:-----------------|:----------|
| **Transacciones Peaje** | XML/JSON | 100 MB/día/estación | 25 años |
| **Video Evidencia** | H.264 | 500 GB/día/estación | 5 años |
| **Fotos Vehículos** | JPEG | 50 GB/día/estación | 5 años |
| **Datos TAG** | Binario | 10 MB/día/estación | 10 años |
| **Logs Sistema** | Texto | 5 MB/día/estación | 2 años |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Servidores Locales** | Activo-Pasivo | Cluster con failover | Operación continua recaudo |
| **Enlaces Comunicación** | Activo-Backup | Fibra + 4G backup | Conectividad garantizada CCO |
| **Alimentación Eléctrica** | N+1 | UPS + Generador | Operación 24/7/365 |
| **Antenas DSRC** | N+1 | Antenas adicionales | Cobertura sin puntos ciegos |
| **Switches Red** | Activo-Pasivo | Stack redundante | Conectividad sin SPOF |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad:** 99.5% mensual (3.6 horas downtime máximo)
- **MTBF:** 8,760 horas (1 año)
- **MTTR:** 2 horas máximo
- **Tiempo respuesta TAG:** < 500ms
- **Precisión clasificación:** > 99%

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Servidor Principal** | No | Cluster activo-pasivo |
| **Conectividad CCO** | No | Fibra + 4G backup |
| **Alimentación** | No | UPS + Generador |
| **Personal Operador** | Sí | Múltiples turnos + soporte remoto |
| **Infraestructura Civil** | Sí | Mantenimiento preventivo |

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- **Perímetro cercado** con control acceso biométrico
- **CCTV perimetral** con detección intrusión
- **Iluminación LED** perimetral con respaldo
- **Casetas blindadas** nivel B4 resistente balas
- **Caja fuerte** para efectivo con doble llave
- **Alarma silenciosa** conectada a central monitoreo

### 6.2 Seguridad Lógica / Ciberseguridad

- **Firewall local** con IPS/IDS integrado
- **Cifrado transacciones** AES-256 extremo-extremo
- **Autenticación multifactor** para operadores
- **Segregación redes** por función (TAG/CCTV/Gestión)
- **Logs auditables** con firma digital
- **Backup cifrado** con almacenamiento seguro

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| **PCI DSS** | Manejo datos tarjetas crédito |
| **ISO 27001** | Gestión seguridad información |
| **Ley 1581/2012** | Protección datos personales |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Capas de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│   CAPA PRESENTACIÓN (Interfaces Usuario)                   │
│   • HMI Operador (Wonderware/Ignition)                     │
│   • Portal Web Consultas                                   │
│   • App Móvil Supervisores                                 │
├─────────────────────────────────────────────────────────────┤
│   CAPA LÓGICA NEGOCIO (Motor Peaje)                        │
│   • Motor transaccional                                    │
│   • Reglas tarifarias                                      │
│   • Validaciones TAG                                       │
│   • Generación reportes                                    │
├─────────────────────────────────────────────────────────────┤
│   CAPA DATOS (Base Datos + Historian)                      │
│   • SQL Server (transacciones)                             │
│   • Historian (eventos)                                    │
│   • File System (evidencias)                               │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Tecnologías Propuestas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **Motor Peaje** | .NET Core/Java | Performance transaccional |
| **Base Datos** | SQL Server | Robustez, transacciones ACID |
| **HMI** | Wonderware InTouch | Estándar industria peajes |
| **Comunicación TAG** | DSRC 5.9GHz | Estándar internacional |
| **Web Services** | REST API | Integración sistemas externos |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | Fibra óptica | TCP/IP | Alta | Transacciones, video, alarmas |
| **ANI (SIINCO)** | VPN Internet | HTTPS/XML | Alta | Reportes recaudo, tráfico |
| **Bancos** | Línea dedicada | ISO 8583 | Alta | Transacciones tarjetas |
| **Proveedores TAG** | Internet | Web Services | Alta | Validación cuentas |
| **Policía Carreteras** | Radio/Internet | Propietario | Media | Infracciones, alertas |
| **Sistema Info Usuarios** | LAN | TCP/IP | Media | Estado peajes, tarifas |
| **Interventoría** | VPN | HTTPS | Media | Auditorías, reportes |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Transacciones/día** | 15,000 | 25,000 | 35,000 | 50,000 (+43%) |
| **Vehículos TAG** | 60% | 80% | 90% | 95% penetración |
| **Carriles operativos** | 14 | 16 | 18 | 20 (+43%) |
| **Storage evidencias** | 2 TB | 10 TB | 20 TB | 30 TB (+50%) |
| **Ancho banda** | 100 Mbps | 200 Mbps | 500 Mbps | 1 Gbps |

### 9.2 Estrategia de Crecimiento

**Escalabilidad carriles:** Infraestructura preparada para 2 carriles adicionales por estación  
**Escalabilidad servidores:** Arquitectura cluster permite adición nodos sin interrupción  
**Escalabilidad storage:** SAN expandible con discos adicionales  
**Escalabilidad red:** Switches modulares con puertos expansión

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Sistema TAG** | Kapsch ETC | 5.9GHz DSRC | Líder mundial, soporte local |
| **Servidores** | Dell PowerEdge R450 | Gen 15 | Confiabilidad, soporte 24/7 |
| **CCTV** | Axis Communications | ARTPEC-8 | Calidad imagen, analytics |
| **Software Peaje** | Kapsch TCS | v8.5 | Integración nativa hardware |
| **Base Datos** | Microsoft SQL Server | 2022 | Robustez transaccional |

### 10.2 Interoperabilidad

- **Con sistemas ANI:** Cumplimiento protocolos SIINCO
- **Con bancos:** Estándares ISO 8583 para transacciones
- **Con otros concesionarios:** Interoperabilidad TAG nacional
- **Con proveedores TAG:** APIs estándar validación cuentas

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Sistema TAG Nacional Existente

**Descripción:** Integración con sistema TAG existente sin infraestructura propia

**Ventajas:**
- Menor inversión inicial
- Interoperabilidad inmediata
- Menor complejidad técnica

**Desventajas:**
- Dependencia proveedor externo
- Menor control operacional
- Comisiones por transacción

**Costo estimado:** $2,500,000 USD

### 11.2 Alternativa 2: Sistema TAG Propio ⭐ **RECOMENDADA**

**Descripción:** Implementación sistema TAG propio con interoperabilidad

**Ventajas:**
- Control total operacional
- Menores costos operativos
- Flexibilidad tarifaria
- Mejor integración CCO

**Desventajas:**
- Mayor inversión inicial
- Mayor complejidad técnica
- Responsabilidad mantenimiento

**Costo estimado:** $4,000,000 USD

**Justificación de selección:** Para concesión 25 años, el control operacional y menores costos operativos justifican la inversión adicional.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Diseño detallado y especificaciones | 4 meses | T02 completado |
| **Fase 2** | Construcción infraestructura civil | 8 meses | Diseño aprobado |
| **Fase 3** | Instalación equipos y sistemas | 6 meses | Infraestructura lista |
| **Fase 4** | Desarrollo e integración software | 8 meses | Equipos instalados |
| **Fase 5** | Pruebas y certificación | 4 meses | Software integrado |
| **Fase 6** | Capacitación y puesta en operación | 2 meses | Pruebas aprobadas |

### 12.2 Hitos Críticos

- **H1:** Aprobación diseño arquitectónico - Mes 4
- **H2:** Infraestructura civil completada - Mes 12
- **H3:** Equipos principales instalados - Mes 18
- **H4:** Sistema TAG certificado - Mes 24
- **H5:** Peajes operativos 24/7 - Mes 30

---

## 13. PRÓXIMOS PASOS

- [ ] Validar arquitectura con fabricantes TAG (Kapsch, TransCore)
- [ ] Desarrollar especificaciones técnicas equipos (T04)
- [ ] Estimar costos detallados con integradores certificados
- [ ] Crear plan de pruebas interoperabilidad TAG
- [ ] Obtener aprobación arquitectónica de stakeholders
- [ ] Iniciar proceso certificación sistema TAG con ANI

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Sistemas Peaje | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas de Peaje