# T02: ANÁLISIS DE REQUISITOS - PUENTES PEATONALES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Puentes Peatonales  
**Responsable:** Ingeniero Civil Estructural  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para el sistema de Puentes Peatonales del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y normativa técnica colombiana.

### 1.2 Alcance
Análisis completo de requisitos para 43 puentes peatonales distribuidos en 5 Unidades Funcionales del corredor de 272.1 km, incluyendo diseño estructural, iluminación y señalización.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **UF** | Unidad Funcional |
| **NSR-10** | Norma Sismo Resistente Colombiana 2010 |
| **AASHTO** | American Association of State Highway and Transportation Officials |
| **LRFD** | Load and Resistance Factor Design |
| **INVIAS** | Instituto Nacional de Vías |
| **Gálibo** | Altura libre mínima sobre la calzada |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Cruce Seguro de Peatones

**ID:** RF-001  
**Descripción:** Los puentes deben proporcionar cruce seguro y eficiente para peatones sobre la vía principal, eliminando conflictos vehiculares  
**Prioridad:** Alta  
**Fuente:** AT1, Tabla 48  

**Criterios de Aceptación:**
- Ancho mínimo 3.0m para paso peatonal
- Gálibo mínimo 5.5m sobre calzada
- Pendiente máxima 8% en rampas de acceso
- Barandas de seguridad altura 1.10m mínimo
- Superficie antideslizante en toda la estructura

### 2.2 Distribución Según Unidades Funcionales

**ID:** RF-002  
**Descripción:** Los puentes deben ubicarse según distribución contractual obligatoria por Unidades Funcionales  
**Prioridad:** Alta  
**Fuente:** AT1, Tabla 48  

**Criterios de Aceptación:**
- UF3: 18 puentes en Río Sogamoso - El Juncal
- UF6: 4 puentes en La Mata - Pailitas  
- UF7: 3 puentes en Variante Pailitas
- UF9: 5 puentes en Curumaní - San Roque
- UF10: 13 puentes en La Gloria - San Roque
- Total: 43 puentes mínimo obligatorio

### 2.3 Resistencia Estructural

**ID:** RF-003  
**Descripción:** Las estructuras deben resistir todas las cargas de diseño según normativa colombiana e internacional  
**Prioridad:** Alta  
**Fuente:** NSR-10, AASHTO LRFD  

**Criterios de Aceptación:**
- Carga viva peatonal: 500 kg/m²
- Resistencia sísmica según NSR-10 zona de amenaza
- Factor de seguridad ≥ 2.0 para cargas permanentes
- Vida útil estructural ≥ 50 años
- Deflexión máxima L/300 bajo carga viva

### 2.4 Iluminación Nocturna

**ID:** RF-004  
**Descripción:** Todos los puentes deben contar con iluminación LED para uso nocturno seguro  
**Prioridad:** Media  
**Fuente:** Manual Señalización 2015  

**Criterios de Aceptación:**
- Iluminación LED mínimo 20 lux promedio
- Uniformidad iluminación ≥ 0.4
- Encendido automático por fotoceldas
- Protección IP65 para intemperie
- Vida útil LEDs ≥ 50,000 horas

### 2.5 Señalización e Información

**ID:** RF-005  
**Descripción:** Los puentes deben contar con señalización adecuada para orientar a usuarios  
**Prioridad:** Media  
**Fuente:** Manual Señalización Vial 2015  

