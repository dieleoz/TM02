# T02: ANÁLISIS DE REQUISITOS - ILUMINACIÓN
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Iluminación  
**Responsable:** Ingeniero Eléctrico  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para el sistema de Iluminación del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y normativa técnica eléctrica colombiana.

### 1.2 Alcance
Análisis completo de requisitos para iluminación en ubicaciones críticas del corredor de 272.1 km, incluyendo estaciones de peaje, puentes peatonales, intersecciones y áreas de servicio.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **RETIE** | Reglamento Técnico de Instalaciones Eléctricas |
| **CIE** | Commission Internationale de l'Éclairage |
| **IESNA** | Illuminating Engineering Society of North America |
| **DALI** | Digital Addressable Lighting Interface |
| **LED** | Light Emitting Diode |
| **Lux** | Unidad de iluminancia |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Iluminación de Estaciones de Peaje

**ID:** RF-001  
**Descripción:** Proporcionar iluminación adecuada para operación 24/7 de las 3 estaciones de peaje  
**Prioridad:** Alta  
**Fuente:** AT1, Tablas UF - Iluminación  

**Criterios de Aceptación:**
- Nivel iluminación mínimo 50 lux en casetas
- Nivel iluminación mínimo 30 lux en aproximaciones
- Uniformidad iluminación ≥ 0.4
- Encendido automático crepuscular
- Operación continua 24/7/365

### 2.2 Iluminación de Puentes Peatonales

**ID:** RF-002  
**Descripción:** Garantizar iluminación segura en los 43 puentes peatonales para uso nocturno  
**Prioridad:** Alta  
**Fuente:** AT1, Tablas UF - Iluminación  

**Criterios de Aceptación:**
- Nivel iluminación mínimo 20 lux promedio
- Uniformidad iluminación ≥ 0.4
- Iluminación en rampas de acceso
- Control automático por fotoceldas
- Protección IP65 para intemperie
### 2.3 Il
uminación de Intersecciones

**ID:** RF-003  
**Descripción:** Iluminar las 3 intersecciones a desnivel para garantizar seguridad vial nocturna  
**Prioridad:** Alta  
**Fuente:** AT1, Tablas UF - Iluminación  

**Criterios de Aceptación:**
- Nivel iluminación según CIE 115 para intersecciones
- Iluminación en rampas de acceso y salida
- Uniformidad longitudinal ≥ 0.4
- Control automático crepuscular
- Integración con señalización vial

### 2.4 Iluminación de Áreas de Servicio

**ID:** RF-004  
**Descripción:** Proporcionar iluminación para servicios nocturnos en áreas de descanso  
**Prioridad:** Media  
**Fuente:** AT1, Tablas UF - Iluminación  

**Criterios de Aceptación:**
- Nivel iluminación mínimo 15 lux en estacionamientos
- Nivel iluminación mínimo 30 lux en edificaciones
- Iluminación perimetral de seguridad
- Control por zonas independientes
- Temporizadores para ahorro energético

### 2.5 Control y Monitoreo Centralizado

**ID:** RF-005  
**Descripción:** Sistema debe permitir control y monitoreo desde CCO de toda la iluminación  
**Prioridad:** Media  
**Fuente:** Mejores prácticas ITS  

