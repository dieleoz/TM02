# T03: ARQUITECTURA CONCEPTUAL - TELECOMUNICACIONES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Telecomunicaciones  
**Responsable:** Ingeniero de Telecomunicaciones  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define la arquitectura conceptual del sistema de Telecomunicaciones, backbone de comunicaciones que interconecta todos los sistemas distribuidos en los 272.1 km del corredor con el CCO.

### 1.2 Alcance
Arquitectura completa de telecomunicaciones incluyendo red de fibra óptica, enlaces de respaldo, equipos de red, protocolos de comunicación y integración con 13 sistemas del proyecto.

### 1.3 Referencias
- T01_14: Ficha Sistema Telecomunicaciones - CAPEX $6.0M USD
- T02_14: Análisis Requisitos Telecomunicaciones - 48 requisitos
- AT2: Sección 3.1.7 - Plataforma tecnológica

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ARQUITECTURA TELECOMUNICACIONES                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌──────────────────────────────────┐    ┌─────────────┐ │
│  │    CCO      │    │         RED BACKBONE             │    │  SISTEMAS   │ │
│  │             │    │                                  │    │   CAMPO     │ │
│  │ • Core L3   │◄──►│  FIBRA ÓPTICA PRINCIPAL         │◄──►│ • Peajes    │ │
│  │ • Firewall  │    │  • 48 hilos SM G.652.D          │    │ • Bases     │ │
│  │ • Routers   │    │  • Topología anillo redundante   │    │ • Paneles   │ │
│  │ • Gestión   │    │  • DWDM para larga distancia     │    │ • Cámaras   │ │
│  └─────────────┘    └──────────────────────────────────┘    └─────────────┘ │
│         │                           │                              │        │
│  ┌─────────────┐    ┌──────────────────────────────────┐    ┌─────────────┐ │
│  │ ENLACES     │    │      NODOS INTERMEDIOS           │    │ SERVICIOS   │ │
│  │ BACKUP      │    │                                  │    │ EXTERNOS    │ │
│  │             │    │ • Repetidores cada 80km          │    │             │ │
│  │ • 4G/5G     │◄──►│ • Switches agregación L2/L3     │◄──►│ • Internet  │ │
│  │ • Satelital │    │ • Equipos DWDM                   │    │ • ANI       │ │
│  │ • Microondas│    │ • UPS locales                    │    │ • Policía   │ │
│  └─────────────┘    └──────────────────────────────────┘    └─────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Descripción del diagrama:**
Red de telecomunicaciones con topología anillo redundante en fibra óptica, conectando CCO con todos los sistemas distribuidos, incluyendo enlaces de respaldo múltiples.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Fibra Óptica Principal** | Backbone comunicaciones | 48 hilos SM G.652.D, ADSS | 272 km |
| **Cable Fibra Respaldo** | Redundancia backbone | 24 hilos SM G.652.D, ducto | 272 km |
| **Equipos DWDM** | Multiplexación óptica | Huawei OptiX OSN 1800 | 8 nodos |
| **Switches Core CCO** | Agregación central | Cisco Catalyst 9500-48Y4C | 2 unidades |
| **Switches Campo** | Conectividad local | Cisco IE-3400-8T2S | 45 unidades |
| **Routers Borde** | Conectividad WAN | Cisco ISR 4331 | 4 unidades |
| **Enlaces 4G Backup** | Respaldo celular | Cradlepoint IBR1700 | 15 unidades |
| **Sistema Gestión Red** | Monitoreo NOC | Cisco Prime Infrastructure | 1 licencia |
| **Repetidores Ópticos** | Amplificación señal | EDFA bidireccional | 6 unidades |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología de Red

- **Tipo de topología:** Anillo redundante con conexiones punto-multipunto
- **Protocolo principal:** Ethernet sobre fibra óptica (10GbE/1GbE)
- **Segmentación:** VLANs por sistema + QoS diferenciado
- **Redundancia:** Doble anillo + enlaces backup 4G/satelital

### 3.2 Diagrama de Topología

