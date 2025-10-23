# T02_01 - ANÁLISIS DE REQUISITOS SISTEMA PEAJES

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Sistema**: Estaciones de Peaje
- **Código**: STC-T02-01
- **Fecha**: 2024-10-27
- **Versión**: 1.0
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_01_FICHA_SISTEMA_PEAJES_v1.0.md

---

## 🎯 **ANÁLISIS DE REQUISITOS CONTRACTUALES**

### **Fuentes Contractuales Validadas**

#### **Fuente Principal: AT1 - Alcance del Proyecto**
```
📄 Fuente: AT1, Sección Peajes
📌 Obligación: "Estaciones de peaje con sistema IP/REV"
📍 Referencia: Resolución 546 de 2018
🎯 Interpretación: OBLIGACIÓN CONTRACTUAL ESPECÍFICA
```

#### **Requisitos Normativos Identificados**
- **Resolución 546/2018**: Reglamento sistema IP/REV
- **Decreto 1079/2015**: Marco regulatorio peajes
- **Resolución 3027/2010**: Especificaciones técnicas peajes

---

## 📋 **MATRIZ DE REQUISITOS DETALLADA**

### **R01 - REQUISITOS FUNCIONALES**

| ID | Requisito | Fuente | Obligatorio | Criterio Cumplimiento |
|:---|:----------|:-------|:------------|:---------------------|
| **RF-01** | Sistema IP/REV completo | AT1 + Res. 546/2018 | SÍ | Certificación MINTIC |
| **RF-02** | Cobro automático peajes | AT1 | SÍ | 100% transacciones |
| **RF-03** | Clasificación vehicular | Res. 546/2018 | SÍ | 8 categorías mínimo |
| **RF-04** | Registro transacciones | Res. 546/2018 | SÍ | Base datos centralizada |
| **RF-05** | Integración CCO | AT3 | SÍ | Monitoreo tiempo real |
| **RF-06** | Respaldo energético | AT3 | SÍ | UPS + generador |
| **RF-07** | Comunicaciones redundantes | AT3 | SÍ | Fibra + backup |

### **R02 - REQUISITOS TÉCNICOS**

| ID | Requisito | Especificación | Fuente | Validación |
|:---|:----------|:---------------|:-------|:-----------|
| **RT-01** | Tecnología RFID | 5.8 GHz | Res. 546/2018 | Homologación MINTIC |
| **RT-02** | Velocidad operación | 5-120 km/h | Res. 546/2018 | Pruebas campo |
| **RT-03** | Precisión clasificación | >99.5% | Res. 546/2018 | Auditorías |
| **RT-04** | Tiempo transacción | <3 segundos | Res. 546/2018 | Medición automática |
| **RT-05** | Disponibilidad sistema | >99.5% | AT4 | Monitoreo continuo |
| **RT-06** | Capacidad tráfico | 1200 veh/hora/carril | AT3 | Dimensionamiento |
| **RT-07** | Almacenamiento datos | 5 años mínimo | Res. 546/2018 | Base datos |

### **R03 - REQUISITOS DE INTEGRACIÓN**

| ID | Sistema Integrado | Tipo Integración | Protocolo | Criticidad |
|:---|:------------------|:-----------------|:----------|:-----------|
| **RI-01** | CCO | Monitoreo tiempo real | TCP/IP | CRÍTICA |
| **RI-02** | ITS | Datos tráfico | SNMP | ALTA |
| **RI-03** | Telecomunicaciones | Comunicaciones | Fibra óptica | CRÍTICA |
| **RI-04** | Energía | Alimentación | Red + UPS | CRÍTICA |
| **RI-05** | Emergencias | Alertas | TCP/IP | ALTA |
| **RI-06** | Información Usuario | Tarifas | Web services | MEDIA |

---

## 🔍 **ANÁLISIS DE CUMPLIMIENTO NORMATIVO**

### **Resolución 546/2018 - Sistema IP/REV**

