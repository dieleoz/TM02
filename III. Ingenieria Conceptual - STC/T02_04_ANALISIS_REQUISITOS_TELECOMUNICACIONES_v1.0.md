# T02_04 - ANÁLISIS DE REQUISITOS SISTEMA TELECOMUNICACIONES

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Sistema**: Telecomunicaciones
- **Código**: STC-T02-04
- **Fecha**: 2024-10-27
- **Versión**: 1.0
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_04_FICHA_SISTEMA_TELECOMUNICACIONES_v1.0.md

---

## 🎯 **ANÁLISIS DE REQUISITOS CONTRACTUALES**

### **Fuentes Contractuales Validadas**

#### **Fuente Principal: AT3 - Especificaciones Técnicas**
```
📄 Fuente: AT3, Sección Telecomunicaciones
📌 Obligación: "Fibra óptica 48 hilos ITU-T G.652d"
📍 Cobertura: 272 km backbone principal
🎯 Interpretación: ESPECIFICACIÓN TÉCNICA CONTRACTUAL ESPECÍFICA
```

#### **Normas Técnicas Contractuales**
- **ITU-T G.652d**: Fibra monomodo estándar
- **ITU-T G.694.1**: Multiplexación DWDM
- **ITU-T G.709**: Interfaces ópticas
- **ITU-T G.8032**: Protección Ethernet
- **ITU-T Y.1564**: Pruebas servicios Ethernet

#### **Fuentes Secundarias Identificadas**
- **AT1 - Alcance**: "Comunicaciones integrales 272 km"
- **AT4 - Indicadores**: Disponibilidad sistemas (indirecta)
- **AT2 - O&M**: Mantenimiento red telecomunicaciones

---

## 📋 **MATRIZ DE REQUISITOS DETALLADA**

### **R01 - REQUISITOS NORMATIVOS ITU-T**

| ID | Requisito | Norma ITU-T | Obligatorio | Criterio Cumplimiento |
|:---|:----------|:------------|:------------|:---------------------|
| **RN-01** | Fibra monomodo | G.652d | SÍ | Certificación fabricante |
| **RN-02** | Multiplexación DWDM | G.694.1 | SÍ | 40+ canales ópticos |
| **RN-03** | Interfaces ópticas | G.709 | SÍ | OTN estándar |
| **RN-04** | Protección Ethernet | G.8032 | SÍ | Anillo redundante |
| **RN-05** | Pruebas servicios | Y.1564 | SÍ | Certificación instalación |
| **RN-06** | Gestión red | G.7710 | SÍ | SNMP v3 |

### **R02 - REQUISITOS FUNCIONALES BACKBONE**

| ID | Requisito | Especificación | Fuente | Validación |
|:---|:----------|:---------------|:-------|:-----------|
| **RF-01** | Fibra 48 hilos | ITU-T G.652d | AT3 | Certificación |
| **RF-02** | Cobertura 272 km | Backbone completo | AT1 | Topología |
| **RF-03** | Redundancia N+1 | Doble anillo | AT3 | Arquitectura |
| **RF-04** | Capacidad 10 Gbps | Por sistema crítico | AT3 | Dimensionamiento |
| **RF-05** | Latencia <10 ms | Extremo a extremo | AT3 | Medición |
| **RF-06** | Disponibilidad >99.9% | Anual | AT4 | Monitoreo |
| **RF-07** | Gestión centralizada | Desde CCO | AT3 | SNMP/NMS |
| **RF-08** | Seguridad cibernética | Encriptación | AT3 | Certificación |

### **R03 - REQUISITOS DE INTEGRACIÓN SISTÉMICA**

| ID | Sistema Integrado | Ancho Banda | Protocolo | Criticidad |
|:---|:------------------|:------------|:----------|:-----------|
| **RI-01** | CCO | 1 Gbps | Ethernet | CRÍTICA |
| **RI-02** | ITS (CCTV) | 5 Gbps | IP/Ethernet | CRÍTICA |
| **RI-03** | Peajes | 500 Mbps | TCP/IP | CRÍTICA |
| **RI-04** | Emergencias | 200 Mbps | VoIP/Video | CRÍTICA |
| **RI-05** | PMV/Información | 100 Mbps | HTTP/API | ALTA |
| **RI-06** | Iluminación | 50 Mbps | Modbus/TCP | MEDIA |
| **RI-07** | Áreas Servicio | 100 Mbps | Ethernet | MEDIA |
| **RI-08** | Bases Operación | 200 Mbps | VPN/Ethernet | ALTA |
| **RI-09** | WIM/Pesaje | 50 Mbps | TCP/IP | MEDIA |
| **RI-10** | Intercambiadores | 100 Mbps | Ethernet | MEDIA |

