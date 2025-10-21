# T03: ARQUITECTURA CONCEPTUAL - BASES DE OPERACIÓN
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Bases de Operación  
**Responsable:** Ingeniero Industrial - Operaciones  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define la arquitectura conceptual de las 2 Bases de Operación del proyecto, centros neurálgicos para la gestión operacional, mantenimiento y respuesta a emergencias en el corredor.

### 1.2 Alcance
Arquitectura completa de las bases de operación incluyendo infraestructura física, equipamiento operacional, sistemas de comunicación, flota vehicular y integración con CCO para cobertura de 272.1 km del corredor.

### 1.3 Referencias
- T01_03: Ficha Sistema Bases Operación - CAPEX $2.2M USD
- T02_03: Análisis Requisitos Bases Operación - 38 requisitos
- AT2: Sección 3.3.3.1 - Atención emergencias

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BASES DE OPERACIÓN (2 UBICACIONES)                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────┐    ┌─────────────────────────────────┐ │
│  │          BASE NORTE             │    │          BASE SUR               │ │
│  │      (km 0 - km 136)            │    │      (km 136 - km 272)          │ │
│  │                                 │    │                                 │ │
│  │ ┌─────────────┐ ┌─────────────┐ │    │ ┌─────────────┐ ┌─────────────┐ │ │
│  │ │   FLOTA     │ │ INSTALAC.   │ │    │ │   FLOTA     │ │ INSTALAC.   │ │ │
│  │ │ VEHICULAR   │ │  FÍSICAS    │ │    │ │ VEHICULAR   │ │  FÍSICAS    │ │ │
│  │ │             │ │             │ │    │ │             │ │             │ │ │
│  │ │ • Grúas     │ │ • Oficinas  │ │    │ │ • Grúas     │ │ • Oficinas  │ │ │
│  │ │ • Patrullas │ │ • Talleres  │ │    │ │ • Patrullas │ │ • Talleres  │ │ │
│  │ │ • Cama Baja │ │ • Almacén   │ │    │ │ • Cama Baja │ │ • Almacén   │ │ │
│  │ │ • Carrotaller│ │ • Dormitor. │ │    │ │ • Carrotaller│ │ • Dormitor. │ │ │
│  │ └─────────────┘ └─────────────┘ │    │ └─────────────┘ └─────────────┘ │ │
│  └─────────────────────────────────┘    └─────────────────────────────────┘ │
│                    │                                      │                │
│  ┌─────────────────────────────────────────────────────────────────────────┤
│  │                        SISTEMAS COMUNES                                 │
│  │                                                                         │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │
│  │ │   SISTEMA   │ │   SISTEMA   │ │   SISTEMA   │ │   SISTEMA   │        │
│  │ │ COMUNICAC.  │ │ DESPACHO    │ │ MANTENIM.   │ │ SEGURIDAD   │        │
│  │ │             │ │             │ │             │ │             │        │
│  │ │ • Radio VHF │ │ • Centro    │ │ • Talleres  │ │ • CCTV      │        │
│  │ │ • Telefonía │ │ • GPS Fleet │ │ • Repuestos │ │ • Control   │        │
│  │ │ • Internet  │ │ • Dispatch  │ │ • Herram.   │ │ • Acceso    │        │
│  │ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘        │
│  └─────────────────────────────────────────────────────────────────────────┤
│                                   │                                        │
└───────────────────────────────────┼────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │          INTEGRACIÓN         │
                    │                              │
                    ├─ CCO (Coordinación) ────────┼─ Ambulancias TAM        │
                    ├─ Policía (Emergencias) ─────┼─ Bomberos Locales       │
                    ├─ Hospitales (Médicas) ──────┼─ Grúas Privadas         │
                    └─ Proveedores (Servicios) ───┴─ Autoridades Locales    │
