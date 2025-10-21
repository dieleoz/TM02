# T01: FICHA DE SISTEMA - ESTACIONES DE PEAJE
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Estaciones de Peaje  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Estaciones de Peaje |
| **Categoría** | Recaudación y Control de Acceso |
| **Prioridad** | Crítica |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT1 (Tabla 2, Tabla 49), AT2 (Sección 2.1.g) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema de recaudación de peajes para el proyecto de concesión APP, que permite el cobro de tarifas a los usuarios de la vía y genera los ingresos principales para la sostenibilidad del proyecto.

### 2.2 Alcance del Sistema
- **Estaciones incluidas:**
  - La Gómez (con reubicación obligatoria)
  - Morrison
  - Pailitas
  
- **Cobertura geográfica:** 272.1 km del corredor vial
- **Integración con:** CCO, Telecomunicaciones, Sistema de Información a Usuarios

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Obligaciones del Contrato
**Según AT1, Tabla 2 - Estaciones de Peaje Existentes:**
"Actualmente este proyecto cuenta con la(s) Estación(es) de Peaje que se relaciona(n) en la siguiente tabla, la(s) cual(es) será(n) será(n) entregada(s) conforme al procedimiento previsto en el numeral 3.6 (b) del Contrato Parte Especial"

**Según AT1, Tabla 49 - Nuevas Estaciones de Peaje:**
"El peaje existente en el PR 37+150 de la ruta nacional 4513 se traslada al PR 37+700 de la ruta nacional 4513"

### 3.2 Requisitos de Apéndices Técnicos
**Según AT2, Sección 2.1.g:**
"Operación de las Estaciones de Peaje"

**Según AT2, Sección 2.1.o:**
"Pago de Peaje con tarjeta o telepeaje, sin perjuicio de lo previsto en la Sección 3.3.4.3 de este mismo Apéndice"

### 3.3 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **Resolución ANI** | Tarifas de peaje | Cobro y recaudación |
| **Ley 105 de 1993** | Transporte y tránsito | Operación vial |
| **Decreto 1079 de 2015** | Sector transporte | Marco regulatorio |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Estación La Gómez** | 1 unidad | PR 37+700 RN 4513 (reubicada) | Recaudación bidireccional |
| **Estación Morrison** | 1 unidad | PR 39+750 RN 4514 | Recaudación bidireccional |
| **Estación Pailitas** | 1 unidad | PR 28+600 RN 4515 | Recaudación bidireccional |
| **Casetas de cobro** | 6-8 por estación | En cada estación | Cobro manual y automático |
| **Sistemas TAG/DSRC** | Por caseta | En cada caseta | Cobro electrónico |
| **Básculas** | Según necesidad | Integradas | Control de peso |
| **Sistemas de vigilancia** | Por estación | Perímetro completo | Seguridad |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Red IP | Ethernet/Fibra | Datos recaudación, alarmas, video |
| Telecomunicaciones | Red de datos | Fibra óptica | Comunicaciones centralizadas |
| Sistema Info Usuarios | Red IP | TCP/IP | Tarifas, estado operacional |
| Bases de Operación | Radio/IP | VHF/Ethernet | Coordinación emergencias |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Reubicación La Gómez** | 1 estación | $1,200,000 | $1,200,000 |
| **Modernización Morrison** | 1 estación | $800,000 | $800,000 |
| **Modernización Pailitas** | 1 estación | $800,000 | $800,000 |
| **Sistemas TAG/DSRC** | 24 equipos | $15,000 | $360,000 |
| **Sistemas vigilancia** | 3 sistemas | $80,000 | $240,000 |
| **Infraestructura civil** | 3 estaciones | $200,000 | $600,000 |
| **TOTAL CAPEX** | | | **$4,000,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal operación (3 estaciones) | $180,000 |
| Mantenimiento preventivo | $120,000 |
| Mantenimiento correctivo | $80,000 |
| Energía eléctrica | $60,000 |
| Comunicaciones | $36,000 |
| Seguros y vigilancia | $48,000 |
| **TOTAL OPEX/año** | **$524,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Retraso reubicación La Gómez | Media | Alto | Plan detallado construcción paralela |
| Vandalismo equipos TAG | Media | Medio | Sistemas antivandalismo + CCTV |
| Fallas sistema recaudación | Baja | Alto | Redundancia sistemas + respaldo |
| Protestas sociales | Media | Alto | Plan comunicación comunitaria |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT4:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **R01** | Disponibilidad sistema recaudación | 99% mensual | Continua |
| **R02** | Tiempo promedio transacción | < 30 segundos | Diaria |
| **R03** | Exactitud recaudación | 99.9% | Diaria |
| **R04** | Disponibilidad TAG/DSRC | 98% | Continua |

---

## 9. PRÓXIMOS PASOS

- [x] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Definir arquitectura conceptual (Template T03)
- [ ] Elaborar especificaciones técnicas (Template T04)
- [ ] Estimar costos detallados con cotizaciones
- [ ] Seleccionar proveedores sistemas TAG
- [ ] Validar con ANI y stakeholders

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Reubicación La Gómez se ejecutará sin interrumpir recaudación actual
- Sistemas TAG compatibles con estándar nacional
- Infraestructura eléctrica y comunicaciones disponible

### 10.2 Dependencias
- Finalización obras viales para reubicación La Gómez
- Aprobación ANI para nuevas tarifas
- Coordinación con operador actual para transición

### 10.3 Restricciones
- Reubicación La Gómez condición precedente para operación doble calzada
- Cumplimiento normativa ANI para sistemas recaudación
- Interoperabilidad con sistema nacional de peajes

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas