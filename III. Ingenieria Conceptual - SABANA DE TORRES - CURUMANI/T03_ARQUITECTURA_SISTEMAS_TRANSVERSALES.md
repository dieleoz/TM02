# T03 - ARQUITECTURA DE SISTEMAS TRANSVERSALES

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Código**: STC-APP4G-T03-TRANSVERSAL
- **Fecha**: 2024-10-23
- **Responsable**: [ASIGNAR]
- **Basado en**: Análisis T02 de todas las UF

## 🎯 OBJETIVO DEL ANÁLISIS
Definir la arquitectura integrada de sistemas que operan transversalmente en todas las UF, incluyendo Centro de Control de Operaciones (CCO), sistemas de peaje, intercambios y comunicaciones.

---

## 🏢 ARQUITECTURA CENTRO CONTROL OPERACIONES (CCO)

### **Ubicación y Características**
- **Localización**: Cerca del peaje Morrison (existente)
- **Área construida**: 800 m²
- **Cobertura**: 272 km de red vial (UF0-UF5)
- **Operación**: 24/7/365

### **Arquitectura Funcional CCO**
```
┌─────────────────────────────────────────────────────────────────┐
│                    CENTRO CONTROL OPERACIONES                  │
├─────────────────────────────────────────────────────────────────┤
│ SALA CONTROL PRINCIPAL (150 m²)                                │
│ ├── 6 Puestos operadores (UF0-UF5)                            │
│ ├── Video wall 3x3 (monitoreo integral)                       │
│ ├── Sistemas redundantes A/B                                   │
│ └── Comunicaciones críticas                                    │
├─────────────────────────────────────────────────────────────────┤
│ SALA SERVIDORES (80 m²)                                        │
│ ├── Servidores principales (redundantes)                       │
│ ├── Sistemas almacenamiento (RAID)                             │
│ ├── UPS 30 minutos + Planta emergencia                         │
│ └── Climatización redundante                                   │
├─────────────────────────────────────────────────────────────────┤
│ OFICINAS ADMINISTRATIVAS (200 m²)                              │
│ ├── Gerencia operaciones                                       │
│ ├── Ingeniería y mantenimiento                                 │
│ ├── Sala reuniones                                             │
│ └── Archivo técnico                                            │
├─────────────────────────────────────────────────────────────────┤
│ FACILIDADES OPERATIVAS (370 m²)                               │
│ ├── Dormitorios personal 24/7 (4 habitaciones)                │
│ ├── Cocina y comedor                                           │
│ ├── Taller mantenimiento equipos                               │
│ ├── Bodega repuestos                                           │
│ └── Parqueadero vehículos operativos                           │
└─────────────────────────────────────────────────────────────────┘
```

### **Sistemas Tecnológicos CCO**
- **A-CCO-01**: Sistema SCADA integrado (supervisión y control)
- **A-CCO-02**: Plataforma GIS en tiempo real
- **A-CCO-03**: Sistema gestión incidentes
- **A-CCO-04**: Integración con sistemas peaje
- **A-CCO-05**: Comunicaciones redundantes (fibra + radio + satelital)

---

## 🛣️ ARQUITECTURA SISTEMA PEAJES INTEGRADO

