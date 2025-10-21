# T03: ARQUITECTURA CONCEPTUAL - ÁREAS DE SERVICIO
## Proyecto APP SABANA DE TORRES - CURUMANÍ

**Fecha:** 21 de Octubre 2025  
**Sistema:** Áreas de Servicio  
**Responsable:** Ingeniero Civil - Arquitecto  
**Versión:** 1.0  

---

## 1. INTRODUCCIÓN

### 1.1 Propósito del Documento
Definir la arquitectura conceptual de las Áreas de Servicio que proporcionarán servicios básicos, comerciales y de descanso para usuarios del corredor, con infraestructura completa de servicios públicos y sistemas de seguridad.

### 1.2 Alcance
Arquitectura completa para áreas de servicio distribuidas estratégicamente en el corredor, incluyendo servicios sanitarios, comerciales, descanso, infraestructura de servicios públicos y sistemas de seguridad.

### 1.3 Referencias
- T01_09: Ficha de Sistema - Áreas de Servicio
- T02_09: Análisis de Requisitos - Áreas de Servicio
- AT2: Servicios mínimos
- Normativa ambiental colombiana

---

## 2. ARQUITECTURA DE ALTO NIVEL

### 2.1 Diagrama de Arquitectura

```
                    ÁREA DE SERVICIO TIPO
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    │  ┌─────────────┐    ┌─────────────────────────┐ │
    │  │  SERVICIOS  │    │      ZONA COMERCIAL     │ │
    │  │   BÁSICOS   │    │  ┌─────────┬─────────┐  │ │
    │  │ ┌─────────┐ │    │  │Estación │ Tienda  │  │ │
    │  │ │Sanitarios│ │    │  │Combusti.│Convenie.│  │ │
    │  │ │H/M/Disc. │ │    │  └─────────┴─────────┘  │ │
    │  │ └─────────┘ │    │  ┌─────────┬─────────┐  │ │
    │  │ ┌─────────┐ │    │  │Restaur. │ Cajero  │  │ │
    │  │ │Agua Pot.│ │    │  │Cafetería│ ATM     │  │ │
    │  │ └─────────┘ │    │  └─────────┴─────────┘  │ │
    │  └─────────────┘    └─────────────────────────┘ │
    │                                                 │
    │  ┌─────────────────────────────────────────────┐ │
    │  │           ZONA DE DESCANSO                  │ │
    │  │  ┌─────────┐ ┌─────────┐ ┌─────────────┐   │ │
    │  │  │ Zonas   │ │Mobiliario│ │   Senderos  │   │ │
    │  │  │ Verdes  │ │ Urbano  │ │  Peatonales │   │ │
    │  │  └─────────┘ └─────────┘ └─────────────┘   │ │
    │  └─────────────────────────────────────────────┘ │
    │                                                 │
    │  ┌─────────────────────────────────────────────┐ │
    │  │         ESTACIONAMIENTOS                    │ │
    │  │  ┌─────────────┐    ┌─────────────────────┐ │ │
    │  │  │  Vehículos  │    │    Vehículos        │ │ │
    │  │  │   Livianos  │    │     Pesados         │ │ │
    │  │  │  50 espacios│    │   20 espacios       │ │ │
    │  │  └─────────────┘    └─────────────────────┘ │ │
    │  └─────────────────────────────────────────────┘ │
    └─────────────────────────────────────────────────┘
```

**Descripción del diagrama:**
Diseño modular integrado con servicios básicos, comerciales y recreativos, estacionamientos diferenciados y sistemas de servicios públicos completos.

### 2.2 Descripción de Componentes

| Componente | Función | Especificación Preliminar | Cantidad |
|:-----------|:--------|:--------------------------|:---------|
| **Edificio Servicios Básicos** | Sanitarios + agua potable | 200m², accesibilidad universal | Por área |
| **Zona Comercial** | Servicios comerciales | 400m², locales modulares | Por área |
| **Estacionamiento Livianos** | Parqueo vehículos | 50 espacios, pavimento rígido | Por área |
| **Estacionamiento Pesados** | Parqueo camiones | 20 espacios, pavimento reforzado | Por área |
| **PTAR** | Tratamiento aguas residuales | Eficiencia >90%, 500 personas/día | Por área |
| **Sistema Eléctrico** | Suministro energía | Transformador + tableros | Por área |
| **Sistema CCTV** | Seguridad y vigilancia | 8 cámaras + grabación | Por área |
| **Iluminación** | Seguridad nocturna | LED, control automático | Por área |

---

## 3. TOPOLOGÍA DEL SISTEMA

### 3.1 Distribución Espacial

- **Tipo de distribución:** Áreas estratégicas cada 60-80 km
- **Criterio ubicación:** Demanda de tráfico y servicios existentes
- **Integración:** Con estaciones de peaje cuando sea posible
- **Accesibilidad:** Desde ambos sentidos de circulación

### 3.2 Zonificación Funcional

```
    ZONIFICACIÓN TIPO (2 hectáreas)
    ┌─────────────────────────────────┐
    │ ACCESO    │        │   ACCESO   │
    │ NORTE     │ ZONA   │    SUR     │
    │           │COMERCIAL│           │
    ├───────────┼────────┼───────────┤
    │ESTACION.  │SERVICIOS│ESTACION.  │
    │LIVIANOS   │BÁSICOS  │PESADOS    │
    ├───────────┼────────┼───────────┤
    │    ZONA DE DESCANSO Y          │
    │       RECREACIÓN               │
    ├────────────────────────────────┤
    │  PTAR + SERVICIOS PÚBLICOS     │
    └────────────────────────────────┘
```

### 3.3 Servicios Públicos

**Infraestructura requerida:**
- **Agua potable:** PTAP si requerido + almacenamiento
- **Alcantarillado:** PTAR con eficiencia >90%
- **Energía eléctrica:** Transformador dedicado + backup
- **Telecomunicaciones:** Fibra óptica + WiFi público
- **Manejo residuos:** Separación + recolección especializada

---

## 4. FLUJO OPERACIONAL

### 4.1 Flujo de Usuario Típico

```
1. [Usuario ingresa al área]
   ↓ Control acceso
2. [Estaciona vehículo]
   ↓ Zona apropiada
3. [Utiliza servicios básicos]
   ↓ Sanitarios, agua
4. [Servicios comerciales opcionales]
   ↓ Combustible, tienda
5. [Área de descanso]
   ↓ Recreación, alimentación
6. [Sale del área]
```

### 4.2 Gestión de Servicios

| Servicio | Operación | Horario | Responsable |
|:---------|:----------|:--------|:------------|
| **Servicios básicos** | 24/7 | Continuo | Concesionario |
| **Limpieza** | Continua | 24/7 | Personal dedicado |
| **Seguridad** | Vigilancia | 24/7 | Personal + CCTV |
| **Mantenimiento** | Preventivo | Programado | Técnicos |

---

## 5. REDUNDANCIA Y DISPONIBILIDAD

### 5.1 Estrategia de Redundancia

| Componente | Tipo de Redundancia | Configuración | Justificación |
|:-----------|:--------------------|:--------------|:--------------|
| **Suministro agua** | Dual fuente | Acueducto + pozo | Continuidad servicio |
| **Energía eléctrica** | Backup | UPS + generador | Servicios críticos |
| **PTAR** | Redundancia parcial | 2 líneas tratamiento | Continuidad operación |
| **Comunicaciones** | Dual ISP | Fibra + 4G backup | Conectividad |

### 5.2 SLA (Service Level Agreement)

- **Disponibilidad servicios básicos:** 100%
- **Disponibilidad servicios comerciales:** 95%
- **Tiempo reparación:** < 4 horas
- **Calidad agua:** Potable según normativa
- **Eficiencia PTAR:** >90%

---

## 6. SEGURIDAD

### 6.1 Seguridad Física

- Sistema CCTV con 8 cámaras por área
- Iluminación perimetral LED
- Personal de seguridad 24/7
- Comunicación directa con CCO
- Control de acceso vehicular

### 6.2 Seguridad Ambiental

- PTAR con eficiencia >90%
- Manejo integral de residuos sólidos
- Separación en la fuente
- Monitoreo calidad agua
- Cumplimiento normativa ambiental

### 6.3 Normativa Aplicable

| Norma | Aplicación |
|:------|:-----------|
| NSR-10 | Construcciones sismo resistentes |
| RETIE | Instalaciones eléctricas |
| RAS 2000 | Agua potable y saneamiento |
| Decreto 1076/2015 | Gestión ambiental |

---

## 7. INTEGRACIÓN CON OTROS SISTEMAS

