# T03: ARQUITECTURA CONCEPTUAL - INTERCAMBIADORES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Intercambiadores  
**Responsable:** Ingeniero Civil Vial - Especialista  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define la arquitectura conceptual de los 3 Intercambiadores del proyecto, infraestructuras viales críticas que garantizan conectividad segura y eficiente entre la vía principal y vías secundarias.

### 1.2 Alcance
Arquitectura completa de intercambiadores viales incluyendo diseño geométrico, estructuras de paso, sistemas de drenaje, señalización, iluminación y sistemas ITS integrados.

### 1.3 Referencias
- T01_12: Ficha Sistema Intercambiadores - CAPEX $28.0M USD
- T02_12: Análisis Requisitos Intercambiadores - 42 requisitos
- AT1: Ubicaciones obligatorias intercambiadores

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INTERCAMBIADORES (3 UBICACIONES)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │ INTERCAMBIADOR  │    │ INTERCAMBIADOR  │    │ INTERCAMBIADOR  │         │
│  │      No. 1      │    │      No. 2      │    │      No. 3      │         │
│  │   (Tipo Trébol) │    │ (Tipo Diamante) │    │ (Tipo Trompeta) │         │
│  │                 │    │                 │    │                 │         │
│  │ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │         │
│  │ │ESTRUCTURAS  │ │    │ │ESTRUCTURAS  │ │    │ │ESTRUCTURAS  │ │         │
│  │ │• Puentes    │ │    │ │• Viaductos  │ │    │ │• Puentes    │ │         │
│  │ │• Rampas     │ │    │ │• Rampas     │ │    │ │• Rampas     │ │         │
│  │ │• Muros      │ │    │ │• Muros      │ │    │ │• Muros      │ │         │
│  │ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │         │
│  │                 │    │                 │    │                 │         │
│  │ ┌─────────────┐ │    │ ┌─────────────┐ │    │ ┌─────────────┐ │         │
│  │ │ SISTEMAS    │ │    │ │ SISTEMAS    │ │    │ │ SISTEMAS    │ │         │
│  │ │• Drenaje    │ │    │ │• Drenaje    │ │    │ │• Drenaje    │ │         │
│  │ │• Iluminación│ │    │ │• Iluminación│ │    │ │• Iluminación│ │         │
│  │ │• Señalizac. │ │    │ │• Señalizac. │ │    │ │• Señalizac. │ │         │
│  │ │• CCTV       │ │    │ │• CCTV       │ │    │ │• CCTV       │ │         │
│  │ └─────────────┘ │    │ └─────────────┘ │    │ └─────────────┘ │         │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
│                                   │                                        │
└───────────────────────────────────┼────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │          INTEGRACIÓN         │
                    │                              │
                    ├─ CCO (Monitoreo) ───────────┼─ Sistema Iluminación    │
                    ├─ Telecomunicaciones ────────┼─ Paneles LED            │
                    ├─ Bases Operación ───────────┼─ CCTV Distribuido       │
                    └─ Mantenimiento Vial ───────┴─ Sistemas Emergencia     │
