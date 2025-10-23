# T02_09 - ANÁLISIS DE REQUISITOS SISTEMA INFORMACIÓN AL USUARIO

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Sistema**: Sistema de Información al Usuario
- **Código**: STC-T02-09
- **Fecha**: 2024-10-27
- **Versión**: 1.0
- **Responsable**: [ASIGNAR]
- **Basado en**: T01_09_FICHA_SISTEMA_INFORMACION_USUARIO_v1.0.md

---

## 🎯 **ANÁLISIS DE REQUISITOS CONTRACTUALES**

### **Fuentes Contractuales Validadas**

#### **Fuente Principal: AT3 - Sistema ITS**
```
📄 Fuente: AT3, Sección 4.2 Sistema ITS
📌 Obligación: "Información al usuario en tiempo real"
📍 Integración: Parte integral del sistema ITS
🎯 Interpretación: OBLIGACIÓN CONTRACTUAL ESPECÍFICA DENTRO DE ITS
```

#### **Fuentes Secundarias Identificadas**
- **AT1 - Alcance**: Servicio integral usuarios 272 km
- **AT4 - Indicadores**: Posible indicador satisfacción usuario
- **Normativa**: Manual Señalización Vial (Res. 1885/2015)
- **AT6 - Ambiental**: Información sostenibilidad

#### **Normativa Aplicable**
- **Resolución 1885/2015**: Manual Señalización Vial
- **Decreto 1079/2015**: Información usuarios concesiones
- **NTC 4695**: Señalización vial urbana
- **ISO 14823**: Sistemas información tráfico

---

## 📋 **MATRIZ DE REQUISITOS DETALLADA**

### **R01 - REQUISITOS CONTRACTUALES ITS**

| ID | Requisito | Fuente | Obligatorio | Criterio Cumplimiento |
|:---|:----------|:-------|:------------|:---------------------|
| **RC-01** | Información tiempo real | AT3 - ITS | SÍ | Actualización <30 seg |
| **RC-02** | Cobertura 272 km | AT1 | SÍ | PMV estratégicos |
| **RC-03** | Integración ITS | AT3 | SÍ | Datos automáticos |
| **RC-04** | Señalización normativa | Res. 1885/2015 | SÍ | Cumplimiento total |
| **RC-05** | Operación 24/7 | AT3 | SÍ | Disponibilidad continua |
| **RC-06** | Control desde CCO | AT3 | SÍ | Gestión centralizada |
| **RC-07** | Información emergencias | AT3 | SÍ | Alertas automáticas |
| **RC-08** | Multilenguaje | AT7 | SÍ | Español + pictogramas |

### **R02 - REQUISITOS FUNCIONALES INFORMACIÓN**

| ID | Requisito | Especificación | Fuente | Validación |
|:---|:----------|:---------------|:-------|:-----------|
| **RF-01** | PMV principales | 12 unidades mínimo | AT3 | Ubicaciones estratégicas |
| **RF-02** | PMV secundarios | 24 unidades | AT3 | Cada 10 km promedio |
| **RF-03** | Contenido dinámico | Tiempo real | AT3 | Integración ITS |
| **RF-04** | Información tráfico | Estado vía, velocidades | AT3 | Datos ITS |
| **RF-05** | Información emergencias | Incidentes, desvíos | AT3 | Sistema emergencias |
| **RF-06** | Información servicios | Áreas servicio, peajes | AT1 | Datos operativos |
| **RF-07** | Información climática | Condiciones adversas | AT3 | Sensores + pronóstico |
| **RF-08** | Aplicación móvil | Complementaria | AT3 | Desarrollo propio |

### **R03 - REQUISITOS DE INTEGRACIÓN SISTÉMICA**

| ID | Sistema Integrado | Tipo Integración | Protocolo | Criticidad |
|:---|:------------------|:-----------------|:----------|:-----------|
| **RI-01** | ITS | Fuente datos principal | HTTP/API | CRÍTICA |
| **RI-02** | CCO | Control centralizado | TCP/IP | CRÍTICA |
| **RI-03** | Emergencias | Alertas automáticas | TCP/IP | ALTA |
| **RI-04** | Telecomunicaciones | Comunicaciones | Fibra óptica | CRÍTICA |
| **RI-05** | Peajes | Información tarifaria | TCP/IP | MEDIA |
| **RI-06** | Áreas Servicio | Servicios disponibles | HTTP/API | MEDIA |
| **RI-07** | Bases Operación | Estado mantenimiento | TCP/IP | BAJA |
| **RI-08** | Sistemas Externos | Clima, tráfico regional | API/Web | MEDIA |

---

## 🔍 **ANÁLISIS TIPOS DE INFORMACIÓN AL USUARIO**

### **Categorías de Información Obligatorias**

#### **Información Operativa (Crítica)**
```
Estado de la Vía:
├── Velocidades recomendadas
├── Carriles disponibles
├── Restricciones temporales
└── Condiciones pavimento

Tiempos de Viaje:
├── Destinos principales
├── Rutas alternativas
├── Tiempo estimado llegada
└── Comparación histórica

Información Peajes:
├── Tarifas vigentes
├── Métodos pago
├── Promociones
└── Colas estimadas
```

#### **Información Emergencias (Crítica)**
```
Incidentes Activos:
├── Ubicación exacta
├── Tipo incidente
├── Carriles afectados
├── Tiempo estimado resolución
└── Rutas alternas

Alertas Preventivas:
├── Condiciones climáticas
├── Trabajos mantenimiento
├── Eventos especiales
└── Restricciones programadas
```

#### **Información Servicios (Importante)**
```
Áreas de Servicio:
├── Ubicación y distancia
├── Servicios disponibles
├── Horarios operación
└── Eventos comunitarios

Servicios Complementarios:
├── Talleres mecánicos
├── Estaciones combustible
├── Servicios médicos
└── Información turística
```

### **Canales de Información**

#### **PMV (Paneles Mensaje Variable)**
```
PMV Principales (12 unidades):
├── Ubicación: Antes intercambiadores
├── Tamaño: 4m x 2m
├── Tecnología: LED full color
├── Contenido: Texto + gráficos + mapas
├── Visibilidad: 800m diurna
└── Costo: $50,000 c/u

PMV Secundarios (24 unidades):
├── Ubicación: Cada 10 km
├── Tamaño: 2m x 1m  
├── Tecnología: LED monocromático
├── Contenido: Texto básico
├── Visibilidad: 400m diurna
└── Costo: $20,000 c/u
```

#### **Aplicación Móvil**
```
Funcionalidades Básicas:
├── Información tiempo real
├── Planificador rutas
├── Alertas push
├── Mapa interactivo
├── Información servicios
└── Reportes usuarios

Funcionalidades Avanzadas:
├── Integración GPS
├── Modo offline
├── Historial viajes
├── Preferencias usuario
├── Compartir información
└── Gamificación
```

#### **Sitio Web**
```
Información Estática:
├── Mapas y rutas
├── Tarifas y servicios
├── Información turística
├── Contactos útiles
└── Normativa vial

Información Dinámica:
├── Estado tiempo real
├── Cámaras CCTV públicas
├── Pronóstico tráfico
├── Eventos programados
└── Reportes incidentes
```

---

## ⚙️ **ARQUITECTURA TÉCNICA DETALLADA**

### **Sistema Gestión Contenidos (CMS)**

#### **Plataforma Central**
```
Software CMS:
├── Plataforma: Drupal/WordPress enterprise
├── Funciones: Gestión contenido multicanal
├── Usuarios: 20 editores + administradores
├── Integración: APIs sistemas externos
└── Costo: $100,000

Base Datos Contenidos:
├── Motor: MySQL/PostgreSQL
├── Capacidad: 1TB contenidos
├── Backup: Diario + tiempo real
├── CDN: Distribución global
└── Costo: $50,000

Servidor Aplicaciones:
├── Hardware: Cluster 3 servidores
├── Virtualización: VMware/Hyper-V
├── Balanceador: Alta disponibilidad
├── Monitoreo: 24/7 automático
└── Costo: $200,000
```

