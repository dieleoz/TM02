# T02: ANÁLISIS DE REQUISITOS - INTERCAMBIADORES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Intercambiadores  
**Responsable:** Ingeniero Civil Vial  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para los Intercambiadores del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y normativa técnica vial colombiana.

### 1.2 Alcance
Análisis completo de requisitos para 3 intercambiadores viales que garantizan conectividad segura y eficiente entre la vía principal y vías secundarias en el corredor de 272.1 km.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **INVIAS** | Instituto Nacional de Vías |
| **AASHTO** | American Association of State Highway Transportation Officials |
| **TPD** | Tráfico Promedio Diario |
| **NSR-10** | Norma Sismo Resistente Colombiana 2010 |
| **PCI** | Pavement Condition Index |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Conectividad Vial Segura

**ID:** RF-001  
**Descripción:** Proporcionar conexión segura y eficiente entre vía principal y vías secundarias  
**Prioridad:** Alta  
**Fuente:** AT1, Intercambiadores obligatorios  

**Criterios de Aceptación:**
- Eliminación completa de conflictos vehiculares
- Velocidades de diseño según normativa INVIAS
- Radios de curvatura mínimos cumplidos
- Distancias de visibilidad garantizadas
- Capacidad para tráfico proyectado 20 años### 2.2 Est
ructuras de Paso

**ID:** RF-002  
**Descripción:** Construir estructuras de paso (puentes/viaductos) para separación de niveles  
**Prioridad:** Alta  
**Fuente:** AT1, Diseño intercambiadores  

**Criterios de Aceptación:**
- Gálibo mínimo 5.5m sobre vía principal
- Ancho calzada según tráfico proyectado
- Resistencia estructural según NSR-10
- Vida útil estructural ≥ 75 años
- Sistemas de drenaje integrados

### 2.3 Rampas de Conexión

**ID:** RF-003  
**Descripción:** Diseñar y construir rampas de conexión con geometría adecuada  
**Prioridad:** Alta  
**Fuente:** INVIAS, Manual Diseño Geométrico  

**Criterios de Aceptación:**
- Pendientes máximas según normativa
- Radios mínimos para velocidad diseño
- Carriles de aceleración y desaceleración
- Longitudes de entrecruzamiento adecuadas
- Señalización horizontal y vertical completa

### 2.4 Sistemas de Drenaje

**ID:** RF-004  
**Descripción:** Implementar sistemas de drenaje para manejo de aguas lluvias  
**Prioridad:** Alta  
**Fuente:** INVIAS, Drenaje vial  

**Criterios de Aceptación:**
- Capacidad para lluvia TR=25 años
- Cunetas y alcantarillas dimensionadas
- Sistemas de recolección en estructuras
- Obras de entrega adecuadas
- Mantenimiento accesible

### 2.5 Iluminación y Señalización

**ID:** RF-005  
**Descripción:** Proporcionar iluminación y señalización completa para operación nocturna  
**Prioridad:** Media  
**Fuente:** Manual Señalización Vial 2015  

**Criterios de Aceptación:**
- Iluminación LED en todas las rampas
- Señalización vertical informativa y reglamentaria
- Demarcación horizontal reflectiva
- Sistemas de contención vehicular
- Señalización de aproximación

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad operacional | 100% | AT2 |
| **RNF-002** | Tiempo cierre por mantenimiento | < 4 horas | Operacional |
| **RNF-003** | Resistencia estructural | 75 años vida útil | AASHTO |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Capacidad vehicular | TPD proyectado 2045 | Estudios tráfico |
| **RNF-005** | Velocidad operación | 80% velocidad diseño | AASHTO |
| **RNF-006** | Nivel servicio | C mínimo | HCM |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Cumplimiento NSR-10 | Diseño sismo resistente | Legal |
| **RNF-008** | Sistemas contención | Barreras según velocidad | Manual Señalización |
| **RNF-009** | Distancias visibilidad | Según velocidad diseño | INVIAS |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Señalización clara | Información anticipada | Manual Señalización |
| **RNF-011** | Geometría intuitiva | Trayectorias naturales | AASHTO |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Acceso mantenimiento | Facilidades inspección | AASHTO |
| **RNF-013** | Materiales durables | Resistencia 25 años | INVIAS |
| **RNF-014** | Juntas de dilatación | Sellado impermeable | NSR-10 |

### 3.6 Requisitos Ambientales

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Manejo aguas lluvias | Sin afectación predios | Ambiental |
| **RNF-016** | Control erosión | Obras de protección | Ambiental |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con Vía Principal

**ID:** RI-001  
**Sistemas:** Intercambiadores ↔ Vía Principal  
**Tipo:** Física/Vial  
**Protocolo:** Continuidad geométrica  
**Datos Intercambiados:** Flujo vehicular  
**Frecuencia:** Continua

### 4.2 Interface con Vías Secundarias

**ID:** RI-002  
**Sistemas:** Intercambiadores ↔ Vías Locales  
**Tipo:** Física/Vial  
**Protocolo:** Empalmes geométricos  
**Datos Intercambiados:** Tráfico local  
**Frecuencia:** Continua

### 4.3 Interface con Sistema Iluminación

**ID:** RI-003  
**Sistemas:** Intercambiadores ↔ Iluminación  
**Tipo:** Física/Eléctrica  
**Protocolo:** Integración luminarias  
**Datos Intercambiados:** Iluminación nocturna  
**Frecuencia:** Crepuscular

### 4.4 Interface con Drenaje Regional

