# T02_07 - ANÁLISIS DE REQUISITOS SISTEMA PESAJE WIM

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Sistema**: Sistema de Pesaje Dinámico (WIM - Weigh In Motion)
- **Código**: STC-T02-07
- **Fecha**: 2024-10-27
- **Versión**: 1.0
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_07_FICHA_SISTEMA_PESAJE_WIM_v1.0.md

---

## 🎯 **ANÁLISIS DE REQUISITOS CONTRACTUALES**

### **Fuentes Contractuales Identificadas**

#### **Análisis Contractual Crítico**
```
📄 Fuente Principal: AT3 - Sistema ITS (Implícito)
📌 Referencia: "Sistema ITS integral"
📍 Estado: IMPLÍCITO - No explícitamente obligatorio
🎯 Interpretación: RECOMENDADO como parte de ITS avanzado
```

#### **Fuentes Normativas Aplicables**
- **Resolución 4100/2004**: Pesos y dimensiones vehiculares
- **Decreto 1079/2015**: Control sobrepeso en concesiones
- **ASTM E1318**: Especificaciones técnicas WIM
- **OIML R134**: Instrumentos pesaje automático

#### **Justificación Técnica-Comercial**
- **Control sobrepeso**: Protección infraestructura
- **Datos tráfico**: Información valiosa para gestión
- **Integración ITS**: Sinergia con sistemas existentes
- **Cumplimiento normativo**: Apoyo autoridades

---

## 📋 **MATRIZ DE REQUISITOS DETALLADA**

### **R01 - REQUISITOS NORMATIVOS (Si se implementa)**

| ID | Requisito | Norma | Obligatorio | Criterio Cumplimiento |
|:---|:----------|:------|:------------|:---------------------|
| **RN-01** | Precisión pesaje | ASTM E1318 | SÍ | ±5% clase B |
| **RN-02** | Certificación metrológica | OIML R134 | SÍ | Aprobación ONAC |
| **RN-03** | Clasificación vehicular | Res. 4100/2004 | SÍ | 8 categorías mínimo |
| **RN-04** | Velocidad operación | ASTM E1318 | SÍ | 10-120 km/h |
| **RN-05** | Registro datos | Decreto 1079 | SÍ | Base datos centralizada |
| **RN-06** | Calibración periódica | ASTM E1318 | SÍ | Cada 6 meses |

### **R02 - REQUISITOS FUNCIONALES TÉCNICOS**

| ID | Requisito | Especificación | Justificación | Validación |
|:---|:----------|:---------------|:--------------|:-----------|
| **RF-01** | Puntos pesaje | 2-3 ubicaciones | Cobertura representativa | Análisis tráfico |
| **RF-02** | Tecnología sensores | Piezoeléctricos | Precisión + durabilidad | ASTM E1318 |
| **RF-03** | Capacidad máxima | 80 toneladas | Vehículos pesados | Normativa |
| **RF-04** | Velocidad detección | 10-120 km/h | Operación normal | Especificación |
| **RF-05** | Clasificación automática | 8+ categorías | Análisis detallado | Algoritmos |
| **RF-06** | Almacenamiento datos | 5 años mínimo | Históricos + auditorías | Base datos |
| **RF-07** | Transmisión tiempo real | <30 segundos | Integración CCO | Comunicaciones |
| **RF-08** | Interfaz autoridades | API estándar | Compartir información | Desarrollo |

### **R03 - REQUISITOS DE INTEGRACIÓN SISTÉMICA**

| ID | Sistema Integrado | Tipo Integración | Protocolo | Criticidad |
|:---|:------------------|:-----------------|:----------|:-----------|
| **RI-01** | ITS | Datos tráfico | TCP/IP | ALTA |
| **RI-02** | CCO | Monitoreo central | SNMP | ALTA |
| **RI-03** | Telecomunicaciones | Comunicaciones | Fibra óptica | CRÍTICA |
| **RI-04** | Peajes | Correlación datos | TCP/IP | MEDIA |
| **RI-05** | Bases Operación | Mantenimiento | Comunicaciones | MEDIA |
| **RI-06** | Autoridades | Reportes | API/Web | BAJA |
| **RI-07** | Información Usuario | Alertas sobrepeso | PMV | BAJA |

---

## 🔍 **ANÁLISIS COSTO-BENEFICIO DETALLADO**

### **Escenarios de Implementación**

#### **Escenario A: No Implementar WIM**
```
Ventajas:
├── Ahorro CAPEX: $2.5M
├── Ahorro OPEX: $300K/año
├── Menor complejidad operativa
└── Sin riesgos técnicos WIM

Desventajas:
├── Sin control sobrepeso
├── Datos tráfico limitados
├── Sin apoyo autoridades
├── Oportunidad perdida ingresos
└── ITS menos completo
```