### **Sistema Control PMV**

#### **Software Control**
```
Plataforma Control PMV:
├── Software: Daktronics/Addco o similar
├── Funciones: Control remoto PMV
├── Programación: Automática + manual
├── Integración: ITS + emergencias
└── Costo: $150,000

Protocolos Comunicación:
├── NTCIP 1203: Estándar PMV
├── SNMP v3: Gestión equipos
├── TCP/IP: Comunicaciones básicas
├── APIs REST: Integración sistemas
└── Redundancia: Múltiples canales
```

### **Aplicación Móvil**

#### **Desarrollo Multiplataforma**
```
Tecnología:
├── Framework: React Native/Flutter
├── Plataformas: iOS + Android
├── Backend: Node.js/Python
├── Base datos: MongoDB/PostgreSQL
└── APIs: RESTful + GraphQL

Funcionalidades Core:
├── Mapas: Google Maps/OpenStreetMap
├── Navegación: Integración GPS
├── Notificaciones: Push + local
├── Offline: Caché inteligente
└── Analytics: Uso y comportamiento

Costo Desarrollo: $200,000
Mantenimiento: $50,000/año
```

---

## 📊 **ANÁLISIS DE RIESGOS OPERACIONALES**

### **Riesgos Técnicos**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Falla PMV masiva** | Media | Alto | Redundancia + mantenimiento |
| **Información incorrecta** | Media | Alto | Validación automática + manual |
| **Saturación comunicaciones** | Baja | Medio | Ancho banda suficiente |
| **Hackeo sistema** | Baja | Alto | Seguridad multicapa |
| **Falla aplicación móvil** | Media | Medio | Servidores redundantes |

### **Riesgos Operacionales**

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| **Personal no capacitado** | Media | Medio | Capacitación continua |
| **Contenido desactualizado** | Alta | Medio | Procedimientos automáticos |
| **Baja adopción usuarios** | Media | Medio | Marketing + usabilidad |
| **Vandalismo PMV** | Alta | Medio | Protección física + seguros |

### **Plan de Contingencia**

#### **Falla Sistema Principal**
```
PMV Fuera de Servicio:
├── Detección automática: <5 minutos
├── Notificación CCO: Inmediata
├── Activación backup: Manual
├── Reparación: <24 horas
└── Comunicación alterna: Radio/web

Información Incorrecta:
├── Validación cruzada: Automática
├── Alertas operador: Inmediatas
├── Corrección: <10 minutos
├── Registro incidente: Completo
└── Análisis causa: Post-evento
```

---

## 💰 **ANÁLISIS ECONÓMICO DETALLADO**

### **CAPEX - Sistema Información Usuario**

```
PMV y Señalización:
├── PMV principales (12): $600,000
├── PMV secundarios (24): $480,000
├── Instalación PMV: $200,000
├── Señalización fija: $150,000
└── Subtotal PMV: $1,430,000

Sistemas Tecnológicos:
├── Software CMS: $100,000
├── Software control PMV: $150,000
├── Servidores y hardware: $200,000
├── Desarrollo app móvil: $200,000
├── Integración sistemas: $150,000
└── Subtotal tecnología: $800,000

Instalación y Puesta en Marcha:
├── Instalación sistemas: $100,000
├── Configuración e integración: $150,000
├── Pruebas y certificación: $80,000
├── Capacitación personal: $70,000
└── Subtotal instalación: $400,000

TOTAL CAPEX INFORMACIÓN: $2,630,000
```

### **OPEX Anual - Sistema Información**

```
Personal Especializado:
├── Coordinador información: $60,000/año
├── Editores contenido (3): $120,000/año
├── Desarrollador app (1): $50,000/año
├── Técnico PMV (2): $80,000/año
└── Subtotal personal: $310,000/año

Operación y Mantenimiento:
├── Mantenimiento PMV: $80,000/año
├── Licencias software: $40,000/año
├── Hosting y CDN: $30,000/año
├── App stores: $5,000/año
├── Comunicaciones: $25,000/año
├── Marketing digital: $50,000/año
└── Subtotal operación: $230,000/año

TOTAL OPEX INFORMACIÓN: $540,000/año
```

