# T01: FICHA DE SISTEMA - PANELES LED
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Paneles LED (Paneles de Mensaje Variable)  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Paneles LED (Paneles de Mensaje Variable - PMV) |
| **Categoría** | ITS - Información a Usuarios |
| **Prioridad** | Alta |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT1 (Sección Paneles LED), AT2 (Sección 3.3.3.2.4) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema de información dinámica que presenta mensajes variables a los usuarios de la vía para informar sobre condiciones del tráfico, incidentes, trabajos en la vía, condiciones meteorológicas y asistencia en la seguridad de la conducción.

### 2.2 Alcance del Sistema
- **Paneles incluidos:**
  - 25 paneles LED mínimo
  - Distribución cada 20 km máximo
  
- **Cobertura geográfica:** 272.1 km del corredor completo
- **Integración con:** CCO, Sistema de Información a Usuarios, Bases de Operación

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Obligaciones del Contrato
**Según AT1, Sección "Paneles LED":**
"El Concesionario deberá instalar cómo mínimo veinticinco (25) paneles LED en el Corredor del Proyecto, los cuales no podrán estar separados uno del otro por una distancia mayor a veinte (20) kilómetros por sentido"

### 3.2 Requisitos de Instalación
**Según AT1:**
"Los paneles LED deberán instalarse alternadamente sobre las bermas externas, a lado y lado de la vía y de forma simultánea mientras se realizan las Obras de Construcción de una vía nueva"

### 3.3 Requisitos Operacionales
**Según AT2, Sección 3.3.3.2.4:**
"El Concesionario deberá contar con pantallas de información y señalización e información dinámica de tipo LED... para presentar información en la vía a los diferentes usuarios, conductores y demás viajeros, que también ofrecen asistencia de seguridad en la conducción"

### 3.4 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **Manual Señalización Vial 2015** | Especificaciones PMV | Diseño y ubicación |
| **NTCIP 1203** | Protocolo comunicación PMV | Interoperabilidad |
| **IEC 62471** | Seguridad fotobiológica LED | Protección usuarios |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Paneles LED principales** | 25 unidades | Cada 20 km máximo | Información dinámica |
| **Paneles LED peajes** | 6 unidades | Aproximación peajes | Info específica peajes |
| **Estructuras soporte** | 31 unidades | Por panel | Soporte mecánico |
| **Controladores locales** | 31 unidades | Por panel | Control local |
| **Sistemas comunicación** | 31 unidades | Por panel | Enlace con CCO |
| **Sistemas energía** | 31 unidades | Por panel | Alimentación eléctrica |
| **Software gestión** | 1 sistema | CCO | Control centralizado |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Red IP | Ethernet/Fibra | Mensajes, estado, alarmas |
| Bases de Operación | Red IP | Ethernet | Información incidentes |
| Estaciones Peaje | Red IP | Ethernet | Tarifas, estado peajes |
| Sistema Info Usuarios | Red IP | TCP/IP | Mensajes coordinados |
| Emisora Radio | Integración | Software | Mensajes sincronizados |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Paneles LED matriz completa** | 25 unidades | $35,000 | $875,000 |
| **Paneles LED peajes** | 6 unidades | $25,000 | $150,000 |
| **Estructuras soporte** | 31 unidades | $8,000 | $248,000 |
| **Controladores locales** | 31 unidades | $3,000 | $93,000 |
| **Sistemas comunicación** | 31 unidades | $2,500 | $77,500 |
| **Instalación eléctrica** | 31 puntos | $5,000 | $155,000 |
| **Software gestión** | 1 licencia | $50,000 | $50,000 |
| **Instalación y puesta en marcha** | 1 proyecto | $80,000 | $80,000 |
| **TOTAL CAPEX** | | | **$1,728,500** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Energía eléctrica (31 paneles) | $62,000 |
| Mantenimiento preventivo | $45,000 |
| Reemplazo LEDs (5% anual) | $35,000 |
| Comunicaciones | $18,000 |
| Licencias software | $12,000 |
| Personal técnico | $24,000 |
| **TOTAL OPEX/año** | **$196,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Vandalismo paneles | Media | Medio | Ubicación elevada + CCTV |
| Falla comunicaciones | Media | Alto | Redundancia enlaces |
| Degradación LEDs | Alta | Medio | Mantenimiento preventivo |
| Cortes energía | Media | Medio | UPS local + generadores |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT4:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **PMV01** | Disponibilidad paneles LED | 95% mensual | Continua |
| **PMV02** | Tiempo actualización mensaje | < 2 minutos | Por cambio |
| **PMV03** | Legibilidad diurna/nocturna | 100% | Semanal |
| **PMV04** | Tiempo respuesta sistema | < 30 segundos | Continua |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Definir ubicaciones específicas con estudios de visibilidad
- [ ] Elaborar especificaciones técnicas detalladas (Template T04)
- [ ] Cotizar paneles LED de fabricantes reconocidos
- [ ] Diseñar arquitectura de comunicaciones
- [ ] Validar cumplimiento normativa señalización vial

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Paneles LED con tecnología full color para máxima versatilidad
- Comunicación via fibra óptica para todos los paneles
- Software de gestión integrado con CCO
- Visibilidad mínima 200m en condiciones normales

### 10.2 Dependencias
- Disponibilidad red de fibra óptica
- Suministro energía eléctrica en cada ubicación
- Aprobación ubicaciones por autoridades viales
- Integración con software CCO

### 10.3 Restricciones
- Separación máxima 20 km entre paneles
- Instalación alternada bermas externas
- Cumplimiento manual señalización vial 2015
- Operación 24/7/365

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas