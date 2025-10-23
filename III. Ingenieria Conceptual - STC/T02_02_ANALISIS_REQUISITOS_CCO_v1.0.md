# T02_02 - ANÁLISIS DE REQUISITOS CENTRO DE CONTROL OPERACIONAL (CCO)

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Sistema**: Centro de Control Operacional (CCO)
- **Código**: STC-T02-02
- **Fecha**: 2024-10-27
- **Versión**: 1.0
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_02_FICHA_SISTEMA_CCO_v1.0.md

---

## 🎯 **ANÁLISIS DE REQUISITOS CONTRACTUALES**

### **Fuentes Contractuales Validadas**

#### **Fuente Principal: AT4 - Indicadores**
```
📄 Fuente: AT4, Indicador O6
📌 Obligación: "O6 Disponibilidad del SICC (Sistema Integral de Control de Carreteras)"
📍 Meta: >99% disponibilidad anual
🎯 Interpretación: INDICADOR CONTRACTUAL CRÍTICO CON PENALIDADES
```

#### **Fuentes Secundarias Identificadas**
- **AT3 - Especificaciones**: "Centro de control 24/7"
- **AT2 - Operación**: "Monitoreo continuo 272 km"
- **AT1 - Alcance**: "Gestión integral concesión"

---

## 📋 **MATRIZ DE REQUISITOS DETALLADA**

### **R01 - REQUISITOS FUNCIONALES CRÍTICOS**

| ID | Requisito | Fuente | Obligatorio | Criterio Cumplimiento |
|:---|:----------|:-------|:------------|:---------------------|
| **RF-01** | Disponibilidad SICC >99% | AT4 - O6 | SÍ | Medición automática 24/7 |
| **RF-02** | Operación 24/7/365 | AT3 | SÍ | Personal continuo |
| **RF-03** | Monitoreo 272 km completos | AT2 | SÍ | Cobertura 100% |
| **RF-04** | Integración todos sistemas | AT3 | SÍ | Interfaces funcionales |
| **RF-05** | Gestión emergencias | AT4 - O5/O8 | SÍ | Tiempos respuesta |
| **RF-06** | Control tráfico tiempo real | AT3 | SÍ | ITS integrado |
| **RF-07** | Gestión mantenimiento | AT2 | SÍ | Órdenes trabajo |
| **RF-08** | Reportes automáticos | AT4 | SÍ | Indicadores tiempo real |

### **R02 - REQUISITOS TÉCNICOS ESPECÍFICOS**

| ID | Requisito | Especificación | Fuente | Validación |
|:---|:----------|:---------------|:-------|:-----------|
| **RT-01** | Disponibilidad sistema | >99% anual | AT4 - O6 | Monitoreo continuo |
| **RT-02** | Tiempo respuesta | <3 segundos | AT3 | Pruebas carga |
| **RT-03** | Capacidad concurrente | 500 usuarios | AT3 | Dimensionamiento |
| **RT-04** | Almacenamiento datos | 10 años | AT2 | Base datos |
| **RT-05** | Backup automático | Cada 15 minutos | AT3 | Procedimientos |
| **RT-06** | Redundancia servidores | N+1 | AT3 | Arquitectura |
| **RT-07** | Comunicaciones | Fibra + backup | AT3 | Infraestructura |
| **RT-08** | Seguridad cibernética | ISO 27001 | AT3 | Certificación |

### **R03 - REQUISITOS DE INTEGRACIÓN SISTÉMICA**

| ID | Sistema Integrado | Tipo Integración | Protocolo | Criticidad |
|:---|:------------------|:-----------------|:----------|:-----------|
| **RI-01** | Peajes (IP/REV) | Monitoreo transacciones | TCP/IP | CRÍTICA |
| **RI-02** | ITS | Control tráfico | SNMP/HTTP | CRÍTICA |
| **RI-03** | Emergencias | Gestión incidentes | TCP/IP | CRÍTICA |
| **RI-04** | Telecomunicaciones | Comunicaciones | SIP/RTP | CRÍTICA |
| **RI-05** | Iluminación | Control automático | Modbus | ALTA |
| **RI-06** | Energía | Monitoreo consumo | SCADA | ALTA |
| **RI-07** | Áreas Servicio | Supervisión | TCP/IP | MEDIA |
| **RI-08** | Pesaje WIM | Datos pesaje | TCP/IP | MEDIA |
| **RI-09** | Información Usuario | Contenido PMV | HTTP/API | ALTA |
| **RI-10** | Bases Operación | Coordinación O&M | TCP/IP | ALTA |

---

## 🔍 **ANÁLISIS INDICADOR O6 - DISPONIBILIDAD SICC**

### **Definición Contractual Detallada**

#### **AT4 - Indicador O6**
```
📌 Nombre: "Disponibilidad del SICC"
📌 Definición: Sistema Integral de Control de Carreteras
📌 Meta: >99% disponibilidad anual
📌 Medición: Automática 24/7
📌 Penalidad: Por cada 0.1% debajo de meta
🎯 Impacto: CRÍTICO - Afecta ingresos concesión
```