```

**Descripción del diagrama:**
Tres intercambiadores con tipologías específicas según tráfico y topografía, integrados con sistemas ITS para monitoreo y control operacional.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Puentes Principales** | Paso sobre vía principal | Luces 30-50m, 2-4 carriles | 6 estructuras |
| **Rampas Conexión** | Acceso/salida intercambiador | Pendiente máx 6%, radio mín 150m | 24 rampas |
| **Viaductos Elevados** | Separación niveles | Altura 8-12m, longitud variable | 4 estructuras |
| **Muros Contención** | Estabilización terraplenes | Altura 3-8m, concreto armado | 2,400 m lineales |
| **Sistema Drenaje** | Manejo aguas lluvias | Alcantarillas, cunetas, obras | 3 sistemas |
| **Iluminación LED** | Visibilidad nocturna | Postes 12m, luminarias 150W | 180 puntos |
| **Señalización Vertical** | Información conductores | Pórticos, señales laterales | 120 elementos |
| **Demarcación Horizontal** | Guía vehicular | Pintura termoplástica reflectiva | 15 km lineales |
| **CCTV Monitoreo** | Supervisión tráfico | Cámaras IP PTZ 4K | 18 cámaras |
| **Sistemas Contención** | Seguridad vehicular | Barreras metálicas/concreto | 8 km lineales |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Tipología por Intercambiador

- **Intercambiador 1:** Trébol completo (alto tráfico, 4 movimientos)
- **Intercambiador 2:** Diamante (tráfico medio, topografía plana)
- **Intercambiador 3:** Trompeta (conexión terminal, menor tráfico)

### 3.2 Diagrama de Configuraciones

```
INTERCAMBIADOR 1 - TIPO TRÉBOL:
                    ┌─────────┐
                    │ VÍA SEC │
                    │    ↕    │
            ┌───────┼─────────┼───────┐
            │       │    ○    │       │
    ────────┤   ○   │         │   ○   ├────────  VÍA PRINCIPAL
            │       │    ○    │       │
            └───────┼─────────┼───────┘
                    │    ↕    │
                    └─────────┘

INTERCAMBIADOR 2 - TIPO DIAMANTE:
                    ┌─────────┐
                    │ VÍA SEC │
                    │    ↕    │
            ┌───────┼─────────┼───────┐
    ────────┤       │    ◊    │       ├────────  VÍA PRINCIPAL
            └───────┼─────────┼───────┘
                    │    ↕    │
                    └─────────┘

INTERCAMBIADOR 3 - TIPO TROMPETA:
                    ┌─────────┐
                    │ VÍA SEC │
                    │    ↕    │
            ┌───────┼─────────┐
    ────────┤       │    ♪    │       VÍA PRINCIPAL
            └───────┼─────────┘
                    │    ↕    │
                    └─────────┘
```

### 3.3 Distribución Física

**Áreas por intercambiador:**
- **Área Total Afectada:** 15-25 hectáreas por intercambiador
- **Estructuras Principales:** Puentes, viaductos, muros
- **Rampas y Accesos:** Longitud total 2-4 km por intercambiador
- **Áreas Verdes:** Paisajismo y control erosión
- **Instalaciones Técnicas:** Casetas equipos, subestaciones

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo Operacional Principal

```
1. MONITOREO TRÁFICO (Cámaras CCTV, sensores)
   ↓
2. ANÁLISIS FLUJO (Algoritmos detección congestión)
   ↓
3. DETECCIÓN INCIDENTES (Automática + operador)
   ↓
4. ACTIVACIÓN RESPUESTA (Señalización dinámica)
   ↓
5. COORDINACIÓN CCO (Despacho recursos)
   ↓
6. GESTIÓN TRÁFICO (Desvíos, control accesos)
   ↓
7. NORMALIZACIÓN (Restablecimiento operación)
   ↓
