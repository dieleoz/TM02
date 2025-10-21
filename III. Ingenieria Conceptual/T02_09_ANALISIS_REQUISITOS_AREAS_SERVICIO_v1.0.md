# T02: ANÁLISIS DE REQUISITOS - ÁREAS DE SERVICIO
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Áreas de Servicio  
**Responsable:** Ingeniero Civil - Arquitecto  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para las Áreas de Servicio del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y estándares internacionales de servicios viales.

### 1.2 Alcance
Análisis completo de requisitos para áreas de servicio distribuidas estratégicamente en el corredor de 272.1 km, incluyendo servicios básicos, comerciales y de descanso para usuarios.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **PTAR** | Planta de Tratamiento de Aguas Residuales |
| **PTAP** | Planta de Tratamiento de Agua Potable |
| **PCI** | Pavement Condition Index |
| **INVIAS** | Instituto Nacional de Vías |
| **RETIE** | Reglamento Técnico de Instalaciones Eléctricas |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Servicios Básicos Obligatorios

**ID:** RF-001  
**Descripción:** Proporcionar servicios básicos esenciales para usuarios del corredor  
**Prioridad:** Alta  
**Fuente:** AT2, Servicios mínimos  

**Criterios de Aceptación:**
- Servicios sanitarios públicos (hombres/mujeres/discapacitados)
- Suministro agua potable
- Estacionamientos vehículos livianos y pesados
- Iluminación nocturna
- Recolección y manejo residuos sólidos

### 2.2 Servicios Comerciales

**ID:** RF-002  
**Descripción:** Facilitar servicios comerciales para comodidad y necesidades de usuarios  
**Prioridad:** Media  
**Fuente:** Mejores prácticas APP  

**Criterios de Aceptación:**
- Estación de combustible
- Tienda de conveniencia
- Restaurante o cafetería
- Cajero automático
- Servicios mecánicos básicos#
## 2.3 Áreas de Descanso

**ID:** RF-003  
**Descripción:** Proporcionar espacios seguros para descanso de conductores y pasajeros  
**Prioridad:** Alta  
**Fuente:** Seguridad vial, AT2  

**Criterios de Aceptación:**
- Zonas verdes y recreativas
- Mobiliario urbano (bancas, mesas)
- Áreas techadas para protección clima
- Senderos peatonales seguros
- Señalización informativa completa

### 2.4 Infraestructura de Servicios Públicos

**ID:** RF-004  
**Descripción:** Garantizar infraestructura completa de servicios públicos  
**Prioridad:** Alta  
**Fuente:** Normativa colombiana  

**Criterios de Aceptación:**
- Sistema agua potable con PTAP si requerido
- Sistema alcantarillado con PTAR
- Suministro energía eléctrica confiable
- Sistema recolección residuos sólidos
- Comunicaciones (internet, telefonía)

### 2.5 Seguridad y Vigilancia

**ID:** RF-005  
**Descripción:** Implementar sistemas de seguridad para protección de usuarios  
**Prioridad:** Alta  
**Fuente:** AT2, Seguridad usuarios  

**Criterios de Aceptación:**
- Sistema CCTV con grabación
- Iluminación perimetral adecuada
- Comunicación directa con CCO
- Personal de seguridad 24/7
- Señalización de emergencia

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad servicios básicos | 100% | AT2 |
| **RNF-002** | Disponibilidad servicios comerciales | 95% | Operacional |
| **RNF-003** | Tiempo reparación servicios | < 4 horas | AT4 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Capacidad estacionamiento | 50 vehículos livianos | Estimación demanda |
| **RNF-005** | Capacidad estacionamiento pesados | 20 vehículos | Estimación demanda |
| **RNF-006** | Tiempo servicio sanitarios | < 5 minutos espera | Estándar servicio |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Cumplimiento NSR-10 | Construcciones sismo resistentes | Legal |
| **RNF-008** | Cumplimiento RETIE | Instalaciones eléctricas seguras | Legal |
| **RNF-009** | Sistemas contra incendios | Extintores y detección | Bomberos |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Accesibilidad universal | Rampas y facilidades discapacitados | Ley 361/1997 |
| **RNF-011** | Señalización clara | Información en español e inglés | Turismo |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Materiales durables | Vida útil mínimo 20 años | Sostenibilidad |
| **RNF-013** | Acceso mantenimiento | Facilidades para limpieza | Operacional |
| **RNF-014** | Sistemas modulares | Ampliación sin rediseño | Escalabilidad |