**ID:** RI-004  
**Sistemas:** Intercambiadores ↔ Drenaje Natural  
**Tipo:** Física/Hidráulica  
**Protocolo:** Obras entrega  
**Datos Intercambiados:** Aguas lluvias  
**Frecuencia:** Por precipitación

### 4.5 Interface con CCO

**ID:** RI-005  
**Sistemas:** Intercambiadores ↔ CCO  
**Tipo:** Informativa  
**Protocolo:** Reportes estado  
**Datos Intercambiados:** Incidentes, mantenimiento  
**Frecuencia:** Por evento

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Conectividad segura | AT1 | Diseño geométrico | Alta |
| RF-002 | Funcional | Estructuras paso | AT1 | Puentes/viaductos | Alta |
| RF-003 | Funcional | Rampas conexión | INVIAS | Geometría rampas | Alta |
| RF-004 | Funcional | Sistemas drenaje | INVIAS | Obras hidráulicas | Alta |
| RF-005 | Funcional | Iluminación señalización | Manual 2015 | Sistemas ITS | Media |
| RNF-001 | No Funcional | Disponibilidad 100% | AT2 | Sistema completo | Alta |
| RNF-003 | No Funcional | Vida útil 75 años | AASHTO | Estructuras | Alta |
| RNF-007 | No Funcional | Cumplimiento NSR-10 | Legal | Diseño estructural | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Ubicaciones fijas contractuales | No modificables | AT1 |
| **REST-002** | Gálibo mínimo 5.5m obligatorio | Altura estructuras | INVIAS |
| **REST-003** | Cumplimiento NSR-10 | Diseño sismo resistente | Legal |
| **REST-004** | Afectación predios mínima | Limitación diseño | Social |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Estudios geotécnicos favorables | Alto (cimentaciones especiales) | Estudios detallados |
| **SUP-002** | Tráfico proyectado según estudios | Medio (sobredimensionamiento) | Validación estudios |
| **SUP-003** | Materiales disponibles región | Bajo (costos transporte) | Estudio mercado |
| **SUP-004** | Permisos ambientales aprobados | Alto (no construcción) | Trámites |

---

## 7. CASOS DE USO

### 7.1 Vehículo Utiliza Intercambiador

**ID:** CU-001  
**Actor:** Conductor  
**Descripción:** Vehículo utiliza intercambiador para cambiar de vía  
**Precondiciones:** Intercambiador operativo, señalización clara  
**Flujo Normal:**
1. Conductor se aproxima al intercambiador
2. Observa señalización de aproximación
3. Selecciona carril según destino
4. Ingresa a rampa de salida
5. Transita por rampa con velocidad adecuada
6. Se incorpora a vía destino
7. Continúa viaje

**Postcondiciones:** Cambio de vía exitoso y seguro  
**Flujos Alternativos:** Si hay congestión, reduce velocidad

### 7.2 Inspección Estructural Intercambiador

**ID:** CU-002  
**Actor:** Inspector Estructural  
**Descripción:** Realizar inspección periódica de estructuras  
**Precondiciones:** Inspector certificado, acceso seguro  
**Flujo Normal:**
1. Inspector programa inspección
2. Coordina cierre parcial si necesario
3. Inspecciona elementos estructurales
4. Verifica estado juntas y apoyos
5. Revisa sistemas drenaje
6. Documenta hallazgos
7. Programa mantenimiento si requerido

**Postcondiciones:** Estado estructural documentado  
**Flujos Alternativos:** Si encuentra daños críticos, cierra temporalmente

### 7.3 Mantenimiento Rutinario

**ID:** CU-003  
**Actor:** Cuadrilla Mantenimiento  
**Descripción:** Realizar mantenimiento rutinario del intercambiador  
**Precondiciones:** Personal capacitado, equipos disponibles  
**Flujo Normal:**
1. Cuadrilla accede según cronograma
2. Limpia sistemas de drenaje
3. Revisa y repara señalización
4. Mantiene áreas verdes
5. Verifica iluminación
6. Actualiza registro mantenimiento
7. Reporta novedades

**Postcondiciones:** Intercambiador en óptimo estado  
**Flujos Alternativos:** Si encuentra daños, programa reparación

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] 3 intercambiadores construidos según ubicaciones contractuales
- [ ] Conectividad completa sin conflictos vehiculares
- [ ] Estructuras con gálibo mínimo 5.5m
- [ ] Sistemas de drenaje dimensionados TR=25 años
- [ ] Iluminación y señalización completa operativa

### 8.2 Criterios de Performance

- [ ] Disponibilidad operacional 100%
- [ ] Capacidad para tráfico proyectado 2045
- [ ] Nivel de servicio C mínimo
- [ ] Velocidad operación ≥ 80% velocidad diseño

### 8.3 Criterios de Calidad

- [ ] Cumplimiento NSR-10 para diseño estructural
- [ ] Vida útil estructural ≥ 75 años
- [ ] Geometría según Manual INVIAS
- [ ] Señalización según Manual 2015

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Estudios Geotécnicos** | Requeridos para cimentaciones | Alta | ⏳ Pendiente |
| **Permisos Ambientales** | Para construcción | Alta | ⏳ Pendiente |
| **Liberación Predios** | Para construcción | Alta | ⏳ Pendiente |
| **Vía Principal** | Para continuidad | Alta | ⏳ Pendiente |
| **Sistema Iluminación** | Para operación nocturna | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Realizar estudios geotécnicos en 3 ubicaciones
- [ ] Validar diseños geométricos con INVIAS
- [ ] Desarrollar diseños estructurales detallados
- [ ] Elaborar especificaciones técnicas construcción (T04)
- [ ] Iniciar proceso liberación de predios

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil Vial | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil Vial