**Criterios de Aceptación:**
- Interface gráfica en CCO
- Control individual y grupal de luminarias
- Monitoreo estado en tiempo real
- Programación horarios automáticos
- Reportes de consumo energético

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad sistema | 95% mensual | AT4, IL01 |
| **RNF-002** | MTBF luminarias LED | 50,000 horas | Fabricante |
| **RNF-003** | Tiempo reparación fallas | < 24 horas | AT4, IL03 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Nivel iluminación peajes | 50 lux | CIE 115 |
| **RNF-005** | Nivel iluminación puentes | 20 lux | CIE 115 |
| **RNF-006** | Uniformidad iluminación | > 0.4 | AT4, IL04 |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Cumplimiento RETIE | Instalaciones según reglamento | Legal |
| **RNF-008** | Protección IP luminarias | IP65 mínimo intemperie | RETIE |
| **RNF-009** | Puesta a tierra | Sistema completo aterrizado | NTC 900 |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Control automático | Encendido/apagado crepuscular | CIE 115 |
| **RNF-011** | Interface operador | Intuitiva desde CCO | Buenas prácticas |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Acceso mantenimiento | Facilidades para limpieza | IESNA |
| **RNF-013** | Luminarias intercambiables | Componentes estandarizados | Buenas prácticas |
| **RNF-014** | Diagnóstico remoto | Detección fallas automática | Mejores prácticas |

### 3.6 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Capacidad expansión | +20% luminarias sin cambios | Buenas prácticas |
| **RNF-016** | Protocolo estándar | DALI para control | Estándar industria |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con Sistema Eléctrico

**ID:** RI-001  
**Sistemas:** Iluminación ↔ Suministro Eléctrico  
**Tipo:** Física/Eléctrica  
**Protocolo:** AC 220V/440V  
**Datos Intercambiados:** Energía eléctrica  
**Frecuencia:** Continua

### 4.2 Interface con CCO

**ID:** RI-002  
**Sistemas:** Iluminación ↔ CCO  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP + DALI  
**Datos Intercambiados:** Estado, control, alarmas, consumo  
**Frecuencia:** Tiempo real

### 4.3 Interface con Puentes Peatonales

**ID:** RI-003  
**Sistemas:** Iluminación ↔ Puentes Peatonales  
**Tipo:** Física/Estructural  
**Protocolo:** Integración mecánica  
**Datos Intercambiados:** Soporte físico luminarias  
**Frecuencia:** Permanente

### 4.4 Interface con Estaciones de Peaje

**ID:** RI-004  
**Sistemas:** Iluminación ↔ Estaciones Peaje  
**Tipo:** Física/Eléctrica  
**Protocolo:** Cableado eléctrico  
**Datos Intercambiados:** Iluminación operacional  
**Frecuencia:** Continua

### 4.5 Interface con Sensores Crepusculares

**ID:** RI-005  
**Sistemas:** Iluminación ↔ Fotoceldas  
**Tipo:** Física/Analógica  
**Protocolo:** Señal 0-10V  
**Datos Intercambiados:** Nivel luminosidad ambiente  
**Frecuencia:** Continua

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Iluminación peajes | AT1, Tablas UF | Luminarias peajes | Alta |
| RF-002 | Funcional | Iluminación puentes | AT1, Tablas UF | Luminarias puentes | Alta |
| RF-003 | Funcional | Iluminación intersecciones | AT1, Tablas UF | Luminarias viales | Alta |
| RF-004 | Funcional | Iluminación áreas servicio | AT1, Tablas UF | Luminarias áreas | Media |
| RF-005 | Funcional | Control centralizado | Mejores prácticas | Sistema control | Media |
| RNF-001 | No Funcional | Disponibilidad 95% | AT4, IL01 | Sistema completo | Alta |
| RNF-004 | No Funcional | Nivel 50 lux peajes | CIE 115 | Luminarias peajes | Alta |
| RNF-007 | No Funcional | Cumplimiento RETIE | Legal | Instalaciones | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Cumplimiento RETIE obligatorio | Diseño instalaciones específico | Legal |
| **REST-002** | Niveles mínimos CIE 115 | Cantidad y potencia luminarias | Normativo |
| **REST-003** | Operación automática crepuscular | Sistemas control requeridos | AT1 |
| **REST-004** | Protección IP65 intemperie | Selección luminarias específicas | RETIE |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Suministro eléctrico estable disponible | Alto (sistema no funciona) | Coordinación eléctrica |
| **SUP-002** | Luminarias LED calidad certificada | Medio (fallas prematuras) | Selección fabricantes |
| **SUP-003** | Acceso para mantenimiento garantizado | Medio (costos adicionales) | Diseño instalaciones |
| **SUP-004** | Personal técnico especializado | Medio (mantenimiento deficiente) | Plan capacitación |