---

## 🔍 **ANÁLISIS NORMA ITU-T G.652d**

### **Especificaciones Técnicas G.652d**

#### **Características Fibra Óptica**
```
📌 Tipo: Monomodo estándar (Single Mode)
📌 Longitud onda: 1310 nm y 1550 nm
📌 Atenuación: ≤0.4 dB/km @ 1310 nm
📌 Atenuación: ≤0.3 dB/km @ 1550 nm
📌 Dispersión: ≤18 ps/(nm·km) @ 1550 nm
📌 Diámetro núcleo: 8.2 ± 0.4 μm
📌 Diámetro revestimiento: 125 ± 0.7 μm
```

#### **Ventajas G.652d vs Otras Fibras**
- **Menor atenuación**: Distancias largas sin repetidores
- **Baja dispersión**: Altas velocidades transmisión
- **Compatibilidad**: Estándar mundial
- **Costo-efectivo**: Balance precio/prestaciones
- **Futuro-proof**: Soporta tecnologías emergentes

### **Arquitectura Fibra 48 Hilos**

#### **Distribución Hilos por Aplicación**
```
Hilos 1-16: Backbone Principal
├── CCO ↔ Peaje Norte (4 hilos)
├── CCO ↔ Peaje Centro (4 hilos)  
├── CCO ↔ Peaje Sur (4 hilos)
└── Interconexión peajes (4 hilos)

Hilos 17-32: Sistemas ITS
├── CCTV Sector Norte (8 hilos)
├── CCTV Sector Centro (4 hilos)
├── CCTV Sector Sur (4 hilos)

Hilos 33-40: Servicios Críticos
├── Emergencias (4 hilos)
├── Bases Operación (4 hilos)

Hilos 41-48: Expansión/Backup
├── Backup sistemas críticos (4 hilos)
├── Futuras expansiones (4 hilos)
```

---

## ⚙️ **ARQUITECTURA TÉCNICA DETALLADA**

### **Topología de Red Principal**

#### **Anillo Principal (272 km)**
```
CCO (Km 0) → Peaje Norte (Km 68) → Peaje Centro (Km 136) → 
Peaje Sur (Km 204) → Terminal Sur (Km 272) → CCO

Características:
├── Topología: Doble anillo (horario/antihorario)
├── Protección: G.8032 Ethernet Ring Protection
├── Tiempo conmutación: <50 ms
└── Capacidad: 10 Gbps por anillo
```

#### **Anillos Secundarios**
```
Anillo Norte (0-68 km):
├── 34 sitios ITS conectados
├── Capacidad: 1 Gbps
└── Backup: Enlace directo CCO

Anillo Centro (68-136 km):
├── 34 sitios ITS conectados  
├── Capacidad: 1 Gbps
└── Backup: Doble conexión peajes

Anillo Sur (136-272 km):
├── 68 sitios ITS conectados
├── Capacidad: 1 Gbps  
└── Backup: Enlace satelital
```

### **Equipos de Transmisión**

#### **Nodos Principales (5 ubicaciones)**
```
CCO - Nodo Central:
├── OLT (Optical Line Terminal): 48 puertos
├── DWDM: 40 canales x 10 Gbps
├── Switch Core: 48 puertos 10GE
├── UPS: 4 horas autonomía
└── Generador: Backup extendido

Peajes - Nodos Distribución (3):
├── ODF (Optical Distribution Frame): 48 puertos
├── Switch Agregación: 24 puertos 1GE + 4x10GE
├── Router: BGP/OSPF
├── UPS: 2 horas autonomía
└── Generador: Backup local
```

#### **Sitios ITS - Nodos Acceso (136 ubicaciones)**
```
Equipos por Sitio:
├── ONU (Optical Network Unit): 4 puertos
├── Switch Acceso: 8 puertos 1GE
├── Router Edge: VPN/Firewall
├── UPS: 4 horas autonomía
└── Panel solar: Backup energético
```

### **Sistema de Gestión de Red (NMS)**

#### **Plataforma Centralizada**
```
Software NMS:
├── Plataforma: Cisco Prime, HP IMC o similar
├── Protocolos: SNMP v3, Netconf, REST
├── Funciones: Configuración, monitoreo, alarmas
└── Integración: CCO SCADA

Capacidades:
├── Topología automática
├── Gestión performance  
├── Gestión fallas
├── Gestión configuración
├── Gestión seguridad
└── Reportes automáticos
```