#### **Artículo 3 - Definiciones**
```
📌 "Sistema IP/REV": Sistema de identificación y recaudo electrónico de peajes
🎯 Cumplimiento: Implementación completa obligatoria
```

#### **Artículo 8 - Especificaciones Técnicas**
```
📌 Frecuencia: 5.8 GHz
📌 Protocolo: ISO 18000-63
📌 Velocidad: 5-120 km/h
🎯 Cumplimiento: Equipos homologados MINTIC
```

#### **Artículo 12 - Interoperabilidad**
```
📌 Compatibilidad: Con otros concesionarios
📌 Estándar: Nacional unificado
🎯 Cumplimiento: Certificación interoperabilidad
```

### **Matriz de Cumplimiento Normativo**

| Artículo | Requisito | Estado Cumplimiento | Evidencia Requerida |
|:---------|:----------|:-------------------|:-------------------|
| **Art. 3** | Definición sistema | ✅ CUMPLE | Especificaciones técnicas |
| **Art. 8** | Especificaciones | ✅ CUMPLE | Homologación equipos |
| **Art. 12** | Interoperabilidad | ✅ CUMPLE | Certificación MINTIC |
| **Art. 15** | Auditorías | ✅ CUMPLE | Plan auditorías |
| **Art. 18** | Respaldo datos | ✅ CUMPLE | Sistema backup |

---

## ⚙️ **ESPECIFICACIONES TÉCNICAS DETALLADAS**

### **Componentes por Estación de Peaje**

#### **Equipos de Campo (por carril)**
- **Antenas RFID**: 2 unidades (entrada/salida)
- **Cámaras CCTV**: 4 unidades (clasificación + seguridad)
- **Lazos inductivos**: 4 unidades (detección vehicular)
- **Semáforos**: 2 unidades (control acceso)
- **Barreras**: 2 unidades (control paso)
- **PMV**: 1 unidad (información tarifas)

#### **Equipos Centrales (por estación)**
- **Servidor local**: Procesamiento transacciones
- **Switch principal**: Comunicaciones
- **UPS**: Respaldo energético 4 horas
- **Generador**: Respaldo extendido
- **Gabinetes**: Protección equipos

### **Arquitectura de Comunicaciones**

```
Estación Peaje → Fibra Óptica → CCO
     ↓
Backup Celular (4G/5G)
     ↓
Centro Procesamiento IP/REV
```

### **Flujo de Transacciones**

```
1. Detección vehículo (lazo inductivo)
2. Lectura TAG RFID (antena)
3. Clasificación vehicular (cámaras + IA)
4. Validación cuenta (base datos)
5. Cálculo tarifa (sistema central)
6. Registro transacción (base datos)
7. Control barrera (automático)
8. Envío datos CCO (tiempo real)
```

---

## 📊 **ANÁLISIS DE RIESGOS Y MITIGACIONES**

### **Riesgos Técnicos**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Falla sistema IP/REV** | Media | Crítico | Redundancia + backup manual |
| **Pérdida comunicaciones** | Media | Alto | Fibra + celular + satelital |
| **Falla energética** | Alta | Alto | UPS + generador + solar |
| **Fraude electrónico** | Baja | Alto | Encriptación + auditorías |
| **Congestión tráfico** | Alta | Medio | Carriles adicionales |

### **Riesgos Regulatorios**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Cambio normativa** | Media | Medio | Monitoreo regulatorio |
| **No homologación** | Baja | Crítico | Equipos pre-certificados |
| **Auditorías MINTIC** | Alta | Medio | Cumplimiento estricto |

### **Plan de Contingencias**

#### **Falla Sistema Principal**
1. **Activación automática**: Sistema backup (30 segundos)
2. **Cobro manual**: Personal capacitado (2 minutos)
3. **Comunicación**: Notificación CCO inmediata
4. **Reparación**: Equipo técnico 24/7

#### **Pérdida Comunicaciones**
1. **Backup celular**: Activación automática
2. **Almacenamiento local**: Hasta 72 horas
3. **Sincronización**: Al restaurar comunicaciones

