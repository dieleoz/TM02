# T02: ANÁLISIS DE REQUISITOS - VARIANTES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Variantes  
**Responsable:** Ingeniero Civil Vial - Especialista  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para las Variantes del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y normativa técnica vial colombiana para construcción de nuevas vías.

### 1.2 Alcance
Análisis completo de requisitos para construcción de variantes que evitan el paso por centros urbanos, mejorando la movilidad y reduciendo impactos en comunidades locales del corredor de 272.1 km.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **INVIAS** | Instituto Nacional de Vías |
| **AASHTO** | American Association of State Highway Transportation Officials |
| **TPD** | Tráfico Promedio Diario |
| **NSR-10** | Norma Sismo Resistente Colombiana 2010 |
| **CBR** | California Bearing Ratio |
| **IRI** | International Roughness Index |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Construcción Vías Nuevas

**ID:** RF-001  
**Descripción:** Construir nuevas vías que eviten el paso por centros urbanos según trazado contractual  
**Prioridad:** Alta  
**Fuente:** AT1, Variantes obligatorias  

**Criterios de Aceptación:**
- Vías doble calzada según especificaciones
- Velocidad de diseño 100 km/h
- Separador central con barrera
- Bermas pavimentadas 2.5m
- Drenaje completo longitudinal y transversal###
 2.2 Estructuras de Drenaje Mayor

**ID:** RF-002  
**Descripción:** Construir puentes y obras de arte para cruce de corrientes de agua  
**Prioridad:** Alta  
**Fuente:** INVIAS, Drenaje vial  

**Criterios de Aceptación:**
- Puentes para caudal TR=100 años
- Gálibo hidráulico adecuado
- Fundaciones profundas si requerido
- Sistemas de protección contra socavación
- Accesos y obras de encauzamiento

### 2.3 Pavimento Estructural

**ID:** RF-003  
**Descripción:** Construir estructura de pavimento para tráfico pesado proyectado  
**Prioridad:** Alta  
**Fuente:** INVIAS, Diseño pavimentos  

**Criterios de Aceptación:**
- Diseño para 20 años vida útil
- Estructura según CBR subrasante
- Carpeta asfáltica MDC-2 mínimo
- IRI inicial < 2.0 m/km
- Juntas construcción selladas

### 2.4 Señalización y Demarcación

**ID:** RF-004  
**Descripción:** Implementar señalización vertical y horizontal completa  
**Prioridad:** Alta  
**Fuente:** Manual Señalización Vial 2015  

**Criterios de Aceptación:**
- Señalización vertical informativa y reglamentaria
- Demarcación horizontal reflectiva
- Delineadores y tachas reflectivas
- Señalización de aproximación a intersecciones
- Sistemas de contención vehicular

### 2.5 Obras Complementarias

**ID:** RF-005  
**Descripción:** Construir obras complementarias para operación segura  
**Prioridad:** Media  
**Fuente:** INVIAS, Especificaciones  

**Criterios de Aceptación:**
- Cercas perimetrales en zonas urbanas
- Pasos de fauna en zonas críticas
- Obras de estabilización de taludes
- Sistemas de recolección aguas lluvias
- Accesos controlados a predios

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad operacional | 100% | AT2 |
| **RNF-002** | Tiempo cierre por mantenimiento | < 2 horas | Operacional |
| **RNF-003** | Vida útil pavimento | 20 años | INVIAS |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Velocidad operación | 90 km/h | Diseño geométrico |
| **RNF-005** | Capacidad vehicular | TPD proyectado 2045 | Estudios tráfico |
| **RNF-006** | Nivel servicio | B mínimo | HCM |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Distancias visibilidad | Según velocidad diseño | INVIAS |
| **RNF-008** | Sistemas contención | Barreras centrales y laterales | Manual Señalización |
| **RNF-009** | Drenaje superficial | Sin encharcamientos | INVIAS |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Geometría consistente | Radios y pendientes uniformes | AASHTO |
| **RNF-011** | Señalización clara | Información anticipada | Manual 2015 |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Acceso mantenimiento | Facilidades para equipos | INVIAS |
| **RNF-013** | Materiales durables | Resistencia 20 años | Especificaciones |
| **RNF-014** | IRI mantenimiento | < 3.5 m/km durante vida útil | INVIAS |

### 3.6 Requisitos Ambientales

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Manejo aguas lluvias | Sin afectación predios | Ambiental |
| **RNF-016** | Control erosión | Obras de protección | Ambiental |
| **RNF-017** | Pasos de fauna | En zonas críticas identificadas | Ambiental |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con Vía Principal Existente

**ID:** RI-001  
**Sistemas:** Variantes ↔ Vía Existente  
**Tipo:** Física/Vial  
**Protocolo:** Empalmes geométricos  
**Datos Intercambiados:** Flujo vehicular  
**Frecuencia:** Continua

### 4.2 Interface con Vías Locales

**ID:** RI-002  
**Sistemas:** Variantes ↔ Vías Municipales  
**Tipo:** Física/Vial  
**Protocolo:** Intersecciones controladas  
**Datos Intercambiados:** Tráfico local  
**Frecuencia:** Continua

### 4.3 Interface con Drenaje Natural

**ID:** RI-003  
**Sistemas:** Variantes ↔ Corrientes Agua  
**Tipo:** Física/Hidráulica  
**Protocolo:** Puentes y alcantarillas  
**Datos Intercambiados:** Flujo hídrico  
**Frecuencia:** Por precipitación

### 4.4 Interface con Servicios Públicos