```

**Descripción del diagrama:**
Dos bases de operación estratégicamente ubicadas para cobertura completa del corredor, con flota vehicular especializada, instalaciones operativas y sistemas integrados de comunicación y despacho.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Grúas Medianas** | Rescate vehículos livianos | 15 ton, pluma telescópica | 4 unidades |
| **Grúas Pesadas** | Rescate vehículos pesados | 35 ton, rotator | 2 unidades |
| **Vehículos Patrulla** | Vigilancia y respuesta | 4x4, equipamiento policial | 6 unidades |
| **Cama Baja** | Transporte vehículos | 40 ton capacidad | 2 unidades |
| **Carrotaller** | Reparaciones menores | Equipamiento mecánico | 2 unidades |
| **Centro Despacho** | Coordinación operaciones | Sala control 24/7 | 2 centros |
| **Sistema Radio** | Comunicaciones campo | VHF/UHF repetidores | 2 sistemas |
| **Talleres Mantenimiento** | Servicio flota | Equipamiento completo | 2 talleres |
| **Oficinas Administrativas** | Gestión operacional | 200 m² por base | 2 oficinas |
| **Dormitorios Personal** | Descanso guardias | 8 camas por base | 2 módulos |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología Operacional

- **Tipo de cobertura:** Sectorial con solapamiento 20%
- **Protocolo comunicación:** Radio VHF/UHF + celular 4G backup
- **Segmentación:** Por tipo emergencia (médica, mecánica, seguridad)
- **Redundancia:** Doble cobertura en zona central del corredor

### 3.2 Diagrama de Cobertura

```
    0 km                    136 km                    272 km
     │                        │                        │
     ▼                        ▼                        ▼
┌────────────────────────────────────────────────────────┐
│                   CORREDOR VIAL                        │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌─────────────────┐              ┌─────────────────┐  │
│  │   BASE NORTE    │              │    BASE SUR     │  │
│  │   Cobertura:    │              │   Cobertura:    │  │
│  │   0-160 km      │◄────────────►│   112-272 km    │  │
│  │   (Solapamiento │              │   (Solapamiento │  │
│  │   20% = 24 km)  │              │   20% = 24 km)  │  │
│  └─────────────────┘              └─────────────────┘  │
│                                                        │
│  ┌─────────────────────────────────────────────────┐  │
│  │           ZONA SOLAPAMIENTO                     │  │
│  │              112-160 km                         │  │
│  │         (Doble cobertura)                       │  │
│  └─────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘

Tiempos Respuesta Objetivo:
• Emergencias Médicas: < 15 minutos
• Rescate Vehicular: < 20 minutos  
• Mantenimiento Vial: < 30 minutos
• Patrullaje Rutinario: < 45 minutos
```

### 3.3 Distribución Física por Base

**Áreas principales (cada base):**
- **Área Operativa (1,500 m²):** Estacionamiento flota, talleres, despacho
- **Área Administrativa (300 m²):** Oficinas, sala reuniones, archivo
- **Área Descanso (200 m²):** Dormitorios, cocina, sala estar
- **Área Almacenamiento (400 m²):** Repuestos, herramientas, combustible
- **Área Servicios (100 m²):** Baños, vestidores, lavandería

---

## 4. FLUJO DE DATOS E INFORMACIÓN

### 4.1 Flujo Operacional Principal

```
1. DETECCIÓN INCIDENTE (CCO, usuarios, patrullaje)
   ↓
2. CLASIFICACIÓN EMERGENCIA (Médica/Mecánica/Seguridad)
   ↓
3. DESPACHO RECURSOS (Base más cercana)
   ↓
4. MOVILIZACIÓN EQUIPOS (Grúa, patrulla, apoyo)
   ↓
5. ATENCIÓN EN SITIO (Rescate, reparación, seguridad)
   ↓
6. COORDINACIÓN EXTERNA (Hospitales, policía, bomberos)
   ↓
7. RESOLUCIÓN INCIDENTE (Normalización tráfico)
   ↓