```
                    ┌─────────────────┐
                    │       CCO       │
                    │   (Nodo Core)   │
                    └─────┬─────┬─────┘
                          │     │
                    ┌─────┴─┐ ┌─┴─────┐
                    │Anillo │ │Anillo │
                    │  A    │ │   B   │
                    │(Ppal) │ │(Resp) │
                    └─────┬─┘ └─┬─────┘
                          │     │
    ┌─────────────────────┼─────┼─────────────────────┐
    │                     │     │                     │
┌───▼───┐             ┌───▼───┐ ┌───▼───┐         ┌───▼───┐
│Nodo 1 │◄───────────►│Nodo 2 │ │Nodo 3 │◄───────►│Nodo 4 │
│Peaje  │             │Bases  │ │Paneles│         │Áreas  │
│La Gómez│            │Oper.  │ │LED    │         │Servic.│
└───┬───┘             └───┬───┘ └───┬───┘         └───┬───┘
    │                     │         │                 │
    ▼                     ▼         ▼                 ▼
┌───────┐             ┌───────┐ ┌───────┐         ┌───────┐
│Sistemas│            │Sistemas│ │Sistemas│        │Sistemas│
│Locales │            │Locales │ │Locales │        │Locales │
└───────┘             └───────┘ └───────┘         └───────┘

    ┌─────────────────────────────────────────────────┐
    │              ENLACES BACKUP                     │
    │  • 4G/5G: 15 sitios críticos                   │
    │  • Satelital: 3 sitios remotos                 │
    │  • Microondas: 2 enlaces punto-punto           │
    └─────────────────────────────────────────────────┘
```

### 3.3 Distribución Física

**Nodos principales:**
- **CCO (Nodo Core):** Equipos centrales, gestión, interconexión externa
- **Nodo Peajes:** La Gómez, Morrison, Pailitas (3 ubicaciones)
- **Nodo Bases:** Base Norte, Base Sur (2 ubicaciones)
- **Nodos Intermedios:** Repetidores cada 80km (4 ubicaciones)
- **Nodos Servicios:** Áreas servicio, intercambiadores (8 ubicaciones)

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo de Datos Principal

```
1. SISTEMAS CAMPO (Sensores, cámaras, equipos)
   ↓ (Ethernet local)
2. SWITCHES CAMPO (Agregación local)
   ↓ (Fibra óptica 1GbE)
3. NODOS INTERMEDIOS (Switching L2/L3)
   ↓ (DWDM 10GbE)
4. CCO CORE NETWORK (Procesamiento central)
   ↓ (Routing/Switching)
5. SERVIDORES APLICACIÓN (SCADA, gestión)
   ↓ (Consultas/comandos)
6. INTERFACES EXTERNAS (ANI, Internet)
```

**Descripción del flujo:**
1. **Captura:** Equipos campo generan datos continuamente
2. **Agregación:** Switches locales concentran tráfico por zona
3. **Transporte:** DWDM multiplexa múltiples servicios en fibra
4. **Enrutamiento:** Core CCO distribuye tráfico según destino
5. **Procesamiento:** Servidores procesan información tiempo real
6. **Distribución:** Información procesada se distribuye a usuarios

### 4.2 Tipos de Datos

| Tipo de Dato | Protocolo | Ancho Banda | Latencia | Prioridad QoS |
|:-------------|:----------|:------------|:---------|:--------------|
| **Video CCTV** | RTSP/HTTP | 2-8 Mbps/cámara | < 200ms | Alta (DSCP 34) |
| **Datos SCADA** | Modbus/OPC | 1-10 Kbps/punto | < 100ms | Crítica (DSCP 46) |
| **Voz (Radio)** | SIP/RTP | 64 Kbps/canal | < 50ms | Crítica (DSCP 46) |
| **Gestión Red** | SNMP/SSH | 1-100 Kbps | < 500ms | Media (DSCP 18) |
| **Navegación Web** | HTTP/HTTPS | Variable | < 1s | Baja (DSCP 0) |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Fibra Backbone** | Anillo dual | Rutas físicas separadas | Eliminar SPOF transporte |
| **Equipos Core** | Activo-Activo | Stack/VSS con LACP | Disponibilidad 99.9% |
| **Enlaces WAN** | Activo-Backup | Fibra + 4G + Satelital | Conectividad garantizada |
| **Alimentación** | N+1 | UPS + Generador por nodo | Operación continua |
| **Gestión** | Activo-Pasivo | Servidores redundantes | Monitoreo sin interrupción |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad:** 99.9% mensual (8.76 horas downtime máximo)
- **MTBF:** 17,520 horas (2 años)
- **MTTR:** 4 horas máximo
- **Latencia:** < 100ms CCO ↔ Nodos campo
- **Pérdida paquetes:** < 0.1%

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Fibra Principal** | No | Anillo dual con rutas separadas |
| **Equipos Core CCO** | No | Stack redundante activo-activo |
| **Alimentación Nodos** | No | UPS + Generador por sitio |
| **Personal NOC** | Sí | Múltiples turnos + soporte remoto |
| **Proveedor Internet** | Sí | Múltiples ISPs con BGP |

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- **Fibra óptica armada** resistente a corte y roedores
- **Cámaras CCTV** en todos los nodos intermedios
- **Cercado perimetral** en repetidores y nodos críticos
- **Racks cerrados** con control acceso individual
- **Detección intrusión** en casetas equipos

### 6.2 Seguridad Lógica / Ciberseguridad

- **Segmentación VLANs** por tipo de tráfico y sistema
- **Firewall distribuido** en cada nodo con ACLs
- **Cifrado túneles** IPSec para tráfico crítico
- **Autenticación 802.1X** para acceso dispositivos
- **Monitoreo SIEM** con correlación eventos seguridad
- **Gestión certificados** PKI para autenticación mutua

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| **IEC 62443** | Ciberseguridad redes industriales |
| **ISO 27001** | Gestión seguridad información |
| **NIST SP 800-82** | Seguridad sistemas control industrial |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Capas de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│   CAPA GESTIÓN (Network Management)                        │
│   • Cisco Prime Infrastructure                             │
│   • SolarWinds NPM                                         │
│   • Dashboards personalizados                              │
├─────────────────────────────────────────────────────────────┤
│   CAPA CONTROL (SDN Controller)                            │
│   • Cisco DNA Center                                       │
│   • Políticas QoS automáticas                              │
│   • Aprovisionamiento automático                           │
├─────────────────────────────────────────────────────────────┤
│   CAPA INFRAESTRUCTURA (Network Devices)                   │
│   • Switches, Routers, DWDM                                │
│   • Protocolos: OSPF, BGP, MPLS, VXLAN                     │
│   • Monitoreo: SNMP, NetFlow, syslog                       │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Tecnologías Propuestas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **Gestión** | Cisco Prime + SolarWinds | Integración nativa equipos Cisco |
| **Control** | Cisco DNA Center | Automatización y políticas centralizadas |
| **Routing** | OSPF + BGP | Estándares abiertos, escalabilidad |
| **QoS** | DiffServ + Traffic Shaping | Garantía servicio aplicaciones críticas |
| **Monitoreo** | SNMP v3 + NetFlow | Visibilidad completa tráfico red |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Ancho Banda | Datos Intercambiados |
|:----------------|:----------|:----------|:------------|:---------------------|
| **CCO** | Fibra 10GbE | Ethernet | 10 Gbps | Todos los datos proyecto |
| **Estaciones Peaje** | Fibra 1GbE | Ethernet | 1 Gbps | Video, transacciones, SCADA |
| **Bases Operación** | Fibra 1GbE | Ethernet | 1 Gbps | Radio, video, datos |
| **Paneles LED** | Fibra 100Mbps | Ethernet | 100 Mbps | Mensajes, estado |
| **CCTV Distribuido** | Fibra 1GbE | Ethernet | Variable | Streams video H.264/H.265 |
| **Internet/ANI** | Fibra 1GbE | BGP/MPLS | 1 Gbps | Reportes, acceso remoto |
| **Backup 4G** | Celular | IP/GRE | 100 Mbps | Tráfico crítico backup |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Ancho Banda Core** | 2 Gbps | 5 Gbps | 8 Gbps | 20 Gbps (+150%) |
| **Nodos Conectados** | 45 | 60 | 80 | 100 (+25%) |
| **Cámaras IP** | 150 | 250 | 400 | 500 (+25%) |
| **Puntos SCADA** | 2,000 | 4,000 | 6,000 | 8,000 (+33%) |
| **Usuarios VPN** | 50 | 100 | 150 | 200 (+33%) |