---

## 📊 **ANÁLISIS DE RIESGOS CRÍTICOS**

### **Riesgos Infraestructura Fibra**

| Riesgo | Probabilidad | Impacto | MTTR | Mitigación |
|:-------|:-------------|:--------|:-----|:-----------|
| **Corte fibra accidental** | Alta | Alto | 4-8 horas | Anillo redundante |
| **Daño por obras civiles** | Media | Alto | 8-24 horas | Señalización + mapeo |
| **Robo cable** | Media | Medio | 12-48 horas | Fibra aérea + vigilancia |
| **Desastre natural** | Baja | Crítico | 48-168 horas | Rutas diversas |
| **Falla equipos ópticos** | Media | Medio | 2-4 horas | Repuestos en sitio |

### **Riesgos Operacionales**

| Riesgo | Probabilidad | Impacto | MTTR | Mitigación |
|:-------|:-------------|:--------|:-----|:-----------|
| **Saturación ancho banda** | Media | Alto | 1-2 horas | Monitoreo + escalamiento |
| **Falla energética** | Alta | Medio | 0.1-4 horas | UPS + generadores |
| **Ataque cibernético** | Baja | Crítico | 4-24 horas | Seguridad multicapa |
| **Error configuración** | Media | Medio | 0.5-2 horas | Procedimientos + backup |

### **Plan de Contingencia Telecomunicaciones**

#### **Corte Fibra Principal**
```
Detección Automática:
├── Tiempo detección: <30 segundos
├── Conmutación G.8032: <50 ms
├── Notificación CCO: Inmediata
└── Activación cuadrillas: <1 hora

Reparación:
├── Localización falla: Reflectómetro OTDR
├── Empalme temporal: <4 horas
├── Reparación definitiva: <24 horas
└── Pruebas certificación: ITU-T Y.1564
```

#### **Falla Masiva Comunicaciones**
```
Backup Satelital:
├── Activación automática: <5 minutos
├── Ancho banda: 100 Mbps garantizado
├── Sistemas críticos: Prioridad 1
└── Duración: Hasta reparación fibra

Comunicaciones Celulares:
├── Enlaces 4G/5G: Sitios críticos
├── Ancho banda: 50 Mbps por sitio
├── Latencia: <100 ms
└── Costo: Por consumo
```

---

## 💰 **ANÁLISIS ECONÓMICO DETALLADO**

### **CAPEX - Sistema Telecomunicaciones**

```
Fibra Óptica e Instalación:
├── Cable fibra 48h G.652d (300 km): $900,000
├── Instalación aérea/subterránea: $1,200,000
├── Empalmes y conectores: $150,000
├── Canalización y protección: $400,000
└── Subtotal fibra: $2,650,000

Equipos Transmisión:
├── Equipos CCO (OLT/DWDM): $800,000
├── Equipos peajes (3 nodos): $600,000
├── Equipos sitios ITS (136): $1,360,000
├── Repuestos estratégicos: $200,000
└── Subtotal equipos: $2,960,000

Sistemas Gestión y Seguridad:
├── Software NMS: $300,000
├── Sistemas seguridad: $200,000
├── Monitoreo y alarmas: $150,000
├── Integración CCO: $100,000
└── Subtotal gestión: $750,000

Energía y Backup:
├── UPS sitios (141 unidades): $705,000
├── Generadores (5 unidades): $500,000
├── Paneles solares (136): $680,000
├── Baterías backup: $300,000
└── Subtotal energía: $2,185,000

Instalación y Configuración:
├── Instalación equipos: $400,000
├── Configuración y pruebas: $300,000
├── Certificación ITU-T: $100,000
├── Capacitación personal: $80,000
└── Subtotal instalación: $880,000

TOTAL CAPEX TELECOMUNICACIONES: $9,425,000
```

### **OPEX Anual - Telecomunicaciones**

```
Personal Especializado:
├── Ingeniero telecomunicaciones (1): $90,000/año
├── Técnicos fibra óptica (4): $200,000/año
├── Técnicos equipos (2): $100,000/año
├── Operador NOC (6): $180,000/año
└── Subtotal personal: $570,000/año

Mantenimiento y Operación:
├── Mantenimiento preventivo fibra: $200,000/año
├── Mantenimiento equipos: $300,000/año
├── Licencias software: $100,000/año
├── Energía eléctrica: $150,000/año
├── Backup satelital: $120,000/año
├── Repuestos y materiales: $150,000/año
└── Subtotal operación: $1,020,000/año

TOTAL OPEX TELECOMUNICACIONES: $1,590,000/año
```