8. REPORTE CIERRE (Documentación, estadísticas)
```

**Descripción del flujo:**
Proceso estandarizado de respuesta a emergencias con tiempos definidos y escalamiento automático según severidad del incidente.

### 4.2 Tipos de Operaciones

| Tipo Operación | Frecuencia Estimada | Tiempo Respuesta | Recursos Requeridos |
|:----------------|:-------------------|:-----------------|:--------------------|
| **Emergencia Médica** | 2-3/día | < 15 minutos | Patrulla + Ambulancia TAM |
| **Rescate Vehicular** | 4-5/día | < 20 minutos | Grúa + Patrulla |
| **Mantenimiento Vial** | 10-15/día | < 30 minutos | Carrotaller + Personal |
| **Patrullaje Rutinario** | Continuo | N/A | Patrulla |
| **Apoyo Eventos** | Variable | < 45 minutos | Según requerimiento |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Flota Grúas** | N+1 | 3 grúas por base (2+1) | Disponibilidad garantizada |
| **Comunicaciones** | Activo-Backup | Radio + Celular + Satelital | Conectividad sin fallas |
| **Personal Operativo** | 24/7/365 | 4 turnos rotativos | Cobertura continua |
| **Alimentación** | N+1 | Red + UPS + Generador | Operación sin interrupciones |
| **Centro Despacho** | Activo-Pasivo | Backup en base alterna | Continuidad operacional |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad operacional:** 99% mensual
- **Tiempo respuesta emergencias:** < 15 minutos (90% casos)
- **Disponibilidad flota:** 85% mínimo
- **MTTR equipos:** < 24 horas
- **Cobertura territorial:** 100% corredor

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Flota Vehicular** | No | Redundancia N+1 por tipo |
| **Personal Especializado** | Sí | Entrenamiento cruzado + backup |
| **Combustible** | Sí | Tanques reserva + proveedores múltiples |
| **Comunicaciones** | No | Múltiples tecnologías backup |
| **Acceso Bases** | Sí | Rutas alternas identificadas |

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- **Perímetro cercado** con alambre concertina
- **Control acceso** biométrico y tarjetas
- **CCTV perimetral** con grabación 30 días
- **Iluminación LED** con sensores movimiento
- **Alarma intrusión** conectada central monitoreo
- **Vigilancia 24/7** con personal de seguridad

### 6.2 Seguridad Operacional

- **Protocolos seguridad** para cada tipo operación
- **EPP completo** para todo el personal
- **Capacitación continua** en seguridad vial
- **Vehículos señalizados** según normativa
- **Comunicación permanente** con CCO
- **Procedimientos emergencia** documentados

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| **Resolución 1565/2014** | Seguridad y salud en trabajo |
| **Código Nacional Tránsito** | Operaciones en vía |
| **NFPA 1006** | Rescate técnico vehicular |

---

## 7. ARQUITECTURA DE SOFTWARE

### 7.1 Capas de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│   CAPA PRESENTACIÓN (Interfaces Operador)                  │
│   • Sistema Despacho (CAD)                                 │
│   • App Móvil Conductores                                  │
│   • Dashboard Supervisores                                 │
├─────────────────────────────────────────────────────────────┤
│   CAPA LÓGICA NEGOCIO (Motor Operaciones)                  │
│   • Algoritmos despacho                                    │
│   • Gestión recursos                                       │
│   • Escalamiento automático                                │
├─────────────────────────────────────────────────────────────┤
│   CAPA DATOS (Base Datos Operacional)                      │
│   • PostgreSQL (operaciones)                               │
│   • GIS (mapas y rutas)                                    │
│   • Historian (eventos)                                    │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Tecnologías Propuestas

| Capa | Tecnología | Justificación |
|:-----|:-----------|:--------------|
| **Sistema Despacho** | Motorola CommandCentral | Estándar industria emergencias |
| **Tracking GPS** | Garmin Fleet | Robustez, precisión |
| **Base Datos** | PostgreSQL + PostGIS | Open source, capacidades GIS |
| **Comunicaciones** | Motorola MOTOTRBO | Confiabilidad, cobertura |
| **App Móvil** | React Native | Multiplataforma, performance |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | Fibra óptica | TCP/IP | Alta | Incidentes, recursos, estado |
| **Ambulancias TAM** | Radio/4G | DMR/IP | Alta | Coordinación médica |
| **Policía Carreteras** | Radio | P25/DMR | Alta | Emergencias, infracciones |
| **Bomberos Locales** | Radio | Convencional | Media | Apoyo emergencias |
| **Hospitales** | Teléfono/4G | SIP/Celular | Media | Traslados médicos |
| **Proveedores Grúas** | Celular | Voz/SMS | Baja | Apoyo adicional |
| **Sistema Info Usuarios** | IP | TCP/IP | Media | Estado operaciones |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Incidentes/día** | 20 | 35 | 50 | 60 (+20% margen) |
| **Flota total** | 16 vehículos | 20 vehículos | 24 vehículos | 28 vehículos |
| **Personal operativo** | 32 personas | 40 personas | 48 personas | 56 personas |
| **Área instalaciones** | 2,500 m² | 3,000 m² | 3,500 m² | 4,000 m² |
| **Cobertura respuesta** | 15 min | 12 min | 10 min | Optimización continua |

### 9.2 Estrategia de Crecimiento

**Escalabilidad flota:** Bahías adicionales preparadas para 4 vehículos más por base  
**Escalabilidad personal:** Dormitorios expandibles para 50% más personal  
**Escalabilidad operaciones:** Sistema despacho soporta hasta 100 unidades  
**Escalabilidad territorial:** Bases intermedias si tráfico lo justifica

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Grúas** | Jerr-Dan/Century | 2024 | Confiabilidad, soporte local |
| **Radio Comunicaciones** | Motorola MOTOTRBO | R2.0 | Estándar emergencias |
| **Sistema Despacho** | Motorola CommandCentral | v2023 | Integración nativa radio |
| **Tracking GPS** | Garmin Fleet 790 | v6.x | Precisión, durabilidad |
| **Vehículos Base** | Toyota Hilux 4x4 | 2024 | Confiabilidad, servicio |

### 10.2 Interoperabilidad

- **Con Policía Nacional:** Radios compatibles P25/DMR
- **Con Bomberos:** Frecuencias convencionales VHF
- **Con Cruz Roja:** Protocolos médicos estándar
- **Con otros concesionarios:** Apoyo mutuo emergencias

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Tercerización Completa

**Descripción:** Contratar empresa especializada para todas las operaciones

**Ventajas:**
- Menor inversión inicial
- Experiencia especializada
- Menor complejidad gestión

**Desventajas:**
- Mayor costo operativo
- Menor control operacional
- Dependencia proveedor único

**Costo estimado:** $1,500,000 CAPEX + $1,200,000/año OPEX

### 11.2 Alternativa 2: Operación Propia ⭐ **RECOMENDADA**

**Descripción:** Bases propias con flota y personal directo

**Ventajas:**
- Control total operacional
- Menores costos largo plazo
- Mejor integración CCO
- Flexibilidad operativa

**Desventajas:**
- Mayor inversión inicial
- Complejidad gestión personal
- Responsabilidad mantenimiento

**Costo estimado:** $2,200,000 CAPEX + $954,000/año OPEX

**Justificación de selección:** Para concesión 25 años, el control operacional y menores costos operativos justifican la inversión inicial.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Diseño detallado y ubicaciones | 3 meses | T02 completado |
| **Fase 2** | Construcción instalaciones | 8 meses | Diseño aprobado |
| **Fase 3** | Adquisición flota y equipos | 6 meses | Instalaciones 50% |
| **Fase 4** | Contratación y capacitación personal | 4 meses | Instalaciones listas |
| **Fase 5** | Instalación sistemas y pruebas | 3 meses | Personal capacitado |
| **Fase 6** | Puesta en operación 24/7 | 2 meses | Sistemas probados |

### 12.2 Hitos Críticos

- **H1:** Ubicaciones bases definidas - Mes 3
- **H2:** Instalaciones físicas completadas - Mes 11
- **H3:** Flota completa entregada - Mes 14
- **H4:** Personal operativo capacitado - Mes 18
- **H5:** Bases operativas 24/7 - Mes 24

---

## 13. PRÓXIMOS PASOS

- [ ] Validar arquitectura con operadores especializados
- [ ] Desarrollar especificaciones técnicas flota (T04)
- [ ] Estimar costos detallados construcción e equipamiento
- [ ] Crear plan de capacitación personal operativo
- [ ] Obtener aprobación arquitectónica de stakeholders
- [ ] Iniciar proceso selección ubicaciones bases

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Industrial - Operaciones | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Industrial - Operaciones