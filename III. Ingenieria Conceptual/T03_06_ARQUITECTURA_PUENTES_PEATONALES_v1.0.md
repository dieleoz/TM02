# T03: ARQUITECTURA CONCEPTUAL - PUENTES PEATONALES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Puentes Peatonales  
**Responsable:** Ingeniero Civil Estructural  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual del sistema de Puentes Peatonales que garantizará el cruce seguro de peatones sobre la vía principal, eliminando conflictos vehiculares y cumpliendo con la distribución contractual obligatoria.

### 1.2 Alcance
Arquitectura completa para 43 puentes peatonales distribuidos según AT1 Tabla 48, incluyendo diseño estructural, iluminación, señalización y sistemas de drenaje para el corredor de 272.1 km.

### 1.3 Referencias
- T01_06: Ficha de Sistema - Puentes Peatonales
- T02_06: Análisis de Requisitos - Puentes Peatonales
- AT1: Tabla 48 - Puentes Peatonales por UF
- NSR-10: Norma Sismo Resistente

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    DISTRIBUCIÓN CONTRACTUAL AT1
                    ┌─────────────────────────────────────┐
                    │         43 PUENTES TOTAL            │
                    └─────────────┬───────────────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
   ┌────▼────┐              ┌─────▼─────┐              ┌────▼────┐
   │  UF3    │              │    UF6    │              │   UF7   │
   │18 puentes│              │ 4 puentes │              │3 puentes│
   │77.20 km │              │ 20.37 km  │              │14.59 km │
   └─────────┘              └───────────┘              └─────────┘
        │                         │                         │
   ┌────▼────┐              ┌─────▼─────┐
   │  UF9    │              │   UF10    │
   │5 puentes│              │13 puentes │
   │22.90 km │              │ 39.04 km  │
   └─────────┘              └───────────┘

            ARQUITECTURA TIPO ESTÁNDAR
    ┌─────────────────────────────────────────────┐
    │              PUENTE PEATONAL                │
    │                                             │
    │  Rampa    ┌─────────────────┐    Rampa     │
    │  Acceso   │    TABLERO      │   Acceso     │
    │    8%     │   Luz 30-40m    │     8%       │
    │    ┌──────┤   Ancho 3.0m    ├──────┐       │
    │    │      │   Gálibo 5.5m   │      │       │
    │    │      └─────────────────┘      │       │
    │    │                               │       │
    │ ┌──▼──┐                         ┌──▼──┐    │
    │ │Apoyo│                         │Apoyo│    │
    │ │ A1  │                         │ A2  │    │
    │ └─────┘                         └─────┘    │
    │                                             │
    │  [Iluminación LED] [Señalización]          │
    └─────────────────────────────────────────────┘
```

**Descripción del diagrama:**
Sistema de 43 puentes distribuidos según obligación contractual AT1, con diseño estructural estándar replicable, adaptable a condiciones específicas de cada ubicación.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Puentes Estándar 30m** | Cruce peatonal | Luz 30m, ancho 3.0m | 35 unidades |
| **Puentes Especiales 40m+** | Cruce vías amplias | Luz 40-50m, ancho 3.0m | 8 unidades |
| **Estructuras Soporte** | Apoyo tablero | Concreto armado, NSR-10 | 86 apoyos |
| **Rampas Acceso** | Acceso peatonal | Pendiente máx 8%, ancho 3.0m | 86 rampas |
| **Sistema Iluminación** | Visibilidad nocturna | LED, 20 lux promedio | 43 sistemas |
| **Señalización** | Información usuarios | Vertical y horizontal | 43 juegos |
| **Sistema Drenaje** | Manejo aguas lluvias | Bajantes y canales | 43 sistemas |
| **Barreras Seguridad** | Protección peatonal | Altura 1.10m, acero | 43 juegos |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Distribución Geográfica Contractual

- **Tipo de distribución:** Según AT1 Tabla 48 (obligatoria)
- **Criterio ubicación:** Unidades Funcionales predefinidas
- **Separación promedio:** Variable según densidad poblacional
- **Integración:** Con sistema de iluminación y señalización

### 3.2 Diagrama de Distribución

```
    KM 0                    KM 272.1
     │                         │
     ▼                         ▼
┌────────┬────────┬────────┬────────┬────────┐
│  UF3   │  UF6   │  UF7   │  UF9   │ UF10   │
│18 ptes │4 ptes  │3 ptes  │5 ptes  │13 ptes │
│        │        │        │        │        │
│●●●●●●●●│●●●●    │●●●     │●●●●●   │●●●●●●●●│
│●●●●●●●●│        │        │        │●●●●●●●●│
│●●      │        │        │        │        │
└────────┴────────┴────────┴────────┴────────┘
   77km     20km     15km     23km     39km