**ID:** RI-004  
**Sistemas:** Variantes ↔ Redes Servicios  
**Tipo:** Física  
**Protocolo:** Reubicaciones y cruces  
**Datos Intercambiados:** Servicios públicos  
**Frecuencia:** Permanente

### 4.5 Interface con CCO

**ID:** RI-005  
**Sistemas:** Variantes ↔ CCO  
**Tipo:** Informativa  
**Protocolo:** Reportes estado  
**Datos Intercambiados:** Incidentes, mantenimiento  
**Frecuencia:** Por evento

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Construcción vías nuevas | AT1 | Infraestructura vial | Alta |
| RF-002 | Funcional | Estructuras drenaje mayor | INVIAS | Puentes | Alta |
| RF-003 | Funcional | Pavimento estructural | INVIAS | Estructura pavimento | Alta |
| RF-004 | Funcional | Señalización demarcación | Manual 2015 | Sistemas ITS | Alta |
| RF-005 | Funcional | Obras complementarias | INVIAS | Obras adicionales | Media |
| RNF-001 | No Funcional | Disponibilidad 100% | AT2 | Sistema completo | Alta |
| RNF-003 | No Funcional | Vida útil 20 años | INVIAS | Pavimento | Alta |
| RNF-017 | No Funcional | Pasos fauna | Ambiental | Obras ambientales | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Trazado contractual fijo | Alineamiento no modificable | AT1 |
| **REST-002** | Especificaciones INVIAS | Diseño según normativa | Legal |
| **REST-003** | Licencias ambientales | Cumplimiento obligatorio | Ambiental |
| **REST-004** | Afectación predios mínima | Limitación diseño | Social |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Liberación predios exitosa | Alto (no construcción) | Proceso jurídico |
| **SUP-002** | Estudios geotécnicos favorables | Alto (rediseños) | Estudios detallados |
| **SUP-003** | Materiales disponibles región | Medio (costos adicionales) | Estudio mercado |
| **SUP-004** | Condiciones climáticas normales | Medio (retrasos construcción) | Planificación |

---

## 7. CASOS DE USO

### 7.1 Vehículo Transita por Variante

**ID:** CU-001  
**Actor:** Conductor  
**Descripción:** Vehículo utiliza variante evitando centro urbano  
**Precondiciones:** Variante operativa, señalización clara  
**Flujo Normal:**
1. Conductor se aproxima a inicio variante
2. Observa señalización direccional
3. Ingresa a variante por empalme
4. Transita a velocidad de diseño
5. Evita paso por centro urbano
6. Se reincorpora a vía principal
7. Continúa viaje

**Postcondiciones:** Tránsito exitoso evitando zona urbana  
**Flujos Alternativos:** Si hay obras, sigue desvíos temporales

### 7.2 Mantenimiento Rutinario Pavimento

**ID:** CU-002  
**Actor:** Cuadrilla Mantenimiento  
**Descripción:** Realizar mantenimiento rutinario del pavimento  
**Precondiciones:** Personal capacitado, equipos disponibles  
**Flujo Normal:**
1. Cuadrilla programa mantenimiento
2. Coordina cierre parcial de carriles
3. Ejecuta bacheo y sellado fisuras
4. Limpia sistemas de drenaje
5. Revisa y repara señalización
6. Mide IRI si programado
7. Actualiza registro mantenimiento

**Postcondiciones:** Pavimento en óptimo estado  
**Flujos Alternativos:** Si IRI > 3.5, programa rehabilitación

### 7.3 Inspección Estructuras Drenaje

**ID:** CU-003  
**Actor:** Inspector Hidráulico  
**Descripción:** Inspeccionar estado de puentes y alcantarillas  
**Precondiciones:** Inspector certificado, acceso seguro  
**Flujo Normal:**
1. Inspector programa inspección
2. Revisa estado estructural puentes
3. Verifica funcionamiento alcantarillas
4. Inspecciona obras de protección
5. Evalúa socavación en fundaciones
6. Documenta hallazgos
7. Programa mantenimiento si requerido

**Postcondiciones:** Estado hidráulico documentado  
**Flujos Alternativos:** Si encuentra daños críticos, restringe tráfico

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Variantes construidas según trazado contractual
- [ ] Vías doble calzada con velocidad diseño 100 km/h
- [ ] Estructuras de drenaje para TR=100 años
- [ ] Pavimento con vida útil 20 años
- [ ] Señalización y demarcación completa

### 8.2 Criterios de Performance

- [ ] Disponibilidad operacional 100%
- [ ] Velocidad operación ≥ 90 km/h
- [ ] Nivel de servicio B mínimo
- [ ] IRI inicial < 2.0 m/km

### 8.3 Criterios de Calidad

- [ ] Cumplimiento especificaciones INVIAS
- [ ] Estructuras según NSR-10
- [ ] Señalización según Manual 2015
- [ ] Obras ambientales según licencias

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Liberación Predios** | Requerida para construcción | Alta | ⏳ Pendiente |
| **Licencias Ambientales** | Para inicio construcción | Alta | ⏳ Pendiente |
| **Estudios Geotécnicos** | Para diseño pavimentos | Alta | ⏳ Pendiente |
| **Reubicación Servicios** | Para construcción | Media | ⏳ Pendiente |
| **Materiales Construcción** | Para ejecución obras | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Completar estudios geotécnicos detallados
- [ ] Finalizar diseños geométricos y estructurales
- [ ] Validar diseños con INVIAS
- [ ] Elaborar especificaciones técnicas construcción (T04)
- [ ] Acelerar proceso liberación de predios

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil Vial | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil Vial - Especialista