### 9.2 Estrategia de Crecimiento

**Escalabilidad fibra:** 48 hilos permiten crecimiento 10x sin nueva instalación  
**Escalabilidad equipos:** Chassis modulares con slots expansión  
**Escalabilidad ancho banda:** Upgrade DWDM 10G→40G→100G sin cambio fibra  
**Escalabilidad nodos:** Topología anillo permite inserción nodos sin interrupción

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Fibra Óptica** | Corning SMF-28 G.652.D | Estándar | Baja atenuación, amplio espectro |
| **Switches Core** | Cisco Catalyst 9500 | IOS-XE 17.x | Robustez, funcionalidades avanzadas |
| **DWDM** | Huawei OptiX OSN 1800 | V100R019 | Costo-beneficio, soporte local |
| **Gestión** | Cisco Prime Infrastructure | 3.10 | Integración nativa Cisco |
| **Monitoreo** | SolarWinds NPM | 2023.4 | Visibilidad completa red |

### 10.2 Interoperabilidad

- **Con sistemas ANI:** Cumplimiento protocolos SIINCO para reportes
- **Con operadores celulares:** Interfaces estándar 4G/5G
- **Con proveedores Internet:** BGP estándar para redundancia
- **Con sistemas legados:** Gateways protocolo para integración

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Red Híbrida Fibra + Microondas

**Descripción:** Combinación fibra óptica tramos principales + microondas enlaces secundarios

**Ventajas:**
- Menor inversión inicial fibra
- Flexibilidad despliegue rápido
- Menor dependencia infraestructura civil

**Desventajas:**
- Mayor latencia microondas
- Susceptible condiciones climáticas
- Menor ancho banda disponible

**Costo estimado:** $4,800,000 USD

### 11.2 Alternativa 2: Red Full Fibra Óptica ⭐ **RECOMENDADA**

**Descripción:** Fibra óptica extremo-extremo con anillo redundante completo

**Ventajas:**
- Máximo ancho banda disponible
- Latencia mínima garantizada
- Inmune interferencias electromagnéticas
- Escalabilidad futura garantizada
- Confiabilidad superior

**Desventajas:**
- Mayor inversión inicial
- Tiempo despliegue más largo
- Dependencia infraestructura civil

**Costo estimado:** $6,000,000 USD

**Justificación de selección:** Para operación crítica 24/7/365 con 25 años vida útil, la confiabilidad y escalabilidad de fibra óptica justifican la inversión adicional.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Diseño detallado red y permisos | 4 meses | T02 completado |
| **Fase 2** | Construcción infraestructura civil | 8 meses | Permisos aprobados |
| **Fase 3** | Instalación fibra óptica | 10 meses | Infraestructura lista |
| **Fase 4** | Instalación equipos activos | 6 meses | Fibra instalada |
| **Fase 5** | Configuración y pruebas | 4 meses | Equipos instalados |
| **Fase 6** | Integración sistemas y puesta en operación | 3 meses | Pruebas aprobadas |

### 12.2 Hitos Críticos

- **H1:** Permisos construcción aprobados - Mes 4
- **H2:** 50% fibra óptica instalada - Mes 16
- **H3:** Equipos core CCO operativos - Mes 24
- **H4:** Anillo principal completo - Mes 28
- **H5:** Red completa operativa - Mes 32

---

## 13. PRÓXIMOS PASOS

- [ ] Validar arquitectura con fabricantes (Cisco, Huawei, Corning)
- [ ] Desarrollar especificaciones técnicas fibra óptica (T04)
- [ ] Estimar costos detallados con contratistas especializados
- [ ] Crear plan de pruebas de integración extremo-extremo
- [ ] Obtener aprobación arquitectónica de stakeholders
- [ ] Iniciar trámites permisos construcción infraestructura

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Telecomunicaciones | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Telecomunicaciones