---

## 7. CASOS DE USO

### 7.1 Encendido Automático Nocturno

**ID:** CU-001  
**Actor:** Sistema Automático  
**Descripción:** Sistema enciende iluminación automáticamente al anochecer  
**Precondiciones:** Fotoceldas operativas, sistema energizado  
**Flujo Normal:**
1. Fotocelda detecta nivel luz < 10 lux
2. Envía señal a controlador local
3. Controlador activa luminarias de la zona
4. Sistema reporta estado a CCO
5. Iluminación permanece encendida
6. Al amanecer (>20 lux) se apaga automáticamente

**Postcondiciones:** Iluminación nocturna operativa  
**Flujos Alternativos:** Si falla fotocelda, control manual desde CCO

### 7.2 Mantenimiento Preventivo Luminarias

**ID:** CU-002  
**Actor:** Técnico Eléctrico  
**Descripción:** Realizar mantenimiento preventivo de luminarias LED  
**Precondiciones:** Cronograma mantenimiento, equipos disponibles  
**Flujo Normal:**
1. Técnico accede a ubicación según cronograma
2. Desconecta luminaria del sistema
3. Limpia ópticas y disipadores térmicos
4. Verifica conexiones eléctricas
5. Mide niveles de iluminación
6. Actualiza registro de mantenimiento
7. Reconecta y verifica funcionamiento

**Postcondiciones:** Luminaria operativa con mantenimiento actualizado  
**Flujos Alternativos:** Si detecta falla, programa reemplazo

### 7.3 Control Manual desde CCO

**ID:** CU-003  
**Actor:** Operador CCO  
**Descripción:** Controlar iluminación manualmente desde centro de control  
**Precondiciones:** Sistema control operativo, operador autorizado  
**Flujo Normal:**
1. Operador accede a interface iluminación
2. Selecciona zona o luminarias específicas
3. Ejecuta comando encender/apagar
4. Sistema confirma ejecución
5. Actualiza estado en pantalla
6. Registra acción en bitácora

**Postcondiciones:** Iluminación controlada según requerimiento  
**Flujos Alternativos:** Si falla comunicación, alarma y reintento

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Iluminación operativa en todas las ubicaciones contractuales
- [ ] Niveles de iluminación según CIE 115 verificados
- [ ] Control automático crepuscular funcionando
- [ ] Interface de control en CCO operativa
- [ ] Monitoreo en tiempo real implementado

### 8.2 Criterios de Performance

- [ ] Disponibilidad ≥ 95% mensual
- [ ] Uniformidad iluminación ≥ 0.4
- [ ] Tiempo reparación fallas < 24 horas
- [ ] MTBF luminarias ≥ 50,000 horas

### 8.3 Criterios de Calidad

- [ ] Cumplimiento RETIE para instalaciones eléctricas
- [ ] Luminarias con certificación IESNA
- [ ] Protección IP65 verificada
- [ ] Sistema puesta a tierra completo

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Suministro Eléctrico** | Debe estar disponible antes | Alta | ⏳ Pendiente |
| **Puentes Peatonales** | Para integración luminarias | Alta | ⏳ Pendiente |
| **CCO Operativo** | Para sistema control | Media | ⏳ Pendiente |
| **Estaciones de Peaje** | Para iluminación operacional | Alta | ⏳ Pendiente |
| **Personal Técnico** | Para mantenimiento | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Realizar estudios fotométricos detallados
- [ ] Validar niveles iluminación con normativa CIE 115
- [ ] Seleccionar fabricantes luminarias certificadas
- [ ] Elaborar especificaciones técnicas instalaciones (T04)
- [ ] Diseñar sistema control DALI integrado

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Eléctrico | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Eléctrico