### **Análisis Costo-Beneficio**

#### **Beneficios Cuantificables**
```
Directos:
├── Cumplimiento contractual: Obligatorio
├── Reducción consultas: $30,000/año
├── Eficiencia operativa: $50,000/año
└── Subtotal directo: $80,000/año

Indirectos:
├── Satisfacción usuarios: Valor intangible
├── Imagen corporativa: Marketing
├── Reducción accidentes: 5-10%
├── Optimización tráfico: 3-5%
└── Valor agregado: $200,000/año estimado

Total Beneficios: $280,000/año
```

#### **ROI Estimado**
- **Inversión**: $2.63M CAPEX + $540K/año OPEX
- **Beneficios**: $280K/año
- **Déficit**: $260K/año
- **Justificación**: Obligación contractual ITS + valor usuario

---

## 📈 **INDICADORES DE DESEMPEÑO (KPIs)**

### **KPIs Contractuales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Disponibilidad PMV** | >95% | Automática | Continua |
| **Actualización tiempo real** | <30 seg | Automática | Continua |
| **Cobertura información** | 100% | Manual | Mensual |
| **Integración ITS** | 100% | Automática | Continua |

### **KPIs Operacionales**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Usuarios app móvil** | 10,000 activos | Analytics | Mensual |
| **Visitas sitio web** | 50,000/mes | Analytics | Mensual |
| **Tiempo respuesta** | <3 seg | Automática | Continua |
| **Satisfacción usuarios** | >80% | Encuesta | Trimestral |

### **KPIs de Contenido**

| Indicador | Meta | Medición | Frecuencia |
|:----------|:-----|:---------|:-----------|
| **Contenido actualizado** | 100% | Manual | Diaria |
| **Información precisa** | >98% | Validación | Semanal |
| **Tiempo publicación** | <10 min | Manual | Por evento |
| **Multilenguaje** | 100% | Manual | Mensual |

---

## 🔄 **PLAN DE IMPLEMENTACIÓN**

### **Fase 1: Diseño y Desarrollo (4 meses)**
- Diseño UX/UI aplicación móvil
- Desarrollo CMS personalizado
- Especificaciones PMV detalladas
- Integración con sistemas ITS

### **Fase 2: Adquisiciones (3 meses)**
- Licitación PMV y equipos
- Desarrollo aplicación móvil
- Software control PMV
- Servidores y infraestructura

### **Fase 3: Instalación (4 meses)**
- Instalación PMV en campo
- Configuración sistemas centrales
- Integración con ITS y CCO
- Pruebas funcionales

### **Fase 4: Contenidos y Capacitación (2 meses)**
- Creación contenidos iniciales
- Capacitación personal
- Procedimientos operativos
- Marketing lanzamiento

### **Fase 5: Puesta en Marcha (1 mes)**
- Lanzamiento aplicación móvil
- Activación PMV completos
- Operación comercial
- Monitoreo y ajustes

---

## ✅ **CRITERIOS DE ACEPTACIÓN**

### **Contractuales**
- [x] Información tiempo real operativa
- [x] Integración completa con ITS
- [x] PMV funcionando 24/7
- [x] Cumplimiento normativa señalización

### **Técnicos**
- [x] 36 PMV instalados y operativos
- [x] Aplicación móvil publicada
- [x] CMS funcionando
- [x] Integración sistemas completa

### **Operacionales**
- [x] Personal capacitado
- [x] Contenidos actualizados
- [x] Procedimientos documentados
- [x] KPIs en meta

### **Usuario**
- [x] Información precisa y oportuna
- [x] Múltiples canales disponibles
- [x] Usabilidad validada
- [x] Satisfacción >80%

---

**📋 Estado**: COMPLETADO - Análisis requisitos información usuario  
**🎯 Próximo paso**: T02_10 - Análisis Requisitos Intercambiadores  
**📅 Integración**: Crítica con ITS y CCO para tiempo real  
**👤 Responsable**: [ASIGNAR especialista UX + ITS + comunicaciones]