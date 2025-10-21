# T02: ANÁLISIS DE REQUISITOS - PANELES LED
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Paneles LED (Paneles de Mensaje Variable - PMV)  
**Responsable:** Ingeniero de Sistemas ITS  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Este documento define los requisitos funcionales y no funcionales para el sistema de Paneles LED (PMV) del proyecto APP Sabana de Torres - Curumaní, basado en las obligaciones contractuales y mejores prácticas de la industria ITS.

### 1.2 Alcance
Análisis completo de requisitos para 31 paneles LED distribuidos en 272.1 km del corredor, incluyendo integración con CCO, comunicaciones, energía y software de gestión.

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|:--------|:-----------|
| **PMV** | Panel de Mensaje Variable |
| **CCO** | Centro de Control de Operación |
| **NTCIP** | National Transportation Communications for ITS Protocol |
| **LED** | Light Emitting Diode |
| **MTBF** | Mean Time Between Failures |
| **MTTR** | Mean Time To Repair |
| **UPS** | Uninterruptible Power Supply |

---

## 2. REQUISITOS FUNCIONALES

### 2.1 Visualización de Mensajes Dinámicos

**ID:** RF-001  
**Descripción:** El sistema debe mostrar mensajes variables en tiempo real para informar a usuarios sobre condiciones de tráfico, incidentes, trabajos viales y condiciones meteorológicas  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.2.4  

**Criterios de Aceptación:**
- Capacidad de mostrar texto alfanumérico y símbolos gráficos
- Soporte para múltiples idiomas (español, inglés)
- Actualización de mensajes en tiempo real desde CCO
- Visibilidad mínima 200m en condiciones normales

### 2.2 Control Centralizado desde CCO

**ID:** RF-002  
**Descripción:** Todos los paneles deben ser controlados centralizadamente desde el CCO con capacidad de gestión individual y grupal  
**Prioridad:** Alta  
**Fuente:** AT2, Sección 3.3.3.2.4  

**Criterios de Aceptación:**
- Interface gráfica para operadores en CCO
- Control individual de cada panel
- Control grupal por zonas o sectores
- Programación de mensajes automáticos

### 2.3 Gestión de Biblioteca de Mensajes

**ID:** RF-003  
**Descripción:** El sistema debe mantener una biblioteca de mensajes predefinidos y permitir creación de mensajes personalizados  
**Prioridad:** Media  
**Fuente:** Mejores prácticas ITS  

**Criterios de Aceptación:**
- Mínimo 100 mensajes predefinidos
- Creación de mensajes personalizados
- Validación de sintaxis y legibilidad
- Historial de mensajes utilizados

### 2.4 Monitoreo de Estado y Diagnóstico

**ID:** RF-004  
**Descripción:** El sistema debe reportar continuamente el estado operacional de cada panel y generar alarmas por fallas  
**Prioridad:** Alta  
**Fuente:** AT4, Indicadores de Desempeño  

**Criterios de Aceptación:**
- Monitoreo en tiempo real de estado operacional
- Detección automática de fallas de LEDs
- Alarmas por pérdida de comunicación
- Reportes de disponibilidad automáticos

### 2.5 Integración con Sistemas Externos

**ID:** RF-005  
**Descripción:** Los paneles deben integrarse con otros sistemas ITS para mostrar información coordinada  
**Prioridad:** Media  
**Fuente:** AT2, Integración de Sistemas  

**Criterios de Aceptación:**
- Recepción de datos de estaciones de peaje
- Integración con sistema de información a usuarios
- Coordinación con bases de operación
- Sincronización con emisora de radio

---

## 3. REQUISITOS NO FUNCIONALES

### 3.1 Requisitos de Disponibilidad

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-001** | Disponibilidad del sistema | 95% mensual | AT4, PMV01 |
| **RNF-002** | MTBF (Tiempo Medio Entre Fallas) | 8,760 horas | Estándar ITS |
| **RNF-003** | MTTR (Tiempo Medio de Reparación) | 4 horas | AT2 |

### 3.2 Requisitos de Performance

| ID | Requisito | Valor Mínimo | Fuente |
|:---|:----------|:-------------|:-------|
| **RNF-004** | Tiempo actualización mensaje | < 2 minutos | AT4, PMV02 |
| **RNF-005** | Tiempo respuesta sistema | < 30 segundos | AT4, PMV04 |
| **RNF-006** | Frecuencia de refresco LED | 60 Hz mínimo | IEC 62471 |

### 3.3 Requisitos de Seguridad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-007** | Autenticación operadores | Control acceso con roles definidos | AT2 |
| **RNF-008** | Cifrado comunicaciones | TLS 1.2 mínimo para datos | AT2 |
| **RNF-009** | Backup configuraciones | Diario, retención 30 días | Mejores prácticas |