| Sistema Externo | Interface | Protocolo | Criticidad | Datos Intercambiados |
|:----------------|:----------|:----------|:-----------|:---------------------|
| **CCO** | IF-001 | TCP/IP | Media | Estado servicios, emergencias |
| **Sistema Eléctrico** | IF-002 | AC 13.2kV | Alta | Suministro energético |
| **Iluminación** | IF-003 | Control automático | Media | Iluminación nocturna |
| **Telecomunicaciones** | IF-004 | Fibra óptica | Media | Internet, comunicaciones |
| **Servicios Municipales** | IF-005 | Físico | Alta | Agua, alcantarillado |

---

## 8. ESCALABILIDAD

### 8.1 Dimensionamiento

| Parámetro | Capacidad Inicial | Capacidad Futura | Diseño |
|:----------|:------------------|:-----------------|:-------|
| **Usuarios/día** | 500 | 800 | 1,000 |
| **Estacionamientos** | 70 espacios | 90 espacios | 100 espacios |
| **Servicios comerciales** | 4 locales | 6 locales | 8 locales |
| **Capacidad PTAR** | 500 personas/día | 800 personas/día | 1,000 personas/día |

### 8.2 Estrategia de Ampliación

Diseño modular permite ampliaciones sin afectar operación:
- Módulos de servicios adicionales
- Ampliación de estacionamientos
- Servicios comerciales escalables
- Infraestructura sobredimensionada 25%

---

## 9. ANÁLISIS DE ALTERNATIVAS

### 9.1 Alternativa 1: Servicios Básicos Únicamente

**Descripción:** Solo sanitarios, agua potable y estacionamiento básico

**Ventajas:**
- Menor inversión inicial
- Operación más simple
- Menor complejidad

**Desventajas:**
- Limitada generación de ingresos
- Menor atractivo para usuarios
- No aprovecha potencial comercial

**Costo estimado:** $2,000,000

### 9.2 Alternativa 2: Áreas de Servicio Integrales ⭐ **RECOMENDADA**

**Descripción:** Servicios básicos + comerciales + recreativos + infraestructura completa

**Ventajas:**
- Mejor experiencia usuario
- Generación de ingresos adicionales
- Cumplimiento estándares internacionales
- Valor agregado al corredor

**Desventajas:**
- Mayor inversión inicial
- Operación más compleja
- Requiere operadores comerciales

**Costo estimado:** $3,390,000

**Justificación de selección:** Mejor servicio a usuarios, potencial de ingresos y cumplimiento de estándares APP 4G.

---

## 10. PLAN DE IMPLEMENTACIÓN

### 10.1 Fases de Implementación

| Fase | Actividad | Duración | Dependencias |
|:-----|:----------|:---------|:-------------|
| **Fase 1** | Estudios ambientales y permisos | 6 meses | Ubicaciones definidas |
| **Fase 2** | Diseño arquitectónico detallado | 3 meses | Permisos aprobados |
| **Fase 3** | Construcción infraestructura | 8 meses | Diseños aprobados |
| **Fase 4** | Instalación equipos y sistemas | 2 meses | Construcción completa |
| **Fase 5** | Pruebas y comisionamiento | 1 mes | Instalación completa |
| **Fase 6** | Operación y servicios comerciales | 1 mes | Pruebas aprobadas |

### 10.2 Hitos Críticos

- **H1:** Permisos ambientales aprobados - Mes 6
- **H2:** Primera área operativa - Mes 14
- **H3:** Servicios comerciales funcionando - Mes 20

---

## 11. PRÓXIMOS PASOS

- [ ] Iniciar trámites permisos ambientales
- [ ] Desarrollar especificaciones técnicas construcción (T04)
- [ ] Identificar operadores comerciales potenciales
- [ ] Estimar costos detallados construcción
- [ ] Crear plan de operación y mantenimiento
- [ ] Establecer convenios servicios públicos municipales

---

## 12. CONTROL DE VERSIONES

| Versión | Fecha | Responsable | Descripción |
|:---:|:---:|:---|:---|
| **v1.0** | 21/10/2025 | Ingeniero Civil - Arquitecto | Arquitectura conceptual inicial |

---

**Versión:** 1.0  
**Estado:** ✅ Arquitectura Conceptual Definida  
**Fecha:** 21/10/2025  
**Responsable:** Ingeniero Civil - Arquitecto