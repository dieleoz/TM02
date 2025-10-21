# T01: FICHA DE SISTEMA - CENTRO DE CONTROL DE OPERACIÓN (CCO)
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Centro de Control de Operación (CCO)  
**Responsable:** Ingeniero de Sistemas  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Centro de Control de Operación (CCO) |
| **Categoría** | Control y Supervisión |
| **Prioridad** | Crítica |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT1 (Iluminación), AT2 (Sección 3.1.7, 3.3.3.3) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Centro neurálgico de control y supervisión de todos los sistemas del proyecto, que permite la operación centralizada, monitoreo en tiempo real y coordinación de respuesta a incidentes en los 272.1 km del corredor vial.

### 2.2 Alcance del Sistema
- **Sistemas supervisados:**
  - Estaciones de Peaje (3)
  - Bases de Operación (2)
  - Paneles LED (25)
  - Sistemas de emergencia
  - Telecomunicaciones
  - Información a usuarios
  
- **Cobertura geográfica:** Todo el corredor del proyecto
- **Integración con:** Todos los sistemas del proyecto

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Obligaciones del Contrato
**Según AT2, Sección 3.1.7 - Disponibilidad de la Información:**
"El Concesionario deberá contar con una plataforma tecnológica (hardware, software, sistemas de información, aplicaciones y portales web, interfases, redes locales de datos y voz, redes de telecomunicación, y en general todos los elementos constitutivos de teleinformática) la cual estará permanentemente disponible, usable y accesible"

### 3.2 Requisitos de Apéndices Técnicos
**Según AT2, Sección 3.1.7:**
"Esta información deberá estar siempre disponible para el Interventor, la ANI, la Policía de Carreteras, los Usuarios y la comunidad en general, según el caso"

**Según AT2, Sección 3.3.3.3:**
"Los libros de registro deberán estar disponibles permanentemente en el Centro de Control de Operación"

### 3.3 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **ISO 27001** | Seguridad de la información | Protección datos |
| **ISO 9001:2015** | Sistema de Gestión de Calidad | Procesos operacionales |
| **RETIE** | Instalaciones eléctricas | Infraestructura eléctrica |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Sala de Control Principal** | 1 unidad | Por definir ubicación | Supervisión 24/7/365 |
| **Videowall** | 1 sistema | Sala control | Visualización múltiple |
| **Puestos de operador** | 4-6 puestos | Sala control | Operación sistemas |
| **Servidores SCADA** | 2 servidores | Sala técnica | Control supervisorio |
| **Servidores base datos** | 2 servidores | Sala técnica | Almacenamiento información |
| **Sistemas comunicación** | 1 sistema | Sala técnica | Radio, telefonía, datos |
| **UPS y respaldo** | 1 sistema | Sala técnica | Continuidad operacional |
| **Sistema CCTV local** | 1 sistema | Perímetro CCO | Seguridad instalaciones |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| Estaciones de Peaje | Red IP | Ethernet/Fibra | Recaudación, alarmas, video |
| Bases de Operación | Red IP/Radio | Ethernet/VHF | Coordinación emergencias |
| Paneles LED | Red IP | Ethernet/Fibra | Mensajes dinámicos |
| Sistema Info Usuarios | Red IP | TCP/IP | Estado vía, incidentes |
| Telecomunicaciones | Red backbone | Fibra óptica | Todas las comunicaciones |
| ANI/Interventoría | VPN/Web | Internet | Reportes, indicadores |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Construcción CCO** | 1 edificio | $800,000 | $800,000 |
| **Videowall 4K** | 1 sistema | $150,000 | $150,000 |
| **Puestos operador** | 6 puestos | $25,000 | $150,000 |
| **Servidores SCADA** | 2 servidores | $80,000 | $160,000 |
| **Servidores BD** | 2 servidores | $60,000 | $120,000 |
| **Sistema comunicaciones** | 1 sistema | $200,000 | $200,000 |
| **UPS y respaldo** | 1 sistema | $100,000 | $100,000 |
| **CCTV local** | 1 sistema | $50,000 | $50,000 |
| **Software SCADA** | 1 licencia | $300,000 | $300,000 |
| **Integración sistemas** | 1 proyecto | $200,000 | $200,000 |
| **TOTAL CAPEX** | | | **$2,230,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal operación 24/7 (12 operadores) | $360,000 |
| Mantenimiento preventivo | $150,000 |
| Licencias software | $80,000 |
| Energía eléctrica | $48,000 |
| Comunicaciones | $60,000 |
| Seguros | $24,000 |
| **TOTAL OPEX/año** | **$722,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Falla sistema SCADA | Baja | Alto | Redundancia servidores + respaldo |
| Corte energía eléctrica | Media | Alto | UPS + generador emergencia |
| Ciberataques | Media | Alto | Firewall + seguridad multicapa |
| Falta personal calificado | Media | Medio | Plan capacitación + contratos |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT4:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **CCO01** | Disponibilidad sistema CCO | 99.5% mensual | Continua |
| **CCO02** | Tiempo respuesta alarmas | < 30 segundos | Por evento |
| **CCO03** | Disponibilidad comunicaciones | 99% mensual | Continua |
| **CCO04** | Tiempo resolución incidentes | < 15 minutos | Por evento |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Definir arquitectura conceptual (Template T03)
- [ ] Elaborar especificaciones técnicas (Template T04)
- [ ] Seleccionar ubicación óptima CCO
- [ ] Cotizar sistemas SCADA especializados
- [ ] Validar con ANI requisitos interoperabilidad

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Ubicación CCO en punto geográfico central del proyecto
- Disponibilidad fibra óptica para todas las conexiones
- Personal operativo con experiencia en sistemas viales
- Integración con sistemas ANI existentes

### 10.2 Dependencias
- Definición ubicación antes de iniciar construcción
- Disponibilidad red de telecomunicaciones
- Capacitación personal antes de puesta en operación
- Aprobación ANI para interfaces sistemas

### 10.3 Restricciones
- Operación 24/7/365 sin interrupciones
- Cumplimiento normativa seguridad información
- Acceso permanente para Interventoría y ANI
- Respaldo información mínimo 5 años

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Sistemas