### 3.4 Requisitos de Usabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-010** | Interface operador | Intuitiva, capacitación < 4 horas | AT2 |
| **RNF-011** | Legibilidad diurna/nocturna | 100% en condiciones normales | AT4, PMV03 |

### 3.5 Requisitos de Mantenibilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-012** | Actualización firmware | Remota, sin interrupción servicio | AT2 |
| **RNF-013** | Diagnóstico remoto | Monitoreo SNMP v3 | NTCIP 1201 |
| **RNF-014** | Repuestos LEDs | Disponibilidad durante concesión | AT2 |

### 3.6 Requisitos de Escalabilidad

| ID | Requisito | Descripción | Fuente |
|:---|:----------|:------------|:-------|
| **RNF-015** | Capacidad crecimiento | +20 paneles sin cambios mayores | Buenas prácticas |
| **RNF-016** | Arquitectura modular | Componentes intercambiables | Buenas prácticas |

---

## 4. REQUISITOS DE INTERFACES

### 4.1 Interface con CCO

**ID:** RI-001  
**Sistemas:** Paneles LED ↔ CCO  
**Tipo:** Red de Datos  
**Protocolo:** NTCIP 1203 sobre TCP/IP  
**Datos Intercambiados:** Mensajes, estado paneles, alarmas, configuraciones  
**Frecuencia:** Tiempo real para mensajes, cada 30 segundos para estado

### 4.2 Interface con Sistema de Telecomunicaciones

**ID:** RI-002  
**Sistemas:** Paneles LED ↔ Red Fibra Óptica  
**Tipo:** Física  
**Protocolo:** Ethernet 100/1000 Mbps  
**Datos Intercambiados:** Todos los datos del sistema  
**Frecuencia:** Continua

### 4.3 Interface con Estaciones de Peaje

**ID:** RI-003  
**Sistemas:** Paneles LED ↔ Estaciones Peaje  
**Tipo:** Red de Datos  
**Protocolo:** API REST sobre HTTPS  
**Datos Intercambiados:** Estado peajes, tarifas, colas  
**Frecuencia:** Cada 5 minutos o por evento

### 4.4 Interface con Bases de Operación

**ID:** RI-004  
**Sistemas:** Paneles LED ↔ Bases Operación  
**Tipo:** Red de Datos  
**Protocolo:** TCP/IP  
**Datos Intercambiados:** Información incidentes, trabajos viales  
**Frecuencia:** Por evento

### 4.5 Interface con Sistema Energía

**ID:** RI-005  
**Sistemas:** Paneles LED ↔ Sistema Eléctrico  
**Tipo:** Física  
**Protocolo:** 220V AC, UPS local  
**Datos Intercambiados:** Alimentación eléctrica, estado UPS  
**Frecuencia:** Continua

---

## 5. MATRIZ DE TRAZABILIDAD

| Requisito ID | Tipo | Descripción | Fuente Contractual | Componente Afectado | Prioridad |
|:-------------|:-----|:------------|:-------------------|:--------------------|:----------|
| RF-001 | Funcional | Visualización mensajes dinámicos | AT2, 3.3.3.2.4 | Paneles LED | Alta |
| RF-002 | Funcional | Control centralizado CCO | AT2, 3.3.3.2.4 | Software gestión | Alta |
| RF-003 | Funcional | Biblioteca mensajes | Mejores prácticas | Software gestión | Media |
| RF-004 | Funcional | Monitoreo y diagnóstico | AT4 | Controladores | Alta |
| RF-005 | Funcional | Integración sistemas | AT2 | Interfaces | Media |
| RNF-001 | No Funcional | Disponibilidad 95% | AT4, PMV01 | Sistema completo | Alta |
| RNF-004 | No Funcional | Tiempo actualización < 2 min | AT4, PMV02 | Comunicaciones | Alta |
| RNF-011 | No Funcional | Legibilidad 100% | AT4, PMV03 | Paneles LED | Alta |

---

## 6. RESTRICCIONES Y SUPUESTOS

### 6.1 Restricciones

| ID | Restricción | Impacto | Origen |
|:---|:------------|:--------|:-------|
| **REST-001** | Separación máxima 20 km entre paneles | Ubicaciones fijas predefinidas | AT1, Contractual |
| **REST-002** | Instalación alternada bermas externas | Diseño estructural específico | AT1, Contractual |
| **REST-003** | Cumplimiento Manual Señalización 2015 | Especificaciones técnicas | Legal |
| **REST-004** | Operación 24/7/365 | Redundancia y mantenibilidad | AT2, Contractual |

### 6.2 Supuestos