```

### 3.3 Tipología Estructural

**Tipos de puentes según luz:**
- **Tipo A (30m):** Vigas pretensadas, 35 unidades
- **Tipo B (40m):** Vigas postensadas, 6 unidades  
- **Tipo C (50m):** Estructura metálica, 2 unidades

---

## 4. DISEÑO ESTRUCTURAL CONCEPTUAL

### 4.1 Arquitectura Estructural Tipo

```
SECCIÓN TRANSVERSAL TIPO
┌─────────────────────────────────┐
│    Baranda 1.10m                │
│  ┌─────────────────────────────┐ │
│  │                             │ │
│  │      TABLERO 3.0m           │ │ 5.5m
│  │   Superficie antideslizante │ │ Gálibo
│  └─────────────────────────────┘ │
│                                 │
│         VIGA PRINCIPAL          │
│                                 │
└─────────────────────────────────┘
              VÍA PRINCIPAL
```

**Elementos estructurales:**
1. **Cimentación:** Zapatas aisladas o pilotes según geotecnia
2. **Apoyos:** Columnas concreto armado, sección variable
3. **Superestructura:** Vigas pretensadas + losa colaborante
4. **Tablero:** Concreto f'c=28 MPa, superficie antideslizante
5. **Barandas:** Acero estructural, altura 1.10m

### 4.2 Cargas de Diseño

| Tipo de Carga | Valor | Norma |
|:---------------|:------|:------|
| **Carga viva peatonal** | 500 kg/m² | NSR-10 |
| **Carga viento** | 0.8 kN/m² | NSR-10 |
| **Carga sísmica** | Zona amenaza intermedia | NSR-10 |
| **Carga muerta** | Peso propio + acabados | NSR-10 |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia Estructural

| Elemento | Tipo de Redundancia | Configuración | Justificación |
|:---------|:--------------------|:--------------|:--------------|
| **Apoyos** | Múltiples columnas | 2 apoyos mínimo | Redistribución cargas |
| **Vigas principales** | Sección sobredimensionada | Factor seguridad 2.0 | Cumplir NSR-10 |
| **Cimentación** | Zapatas independientes | Una por apoyo | Falla localizada |
| **Accesos** | Rampas duales | 2 rampas por puente | Acceso alternativo |

### 5.2 Disponibilidad Operacional

- **Disponibilidad:** 100% estructural
- **Vida útil:** 75 años mínimo
- **Mantenimiento:** Inspecciones cada 6 meses
- **Tiempo reparación:** < 48 horas para daños menores
- **Cierre temporal:** Solo por daños estructurales críticos

### 5.3 Análisis de Fallas

| Modo de Falla | Probabilidad | Consecuencia | Mitigación |
|:---------------|:-------------|:-------------|:-----------|
| **Fatiga materiales** | Baja | Media | Inspecciones regulares |
| **Socavación cimientos** | Media | Alta | Obras de protección |
| **Impacto vehicular** | Baja | Alta | Gálibo adecuado |
| **Vandalismo** | Media | Baja | Diseño antivandalismo |

---

## 6. SEGURIDAD

### 6.1 Seguridad Estructural

- Cumplimiento NSR-10 para diseño sismo resistente
- Factor de seguridad 2.0 para cargas permanentes
- Materiales certificados (concreto, acero)
- Supervisión técnica especializada
- Pruebas de carga antes de puesta en servicio

### 6.2 Seguridad Operacional

- Barreras vehiculares en accesos
- Superficie antideslizante en tablero
- Barandas altura 1.10m con resistencia 150 kg/m
- Iluminación nocturna 20 lux mínimo
- Señalización clara y reflectiva

### 6.3 Normativa de Seguridad Aplicable

| Norma | Aplicación |
|:------|:-----------|
| NSR-10 | Diseño sismo resistente |
| AASHTO LRFD | Diseño de puentes |
| INVIAS 2013 | Especificaciones construcción |
| Manual Señalización 2015 | Señalización y demarcación |

---

## 7. ARQUITECTURA DE MATERIALES

### 7.1 Especificaciones de Materiales

```
MATERIALES PRINCIPALES
┌─────────────────────────────────┐
│  CONCRETO                       │
│  - f'c = 28 MPa (tablero)      │
│  - f'c = 21 MPa (apoyos)       │
│  - Aditivos impermeabilizantes  │
├─────────────────────────────────┤
│  ACERO DE REFUERZO              │
│  - fy = 420 MPa (Grado 60)     │
│  - Recubrimiento 4 cm mínimo    │
│  - Malla electrosoldada tablero │
├─────────────────────────────────┤
│  ACERO ESTRUCTURAL              │
│  - ASTM A572 Gr 50 (barandas)  │
│  - Galvanizado en caliente     │
│  - Pintura anticorrosiva        │
└─────────────────────────────────┘
```

### 7.2 Durabilidad y Mantenimiento

| Material | Vida Útil | Mantenimiento | Reemplazo |
|:---------|:----------|:--------------|:----------|
| **Concreto estructural** | 75 años | Sellado fisuras | No requerido |
| **Acero refuerzo** | 75 años | Inspección visual | Reparación local |
| **Barandas acero** | 25 años | Pintura cada 5 años | Reemplazo parcial |
| **Superficie tablero** | 15 años | Limpieza regular | Renovación |

---

## 8. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **Sistema Iluminación** | IF-001 | Eléctrico | Media | Energía para luminarias |
| **Señalización Vial** | IF-002 | Físico | Media | Integración señales |
| **Drenaje Vial** | IF-003 | Hidráulico | Media | Manejo aguas lluvias |
| **CCO** | IF-004 | Informativo | Baja | Reportes estado |
| **Áreas de Servicio** | IF-005 | Físico | Baja | Conectividad peatonal |

---

## 9. ESCALABILIDAD

### 9.1 Capacidad Actual vs Futura

| Parámetro | Actual | Año 10 | Año 20 | Capacidad Diseñada |
|:----------|:-------|:-------|:-------|:-------------------|
| **Flujo peatonal** | 500 peat/día | 800 peat/día | 1200 peat/día | 2000 peat/día |
| **Carga viva** | 500 kg/m² | 500 kg/m² | 500 kg/m² | 750 kg/m² |
| **Puentes adicionales** | 43 | 45 | 48 | Estructura permite +10 |

### 9.2 Estrategia de Ampliación

El diseño permite agregar puentes adicionales usando la misma tipología estructural. Para ampliaciones futuras:
- Diseño estándar replicable
- Proveedores de materiales establecidos
- Procedimientos constructivos probados
- Personal técnico capacitado

---

## 10. TECNOLOGÍA Y ESTÁNDARES

### 10.1 Tecnologías Constructivas

| Categoría | Tecnología | Justificación |
|:----------|:-----------|:--------------|
| **Cimentación** | Zapatas/Pilotes | Según condiciones geotécnicas |
| **Superestructura** | Vigas pretensadas | Eficiencia estructural |
| **Tablero** | Losa colaborante | Rapidez constructiva |
| **Acabados** | Concreto arquitectónico | Durabilidad y estética |

### 10.2 Interoperabilidad

- **Con normativa INVIAS:** Cumplimiento especificaciones
- **Con otros concesionarios:** Diseño estándar replicable
- **Con autoridades locales:** Coordinación ubicaciones

---

## 11. ANÁLISIS DE ALTERNATIVAS

### 11.1 Alternativa 1: Puentes Metálicos

**Descripción:** Estructura metálica con tablero de concreto

**Ventajas:**
- Menor peso propio
- Rapidez de montaje
- Luces mayores posibles

**Desventajas:**
- Mayor costo inicial
- Mantenimiento frecuente
- Corrosión en ambiente tropical

**Costo estimado:** $9,500,000

### 11.2 Alternativa 2: Puentes Concreto ⭐ **RECOMENDADA**

**Descripción:** Estructura de concreto armado/pretensado

**Ventajas:**
- Menor mantenimiento
- Durabilidad en clima tropical
- Costo competitivo
- Mano de obra local disponible

**Desventajas:**
- Mayor peso propio
- Tiempo construcción mayor

**Costo estimado:** $7,968,000

**Justificación de selección:** Mejor balance costo-beneficio considerando vida útil, mantenimiento y condiciones climáticas locales.

---

## 12. PLAN DE IMPLEMENTACIÓN

### 12.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Estudios geotécnicos 43 sitios | 3 meses | Ubicaciones definidas |
| **Fase 2** | Diseños estructurales detallados | 4 meses | Geotecnia completada |
| **Fase 3** | Construcción puentes piloto (5) | 6 meses | Diseños aprobados |
| **Fase 4** | Construcción masiva (38) | 12 meses | Piloto exitoso |
| **Fase 5** | Pruebas de carga y certificación | 2 meses | Construcción completa |

### 12.2 Hitos Críticos

- **H1:** Estudios geotécnicos completados - Mes 3
- **H2:** Primer puente operativo - Mes 9
- **H3:** 50% puentes operativos - Mes 15
- **H4:** Sistema completo certificado - Mes 21

---

## 13. PRÓXIMOS PASOS

- [ ] Realizar estudios geotécnicos en 43 ubicaciones
- [ ] Desarrollar diseños estructurales tipo (T04)
- [ ] Validar ubicaciones con comunidades locales
- [ ] Obtener permisos construcción INVIAS
- [ ] Estimar costos detallados con constructores
- [ ] Crear especificaciones técnicas construcción

---

## 14. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil Estructural | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil Estructural