**Criterios de Aceptación:**
- Señales informativas de aproximación
- Demarcación horizontal en accesos
- Señalización vertical en estructura
- Información de restricciones (no vehículos)
- Señales reflectivas para visibilidad nocturna

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad estructural | 100% | AT4, PP01 |
| **RNF-002** | Disponibilidad iluminación | 95% | AT4, PP02 |
| **RNF-003** | Tiempo reparación daños | < 48 horas | AT4, PP03 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Capacidad peatonal | 2,000 peatones/hora | AASHTO |
| **RNF-005** | Velocidad peatonal diseño | 1.2 m/s | AASHTO |
| **RNF-006** | Ancho efectivo mínimo | 3.0 m | INVIAS |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Barreras vehiculares | Impedir acceso vehículos | Manual Señalización |
| **RNF-008** | Barandas seguridad | Altura 1.10m, resistencia 150 kg/m | NSR-10 |
| **RNF-009** | Superficie antideslizante | Coeficiente fricción ≥ 0.6 | INVIAS |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Accesibilidad universal | Rampas para discapacitados | Ley 361/1997 |
| **RNF-011** | Pendiente máxima rampas | 8% máximo | INVIAS |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Acceso para mantenimiento | Facilidades inspección | AASHTO |
| **RNF-013** | Materiales durables | Resistencia corrosión 50 años | NSR-10 |
| **RNF-014** | Juntas de dilatación | Sellado impermeable | INVIAS |

### 3.6 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Diseño modular | Componentes estandarizados | Buenas prácticas |
| **RNF-016** | Capacidad ampliación | Previsión ensanche futuro | Buenas prácticas |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con Sistema de Iluminación

**ID:** RI-001  
**Sistemas:** Puentes Peatonales ↔ Sistema Iluminación  
**Tipo:** Física/Eléctrica  
**Protocolo:** Cableado eléctrico 220V  
**Datos Intercambiados:** Energía eléctrica, control encendido  
**Frecuencia:** Continua

### 4.2 Interface con Señalización Vial

**ID:** RI-002  
**Sistemas:** Puentes Peatonales ↔ Señalización  
**Tipo:** Física/Visual  
**Protocolo:** Integración estructural  
**Datos Intercambiados:** Información visual usuarios  
**Frecuencia:** Permanente

### 4.3 Interface con Vía Principal

**ID:** RI-003  
**Sistemas:** Puentes Peatonales ↔ Calzada  
**Tipo:** Física/Estructural  
**Protocolo:** Gálibo y separaciones  
**Datos Intercambiados:** Espacio físico, restricciones  
**Frecuencia:** Permanente

### 4.4 Interface con Áreas de Servicio

**ID:** RI-004  
**Sistemas:** Puentes Peatonales ↔ Áreas Servicio  
**Tipo:** Física/Accesos  
**Protocolo:** Conectividad peatonal  
**Datos Intercambiados:** Flujo peatonal  
**Frecuencia:** Continua

### 4.5 Interface con CCO

**ID:** RI-005  
**Sistemas:** Puentes Peatonales ↔ CCO  
**Tipo:** Informativa  
**Protocolo:** Reportes estado  
**Datos Intercambiados:** Estado estructural, incidentes  
**Frecuencia:** Mensual o por evento

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Cruce seguro peatones | AT1, Tabla 48 | Estructura completa | Alta |
| RF-002 | Funcional | Distribución por UF | AT1, Tabla 48 | Ubicaciones | Alta |
| RF-003 | Funcional | Resistencia estructural | NSR-10, AASHTO | Diseño estructural | Alta |
| RF-004 | Funcional | Iluminación nocturna | Manual Señalización | Sistema eléctrico | Media |
| RF-005 | Funcional | Señalización | Manual Señalización | Señales | Media |
| RNF-001 | No Funcional | Disponibilidad 100% | AT4, PP01 | Sistema completo | Alta |
| RNF-003 | No Funcional | Reparación < 48h | AT4, PP03 | Mantenimiento | Alta |
| RNF-007 | No Funcional | Barreras vehiculares | Manual Señalización | Accesos | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Ubicaciones fijas según Tabla 48 | No modificables | AT1, Contractual |
| **REST-002** | Gálibo mínimo 5.5m sobre calzada | Altura estructura fija | INVIAS |
| **REST-003** | Cumplimiento NSR-10 obligatorio | Diseño sismo resistente | Legal |
| **REST-004** | Ancho mínimo 3.0m peatonal | Dimensiones estructura | INVIAS |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Suelos con capacidad portante adecuada | Alto (cimentaciones especiales) | Estudios geotécnicos |
| **SUP-002** | Disponibilidad energía eléctrica | Medio (iluminación manual) | Coordinación eléctrica |
| **SUP-003** | Acceso para construcción disponible | Medio (costos adicionales) | Estudios topográficos |
| **SUP-004** | Materiales disponibles en región | Bajo (transporte adicional) | Estudio mercado |