### **Configuración Dual de Peajes**
```
┌─────────────────────────────────────────────────────────────────┐
│                    SISTEMA PEAJES INTEGRADO                    │
├─────────────────────────────────────────────────────────────────┤
│ PEAJE LA GÓMEZ REUBICADO (UF3)                                │
│ ├── Capacidad: 6 casetas (4+2 reserva)                        │
│ ├── Tecnología: TAG + Manual + WIM                             │
│ ├── Edificio: 200 m² (administración)                          │
│ └── Integración: CCO + Sistema Central                         │
├─────────────────────────────────────────────────────────────────┤
│ PEAJE LA GÓMEZ NUEVO (UF2)                                     │
│ ├── Capacidad: 4 casetas (3+1 reserva)                        │
│ ├── Tecnología: TAG + Manual + WIM                             │
│ ├── Edificio: 150 m² (administración)                          │
│ └── Integración: CCO + Sistema Central                         │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMA CENTRAL RECAUDO                                        │
│ ├── Servidor principal: CCO Morrison                           │
│ ├── Backup: Oficinas Bogotá                                    │
│ ├── Comunicaciones: Fibra óptica redundante                    │
│ └── Integración: Bancos + ANI + Concesionario                  │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Tecnológica Peajes**
- **A-PEA-01**: Sistema recaudo unificado (ambos peajes)
- **A-PEA-02**: Base datos transacciones centralizada
- **A-PEA-03**: Comunicaciones tiempo real con CCO
- **A-PEA-04**: Sistema pesaje dinámico (WIM) integrado
- **A-PEA-05**: Cámaras seguridad y reconocimiento placas

---

## 🛤️ ARQUITECTURA INTERCAMBIOS VIALES

### **Intercambio San Martín Norte (UF3)**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTERCAMBIO SAN MARTÍN NORTE                      │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN: Diamante Modificado                             │
│ ├── Puente principal: 35 m luz, 12 m ancho                     │
│ ├── 4 Rampas: Radio 120 m, pendiente 5%                       │
│ ├── Carriles auxiliares: 150 m aceleración/desaceleración      │
│ └── Integración urbana: Accesos controlados                    │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMAS INTEGRADOS                                             │
│ ├── Señalización dinámica (VMS)                                │
│ ├── Iluminación LED completa                                   │
│ ├── Cámaras CCTV (8 puntos)                                    │
│ ├── Comunicación con CCO                                       │
│ └── Integración red urbana San Martín                          │
└─────────────────────────────────────────────────────────────────┘
```

### **Intercambio San Alberto Sur (UF5)**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTERCAMBIO SAN ALBERTO SUR                       │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN: Trompeta Modificada                             │
│ ├── Puente principal: 30 m luz, 12 m ancho                     │
│ ├── 3 Rampas principales: Radio 80 m, pendiente 6%             │
│ ├── Carriles auxiliares: 120 m aceleración/desaceleración      │
│ └── Integración urbana: Acceso sur San Alberto                 │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMAS INTEGRADOS                                             │
│ ├── Señalización urbana específica                             │
│ ├── Iluminación LED + semáforos                                │
│ ├── Cámaras CCTV (6 puntos)                                    │
│ ├── Comunicación con CCO                                       │
│ └── Integración transporte público urbano                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📡 ARQUITECTURA COMUNICACIONES INTEGRADA

### **Red Troncal de Comunicaciones**
```
┌─────────────────────────────────────────────────────────────────┐
│                RED COMUNICACIONES INTEGRADA                    │
├─────────────────────────────────────────────────────────────────┤
│ FIBRA ÓPTICA PRINCIPAL (272 km)                               │
│ ├── Ruta A: Por UF1-UF2-UF3 (backbone principal)             │
│ ├── Ruta B: Por UF4-UF5 (backup y redundancia)               │
│ ├── Capacidad: 144 hilos (48 activos + 96 reserva)            │
│ └── Tecnología: DWDM (Dense Wavelength Division)              │
├─────────────────────────────────────────────────────────────────┤
│ NODOS PRINCIPALES                                               │
│ ├── CCO Morrison (nodo central)                                │
│ ├── Peaje La Gómez Reubicado (nodo secundario)                │
│ ├── Peaje La Gómez Nuevo (nodo terciario)                     │
│ ├── Intercambio San Martín (nodo operativo)                   │
│ └── Intercambio San Alberto (nodo operativo)                  │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMAS BACKUP                                                 │
│ ├── Radio enlaces (backup fibra)                               │
│ ├── Comunicación satelital (emergencias)                       │
│ ├── Red celular (comunicaciones móviles)                       │
│ └── Sistema VHF (operaciones campo)                            │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura de Red**
- **A-COM-01**: Red MPLS corporativa (datos)
- **A-COM-02**: Red VoIP (comunicaciones voz)
- **A-COM-03**: Red videovigilancia (CCTV)
- **A-COM-04**: Red control industrial (SCADA)
- **A-COM-05**: Red WiFi operativa (mantenimiento)

---

## 🔧 ARQUITECTURA MANTENIMIENTO INTEGRADO

### **Sistema Gestión Mantenimiento**
```
┌─────────────────────────────────────────────────────────────────┐
│              SISTEMA MANTENIMIENTO INTEGRADO                   │
├─────────────────────────────────────────────────────────────────┤
│ CENTRO MANTENIMIENTO PRINCIPAL (CCO)                          │
│ ├── Taller especializado (200 m²)                              │
│ ├── Bodega repuestos centralizados                             │
│ ├── Flota vehículos operativos (8 unidades)                   │
│ └── Personal especializado 24/7                                │
├─────────────────────────────────────────────────────────────────┤
│ CENTROS MANTENIMIENTO SECUNDARIOS                              │
│ ├── Peaje La Gómez: Mantenimiento sistemas peaje              │
│ ├── Intercambio San Martín: Mantenimiento obras arte          │
│ ├── Intercambio San Alberto: Mantenimiento urbano             │
│ └── Puntos estratégicos: Mantenimiento rutinario              │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMA GESTIÓN (CMMS)                                         │
│ ├── Órdenes trabajo automatizadas                              │
│ ├── Inventario repuestos tiempo real                           │
│ ├── Programación mantenimiento preventivo                      │
│ ├── Seguimiento indicadores desempeño                          │
│ └── Integración con CCO y sistemas operativos                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 INTEGRACIÓN ENTRE SISTEMAS