8. REPORTE ESTADÍSTICO (Análisis performance)
```

**Descripción del flujo:**
Monitoreo continuo del tráfico con respuesta automatizada a incidentes y coordinación con CCO para gestión integral.

### 4.2 Tipos de Datos Generados

| Tipo de Dato | Fuente | Volumen Estimado | Uso Principal |
|:-------------|:-------|:-----------------|:--------------|
| **Video Tráfico** | Cámaras CCTV | 200 GB/día/intercambiador | Monitoreo, evidencia |
| **Conteos Vehiculares** | Sensores tráfico | 10 MB/día/intercambiador | Estadísticas, planificación |
| **Eventos Incidentes** | Detección automática | 5 MB/día/intercambiador | Gestión operacional |
| **Estado Iluminación** | Controladores LED | 1 MB/día/intercambiador | Mantenimiento |
| **Alarmas Sistemas** | Equipos ITS | 2 MB/día/intercambiador | Mantenimiento preventivo |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Estructuras Principales** | N/A | Diseño robusto NSR-10 | Vida útil 75 años |
| **Sistemas Iluminación** | N+1 | Circuitos independientes | Operación nocturna garantizada |
| **CCTV Monitoreo** | N+1 | Cámaras solapamiento | Cobertura sin puntos ciegos |
| **Comunicaciones** | Activo-Backup | Fibra + 4G backup | Conectividad CCO garantizada |
| **Alimentación Eléctrica** | N+1 | Doble acometida + UPS | Sistemas críticos sin interrupción |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad estructural:** 100% (excepto mantenimiento programado)
- **Disponibilidad sistemas ITS:** 95% mensual
- **MTBF estructuras:** 25 años (mantenimiento mayor)
- **MTTR sistemas:** < 8 horas
- **Tiempo respuesta incidentes:** < 15 minutos

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Estructura Principal** | Sí | Diseño sísmico robusto + inspecciones |
| **Sistemas Drenaje** | Sí | Mantenimiento preventivo + redundancia |
| **Alimentación Eléctrica** | No | Doble acometida + UPS |
| **Comunicaciones** | No | Fibra + backup 4G |
| **Personal Mantenimiento** | Sí | Contratos múltiples proveedores |

---

## 6. SEGURIDAD

### 6.1 Seguridad Estructural

- **Diseño sísmico** según NSR-10 zona amenaza alta
- **Factores seguridad** estructural ≥ 2.0
- **Materiales certificados** concreto f'c≥28MPa, acero 420MPa
- **Inspecciones regulares** cada 6 meses
- **Mantenimiento preventivo** según cronograma

### 6.2 Seguridad Vial

- **Señalización completa** según Manual 2015
- **Barreras contención** según velocidad diseño
- **Iluminación adecuada** niveles CIE 115
- **Drenaje superficial** sin encharcamientos
- **Visibilidad garantizada** distancias según velocidad

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| **NSR-10** | Diseño sismo resistente |
| **AASHTO LRFD** | Diseño puentes |
| **Manual Señalización 2015** | Señalización vial |
| **INVIAS 2013** | Especificaciones construcción |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Capas de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│   CAPA PRESENTACIÓN (Interfaces Monitoreo)                 │
│   • Dashboard CCO                                          │
│   • App Móvil Inspectores                                  │
│   • Reportes Web                                           │
├─────────────────────────────────────────────────────────────┤
│   CAPA LÓGICA NEGOCIO (Análisis Tráfico)                   │
│   • Algoritmos detección incidentes                        │
│   • Análisis flujo vehicular                               │
│   • Generación alertas                                     │
├─────────────────────────────────────────────────────────────┤
│   CAPA DATOS (Almacenamiento)                              │
│   • Base datos eventos                                     │
│   • Almacenamiento video                                   │
│   • Datos históricos tráfico                               │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Tecnologías Propuestas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **Análisis Video** | OpenCV + AI | Detección automática incidentes |
| **Base Datos** | PostgreSQL + TimescaleDB | Datos temporales tráfico |
| **Visualización** | Grafana + Mapbox | Dashboards tiempo real |
| **CCTV** | Milestone XProtect | Gestión video profesional |
| **Comunicaciones** | MQTT/HTTP | Protocolos IoT estándar |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | Fibra óptica | TCP/IP | Alta | Video, eventos, alarmas |
| **Sistema Iluminación** | Red local | DALI/TCP | Media | Control, estado luminarias |
| **Paneles LED** | Fibra | NTCIP 1203 | Media | Mensajes tráfico |
| **Bases Operación** | Radio/IP | DMR/TCP | Alta | Incidentes, recursos |
| **CCTV Distribuido** | Fibra | IP | Media | Streams video |
| **Telecomunicaciones** | Backbone | Ethernet | Alta | Conectividad general |
| **Mantenimiento Vial** | Móvil | 4G/WiFi | Baja | Reportes, programación |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **TPD Total** | 25,000 | 40,000 | 55,000 | 70,000 (+27%) |
| **Hora Pico** | 3,500 veh/h | 5,500 veh/h | 7,500 veh/h | 9,000 veh/h |
| **Cámaras CCTV** | 18 | 24 | 30 | 36 (+20%) |
| **Puntos Iluminación** | 180 | 200 | 220 | 250 (+14%) |
| **Sensores Tráfico** | 12 | 18 | 24 | 30 (+25%) |

### 9.2 Estrategia de Crecimiento

**Escalabilidad estructural:** Diseño permite ampliación carriles sin reconstrucción  
**Escalabilidad sistemas:** Arquitectura modular permite adición equipos  
**Escalabilidad software:** Plataforma cloud-ready para crecimiento demanda  
**Escalabilidad operacional:** Procedimientos estandarizados replicables

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Concreto Estructural** | f'c = 28 MPa | NSR-10 | Durabilidad, resistencia |
| **Acero Refuerzo** | Grado 420 MPa | ASTM A706 | Ductilidad sísmica |
| **Cámaras CCTV** | Axis P5655-E | Firmware 10.x | Robustez, analytics |
| **Iluminación** | Philips LED | CityTouch | Eficiencia, control |
| **Señalización** | 3M Diamond Grade | DG³ | Reflectividad, durabilidad |

### 10.2 Interoperabilidad

- **Con sistemas ANI:** Reportes según protocolos SIINCO
- **Con autoridades locales:** Coordinación tráfico urbano
- **Con otros concesionarios:** Estándares comunes señalización
- **Con sistemas emergencia:** Protocolos respuesta unificados

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Intersecciones a Nivel

**Descripción:** Intersecciones semaforizadas en lugar de intercambiadores

**Ventajas:**
- Menor inversión inicial
- Construcción más rápida
- Menor impacto ambiental

**Desventajas:**
- Mayor congestión tráfico
- Menor seguridad vial
- Mayores costos operativos

**Costo estimado:** $8,000,000 USD

### 11.2 Alternativa 2: Intercambiadores Completos ⭐ **RECOMENDADA**

**Descripción:** Intercambiadores a desnivel según tipología óptima

**Ventajas:**
- Fluidez tráfico garantizada
- Máxima seguridad vial
- Menor impacto operacional
- Vida útil 75 años

**Desventajas:**
- Mayor inversión inicial
- Construcción más compleja
- Mayor impacto temporal

**Costo estimado:** $28,000,000 USD

**Justificación de selección:** Para autopista 4G con concesión 25 años, los intercambiadores garantizan nivel de servicio y seguridad requeridos.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Estudios detallados y diseños | 8 meses | T02 completado |
| **Fase 2** | Liberación predios y permisos | 6 meses | Diseños aprobados |
| **Fase 3** | Construcción estructuras principales | 18 meses | Predios liberados |
| **Fase 4** | Instalación sistemas ITS | 6 meses | Estructuras 80% |
| **Fase 5** | Pruebas y comisionamiento | 4 meses | Instalación completa |
| **Fase 6** | Puesta en operación | 2 meses | Pruebas aprobadas |

### 12.2 Hitos Críticos

- **H1:** Diseños estructurales aprobados - Mes 8
- **H2:** Liberación predios completada - Mes 14
- **H3:** Primera estructura terminada - Mes 24
- **H4:** Sistemas ITS operativos - Mes 36
- **H5:** Intercambiadores operativos - Mes 42

---

## 13. PRÓXIMOS PASOS

- [ ] Validar tipologías con especialistas viales
- [ ] Desarrollar estudios geotécnicos detallados
- [ ] Crear especificaciones técnicas construcción (T04)
- [ ] Estimar costos detallados con constructores
- [ ] Obtener aprobación diseños con INVIAS
- [ ] Iniciar proceso liberación de predios

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil Vial | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil Vial - Especialista