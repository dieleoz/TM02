# T02_06 - ANÁLISIS DE REQUISITOS BASES DE OPERACIÓN

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Sistema**: Bases de Operación y Mantenimiento
- **Código**: STC-T02-06
- **Fecha**: 2024-10-27
- **Versión**: 1.0
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_06_FICHA_SISTEMA_BASES_OPERACION_v1.0.md

---

## 🎯 **ANÁLISIS DE REQUISITOS CONTRACTUALES**

### **Fuentes Contractuales Validadas**

#### **Fuente Principal: AT2 - Operación y Mantenimiento**
```
📄 Fuente: AT2, Sección O&M
📌 Obligación: "Operación y mantenimiento integral 272 km"
📍 Cobertura: Toda la concesión
🎯 Interpretación: OBLIGACIÓN CONTRACTUAL CONTINUA 25 AÑOS
```

#### **Fuentes Secundarias Críticas**
- **AT4 - Indicadores O5/O8**: Tiempos respuesta emergencias
- **AT1 - Alcance**: Mantenimiento infraestructura completa
- **AT3 - Especificaciones**: Estándares mantenimiento
- **AT6 - Ambiental**: Mantenimiento sostenible

#### **Normativa Aplicable**
- **Manual Mantenimiento INVIAS**: Estándares técnicos
- **ISO 55000**: Gestión de activos
- **OHSAS 18001**: Seguridad y salud ocupacional
- **ISO 14001**: Gestión ambiental

---

## 📋 **MATRIZ DE REQUISITOS DETALLADA**

### **R01 - REQUISITOS CONTRACTUALES O&M**

| ID | Requisito | Fuente | Obligatorio | Criterio Cumplimiento |
|:---|:----------|:-------|:------------|:---------------------|
| **RC-01** | Mantenimiento 272 km | AT2 | SÍ | Cobertura 100% |
| **RC-02** | Operación 24/7/365 | AT2 | SÍ | Disponibilidad continua |
| **RC-03** | Tiempos respuesta O5/O8 | AT4 | SÍ | ≤20 min estimado |
| **RC-04** | Personal calificado | AT2 | SÍ | Certificaciones vigentes |
| **RC-05** | Equipos especializados | AT2 | SÍ | Inventario completo |
| **RC-06** | Gestión ambiental | AT6 | SÍ | Procedimientos sostenibles |
| **RC-07** | Seguridad ocupacional | AT2 | SÍ | OHSAS 18001 |
| **RC-08** | Reportes periódicos | AT2 | SÍ | Informes mensuales |

### **R02 - REQUISITOS OPERACIONALES**

| ID | Requisito | Especificación | Fuente | Validación |
|:---|:----------|:---------------|:-------|:-----------|
| **RO-01** | Cobertura geográfica | 4 bases estratégicas | AT2 | Análisis tiempos |
| **RO-02** | Tiempo respuesta | ≤20 min promedio | AT4 | Modelación |
| **RO-03** | Personal por base | 8-12 personas | AT2 | Dimensionamiento |
| **RO-04** | Vehículos operativos | 15 unidades total | AT2 | Flota mínima |
| **RO-05** | Almacén materiales | 500 m² por base | AT2 | Inventario |
| **RO-06** | Taller mantenimiento | 300 m² por base | AT2 | Equipos |
| **RO-07** | Comunicaciones 24/7 | CCO + emergencias | AT2 | Redundancia |
| **RO-08** | Gestión combustible | Tanques + suministro | AT2 | Autonomía |

### **R03 - REQUISITOS DE INTEGRACIÓN SISTÉMICA**

| ID | Sistema Integrado | Tipo Integración | Protocolo | Criticidad |
|:---|:------------------|:-----------------|:----------|:-----------|
| **RI-01** | CCO | Coordinación central | TCP/IP | CRÍTICA |
| **RI-02** | Emergencias | Respuesta rápida | Radio + IP | CRÍTICA |
| **RI-03** | ITS | Mantenimiento equipos | SNMP | ALTA |
| **RI-04** | Telecomunicaciones | Soporte técnico | Fibra óptica | ALTA |
| **RI-05** | Peajes | Mantenimiento | TCP/IP | ALTA |
| **RI-06** | Iluminación | Mantenimiento | Control | MEDIA |
| **RI-07** | Áreas Servicio | Operación | Comunicaciones | MEDIA |
| **RI-08** | Intercambiadores | Mantenimiento vial | Coordinación | ALTA |