#### **Escenario B: WIM Básico (2 puntos)**
```
Ventajas:
├── Control sobrepeso básico
├── Datos tráfico valiosos
├── Integración ITS
├── Apoyo autoridades
└── ROI potencial 5-7 años

Desventajas:
├── Inversión $1.5M
├── OPEX $200K/año
├── Complejidad técnica
└── Mantenimiento especializado
```

#### **Escenario C: WIM Completo (3 puntos)**
```
Ventajas:
├── Control sobrepeso completo
├── Datos tráfico exhaustivos
├── Cobertura representativa
├── Valor comercial alto
└── ITS clase mundial

Desventajas:
├── Inversión $2.5M
├── OPEX $300K/año
├── Alta complejidad
└── Riesgo técnico mayor
```

### **Recomendación Técnico-Económica**

#### **RECOMENDACIÓN: Escenario B - WIM Básico**
```
Justificación:
├── Balance costo-beneficio óptimo
├── Cumple objetivos principales
├── Riesgo técnico controlado
├── Integración ITS efectiva
└── Escalabilidad futura

Implementación:
├── 2 puntos estratégicos
├── Tecnología probada
├── Integración gradual
└── Evaluación resultados
```

---

## ⚙️ **ESPECIFICACIONES TÉCNICAS DETALLADAS**

### **Sistema WIM por Punto de Pesaje**

#### **Componentes Principales**
```
Sensores de Pesaje:
├── Sensores piezoeléctricos: 8 unidades/carril
├── Instalación: Ranuras en pavimento
├── Protección: Encapsulado IP68
├── Vida útil: 10 años
└── Costo: $80,000/carril

Sistema Clasificación:
├── Lazos inductivos: 4 unidades/carril
├── Sensores neumáticos: 2 unidades/carril
├── Algoritmos IA: Clasificación automática
├── Precisión: >95% clasificación
└── Costo: $30,000/carril

Equipos Procesamiento:
├── Controlador WIM: 1 unidad/punto
├── Servidor local: Procesamiento datos
├── UPS: 4 horas autonomía
├── Comunicaciones: Fibra + backup
└── Costo: $150,000/punto
```

#### **Ubicaciones Estratégicas Propuestas**

```
Punto WIM 1 - Km 68 (Sector Norte):
├── Justificación: Tráfico pesado alto
├── Carriles: 4 (2 por sentido)
├── Integración: Peaje Norte
└── Cobertura: 25% tráfico total

Punto WIM 2 - Km 204 (Sector Sur):
├── Justificación: Control complementario
├── Carriles: 4 (2 por sentido)  
├── Integración: Peaje Sur
└── Cobertura: 30% tráfico total

Cobertura Total: 55% tráfico pesado
Representatividad: Estadísticamente válida
```

### **Centro Procesamiento WIM**

#### **Software Especializado**
```
Plataforma WIM:
├── Software: Kistler KiTraffic o similar
├── Funciones: Pesaje, clasificación, reportes
├── Integración: APIs estándar
├── Licencias: 2 puntos + servidor central
└── Costo: $200,000

Base Datos:
├── Motor: PostgreSQL + TimescaleDB
├── Capacidad: 10M registros/año
├── Retención: 5 años datos detallados
├── Backup: Diario + tiempo real
└── Costo: Incluido en software

Reportes y Análisis:
├── Dashboard tiempo real
├── Reportes automáticos
├── Análisis estadísticos
├── Exportación datos
└── API para terceros
```

---

## 📊 **ANÁLISIS DE RIESGOS TÉCNICOS**

### **Riesgos Tecnológicos**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Falla sensores piezoeléctricos** | Media | Alto | Redundancia + mantenimiento |
| **Deriva calibración** | Alta | Medio | Calibración automática + manual |
| **Daño por tráfico pesado** | Media | Alto | Diseño robusto + protección |
| **Interferencia electromagnética** | Baja | Medio | Blindaje + filtros |
| **Problemas software** | Media | Medio | Soporte técnico + backup |

### **Riesgos Operacionales**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Personal no capacitado** | Media | Alto | Capacitación especializada |
| **Mantenimiento inadecuado** | Alta | Alto | Contratos especializados |
| **Vandalismo/robo** | Media | Medio | Protección física + seguros |
| **Cambios normativos** | Baja | Medio | Monitoreo regulatorio |

### **Plan de Contingencia WIM**

#### **Falla Sistema Principal**
```
Detección Automática:
├── Monitoreo continuo: Sensores + software
├── Alertas inmediatas: CCO + técnicos
├── Diagnóstico remoto: 80% problemas
└── Tiempo detección: <5 minutos

Respuesta:
├── Técnico en sitio: <4 horas
├── Reparación temporal: Sensores backup
├── Calibración: Después reparación
└── Documentación: Registro completo
```

---

## 💰 **ANÁLISIS ECONÓMICO DETALLADO**

### **CAPEX - Sistema WIM (Escenario B - 2 puntos)**