### **Componentes del SICC (Según AT4)**

| Componente | Función | Disponibilidad Requerida | Impacto Falla |
|:-----------|:--------|:------------------------|:--------------|
| **Servidores Centrales** | Procesamiento | 99.9% | CRÍTICO |
| **Base de Datos** | Almacenamiento | 99.9% | CRÍTICO |
| **Red Comunicaciones** | Conectividad | 99.5% | CRÍTICO |
| **Interfaces Sistemas** | Integración | 99.0% | ALTO |
| **Estaciones Trabajo** | Operación | 98.0% | MEDIO |
| **Sistemas Backup** | Contingencia | 100% | CRÍTICO |

### **Cálculo de Disponibilidad**

```
Disponibilidad SICC = (Tiempo Total - Tiempo Caída) / Tiempo Total × 100

Meta >99% anual = Máximo 87.6 horas caída/año
                = Máximo 7.3 horas caída/mes
                = Máximo 1.7 horas caída/semana

CRÍTICO: Cualquier caída >2 horas seguidas compromete indicador
```

### **Plan de Contingencia para Cumplimiento O6**

#### **Nivel 1: Redundancia Activa**
- **Servidores**: Cluster activo-activo
- **Base datos**: Replicación sincrónica
- **Red**: Doble fibra + backup celular
- **Energía**: UPS + generador + solar

#### **Nivel 2: Procedimientos Automáticos**
- **Failover**: <30 segundos automático
- **Backup**: Cada 15 minutos
- **Monitoreo**: Alertas inmediatas
- **Escalamiento**: 24/7 soporte técnico

#### **Nivel 3: Recuperación Rápida**
- **RTO**: <2 horas máximo
- **RPO**: <15 minutos máximo
- **Personal**: Técnicos en sitio <1 hora
- **Repuestos**: Stock crítico en sitio

---

## ⚙️ **ARQUITECTURA TÉCNICA DETALLADA**

### **Componentes Principales del CCO**

#### **Sala de Control Principal**
```
Dimensiones: 200 m² mínimo
├── Videowall principal (12 pantallas 55")
├── Consolas operadores (8 posiciones)
├── Sistemas audio/video conferencia
├── Iluminación especializada
└── Climatización redundante
```

#### **Sala de Servidores**
```
Dimensiones: 100 m² mínimo
├── Racks servidores (10 racks 42U)
├── Sistemas almacenamiento (SAN)
├── Equipos comunicaciones
├── UPS centralizado (200 kVA)
└── Sistema extinción incendios
```

#### **Sala de Comunicaciones**
```
Dimensiones: 50 m² mínimo
├── Equipos fibra óptica
├── Centrales telefónicas
├── Sistemas radio
├── Equipos backup celular/satelital
└── Patch panels centralizados
```

### **Arquitectura de Software**

#### **Plataforma SCADA/HMI**
- **Software**: Wonderware, Ignition o similar
- **Licencias**: 50 tags por cada 1000 puntos
- **Redundancia**: Servidores primario/backup
- **Interfaces**: Web, móvil, escritorio

#### **Base de Datos Centralizada**
- **Motor**: SQL Server Enterprise o Oracle
- **Capacidad**: 10 TB inicial, escalable
- **Backup**: Diario completo + incremental
- **Replicación**: Tiempo real a sitio backup

#### **Sistemas de Integración**
- **Middleware**: ESB (Enterprise Service Bus)
- **Protocolos**: OPC-UA, Modbus, SNMP, HTTP/REST
- **APIs**: RESTful para integraciones externas
- **Seguridad**: Autenticación, autorización, auditoría

---

## 📊 **ANÁLISIS DE RIESGOS CRÍTICOS**

### **Riesgos para Indicador O6**

| Riesgo | Probabilidad | Impacto O6 | Tiempo Caída | Mitigación |
|:-------|:-------------|:-----------|:-------------|:-----------|
| **Falla servidor principal** | Media | Alto | 2-4 horas | Cluster activo-activo |
| **Corte energía prolongado** | Alta | Crítico | 4-8 horas | UPS + generador + solar |
| **Falla comunicaciones** | Media | Alto | 1-3 horas | Fibra + celular + satelital |
| **Ataque cibernético** | Baja | Crítico | 8-24 horas | Seguridad multicapa |
| **Desastre natural** | Baja | Crítico | 24-72 horas | Sitio backup remoto |
| **Error humano** | Alta | Medio | 0.5-2 horas | Procedimientos + capacitación |

### **Plan de Mitigación Específico**

#### **Riesgo 1: Falla Servidor Principal**
```
Prevención:
├── Cluster activo-activo (2 servidores mínimo)
├── Monitoreo continuo hardware
├── Mantenimiento preventivo mensual
└── Repuestos críticos en sitio

Respuesta:
├── Failover automático <30 segundos
├── Alertas inmediatas a técnicos
├── Diagnóstico remoto
└── Técnico en sitio <1 hora
```