### 3.6 Requisitos Ambientales

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Tratamiento aguas residuales | PTAR con eficiencia >90% | Ambiental |
| **RNF-016** | Manejo residuos sólidos | Separación y reciclaje | Ambiental |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con CCO

**ID:** RI-001  
**Sistemas:** Áreas Servicio ↔ CCO  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP  
**Datos Intercambiados:** Estado servicios, emergencias, ocupación  
**Frecuencia:** Tiempo real

### 4.2 Interface con Sistema Eléctrico

**ID:** RI-002  
**Sistemas:** Áreas Servicio ↔ Suministro Eléctrico  
**Tipo:** Física/Eléctrica  
**Protocolo:** AC 220V/440V  
**Datos Intercambiados:** Energía eléctrica  
**Frecuencia:** Continua

### 4.3 Interface con Iluminación

**ID:** RI-003  
**Sistemas:** Áreas Servicio ↔ Sistema Iluminación  
**Tipo:** Física/Eléctrica  
**Protocolo:** Control automático  
**Datos Intercambiados:** Iluminación nocturna  
**Frecuencia:** Crepuscular

### 4.4 Interface con Telecomunicaciones

**ID:** RI-004  
**Sistemas:** Áreas Servicio ↔ Red Telecomunicaciones  
**Tipo:** Red de Datos  
**Protocolo:** Fibra óptica/Ethernet  
**Datos Intercambiados:** Internet, telefonía, datos  
**Frecuencia:** Continua

### 4.5 Interface con Servicios Públicos

**ID:** RI-005  
**Sistemas:** Áreas Servicio ↔ Acueducto/Alcantarillado  
**Tipo:** Física/Hidráulica  
**Protocolo:** Tuberías y conexiones  
**Datos Intercambiados:** Agua potable, aguas residuales  
**Frecuencia:** Continua

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Servicios básicos | AT2 | Infraestructura básica | Alta |
| RF-002 | Funcional | Servicios comerciales | Mejores prácticas | Edificaciones comerciales | Media |
| RF-003 | Funcional | Áreas descanso | AT2, Seguridad vial | Zonas recreativas | Alta |
| RF-004 | Funcional | Servicios públicos | Normativa | Infraestructura servicios | Alta |
| RF-005 | Funcional | Seguridad vigilancia | AT2 | Sistema seguridad | Alta |
| RNF-001 | No Funcional | Disponibilidad 100% | AT2 | Sistema completo | Alta |
| RNF-007 | No Funcional | Cumplimiento NSR-10 | Legal | Construcciones | Alta |
| RNF-015 | No Funcional | PTAR eficiencia >90% | Ambiental | Tratamiento aguas | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Cumplimiento normativa ambiental | Diseño PTAR específico | Legal |
| **REST-002** | Distancias mínimas entre áreas | Ubicaciones predefinidas | INVIAS |
| **REST-003** | Accesibilidad universal obligatoria | Diseño inclusivo | Ley 361/1997 |
| **REST-004** | Servicios 24/7 en ubicaciones críticas | Operación continua | AT2 |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Demanda servicios según estimación | Medio (sobredimensionamiento) | Estudios tráfico |
| **SUP-002** | Operadores comerciales disponibles | Alto (servicios limitados) | Estudio mercado |
| **SUP-003** | Permisos ambientales aprobados | Alto (no construcción) | Trámites ambientales |
| **SUP-004** | Servicios públicos disponibles | Alto (infraestructura adicional) | Coordinación municipal |