| ID | Supuesto | Riesgo si no se cumple | Validación |
|:---|:---------|:-----------------------|:-----------|
| **SUP-001** | Fibra óptica disponible en todas las ubicaciones | Alto (falta comunicaciones) | Validar en diseño detallado |
| **SUP-002** | Suministro eléctrico estable en cada punto | Medio (requiere UPS mayor) | Estudio eléctrico |
| **SUP-003** | Permisos instalación aprobados | Alto (retrasos proyecto) | Gestión con autoridades |
| **SUP-004** | Tecnología LED estable 10 años | Medio (costos mantenimiento) | Selección fabricante |

---

## 7. CASOS DE USO

### 7.1 Mostrar Mensaje de Incidente

**ID:** CU-001  
**Actor:** Operador CCO  
**Descripción:** Operador debe mostrar mensaje de incidente en paneles específicos  
**Precondiciones:** Sistema operativo, comunicaciones activas  
**Flujo Normal:**
1. Operador recibe reporte de incidente
2. Selecciona paneles afectados en mapa
3. Elige mensaje predefinido o crea personalizado
4. Confirma y envía mensaje
5. Sistema actualiza paneles en < 2 minutos
6. Sistema confirma actualización exitosa

**Postcondiciones:** Mensaje visible en paneles seleccionados  
**Flujos Alternativos:** Si falla comunicación, alarma y reintento automático

### 7.2 Monitoreo Automático de Estado

**ID:** CU-002  
**Actor:** Sistema Automático  
**Descripción:** Sistema monitorea continuamente estado de paneles  
**Precondiciones:** Paneles instalados y configurados  
**Flujo Normal:**
1. Sistema consulta estado cada 30 segundos
2. Recibe respuesta de controladores locales
3. Actualiza base de datos de estado
4. Si detecta falla, genera alarma
5. Notifica a operadores por múltiples medios

**Postcondiciones:** Estado actualizado en CCO  
**Flujos Alternativos:** Si no hay respuesta, marca como "Sin comunicación"

### 7.3 Programación de Mensajes Automáticos

**ID:** CU-003  
**Actor:** Supervisor de Operaciones  
**Descripción:** Programar mensajes automáticos por horarios o eventos  
**Precondiciones:** Permisos de supervisor, sistema operativo  
**Flujo Normal:**
1. Supervisor accede a módulo programación
2. Define condiciones de activación (horario/evento)
3. Selecciona paneles y mensaje
4. Configura duración y repetición
5. Sistema valida y guarda programación
6. Ejecuta automáticamente según condiciones

**Postcondiciones:** Programación activa en sistema  
**Flujos Alternativos:** Si conflicto con mensaje manual, prioriza manual

---

## 8. CRITERIOS DE ACEPTACIÓN

### 8.1 Criterios Funcionales

- [ ] Todos los paneles muestran mensajes correctamente desde CCO
- [ ] Tiempo de actualización de mensajes < 2 minutos
- [ ] Biblioteca con mínimo 100 mensajes predefinidos
- [ ] Monitoreo en tiempo real de estado de todos los paneles
- [ ] Integración exitosa con estaciones de peaje y bases de operación

### 8.2 Criterios de Performance

- [ ] Disponibilidad ≥ 95% mensual por panel
- [ ] Tiempo de respuesta sistema < 30 segundos
- [ ] Legibilidad 100% diurna y nocturna
- [ ] MTBF ≥ 8,760 horas por panel

### 8.3 Criterios de Calidad

- [ ] Cumplir Manual de Señalización Vial 2015
- [ ] Certificación IEC 62471 (seguridad fotobiológica)
- [ ] Protocolo NTCIP 1203 implementado
- [ ] Pruebas de visibilidad en condiciones adversas

---

## 9. DEPENDENCIAS

| Sistema/Recurso | Tipo de Dependencia | Criticidad | Estado |
|:----------------|:--------------------|:-----------|:-------|
| **Red Fibra Óptica** | Debe estar instalada antes | Alta | ⏳ Pendiente |
| **CCO Operativo** | Debe estar funcionando | Alta | ⏳ Pendiente |
| **Suministro Eléctrico** | Requerido para operación | Alta | ⏳ Pendiente |
| **Permisos Instalación** | Necesarios para construcción | Alta | ⏳ Pendiente |
| **Estaciones de Peaje** | Para integración completa | Media | ⏳ Pendiente |

---

## 10. PRÓXIMOS PASOS

- [ ] Desarrollar arquitectura conceptual (T03)
- [ ] Definir ubicaciones específicas con estudios de visibilidad
- [ ] Validar requisitos con operadores de CCO
- [ ] Solicitar aclaraciones sobre mensajes en idiomas indígenas
- [ ] Elaborar especificaciones técnicas detalladas (T04)
- [ ] Cotizar con fabricantes certificados NTCIP

---

## 11. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Sistemas ITS | Análisis inicial de requisitos |

---

**Versión:** 1.0  
**Estado:** ✅ Análisis de Requisitos Completado  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas ITS