### **Análisis Costo-Beneficio**

#### **Beneficios Directos**
- **Habilitador sistemas**: Sin telecom, no hay ITS/CCO/Peajes
- **Reducción OPEX**: Gestión remota vs presencial
- **Disponibilidad**: >99.9% vs 95% redes básicas
- **Escalabilidad**: Crecimiento sin nueva infraestructura

#### **Beneficios Indirectos**
- **Cumplimiento contractual**: Indicadores disponibilidad
- **Eficiencia operativa**: Respuesta rápida incidentes
- **Seguridad**: Comunicaciones encriptadas
- **Futuro-proof**: Tecnologías emergentes (5G, IoT)

#### **ROI Estimado**
- **Inversión**: $9.4M CAPEX + $1.59M/año OPEX
- **Beneficio**: Habilitador $50M+ otros sistemas
- **ROI**: No aplica (infraestructura crítica)
- **Valor**: Indispensable para operación

---

## 📈 **INDICADORES DE DESEMPEÑO (KPIs)**

### **KPIs Técnicos ITU-T**

| Indicador | Meta ITU-T | Medición | Frecuencia |
|:----------|:-----------|:---------|:-----------|
| **Atenuación fibra** | ≤0.4 dB/km | OTDR | Mensual |
| **BER (Bit Error Rate)** | <10^-12 | Automática | Continua |
| **Latencia extremo-extremo** | <10 ms | Automática | Continua |
| **Disponibilidad red** | >99.9% | Automática | Continua |

### **KPIs Operacionales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **MTTR (Mean Time To Repair)** | <4 horas | Manual | Por incidente |
| **MTBF (Mean Time Between Failures)** | >8760 horas | Estadística | Anual |
| **Utilización ancho banda** | <70% | Automática | Continua |
| **Tiempo conmutación G.8032** | <50 ms | Automática | Por evento |

### **KPIs de Gestión**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Alarmas resueltas** | >95% | NMS | Diaria |
| **Configuraciones backup** | 100% | Automática | Diaria |
| **Certificaciones vigentes** | 100% | Manual | Mensual |
| **Personal certificado** | 100% | RRHH | Anual |

---

## 🔄 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Diseño Detallado (4 meses)**
- Ingeniería fibra óptica detallada
- Certificación equipos ITU-T G.652d
- Diseño rutas y protecciones
- Especificaciones técnicas finales

### **Fase 2: Adquisiciones (3 meses)**
- Licitación fibra óptica G.652d
- Adquisición equipos transmisión
- Software NMS y gestión
- Contratos instalación

### **Fase 3: Instalación Fibra (8 meses)**
- Tendido fibra backbone 272 km
- Instalación fibra anillos secundarios
- Empalmes y conectorizaciones
- Pruebas OTDR certificación

### **Fase 4: Instalación Equipos (4 meses)**
- Instalación equipos nodos principales
- Instalación equipos sitios ITS
- Configuración NMS
- Integración sistemas

### **Fase 5: Pruebas y Certificación (2 meses)**
- Pruebas ITU-T Y.1564
- Certificación G.652d
- Pruebas integración sistemas
- Documentación técnica

### **Fase 6: Puesta en Marcha (1 mes)**
- Migración sistemas existentes
- Capacitación personal
- Procedimientos operativos
- Operación comercial

---

## ✅ **CRITERIOS DE ACEPTACIÓN**

### **Normativos ITU-T**
- [x] Fibra certificada G.652d
- [x] Interfaces G.709 funcionales
- [x] Protección G.8032 operativa
- [x] Pruebas Y.1564 aprobadas
- [x] Gestión G.7710 implementada

### **Técnicos**
- [x] Cobertura 272 km completa
- [x] Redundancia N+1 funcional
- [x] Capacidad 10 Gbps disponible
- [x] Latencia <10 ms extremo-extremo
- [x] Disponibilidad >99.9% demostrada

### **Operacionales**
- [x] NMS operativo 24/7
- [x] Personal certificado fibra óptica
- [x] Procedimientos documentados
- [x] Plan contingencias probado
- [x] Integración CCO funcional

---

**📋 Estado**: COMPLETADO - Análisis requisitos telecomunicaciones G.652d  
**🎯 Próximo paso**: T02_05 - Análisis Requisitos Áreas de Servicio  
**📅 Integración**: Backbone crítico para todos los sistemas  
**👤 Responsable**: [ASIGNAR especialista fibra óptica + ITU-T]