---

## 7. CASOS DE USO

### 7.1 Usuario Utiliza Servicios Básicos

**ID:** CU-001  
**Actor:** Usuario Vial  
**Descripción:** Usuario utiliza servicios básicos en área de servicio  
**Precondiciones:** Área operativa, servicios disponibles  
**Flujo Normal:**
1. Usuario ingresa al área de servicio
2. Estaciona vehículo en zona designada
3. Utiliza servicios sanitarios
4. Consume agua potable si necesario
5. Descansa en área recreativa
6. Sale del área de servicio

**Postcondiciones:** Usuario atendido satisfactoriamente  
**Flujos Alternativos:** Si servicios no disponibles, reporta a administración

### 7.2 Mantenimiento Preventivo Instalaciones

**ID:** CU-002  
**Actor:** Personal Mantenimiento  
**Descripción:** Realizar mantenimiento preventivo de instalaciones  
**Precondiciones:** Cronograma establecido, personal capacitado  
**Flujo Normal:**
1. Personal accede según cronograma
2. Inspecciona estado general instalaciones
3. Realiza limpieza profunda servicios sanitarios
4. Verifica funcionamiento sistemas (agua, luz)
5. Mantiene áreas verdes y mobiliario
6. Actualiza registro mantenimiento
7. Reporta novedades a administración

**Postcondiciones:** Instalaciones en óptimo estado  
**Flujos Alternativos:** Si encuentra daños, programa reparación

### 7.3 Emergencia en Área de Servicio

**ID:** CU-003  
**Actor:** Personal Seguridad  
**Descripción:** Atender emergencia en área de servicio  
**Precondiciones:** Sistema seguridad operativo  
**Flujo Normal:**
1. Sistema detecta emergencia (CCTV/alarma)
2. Personal seguridad evalúa situación
3. Contacta CCO para reportar incidente
4. Toma medidas inmediatas según protocolo
5. Coordina con autoridades si necesario
6. Documenta incidente en reporte
7. Sigue protocolo post-emergencia

**Postcondiciones:** Emergencia atendida y documentada  
**Flujos Alternativos:** Si emergencia mayor, evacúa área

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Servicios básicos operativos en todas las áreas
- [ ] Servicios comerciales funcionando según demanda
- [ ] Áreas de descanso seguras y cómodas
- [ ] Infraestructura servicios públicos completa
- [ ] Sistema seguridad y vigilancia operativo

### 8.2 Criterios de Performance

- [ ] Disponibilidad servicios básicos 100%
- [ ] Capacidad estacionamiento según diseño
- [ ] Tiempo espera servicios < 5 minutos
- [ ] PTAR con eficiencia >90%

### 8.3 Criterios de Calidad

- [ ] Cumplimiento NSR-10 para construcciones
- [ ] Cumplimiento RETIE para instalaciones eléctricas
- [ ] Accesibilidad universal implementada
- [ ] Certificaciones ambientales obtenidas

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Permisos Ambientales** | Requeridos para construcción | Alta | ⏳ Pendiente |
| **Servicios Públicos Municipales** | Conexión agua/alcantarillado | Alta | ⏳ Pendiente |
| **Suministro Eléctrico** | Para operación servicios | Alta | ⏳ Pendiente |
| **Operadores Comerciales** | Para servicios comerciales | Media | ⏳ Pendiente |
| **Personal Operativo** | Para mantenimiento y seguridad | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Realizar estudios de demanda detallados
- [ ] Validar ubicaciones con estudios ambientales
- [ ] Diseñar PTAR según normativa ambiental
- [ ] Elaborar especificaciones técnicas construcción (T04)
- [ ] Iniciar trámites permisos ambientales

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil - Arquitecto | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil - Arquitecto