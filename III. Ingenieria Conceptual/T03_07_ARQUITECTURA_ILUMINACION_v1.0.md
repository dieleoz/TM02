# T03: ARQUITECTURA CONCEPTUAL - ILUMINACIÓN
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Iluminación  
**Responsable:** Ingeniero Eléctrico  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual del sistema de Iluminación que garantizará visibilidad y seguridad nocturna en ubicaciones críticas del corredor, cumpliendo con estándares de iluminación vial y optimizando eficiencia energética.

### 1.2 Alcance
Arquitectura completa para iluminación en estaciones de peaje, puentes peatonales, intersecciones, áreas de servicio y otros puntos críticos del corredor de 272.1 km, con control automatizado y gestión centralizada.

### 1.3 Referencias
- T01_07: Ficha de Sistema - Iluminación
- T02_07: Análisis de Requisitos - Iluminación
- AT1: Tablas UF - Iluminación obligatoria
- CIE 115: Iluminación de carreteras

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    ┌─────────────────────────────────────┐
                    │              CCO                    │
                    │  ┌─────────────────────────────┐    │
                    │  │   Sistema Gestión Ilum.    │    │
                    │  │   - Control automático      │    │
                    │  │   - Monitoreo consumo       │    │
                    │  │   - Programación horarios   │    │
                    │  └─────────────────────────────┘    │
                    └─────────────┬───────────────────────┘
                                  │ Red IP/DALI
                    ┌─────────────┴───────────────────────┐
                    │        Red Eléctrica + Control     │
                    │     (Tableros + Comunicaciones)    │
                    └─┬─────────┬─────────┬──────────────┘
                      │         │         │
        ┌─────────────┴─┐ ┌─────┴─────┐ ┌─┴──────────────┐
        │   Zona 1      │ │  Zona 2   │ │    Zona 3      │
        │ Peajes Norte  │ │Puentes+Int│ │ Peajes+Áreas   │
        │ (120 luminar.)│ │(172 luminar)│ │ (140 luminar.) │
        └─┬─────────────┘ └─┬─────────┘ └─┬──────────────┘
          │                 │             │
    ┌─────┴─────┐     ┌─────┴─────┐ ┌─────┴─────┐
    │Luminarias │     │Luminarias │ │Luminarias │
    │LED + Poste│     │LED + Poste│ │LED + Poste│
    │+ Fotocelda│     │+ Fotocelda│ │+ Fotocelda│
    │+ Control  │     │+ Control  │ │+ Control  │
    └───────────┘     └───────────┘ └───────────┘
```

**Descripción del diagrama:**
Sistema distribuido con control centralizado desde CCO, tableros eléctricos zonificados, luminarias LED inteligentes con control DALI y fotoceldas para operación automática crepuscular.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Luminarias LED 150W** | Iluminación peajes/intersecciones | 150W, 20,000 lm, IP65 | 300 unidades |
| **Luminarias LED 100W** | Iluminación puentes/áreas | 100W, 13,000 lm, IP65 | 132 unidades |
| **Postes Metálicos 12m** | Soporte luminarias principales | Acero galvanizado, fundación | 350 unidades |
| **Postes Metálicos 8m** | Soporte luminarias secundarias | Acero galvanizado, fundación | 82 unidades |
| **Tableros Eléctricos** | Control y protección | IP65, contactores, protecciones | 15 unidades |
| **Sistemas Control DALI** | Automatización inteligente | Controlador + sensores | 15 sistemas |
| **Fotoceldas** | Control crepuscular | Sensor luz + temporizador | 432 unidades |
| **Cableado Subterráneo** | Distribución eléctrica | Cable XLPE, ductos PVC | 25 km |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Topología Eléctrica

- **Tipo de topología:** Radial con anillos locales
- **Tensión primaria:** 13.2 kV (suministro)
- **Tensión secundaria:** 220V/440V (distribución)
- **Control:** Protocolo DALI sobre bus dedicado
- **Redundancia:** Sí - Alimentadores duales en zonas críticas

### 3.2 Diagrama de Topología

```
                     Suministro Eléctrico
                    ┌─────────────────────┐
                    │   Red 13.2 kV      │
                    │   (Distribuidora)   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │  Transformadores    │
                    │   13.2kV/440V       │
                    └─┬─────────┬─────────┘
                      │         │
            ┌─────────┴─┐   ┌───┴─────────┐
            │Tablero    │   │  Tablero    │
            │Zona 1     │   │  Zona 2     │
            │440V/220V  │   │  440V/220V  │
            └─┬─────────┘   └─┬───────────┘
              │               │
        ┌─────┴─────┐   ┌─────┴─────┐
        │Circuito   │   │Circuito   │
        │Luminarias │   │Luminarias │
        │+ Control  │   │+ Control  │
        │DALI       │   │DALI       │
        └───────────┘   └───────────┘
