# T01: FICHA DE SISTEMA - TELECOMUNICACIONES
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Telecomunicaciones  
**Responsable:** Ingeniero de Telecomunicaciones  
**Versión:** 1.0  

---

## 1. IDENTIFICACIÓN DEL SISTEMA

| Campo | Valor |
|-------|-------|
| **Nombre del sistema** | Telecomunicaciones |
| **Categoría** | Infraestructura de Comunicaciones |
| **Prioridad** | Crítica |
| **Fase contractual** | Construcción / O&M |
| **AT relacionados** | AT2 (Sección 3.1.7 - Plataforma Tecnológica) |

---

## 2. DESCRIPCIÓN GENERAL

### 2.1 Propósito del Sistema
Sistema backbone de comunicaciones que interconecta todos los sistemas del proyecto, proporcionando la infraestructura de red necesaria para la operación centralizada, monitoreo remoto y comunicaciones de voz y datos en tiempo real.

### 2.2 Alcance del Sistema
- **Componentes incluidos:**
  - Red de fibra óptica backbone
  - Sistemas de radio comunicaciones
  - Red de datos IP
  - Telefonía corporativa
  - Enlaces de respaldo
  
- **Cobertura geográfica:** 272.1 km del corredor completo
- **Integración con:** Todos los sistemas del proyecto

---

## 3. REQUISITOS CONTRACTUALES

### 3.1 Plataforma Tecnológica Obligatoria
**Según AT2, Sección 3.1.7:**
"El Concesionario deberá contar con una plataforma tecnológica (hardware, software, sistemas de información, aplicaciones y portales web, interfases, redes locales de datos y voz, redes de telecomunicación, y en general todos los elementos constitutivos de teleinformática)"

### 3.2 Disponibilidad Permanente
**Según AT2, Sección 3.1.7:**
"la cual estará permanentemente disponible, usable y accesible"

### 3.3 Acceso Múltiple
**Según AT2, Sección 3.1.7:**
"Esta información deberá estar siempre disponible para el Interventor, la ANI, la Policía de Carreteras, los Usuarios y la comunidad en general"

### 3.4 Normativa Aplicable

| Norma | Descripción | Alcance |
|:------|:------------|:--------|
| **MinTIC** | Regulación telecomunicaciones | Licencias y permisos |
| **UIT-T** | Estándares internacionales | Protocolos comunicación |
| **IEEE 802.11** | Redes inalámbricas | WiFi y enlaces |
| **TIA/EIA** | Cableado estructurado | Instalaciones |

---

## 4. COMPONENTES PRINCIPALES

| Componente | Cantidad | Ubicación | Función |
|:-----------|:---------|:----------|:--------|
| **Fibra óptica backbone** | 300 km | Todo el corredor | Red principal datos |
| **Nodos principales** | 5 nodos | CCO, peajes, bases | Concentración tráfico |
| **Repetidoras fibra** | 15 unidades | Cada 20 km | Amplificación señal |
| **Sistema radio VHF** | 1 red | Cobertura total | Comunicaciones voz |
| **Repetidoras radio** | 8 unidades | Puntos altos | Cobertura radio |
| **Central telefónica IP** | 1 sistema | CCO | Telefonía corporativa |
| **Enlaces microondas** | 3 enlaces | Respaldo crítico | Redundancia |
| **Equipos networking** | 50 equipos | Distribuidos | Conmutación datos |

---

## 5. INTERFACES CON OTROS SISTEMAS

| Sistema Relacionado | Tipo de Interface | Protocolo/Medio | Datos Intercambiados |
|:--------------------|:------------------|:----------------|:---------------------|
| CCO | Fibra óptica | Ethernet Gigabit | Todos los datos sistemas |
| Estaciones Peaje | Fibra óptica | TCP/IP | Recaudación, video, alarmas |
| Paneles LED | Fibra óptica | TCP/IP | Mensajes dinámicos |
| Bases Operación | Radio/Fibra | VHF/Ethernet | Coordinación emergencias |
| Ambulancias TAM | Radio | VHF/UHF | Comunicaciones médicas |
| Sistema Web | Internet | HTTPS/VPN | Acceso remoto |