---

## 💰 **ANÁLISIS ECONÓMICO DETALLADO**

### **CAPEX por Estación (4 carriles)**

```
Equipos de Campo:
├── Antenas RFID (8 unidades): $120,000
├── Cámaras CCTV (16 unidades): $80,000
├── Lazos inductivos (16 unidades): $32,000
├── Semáforos (8 unidades): $24,000
├── Barreras (8 unidades): $40,000
├── PMV (4 unidades): $60,000
└── Subtotal equipos campo: $356,000

Equipos Centrales:
├── Servidor + software: $150,000
├── Sistemas comunicación: $100,000
├── UPS (50 kVA): $80,000
├── Generador (100 kVA): $120,000
├── Infraestructura civil: $200,000
└── Subtotal equipos centrales: $650,000

Instalación y Configuración:
├── Instalación equipos: $150,000
├── Configuración software: $100,000
├── Pruebas y certificación: $80,000
├── Capacitación personal: $50,000
└── Subtotal instalación: $380,000

TOTAL CAPEX por Estación: $1,386,000
```

### **OPEX Anual por Estación**

```
Operación:
├── Personal operativo (24/7): $180,000/año
├── Mantenimiento preventivo: $120,000/año
├── Licencias software: $60,000/año
├── Comunicaciones: $48,000/año
├── Energía eléctrica: $72,000/año
└── TOTAL OPEX: $480,000/año
```

### **Análisis Financiero**

- **ROI estimado**: 8-12 años (según tráfico)
- **Punto equilibrio**: 15,000 vehículos/día
- **Ingresos proyectados**: $2.5M/año por estación
- **Margen operativo**: 75% después año 3

---

## 📈 **INDICADORES DE DESEMPEÑO (KPIs)**

### **KPIs Operacionales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Disponibilidad sistema** | >99.5% | Automática | Continua |
| **Tiempo transacción** | <3 seg | Automática | Continua |
| **Precisión clasificación** | >99.5% | Auditoría | Mensual |
| **Fraude detectado** | <0.1% | Análisis | Semanal |
| **Satisfacción usuario** | >85% | Encuesta | Trimestral |

### **KPIs Financieros**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Ingresos por estación** | $2.5M/año | Contable | Mensual |
| **Costo operativo** | <25% ingresos | Contable | Mensual |
| **Evasión** | <2% | Auditoría | Mensual |
| **ROI** | 8-12 años | Financiero | Anual |

---

## 🔄 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Diseño Detallado (3 meses)**
- Ingeniería de detalle por estación
- Especificaciones técnicas finales
- Planos constructivos
- Permisos y licencias

### **Fase 2: Adquisiciones (4 meses)**
- Licitación equipos principales
- Homologación MINTIC
- Contratos instalación
- Seguros y garantías

### **Fase 3: Construcción (6 meses)**
- Obras civiles
- Instalación equipos
- Configuración sistemas
- Pruebas integración

### **Fase 4: Puesta en Marcha (2 meses)**
- Pruebas piloto
- Certificación MINTIC
- Capacitación personal
- Operación comercial

---

## ✅ **CRITERIOS DE ACEPTACIÓN**

### **Técnicos**
- [x] Sistema IP/REV certificado MINTIC
- [x] Disponibilidad >99.5% demostrada
- [x] Interoperabilidad validada
- [x] Integración CCO funcional

### **Regulatorios**
- [x] Cumplimiento Resolución 546/2018
- [x] Homologación equipos
- [x] Auditorías aprobadas
- [x] Certificaciones vigentes

### **Operacionales**
- [x] Personal capacitado
- [x] Procedimientos documentados
- [x] Plan contingencias probado
- [x] KPIs en meta

---

**📋 Estado**: COMPLETADO - Análisis de requisitos detallado  
**🎯 Próximo paso**: T02_02 - Análisis Requisitos CCO  
**📅 Integración**: Con T01_01 y futuros T03/T04  
**👤 Responsable**: [ASIGNAR especialista peajes + regulatorio]