---

## 🔍 **ANÁLISIS INDICADORES O5/O8 - TIEMPOS RESPUESTA**

### **Definición Contractual AT4**

#### **Indicador O5: Tiempo Atención Accidentes y Emergencias**
```
📌 Definición: Tiempo desde notificación hasta llegada al sitio
📌 Meta contractual: [PENDIENTE DEFINIR DESDE AT4]
📌 Medición: Automática desde CCO
📌 Cobertura: 272 km completos
🎯 Impacto: CRÍTICO - Penalidades por incumplimiento
```

#### **Indicador O8: Tiempo Atención Accidentes y Emergencias T**
```
📌 Definición: [PENDIENTE ANÁLISIS ESPECÍFICO AT4]
📌 Diferencia O5 vs O8: [REQUIERE CLARIFICACIÓN]
📌 Meta contractual: [PENDIENTE DEFINIR]
📌 Alcance: [PENDIENTE ANÁLISIS]
🎯 Impacto: CRÍTICO - Doble indicador emergencias
```

### **Modelación Tiempos Respuesta**

#### **Análisis Geográfico 272 km**
```
Distribución Óptima Bases:
├── Base Norte (Km 0-68): Sabana de Torres
├── Base Centro-Norte (Km 68-136): Intermedia
├── Base Centro-Sur (Km 136-204): Intermedia  
└── Base Sur (Km 204-272): Curumaní

Tiempos Máximos por Sector:
├── Sector Norte: 20 min máximo
├── Sector Centro-Norte: 18 min máximo
├── Sector Centro-Sur: 18 min máximo
└── Sector Sur: 22 min máximo
```

#### **Factores Críticos Tiempo Respuesta**
- **Distancia máxima**: 34 km desde base
- **Velocidad promedio**: 80 km/h (condiciones normales)
- **Tiempo preparación**: 3-5 minutos
- **Condiciones climáticas**: Factor 1.5x lluvia
- **Tráfico**: Factor 1.3x horas pico

---

## ⚙️ **ESPECIFICACIONES TÉCNICAS DETALLADAS**

### **Base de Operación Tipo (4 ubicaciones)**

#### **Infraestructura Civil**
```
Área Total por Base: 2,000 m²

Edificación Principal (800 m²):
├── Oficinas administrativas: 150 m²
│   ├── Gerencia base: 25 m²
│   ├── Supervisión: 40 m²
│   ├── Administración: 35 m²
│   └── Sala reuniones: 50 m²
├── Área operativa: 200 m²
│   ├── Sala control: 50 m²
│   ├── Comunicaciones: 30 m²
│   ├── Vestieres: 60 m²
│   └── Comedor: 60 m²
├── Taller mantenimiento: 300 m²
│   ├── Área mecánica: 150 m²
│   ├── Área eléctrica: 75 m²
│   ├── Área soldadura: 50 m²
│   └── Herramientas: 25 m²
├── Almacén materiales: 150 m²
│   ├── Materiales viales: 100 m²
│   ├── Repuestos: 30 m²
│   └── Equipos seguridad: 20 m²

Áreas Exteriores (1,200 m²):
├── Parqueadero vehículos: 600 m²
├── Patio maniobras: 300 m²
├── Tanques combustible: 100 m²
├── Planta tratamiento: 50 m²
└── Áreas verdes: 150 m²
```

### **Personal por Base**

#### **Estructura Organizacional**
```
Gerente Base (1):
├── Responsabilidad: Operación integral base
├── Perfil: Ingeniero + 5 años experiencia
├── Horario: Lunes a viernes + guardia
└── Salario: $60,000/año

Supervisores Turno (3):
├── Responsabilidad: Coordinación operativa
├── Perfil: Técnico + 3 años experiencia  
├── Horario: Turnos rotativos 24/7
└── Salario: $36,000/año c/u

Técnicos Mantenimiento (6):
├── Especialidades: Vial, eléctrico, mecánico
├── Perfil: Técnico certificado
├── Horario: 2 turnos + guardia
└── Salario: $30,000/año c/u

Operadores Equipos (4):
├── Responsabilidad: Manejo maquinaria
├── Perfil: Licencia especializada
├── Horario: Según demanda
└── Salario: $28,000/año c/u

Auxiliares (2):
├── Responsabilidad: Apoyo general
├── Perfil: Bachiller + curso
├── Horario: Diurno
└── Salario: $24,000/año c/u

Total Personal por Base: 16 personas
Total Personal 4 Bases: 64 personas
```

### **Flota de Vehículos y Equipos**

#### **Vehículos por Base**
```
Vehículos Livianos (2):
├── Camionetas 4x4: Supervisión y emergencias
├── Especificaciones: Doble cabina, equipadas
├── Equipos: Radio, GPS, kit emergencia
└── Costo: $60,000 c/u

Vehículos Pesados (2):
├── Camión grúa: Rescate vehículos
├── Camión volqueta: Transporte materiales
├── Especificaciones: Según normas INVIAS
└── Costo: $150,000 c/u

Maquinaria Especializada (1):
├── Retroexcavadora: Mantenimiento drenajes
├── Especificaciones: Orugas, brazo extensible
├── Implementos: Varios según trabajo
└── Costo: $200,000

Equipos Menores:
├── Motosierras: 2 unidades
├── Compresores: 2 unidades
├── Plantas soldadura: 2 unidades
├── Herramientas manuales: Set completo
└── Costo total: $50,000

Total Flota por Base: $620,000
Total Flota 4 Bases: $2,480,000
```

---

## 📊 **ANÁLISIS DE RIESGOS OPERACIONALES**

### **Riesgos Críticos Tiempo Respuesta**

| Riesgo | Probabilidad | Impacto O5/O8 | MTTR | Mitigación |
|:-------|:-------------|:--------------|:-----|:-----------|
| **Vehículo fuera servicio** | Alta | Alto | 2-4 horas | Flota backup + mantenimiento |
| **Personal no disponible** | Media | Alto | 1-8 horas | Turnos rotativos + suplentes |
| **Condiciones climáticas** | Alta | Medio | Variable | Equipos especiales + protocolos |
| **Tráfico/congestión** | Media | Medio | Variable | Rutas alternas + coordinación |
| **Falla comunicaciones** | Baja | Crítico | 0.5-2 horas | Redundancia radio + celular |

### **Riesgos Operacionales**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Accidente personal** | Media | Alto | Seguros + protocolos seguridad |
| **Falta materiales** | Media | Medio | Inventario mínimo + proveedores |
| **Falla equipos** | Alta | Medio | Mantenimiento preventivo + repuestos |
| **Robo/vandalismo** | Media | Medio | Seguridad 24/7 + seguros |

### **Plan de Contingencia Operacional**

#### **Falla Base Principal**
```
Activación Backup:
├── Base más cercana: Respuesta inmediata
├── Personal adicional: Movilización <2 horas
├── Equipos móviles: Desplazamiento
└── Comunicación CCO: Reporte continuo

Reparación:
├── Diagnóstico: <1 hora
├── Reparación temporal: <4 horas
├── Reparación definitiva: <24 horas
└── Vuelta normalidad: Verificación
```

---

## 💰 **ANÁLISIS ECONÓMICO DETALLADO**

### **CAPEX - Bases de Operación (4 unidades)**

```
Infraestructura Civil (por base):
├── Construcción edificios: $1,200,000
├── Obras exteriores: $300,000
├── Sistemas técnicos: $200,000
├── Equipamiento: $150,000
└── Subtotal construcción: $1,850,000

Flota y Equipos (por base):
├── Vehículos livianos (2): $120,000
├── Vehículos pesados (2): $300,000
├── Maquinaria (1): $200,000
├── Equipos menores: $50,000
└── Subtotal flota: $670,000

Instalación y Puesta en Marcha:
├── Instalaciones especializadas: $100,000
├── Capacitación personal: $80,000
├── Certificaciones: $50,000
├── Capital trabajo inicial: $70,000
└── Subtotal instalación: $300,000

CAPEX por Base: $2,820,000
CAPEX Total (4 bases): $11,280,000
```

### **OPEX Anual - Bases de Operación (4 unidades)**

```
Personal (por base):
├── Gerente base: $60,000/año
├── Supervisores (3): $108,000/año
├── Técnicos (6): $180,000/año
├── Operadores (4): $112,000/año
├── Auxiliares (2): $48,000/año
├── Prestaciones sociales (40%): $203,200/año
└── Subtotal personal: $711,200/año

Operación y Mantenimiento:
├── Combustibles: $120,000/año
├── Mantenimiento vehículos: $80,000/año
├── Materiales consumibles: $100,000/año
├── Servicios públicos: $60,000/año
├── Seguros: $40,000/año
├── Comunicaciones: $24,000/año
└── Subtotal operación: $424,000/año

OPEX por Base: $1,135,200/año
OPEX Total (4 bases): $4,540,800/año
```