---

## 6. ESTIMACIÓN PRELIMINAR

### 6.1 CAPEX (Inversión Inicial)

| Ítem | Cantidad | Costo Unitario (USD) | Costo Total (USD) |
|:-----|:---------|:---------------------|:------------------|
| **Fibra óptica 48 hilos** | 300 km | $8,000 | $2,400,000 |
| **Instalación fibra óptica** | 300 km | $3,000 | $900,000 |
| **Nodos principales** | 5 nodos | $150,000 | $750,000 |
| **Repetidoras fibra** | 15 unidades | $25,000 | $375,000 |
| **Sistema radio VHF** | 1 red | $200,000 | $200,000 |
| **Repetidoras radio** | 8 unidades | $40,000 | $320,000 |
| **Central telefónica IP** | 1 sistema | $80,000 | $80,000 |
| **Enlaces microondas** | 3 enlaces | $60,000 | $180,000 |
| **Equipos networking** | 50 equipos | $8,000 | $400,000 |
| **Instalación y configuración** | 1 proyecto | $395,000 | $395,000 |
| **TOTAL CAPEX** | | | **$6,000,000** |

### 6.2 OPEX (Operación y Mantenimiento - Anual)

| Ítem | Costo Anual (USD) |
|:-----|:------------------|
| Personal técnico especializado | $180,000 |
| Mantenimiento preventivo | $240,000 |
| Licencias software | $60,000 |
| Enlaces internet | $48,000 |
| Energía equipos | $120,000 |
| Repuestos y consumibles | $90,000 |
| **TOTAL OPEX/año** | **$738,000** |

---

## 7. RIESGOS IDENTIFICADOS

| Riesgo | Probabilidad | Impacto | Mitigación |
|:-------|:-------------|:--------|:-----------|
| Corte fibra óptica | Media | Alto | Rutas redundantes + respaldo microondas |
| Falla equipos críticos | Media | Alto | Equipos redundantes + contratos soporte |
| Interferencias radio | Media | Medio | Coordinación frecuencias + filtros |
| Robo cables/equipos | Alta | Alto | Enterrado + equipos seguros + vigilancia |

---

## 8. INDICADORES DE DESEMPEÑO (KPIs)

**Según AT2:**

| Indicador ID | Descripción | Valor Mínimo Aceptación | Frecuencia Medición |
|:-------------|:------------|:------------------------|:--------------------|
| **TEL01** | Disponibilidad red backbone | 99.5% mensual | Continua |
| **TEL02** | Tiempo respuesta red | < 50 ms | Continua |
| **TEL03** | Disponibilidad comunicaciones radio | 99% | Continua |
| **TEL04** | Tiempo reparación fallas | < 4 horas | Por evento |

---

## 9. PRÓXIMOS PASOS

- [ ] Desarrollar análisis de requisitos detallado (Template T02)
- [ ] Realizar estudios de cobertura radio
- [ ] Elaborar especificaciones técnicas equipos (Template T04)
- [ ] Diseñar arquitectura de red detallada
- [ ] Tramitar permisos y licencias MinTIC
- [ ] Cotizar equipos especializados

---

## 10. OBSERVACIONES Y SUPUESTOS

### 10.1 Supuestos Técnicos
- Fibra óptica enterrada en todo el corredor
- Cobertura radio 100% del corredor
- Redundancia en enlaces críticos
- Personal técnico especializado disponible

### 10.2 Dependencias
- Permisos MinTIC para frecuencias radio
- Disponibilidad internet banda ancha
- Coordinación con operadores existentes
- Finalización obras civiles para instalación

### 10.3 Restricciones
- Disponibilidad 99.5% para sistemas críticos
- Cumplimiento normativa MinTIC
- Compatibilidad con sistemas ANI
- Acceso remoto para múltiples entidades

---

**Versión:** 1.0  
**Estado:** ✅ Ficha de Sistema Completada  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero de Telecomunicaciones