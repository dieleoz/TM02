# T01: FICHA DE SISTEMA - ILUMINACIÓN
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Iluminación  
**Responsable:** Ingeniero Eléctrico  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Iluminación |
| **Categoría** | Infraestructura Eléctrica - Seguridad Vial |
| **Prioridad** | Alta |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT1 (Tablas UF - Iluminación obligatoria) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema de iluminación artificial que garantiza la visibilidad y seguridad nocturna en ubicaciones críticas del corredor vial, cumpliendo con los estándares de iluminación vial y reduciendo la accidentalidad nocturna.

### 2.2 Alcance del Sistema
- **Ubicaciones obligatorias:**
  - Estaciones de Peaje (3)
  - Estaciones de Pesaje
  - Centro de Control de Operación
  - Áreas de Servicio
  - Intersecciones a Nivel y Desnivel (3)
  - Paraderos y Puentes Peatonales (43)
  
- **Cobertura geográfica:** Puntos críticos en 272.1 km del corredor
- **Integración con:** Energía Eléctrica, CCO, Puentes Peatonales

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Obligaciones del Contrato
**Según AT1, Tablas de Unidades Funcionales:**
"Iluminación" aparece como ítem obligatorio en las siguientes ubicaciones:

### 3.2 Ubicaciones Contractuales Obligatorias

| Ubicación | Justificación Contractual | Fuente AT1 |
|:----------|:--------------------------|:-----------|
| **Estaciones de Peaje** | Operación 24/7 | Tablas UF - Iluminación |
| **Estaciones de Pesaje** | Control nocturno | Tablas UF - Iluminación |
| **CCO** | Operación continua | Tablas UF - Iluminación |
| **Áreas de Servicio** | Servicios nocturnos | Tablas UF - Iluminación |
| **Intersecciones Desnivel** | Seguridad vial | Tablas UF - Iluminación |
| **Puentes Peatonales** | Seguridad peatonal | Tablas UF - Iluminación |
| **Paraderos** | Seguridad usuarios | Tablas UF - Iluminación |

### 3.3 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **RETIE** | Reglamento Técnico Instalaciones Eléctricas | Instalaciones eléctricas |
| **NTC 900** | Código Eléctrico Colombiano | Diseño eléctrico |
| **CIE 115** | Iluminación de carreteras | Niveles de iluminación |
| **IESNA RP-8** | Iluminación vial | Estándares internacionales |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Luminarias LED peajes** | 120 unidades | 3 estaciones peaje | Iluminación operacional |
| **Luminarias LED puentes** | 172 unidades | 43 puentes peatonales | Seguridad peatonal |
| **Luminarias LED intersecciones** | 60 unidades | 3 intercambiadores | Seguridad vial |
| **Luminarias LED áreas servicio** | 80 unidades | Múltiples áreas | Servicios nocturnos |
| **Postes iluminación** | 432 unidades | Todas las ubicaciones | Soporte luminarias |
| **Tableros eléctricos** | 15 unidades | Por zona | Control y protección |
| **Sistemas control** | 15 sistemas | Por zona | Automatización |
| **Cableado y accesorios** | 1 lote | Todo el sistema | Conexiones eléctricas |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| Energía Eléctrica | Física/Eléctrica | AC 220V/440V | Suministro energía |
| CCO | Red IP | Ethernet | Estado, control, alarmas |
| Puentes Peatonales | Física | Estructural | Integración luminarias |
| Estaciones Peaje | Física/Eléctrica | Cableado | Iluminación operacional |
| Áreas de Servicio | Física/Eléctrica | Cableado | Iluminación servicios |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Luminarias LED 150W** | 300 unidades | $800 | $240,000 |
| **Luminarias LED 100W** | 132 unidades | $600 | $79,200 |
| **Postes metálicos 12m** | 350 unidades | $1,200 | $420,000 |
| **Postes metálicos 8m** | 82 unidades | $800 | $65,600 |
| **Tableros eléctricos** | 15 unidades | $8,000 | $120,000 |
| **Sistemas control/automatización** | 15 sistemas | $12,000 | $180,000 |
| **Cableado subterráneo** | 25 km | $15,000 | $375,000 |
| **Cimentaciones** | 432 unidades | $600 | $259,200 |
| **Instalación y puesta en marcha** | 1 proyecto | $180,000 | $180,000 |
| **TOTAL CAPEX** | | | **$1,919,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Energía eléctrica (432 luminarias) | $155,000 |
| Mantenimiento preventivo | $48,000 |
| Reemplazo luminarias (5% anual) | $32,000 |
| Reparaciones cableado | $24,000 |
| Limpieza luminarias | $18,000 |
| Personal técnico | $36,000 |
| **TOTAL OPEX/año** | **$313,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Robo de luminarias/cables | Alta | Alto | Luminarias antivandalismo + vigilancia |
| Fallas por sobretensión | Media | Medio | Protecciones eléctricas + UPS |
| Degradación LED prematura | Media | Medio | Luminarias calidad certificada |
| Cortes energía eléctrica | Media | Alto | Sistemas respaldo + generadores |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT4:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **IL01** | Disponibilidad sistema iluminación | 95% mensual | Continua |
| **IL02** | Nivel iluminación promedio | Según CIE 115 | Semestral |
| **IL03** | Tiempo reparación fallas | < 24 horas | Por evento |
| **IL04** | Uniformidad iluminación | > 0.4 | Semestral |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Realizar estudios fotométricos específicos
- [ ] Elaborar especificaciones técnicas luminarias (Template T04)
- [ ] Cotizar luminarias LED certificadas
- [ ] Diseñar sistemas control automatizado
- [ ] Validar niveles iluminación con normativa

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Luminarias LED con vida útil 50,000 horas
- Niveles iluminación según CIE 115 para vías clase A
- Disponibilidad energía eléctrica en todas las ubicaciones
- Sistemas control con protocolo DALI para automatización

### 10.2 Dependencias
- Suministro energía eléctrica estable
- Finalización obras civiles para instalación
- Aprobación diseños fotométricos
- Coordinación con otros sistemas (puentes, peajes)

### 10.3 Restricciones
- Cumplimiento RETIE para instalaciones eléctricas
- Niveles mínimos iluminación según CIE 115
- Luminarias con certificación IESNA
- Operación automática crepuscular

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Eléctrico