### **Matriz de Integración**
| Sistema Origen | Sistema Destino | Tipo Integración | Protocolo | Criticidad |
|----------------|-----------------|------------------|-----------|------------|
| CCO | Peajes | Tiempo Real | TCP/IP | Crítica |
| CCO | Intercambios | Monitoreo | SNMP | Alta |
| Peajes | Sistema Central | Transaccional | HTTPS | Crítica |
| CCTV | CCO | Video Streaming | RTSP | Alta |
| SCADA | CCO | Control | Modbus | Crítica |
| Mantenimiento | CCO | Gestión | API REST | Media |

### **Flujos de Información Críticos**
- **F-INT-01**: Transacciones peaje → Sistema central (tiempo real)
- **F-INT-02**: Eventos tráfico → CCO → Respuesta operativa
- **F-INT-03**: Alarmas sistemas → CCO → Mantenimiento
- **F-INT-04**: Video vigilancia → CCO → Seguridad
- **F-INT-05**: Datos operativos → Reportes → ANI/Concesionario

---

## 📊 INDICADORES ARQUITECTURA

### **Disponibilidad Sistemas**
- **CCO**: 99.9% anual (máximo 8.76 horas fuera servicio)
- **Peajes**: 99.5% anual (máximo 43.8 horas fuera servicio)
- **Comunicaciones**: 99.8% anual (máximo 17.5 horas fuera servicio)
- **Intercambios**: 99.0% anual (sistemas electrónicos)

### **Capacidad y Rendimiento**
- **Procesamiento CCO**: 10,000 eventos/hora
- **Transacciones peaje**: 2,000 vehículos/hora (pico)
- **Ancho banda comunicaciones**: 1 Gbps (principal) + 100 Mbps (backup)
- **Almacenamiento datos**: 10 TB (3 años histórico)

---

## ✅ CRITERIOS VALIDACIÓN ARQUITECTURA

### **Técnicos**
- ✅ Integración perfecta entre todos los sistemas
- ✅ Redundancia en sistemas críticos
- ✅ Escalabilidad para crecimiento futuro
- ✅ Cumplimiento estándares internacionales

### **Operacionales**
- ✅ Operación 24/7 sin interrupciones
- ✅ Tiempo respuesta ≤ 20 minutos emergencias
- ✅ Disponibilidad según indicadores contractuales
- ✅ Integración con sistemas externos (ANI, bancos)

### **Mantenimiento**
- ✅ Acceso remoto para diagnóstico
- ✅ Mantenimiento predictivo implementado
- ✅ Repuestos críticos disponibles 24/7
- ✅ Personal especializado capacitado

---

## 🎯 PRÓXIMOS PASOS

### **Validación Técnica**
- [ ] Aprobación arquitectura por especialistas
- [ ] Validación integración con sistemas existentes
- [ ] Pruebas concepto elementos críticos
- [ ] Definición especificaciones técnicas detalladas

### **Implementación**
- [ ] Cronograma implementación por fases
- [ ] Plan migración sistemas existentes
- [ ] Protocolos pruebas integración
- [ ] Capacitación personal operativo

---
**Próximo paso**: T03 - Arquitectura específica por UF