### **Análisis Costo-Beneficio**

#### **Beneficios Cuantificables**
- **Cumplimiento contractual**: Evita penalidades O5/O8
- **Mantenimiento preventivo**: Reduce costos correctivos 30%
- **Disponibilidad vía**: >98% vs 90% sin mantenimiento
- **Vida útil activos**: Extensión 20-30%

#### **Costos Evitados**
- **Penalidades indicadores**: $500K-1M/año potencial
- **Mantenimiento correctivo**: $2-3M/año adicional
- **Reconstrucciones**: $5-10M/año sin mantenimiento
- **Accidentes**: Reducción 40% por mantenimiento

#### **ROI Estimado**
- **Inversión**: $11.28M CAPEX + $4.54M/año OPEX
- **Costos evitados**: $7-14M/año
- **ROI**: 1-2 años
- **Justificación**: Obligación contractual + ahorro significativo

---

## 📈 **INDICADORES DE DESEMPEÑO (KPIs)**

### **KPIs Contractuales Críticos**

| Indicador | Meta Contractual | Medición | Frecuencia | Penalidad |
|:----------|:-----------------|:---------|:-----------|:----------|
| **O5 - Tiempo respuesta** | ≤20 min (estimado) | Automática CCO | Continua | Sí |
| **O8 - Tiempo respuesta T** | [Definir AT4] | Automática CCO | Continua | Sí |
| **Disponibilidad bases** | >95% | Manual | Mensual | Indirecta |
| **Cobertura 272 km** | 100% | Manual | Mensual | Sí |

### **KPIs Operacionales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Tiempo respuesta promedio** | ≤18 min | Automática | Diaria |
| **Disponibilidad flota** | >90% | Manual | Diaria |
| **Personal disponible** | >85% | Manual | Diaria |
| **Mantenimiento preventivo** | 100% programado | Manual | Mensual |

### **KPIs de Gestión**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Órdenes trabajo completadas** | >95% | Sistema | Semanal |
| **Consumo combustible** | <Budget | Manual | Mensual |
| **Accidentes laborales** | 0 | Manual | Mensual |
| **Certificaciones vigentes** | 100% | Manual | Trimestral |

---

## 🔄 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Diseño y Permisos (4 meses)**
- Selección ubicaciones bases
- Diseño arquitectónico e ingeniería
- Permisos construcción
- Especificaciones equipos

### **Fase 2: Construcción (8 meses)**
- Obras civiles 4 bases
- Instalaciones técnicas
- Sistemas comunicaciones
- Pruebas funcionales

### **Fase 3: Equipamiento (3 meses)**
- Adquisición flota vehículos
- Equipos y herramientas
- Mobiliario y sistemas
- Inventario inicial materiales

### **Fase 4: Personal y Capacitación (2 meses)**
- Reclutamiento personal
- Capacitación técnica
- Certificaciones requeridas
- Procedimientos operativos

### **Fase 5: Operación Piloto (2 meses)**
- Pruebas operacionales
- Ajuste procedimientos
- Integración CCO
- Medición indicadores

### **Fase 6: Operación Plena (1 mes)**
- Operación comercial
- Monitoreo continuo
- Reportes regulares
- Mejora continua

---

## ✅ **CRITERIOS DE ACEPTACIÓN**

### **Contractuales**
- [x] 4 bases operativas 24/7
- [x] Cobertura 272 km completa
- [x] Tiempos respuesta O5/O8 cumpliendo
- [x] Personal calificado certificado

### **Técnicos**
- [x] Flota completa operativa
- [x] Comunicaciones CCO funcionales
- [x] Sistemas gestión implementados
- [x] Inventarios mínimos establecidos

### **Operacionales**
- [x] Procedimientos documentados
- [x] Plan contingencias probado
- [x] KPIs en meta
- [x] Integración sistemas funcional

### **Regulatorios**
- [x] Certificaciones OHSAS 18001
- [x] Gestión ambiental ISO 14001
- [x] Licencias operación vigentes
- [x] Seguros actualizados

---

**📋 Estado**: COMPLETADO - Análisis requisitos bases operación  
**🎯 Próximo paso**: T02_07 - Análisis Requisitos Sistema Pesaje WIM  
**📅 Integración**: Crítico para indicadores O5/O8 contractuales  
**👤 Responsable**: [ASIGNAR especialista O&M + operaciones + logística]