---

## 7. CASOS DE USO

### 7.1 Cruce Peatonal Diurno

**ID:** CU-001  
**Actor:** Peatón  
**Descripción:** Peatón cruza vía principal usando puente peatonal durante el día  
**Precondiciones:** Puente operativo, accesos despejados  
**Flujo Normal:**
1. Peatón se aproxima al puente por rampa de acceso
2. Observa señalización informativa
3. Asciende por rampa con pendiente ≤ 8%
4. Cruza sobre la vía por tablero del puente
5. Desciende por rampa del lado opuesto
6. Sale del área del puente

**Postcondiciones:** Peatón ha cruzado la vía de forma segura  
**Flujos Alternativos:** Si hay obstáculos, utiliza puente alternativo más cercano

### 7.2 Cruce Peatonal Nocturno

**ID:** CU-002  
**Actor:** Peatón  
**Descripción:** Peatón utiliza puente durante horas nocturnas con iluminación  
**Precondiciones:** Puente operativo, iluminación funcionando  
**Flujo Normal:**
1. Sistema detecta oscuridad y enciende iluminación LED
2. Peatón se aproxima con visibilidad adecuada
3. Utiliza barandas para apoyo y seguridad
4. Cruza con iluminación mínimo 20 lux
5. Sistema mantiene iluminación durante uso
6. Iluminación se mantiene hasta amanecer

**Postcondiciones:** Cruce nocturno seguro completado  
**Flujos Alternativos:** Si falla iluminación, reporta a CCO para reparación

### 7.3 Inspección Estructural

**ID:** CU-003  
**Actor:** Inspector Estructural  
**Descripción:** Realizar inspección mensual del estado del puente  
**Precondiciones:** Inspector certificado, equipos de medición  
**Flujo Normal:**
1. Inspector accede al puente con equipos
2. Revisa estado de barandas y superficie
3. Verifica funcionamiento de iluminación
4. Inspecciona juntas y elementos estructurales
5. Mide deflexiones si es necesario
6. Documenta hallazgos en reporte
7. Programa mantenimiento si es requerido

**Postcondiciones:** Estado estructural documentado  
**Flujos Alternativos:** Si encuentra daños críticos, cierra puente temporalmente

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] 43 puentes construidos según distribución contractual
- [ ] Todos los puentes con gálibo mínimo 5.5m
- [ ] Ancho peatonal mínimo 3.0m en todos los puentes
- [ ] Iluminación LED operativa en todos los puentes
- [ ] Señalización completa según manual vigente

### 8.2 Criterios de Performance

- [ ] Disponibilidad estructural 100%
- [ ] Disponibilidad iluminación ≥ 95%
- [ ] Capacidad 2,000 peatones/hora por puente
- [ ] Deflexión máxima L/300 bajo carga viva

### 8.3 Criterios de Calidad

- [ ] Cumplimiento NSR-10 para diseño sismo resistente
- [ ] Certificación INVIAS para especificaciones
- [ ] Resistencia estructural según AASHTO LRFD
- [ ] Materiales con vida útil ≥ 50 años

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Estudios Geotécnicos** | Requeridos para diseño cimentaciones | Alta | ⏳ Pendiente |
| **Finalización Vías** | Ubicaciones definitivas | Alta | ⏳ Pendiente |
| **Sistema Eléctrico** | Para iluminación | Media | ⏳ Pendiente |
| **Aprobación INVIAS** | Para diseños estructurales | Alta | ⏳ Pendiente |
| **Materiales Construcción** | Disponibilidad en región | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Realizar estudios geotécnicos en 43 ubicaciones
- [ ] Validar ubicaciones con estudios topográficos detallados
- [ ] Desarrollar diseño estructural tipo replicable
- [ ] Elaborar especificaciones técnicas construcción (T04)
- [ ] Coordinar con comunidades locales ubicaciones finales

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil Estructural | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil Estructural