```

### 3.3 Zonificación del Sistema

**Zonas de iluminación:**
- **Zona 1 (km 0-90):** Estación peaje La Gómez + puentes zona norte
- **Zona 2 (km 90-180):** Estación peaje Morrison + intersecciones + puentes centro
- **Zona 3 (km 180-272):** Estación peaje Pailitas + áreas servicio + puentes sur

---

## 4. FLUJO DE ENERGÍA E INFORMACIÓN

### 4.1 Flujo de Control Automático

```
1. [Fotocelda detecta oscuridad]
   ↓ Señal analógica
2. [Controlador DALI procesa]
   ↓ Protocolo DALI
3. [Luminarias se encienden]
   ↓ Confirmación estado
4. [Sistema reporta a CCO]
   ↓ Red IP
5. [CCO monitorea consumo]
   ↓ Base de datos
6. [Al amanecer se apagan]
```

**Descripción del flujo:**
1. **Detección:** Fotoceldas detectan nivel de luz < 10 lux
2. **Procesamiento:** Controlador DALI evalúa condiciones
3. **Activación:** Luminarias LED se encienden progresivamente
4. **Monitoreo:** Sistema reporta estado y consumo al CCO
5. **Gestión:** CCO almacena datos y genera reportes
6. **Desactivación:** Al amanecer (>20 lux) se apagan automáticamente

### 4.2 Tipos de Datos

| Tipo de Dato | Formato | Volumen Estimado | Retención |
|:-------------|:--------|:-----------------|:----------|
| **Estado luminarias** | DALI digital | 50 MB/día | 90 días |
| **Consumo energético** | Medición kWh | 10 MB/día | 2 años |
| **Alarmas sistema** | JSON | 5 MB/día | 1 año |
| **Programación horarios** | XML | 1 MB/día | 6 meses |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Alimentación eléctrica** | Dual feed | 2 transformadores | Continuidad suministro |
| **Controladores DALI** | N+1 | Controlador backup | Operación automática |
| **Luminarias críticas** | Sobredimensionamiento | +20% luminarias | Compensar fallas |
| **Cableado** | Anillos cerrados | Alimentación dual | Continuidad circuitos |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad:** 95% mensual mínimo (según AT4, IL01)
- **MTBF luminarias:** 50,000 horas (5.7 años)
- **MTTR:** 24 horas para reparaciones
- **Uniformidad:** >0.4 según CIE 115
- **Tiempo reparación:** <24 horas (según AT4, IL03)

### 5.3 Puntos Únicos de Falla

| Componente | Es SPOF? | Mitigación |
|:-----------|:---------|:-----------|
| **Transformador zona** | Sí | Transformador backup |
| **Tablero eléctrico** | Sí | Tablero redundante zonas críticas |
| **Luminaria individual** | Sí | Solapamiento iluminación |
| **Controlador DALI** | Sí | Controlador backup |

---

## 6. SEGURIDAD

### 6.1 Seguridad Eléctrica

- Cumplimiento RETIE para todas las instalaciones
- Puesta a tierra completa del sistema
- Protecciones diferenciales en todos los circuitos
- Interruptores termomagnéticos dimensionados
- Señalización de riesgo eléctrico

### 6.2 Seguridad Física

- Luminarias antivandalismo IK10
- Postes con base antirrobo
- Tableros eléctricos con cerradura
- Cableado subterráneo protegido
- Cámaras CCTV en ubicaciones críticas

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| RETIE | Instalaciones eléctricas |
| NTC 900 | Código eléctrico colombiano |
| CIE 115 | Niveles de iluminación |
| IESNA RP-8 | Estándares iluminación vial |

---

## 7. ARQUITECTURA DE CONTROL

### 7.1 Sistema de Control DALI

```
┌─────────────────────────────────┐
│   NIVEL SUPERVISIÓN (CCO)       │ (Monitoreo y reportes)
├─────────────────────────────────┤
│   NIVEL CONTROL (Tableros)      │ (Controladores DALI)
├─────────────────────────────────┤
│   NIVEL CAMPO (Luminarias)      │ (LEDs + sensores)
└─────────────────────────────────┘
```

### 7.2 Funcionalidades de Control

| Función | Descripción | Protocolo |
|:--------|:------------|:----------|
| **Encendido/Apagado** | Control automático crepuscular | DALI |
| **Dimming** | Regulación intensidad lumínica | DALI |
| **Monitoreo** | Estado y consumo luminarias | DALI + IP |
| **Programación** | Horarios y escenarios | DALI |
| **Diagnóstico** | Detección fallas automática | DALI |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | IF-001 | TCP/IP | Media | Estado, consumo, alarmas |
| **Puentes Peatonales** | IF-002 | Eléctrico | Alta | Energía para iluminación |
| **Estaciones Peaje** | IF-003 | Eléctrico | Alta | Iluminación operacional |
| **Áreas de Servicio** | IF-004 | Eléctrico | Media | Iluminación nocturna |
| **Red Eléctrica** | IF-005 | AC 13.2kV | Alta | Suministro energético |

---

## 9. ESCALABILIDAD

### 9.1 Dimensionamiento Actual vs Futuro

| Parámetro | Año 1 | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:------|:-------|:-------|:-------------------|
| **Luminarias LED** | 432 | 450 | 480 | Capacidad 500 |
| **Consumo energético** | 180 kW | 190 kW | 200 kW | Dimensionado 250 kW |
| **Puntos control** | 15 | 16 | 18 | Sistema para 20 |
| **Longitud cableado** | 25 km | 27 km | 30 km | Ductos para 35 km |

### 9.2 Estrategia de Crecimiento

El sistema permite agregar luminarias adicionales sin cambios arquitectónicos mayores:
- Capacidad eléctrica sobredimensionada 25%
- Controladores DALI escalables
- Ductos con capacidad de reserva
- Tableros con espacios disponibles

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Seleccionadas

| Categoría | Tecnología | Versión | Justificación |
|:----------|:-----------|:--------|:--------------|
| **Luminarias** | LED SMD | Última generación | Eficiencia y durabilidad |
| **Control** | DALI | v2.0 | Estándar internacional |
| **Comunicaciones** | Ethernet | 100 Mbps | Integración CCO |
| **Sensores** | Fotoceldas digitales | IP65 | Precisión y durabilidad |

### 10.2 Interoperabilidad

- **Con sistemas ANI:** Protocolo DALI estándar
- **Con otros concesionarios:** Tecnología compatible
- **Con distribuidora eléctrica:** Conexión estándar

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Iluminación Convencional

**Descripción:** Luminarias sodio alta presión con control básico

**Ventajas:**
- Menor costo inicial
- Tecnología conocida
- Mantenimiento simple

**Desventajas:**
- Mayor consumo energético
- Menor vida útil
- Control limitado
- Mayor impacto ambiental

**Costo estimado:** $1,200,000

### 11.2 Alternativa 2: Iluminación LED Inteligente ⭐ **RECOMENDADA**

**Descripción:** Luminarias LED con control DALI y gestión inteligente

**Ventajas:**
- 60% menor consumo energético
- Vida útil 50,000 horas
- Control inteligente
- Menor mantenimiento
- Mejor calidad lumínica

**Desventajas:**
- Mayor inversión inicial
- Tecnología más compleja

**Costo estimado:** $1,919,000

**Justificación de selección:** ROI en 4 años por ahorro energético, mejor cumplimiento normativo y menor impacto ambiental.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Diseño fotométrico detallado | 2 meses | Ubicaciones definidas |
| **Fase 2** | Adquisición luminarias y postes | 3 meses | Diseño aprobado |
| **Fase 3** | Instalación infraestructura eléctrica | 4 meses | Suministro eléctrico |
| **Fase 4** | Instalación luminarias zona piloto | 2 meses | Infraestructura lista |
| **Fase 5** | Pruebas y comisionamiento | 1 mes | Instalación completa |
| **Fase 6** | Despliegue completo | 3 meses | Zona piloto aprobada |

### 12.2 Hitos Críticos

- **H1:** Estudios fotométricos aprobados - Mes 2
- **H2:** Primera zona iluminada (piloto) - Mes 8
- **H3:** Sistema completo operativo - Mes 12

---

## 13. PRÓXIMOS PASOS

- [ ] Realizar estudios fotométricos detallados por zona
- [ ] Desarrollar especificaciones técnicas luminarias (T04)
- [ ] Validar niveles iluminación con normativa CIE 115
- [ ] Estimar costos detallados con fabricantes LED
- [ ] Crear plan de mantenimiento preventivo
- [ ] Obtener aprobación diseños con distribuidora eléctrica

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Eléctrico | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Eléctrico