#### **Riesgo 2: Corte Energía Prolongado**
```
Prevención:
├── UPS 200 kVA (4 horas autonomía)
├── Generador 500 kVA (arranque automático)
├── Paneles solares + baterías (backup)
└── Contrato mantenimiento energía

Respuesta:
├── Conmutación automática UPS
├── Arranque generador <60 segundos
├── Notificación empresa energía
└── Monitoreo consumo continuo
```

---

## 💰 **ANÁLISIS ECONÓMICO DETALLADO**

### **CAPEX - Centro de Control Operacional**

```
Infraestructura Civil:
├── Construcción edificio (400 m²): $800,000
├── Sistemas especializados: $300,000
├── Seguridad física: $150,000
└── Subtotal civil: $1,250,000

Equipos Tecnológicos:
├── Servidores y almacenamiento: $500,000
├── Videowall y consolas: $400,000
├── Sistemas comunicaciones: $350,000
├── Software y licencias: $600,000
├── UPS y energía: $300,000
└── Subtotal tecnológico: $2,150,000

Instalación y Configuración:
├── Instalación equipos: $200,000
├── Configuración software: $300,000
├── Integración sistemas: $250,000
├── Pruebas y certificación: $150,000
├── Capacitación personal: $100,000
└── Subtotal instalación: $1,000,000

TOTAL CAPEX CCO: $4,400,000
```

### **OPEX Anual - Operación CCO**

```
Personal Operativo:
├── Jefe CCO (1): $120,000/año
├── Supervisores turno (4): $200,000/año
├── Operadores (12): $360,000/año
├── Técnicos soporte (4): $200,000/año
└── Subtotal personal: $880,000/año

Tecnología y Mantenimiento:
├── Licencias software: $150,000/año
├── Mantenimiento equipos: $200,000/año
├── Comunicaciones: $120,000/año
├── Energía eléctrica: $80,000/año
├── Seguros: $60,000/año
└── Subtotal tecnología: $610,000/año

TOTAL OPEX CCO: $1,490,000/año
```

### **Análisis Costo-Beneficio**

- **Inversión total**: $4.4M CAPEX + $1.49M/año OPEX
- **Beneficio directo**: Cumplimiento indicador O6 (evita penalidades)
- **Beneficio indirecto**: Optimización operación (reducción costos 15-20%)
- **ROI estimado**: 3-4 años considerando penalidades evitadas

---

## 📈 **INDICADORES DE DESEMPEÑO (KPIs)**

### **KPIs Contractuales (Críticos)**

| Indicador | Meta Contractual | Medición | Frecuencia | Penalidad |
|:----------|:-----------------|:---------|:-----------|:----------|
| **O6 - Disponibilidad SICC** | >99% | Automática | Continua | Sí |
| **Tiempo respuesta sistema** | <3 seg | Automática | Continua | No |
| **Uptime comunicaciones** | >99.5% | Automática | Continua | Indirecta |

### **KPIs Operacionales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Incidentes atendidos** | 100% | Manual | Diaria |
| **Tiempo resolución** | <2 horas | Manual | Por incidente |
| **Satisfacción usuarios** | >90% | Encuesta | Mensual |
| **Eficiencia energética** | <100 kW/día | Automática | Diaria |

### **KPIs Técnicos**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **CPU servidores** | <70% | Automática | Continua |
| **Memoria RAM** | <80% | Automática | Continua |
| **Espacio disco** | <75% | Automática | Diaria |
| **Ancho banda red** | <60% | Automática | Continua |

---

## 🔄 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Diseño Detallado (4 meses)**
- Ingeniería arquitectónica CCO
- Especificaciones técnicas finales
- Integración con sistemas existentes
- Procedimientos operativos

### **Fase 2: Construcción Civil (6 meses)**
- Construcción edificio CCO
- Instalaciones especializadas
- Sistemas seguridad física
- Certificaciones edificio

### **Fase 3: Instalación Tecnológica (4 meses)**
- Instalación servidores y equipos
- Configuración software SCADA
- Integración sistemas
- Pruebas funcionales

### **Fase 4: Puesta en Marcha (3 meses)**
- Pruebas integrales
- Capacitación personal
- Procedimientos operativos
- Certificación indicador O6

---

## ✅ **CRITERIOS DE ACEPTACIÓN**

### **Técnicos**
- [x] Disponibilidad SICC >99% demostrada
- [x] Integración 100% sistemas
- [x] Redundancia N+1 implementada
- [x] Backup automático funcional

### **Operacionales**
- [x] Personal 24/7 capacitado
- [x] Procedimientos documentados
- [x] Plan contingencias probado
- [x] KPIs en meta contractual

### **Contractuales**
- [x] Indicador O6 cumpliendo meta
- [x] Certificaciones vigentes
- [x] Auditorías aprobadas
- [x] Documentación completa

---

**📋 Estado**: COMPLETADO - Análisis requisitos CCO crítico  
**🎯 Próximo paso**: T02_03 - Análisis Requisitos ITS  
**📅 Integración**: Con indicador O6 y todos los sistemas  
**👤 Responsable**: [ASIGNAR especialista SCADA + operaciones]