```
Equipos WIM por Punto:
├── Sensores piezoeléctricos (8): $320,000
├── Sistema clasificación: $120,000
├── Controlador y procesamiento: $150,000
├── Instalación especializada: $200,000
├── Calibración inicial: $50,000
└── Subtotal por punto: $840,000

Centro Procesamiento:
├── Software WIM: $200,000
├── Servidor central: $100,000
├── Integración sistemas: $150,000
├── Capacitación: $50,000
└── Subtotal centro: $500,000

CAPEX Total WIM (2 puntos): $2,180,000
```

### **OPEX Anual - Sistema WIM**

```
Mantenimiento Especializado:
├── Contrato mantenimiento: $150,000/año
├── Calibraciones (4/año): $40,000/año
├── Repuestos sensores: $60,000/año
├── Licencias software: $30,000/año
└── Subtotal mantenimiento: $280,000/año

Personal y Operación:
├── Técnico especialista (0.5): $30,000/año
├── Comunicaciones: $12,000/año
├── Energía eléctrica: $8,000/año
├── Seguros: $15,000/año
└── Subtotal operación: $65,000/año

OPEX Total WIM: $345,000/año
```

### **Análisis ROI**

#### **Beneficios Potenciales**
```
Directos:
├── Datos tráfico comercializables: $50,000/año
├── Servicios autoridades: $30,000/año
├── Optimización mantenimiento: $40,000/año
└── Subtotal directo: $120,000/año

Indirectos:
├── Protección infraestructura: $200,000/año
├── Valor agregado ITS: $100,000/año
├── Información estratégica: $80,000/año
└── Subtotal indirecto: $380,000/año

Total Beneficios: $500,000/año
```

#### **Cálculo ROI**
- **Inversión**: $2.18M CAPEX + $345K/año OPEX
- **Beneficios**: $500K/año
- **Flujo neto**: $155K/año positivo
- **Payback**: 14 años
- **VPN (10 años, 10%)**: $-1.2M
- **Conclusión**: **NO RENTABLE** financieramente

---

## 📈 **INDICADORES DE DESEMPEÑO (KPIs)**

### **KPIs Técnicos (Si se implementa)**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Precisión pesaje** | ±5% | Calibración | Mensual |
| **Disponibilidad sistema** | >95% | Automática | Continua |
| **Clasificación correcta** | >95% | Validación | Semanal |
| **Tiempo respuesta** | <3 seg | Automática | Continua |

### **KPIs Operacionales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Vehículos procesados** | 100% tráfico | Automática | Diaria |
| **Datos transmitidos** | 100% | Automática | Continua |
| **Mantenimiento preventivo** | 100% programado | Manual | Mensual |
| **Calibraciones** | 4/año | Manual | Trimestral |

---

## 🔄 **RECOMENDACIÓN FINAL**

### **Análisis Integral**

#### **Factores A Favor**
- ✅ Integración natural con ITS
- ✅ Datos valiosos para gestión
- ✅ Apoyo control sobrepeso
- ✅ Tecnología madura disponible

#### **Factores En Contra**
- ❌ No es obligación contractual explícita
- ❌ ROI negativo (14 años payback)
- ❌ Alta complejidad técnica
- ❌ OPEX significativo ($345K/año)

### **RECOMENDACIÓN: NO IMPLEMENTAR EN FASE INICIAL**

#### **Justificación**
```
Razones Principales:
├── No obligatorio contractualmente
├── ROI negativo en análisis conservador
├── Recursos limitados para sistemas críticos
└── Complejidad operativa adicional

Alternativa Propuesta:
├── Preparar infraestructura (ductos, energía)
├── Incluir en diseño ITS (interfaces)
├── Evaluar implementación futura
└── Monitorear cambios normativos
```

#### **Implementación Futura Condicionada**
```
Condiciones para Reconsiderar:
├── Cambio normativo (obligatoriedad)
├── Mejora ROI (nuevos ingresos)
├── Reducción costos tecnología
├── Demanda específica autoridades
└── Fase 2 del proyecto (expansión)
```

---

## ✅ **CRITERIOS DE DECISIÓN**

### **Si NO se Implementa (Recomendado)**
- [x] Recursos enfocados en sistemas obligatorios
- [x] Menor complejidad operativa
- [x] Ahorro CAPEX $2.18M
- [x] Ahorro OPEX $345K/año
- [x] Preparación infraestructura futura

### **Si se Implementa (Condicional)**
- [x] Cumplimiento especificaciones ASTM E1318
- [x] Certificación metrológica OIML R134
- [x] Integración completa con ITS
- [x] Personal capacitado especializado
- [x] Contratos mantenimiento vigentes

---

**📋 Estado**: COMPLETADO - Análisis costo-beneficio WIM  
**🎯 Recomendación**: NO implementar en fase inicial  
**📅 Alternativa**: Preparar infraestructura para futuro  
**👤 Responsable**: [ASIGNAR especialista ITS + análisis financiero]