# T03 - ARQUITECTURA DE SISTEMAS UF2: LAS PAMPAS - LLANO GRANDE

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Código**: STC-APP4G-UF2-T03
- **Fecha**: 2024-10-23
- **Responsable**: [ASIGNAR]
- **Basado en**: T02_UF2_ANALISIS_REQUISITOS.md

## 🎯 OBJETIVO DEL ANÁLISIS
Definir la arquitectura detallada de sistemas para UF2, incluyendo construcción de 9.86 km de vía nueva, calzada adicional por La Gómez, Variante La Gómez y Nuevo Peaje La Gómez, con coordinación dual de peajes.

---

## 🛣️ ARQUITECTURA SISTEMA VIAL DUAL

### **Configuración Vial Compleja - 9.86 KM**
```
┌─────────────────────────────────────────────────────────────────┐
│                  SISTEMA VIAL DUAL UF2                        │
├─────────────────────────────────────────────────────────────────┤
│ VÍA PRINCIPAL NUEVA (7.5 km)                                  │
│ ├── Calzada: 7.30 m (2 carriles × 3.65 m)                     │
│ ├── Bermas: 1.80 m cada lado                                   │
│ ├── Velocidad diseño: 80 km/h                                  │
│ └── Estructura: Pavimento nuevo completo                       │
├─────────────────────────────────────────────────────────────────┤
│ CALZADA ADICIONAL LA GÓMEZ (2.36 km)                          │
│ ├── Calzada urbana: 7.00 m (2 carriles × 3.50 m)             │
│ ├── Bermas urbanas: 1.00 m (reducidas)                        │
│ ├── Velocidad diseño: 50 km/h (zona urbana)                   │
│ └── Facilidades urbanas: Andenes + cicloruta                  │
├─────────────────────────────────────────────────────────────────┤
│ VARIANTE LA GÓMEZ (3.2 km)                                    │
│ ├── Calzada bypass: 7.30 m (estándar)                         │
│ ├── Bermas: 1.50 m (reducidas por restricciones)              │
│ ├── Velocidad diseño: 70 km/h (transición)                    │
│ └── Integración paisajística                                   │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Constructiva Coordinada**
- **A-UF2-V01**: Construcción vía principal (8 meses)
- **A-UF2-V02**: Calzada adicional La Gómez (6 meses, paralelo)
- **A-UF2-V03**: Variante La Gómez (10 meses, crítico social)
- **A-UF2-V04**: Nuevo peaje (8 meses, paralelo con variante)
- **A-UF2-V05**: Coordinación con UF1 y UF3 (empalmes perfectos)

---

## 🏘️ ARQUITECTURA VARIANTE LA GÓMEZ

### **Diseño Urbano Sensible**
```
┌─────────────────────────────────────────────────────────────────┐
│                    VARIANTE LA GÓMEZ                           │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN BYPASS URBANO (3.2 km)                          │
│                                                                 │
│         LA GÓMEZ ●──────────────────────────●                  │
│         CENTRO   │      VARIANTE NORTE      │                  │
│         POBLADO  │   ┌─────────────────────┐ │                  │
│                  │   │                     │ │                  │
│ ═════════════════●═══│   VÍA PRINCIPAL     │═●═══════════════   │
│                      │      UF2            │                    │
│                      └─────────────────────┘                    │
│                         CALZADA ADICIONAL                       │
│                        (POR CENTRO POBLADO)                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ ELEMENTOS URBANOS INTEGRADOS                                    │
│ ├── Acceso Norte: Glorieta urbana (R=25m)                     │
│ ├── Acceso Sur: Intersección semaforizada                      │
│ ├── Puente peatonal: Sobre variante (ancho 4m)                │
│ ├── Parque lineal: 500m × 20m (zona verde)                    │
│ └── Cicloruta: Integrada con trama urbana                     │
├─────────────────────────────────────────────────────────────────┤
│ FACILIDADES COMUNITARIAS                                        │
│ ├── Plaza de encuentro: 800 m² (acceso norte)                 │
│ ├── Juegos infantiles: Área recreativa                        │
│ ├── Gimnasio biosaludable: 15 equipos                         │
│ ├── Mobiliario urbano: Bancas + luminarias + basureras        │
│ └── WiFi público: 2 puntos acceso                             │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Gestión Social Intensiva**
```
┌─────────────────────────────────────────────────────────────────┐
│              GESTIÓN SOCIAL LA GÓMEZ                          │
├─────────────────────────────────────────────────────────────────┤
│ FASE 1: SOCIALIZACIÓN INTENSIVA (4 meses)                     │
│ ├── Oficina permanente: Centro La Gómez                       │
│ ├── Reuniones semanales: Salón comunal                        │
│ ├── Talleres participativos: 12 sesiones                      │
│ ├── Diseño participativo: Espacios públicos                   │
│ └── Acuerdos comunitarios: Formalizados                       │
├─────────────────────────────────────────────────────────────────┤
│ FASE 2: COMPENSACIONES ACORDADAS (6 meses)                    │
│ ├── Avalúos prediales: 25 predios afectados                   │
│ ├── Negociación directa: 20 casos exitosos                    │
│ ├── Expropiación: 5 casos (último recurso)                    │
│ ├── Reubicación temporal: 8 familias                          │
│ └── Compensación colectiva: Obras comunitarias                │
├─────────────────────────────────────────────────────────────────┤
│ FASE 3: CONSTRUCCIÓN PARTICIPATIVA (10 meses)                 │
│ ├── Empleo local: 40% mano obra no calificada                │
│ ├── Veeduría ciudadana: Comité seguimiento                    │
│ ├── Información semanal: Avances + cronograma                 │
│ ├── Gestión quejas: Respuesta ≤ 48 horas                      │
│ └── Obras adicionales: Según acuerdos                         │
├─────────────────────────────────────────────────────────────────┤
│ FASE 4: SEGUIMIENTO POST-OBRA (24 meses)                      │
│ ├── Mantenimiento conjunto: Comunidad + concesionario         │
│ ├── Capacitación: Uso adecuado infraestructura               │
│ ├── Monitoreo impactos: Sociales + ambientales               │
│ └── Ajustes menores: Según necesidades                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏢 ARQUITECTURA NUEVO PEAJE LA GÓMEZ

### **Diseño Funcional Coordinado**
```
┌─────────────────────────────────────────────────────────────────┐
│                NUEVO PEAJE LA GÓMEZ                            │
├─────────────────────────────────────────────────────────────────┤
│ PLAZA DE PEAJE (1.8 hectáreas)                                │
│ ├── 4 Casetas (3 operativas + 1 reserva)                      │
│ ├── Carriles aproximación: 120 m                               │
│ ├── Carriles salida: 80 m                                      │
│ └── Área maniobras: Vehículos pesados                         │
├─────────────────────────────────────────────────────────────────┤
│ EDIFICIO ADMINISTRACIÓN (150 m²)                               │
│ ├── Sala control: 30 m² (4 puestos operadores)                │
│ ├── Oficina supervisor: 15 m²                                  │
│ ├── Sala servidores: 12 m² (climatizada)                      │
│ ├── Archivo y bodega: 20 m²                                    │
│ ├── Facilidades personal: 40 m²                                │
│ ├── Cafetería usuarios: 25 m²                                  │
│ └── Servicios sanitarios: 20 m²                                │
├─────────────────────────────────────────────────────────────────┤
│ COORDINACIÓN OPERACIONAL                                        │
│ ├── Integración con peaje reubicado UF3                       │
│ ├── Sistema recaudo unificado                                  │
│ ├── Comunicación tiempo real CCO                               │
│ ├── Backup operacional mutuo                                   │
│ └── Gestión tráfico coordinada                                 │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Tecnológica Dual Peajes**
```
┌─────────────────────────────────────────────────────────────────┐
│              SISTEMA DUAL PEAJES LA GÓMEZ                     │
├─────────────────────────────────────────────────────────────────┤
│ NUEVO PEAJE (UF2)          │  PEAJE REUBICADO (UF3)           │
│ ├── 4 Casetas TAG+Manual   │  ├── 6 Casetas TAG+Manual        │
│ ├── 2 Carriles WIM         │  ├── 2 Carriles WIM              │
│ ├── 8 Cámaras CCTV         │  ├── 12 Cámaras CCTV             │
│ ├── Fibra óptica CCO       │  ├── Fibra óptica CCO            │
│ └── Backup radio           │  └── Backup radio                │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMA CENTRAL UNIFICADO                                       │
│ ├── Servidor principal: CCO Morrison                           │
│ ├── Base datos única: Transacciones ambos peajes              │
│ ├── Balanceador carga: Distribución tráfico                   │
│ ├── Respaldo automático: Cada 15 minutos                      │
│ └── Reportes consolidados: Ingresos + tráfico                 │
├─────────────────────────────────────────────────────────────────┤
│ OPERACIÓN COORDINADA                                            │
│ ├── Tarifas unificadas: Misma estructura                      │
│ ├── Horarios coordinados: Mantenimiento alternado             │
│ ├── Personal intercambiable: Capacitación cruzada             │
│ ├── Repuestos compartidos: Inventario optimizado              │
│ └── Gestión incidentes: Backup mutuo                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💧 ARQUITECTURA DRENAJE URBANO-RURAL

### **Sistema Drenaje Integrado**
```
┌─────────────────────────────────────────────────────────────────┐
│              DRENAJE INTEGRADO UF2                            │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE VÍA PRINCIPAL (7.5 km)                                │
│ ├── Cunetas: Sección triangular 0.8 m                         │
│ ├── Alcantarillas: 18 unidades Ø 0.90-1.20 m                 │
│ ├── Subdrenaje: Filtro francés continuo                       │
│ └── Entregas: 8 puntos drenaje natural                        │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE URBANO LA GÓMEZ                                        │
│ ├── Sumideros: Cada 40 m (60 unidades)                        │
│ ├── Red colectora: Tubería concreto 300-800 mm                │
│ ├── Cámaras inspección: 15 unidades                           │
│ ├── Planta tratamiento: 100 L/s                               │
│ └── Entrega: Caño La Gómez (tratada)                          │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE VARIANTE (3.2 km)                                     │
│ ├── Cunetas verdes: Bioretención                              │
│ ├── Jardines lluvia: 8 unidades                               │
│ ├── Pavimento permeable: Andenes                              │
│ ├── Humedal artificial: 200 m²                                │
│ └── Infiltración natural: Maximizada                          │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE NUEVO PEAJE                                            │
│ ├── Captación: 1,800 m² área                                  │
│ ├── Tratamiento: Trampa grasas + sedimentador                 │
│ ├── Almacenamiento: Tanque 30 m³                              │
│ ├── Reutilización: Riego paisajismo                           │
│ └── Entrega excesos: Sistema municipal                        │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Sostenible Agua**
- **A-UF2-D01**: Sistemas urbanos drenaje sostenible (SUDS)
- **A-UF2-D02**: Reutilización aguas lluvias (30% necesidades riego)
- **A-UF2-D03**: Tratamiento antes entrega (100% aguas)
- **A-UF2-D04**: Monitoreo calidad (3 estaciones automáticas)
- **A-UF2-D05**: Integración con sistema municipal La Gómez

---

## 🔧 ARQUITECTURA SISTEMAS AUXILIARES

### **Sistema Iluminación Diferenciada**
```
┌─────────────────────────────────────────────────────────────────┐
│              ILUMINACIÓN DIFERENCIADA UF2                     │
├─────────────────────────────────────────────────────────────────┤
│ ILUMINACIÓN VIAL PRINCIPAL                                      │
│ ├── Intersecciones: LED 100W (8 puntos)                       │
│ ├── Nuevo peaje: LED 150W (20 luminarias)                     │
│ ├── Empalmes UF: LED 75W (4 puntos)                          │
│ └── Curvas críticas: LED 50W (6 puntos)                       │
├─────────────────────────────────────────────────────────────────┤
│ ILUMINACIÓN URBANA LA GÓMEZ                                    │
│ ├── Calzada adicional: LED 75W cada 25m (95 luminarias)      │
│ ├── Variante: LED 100W cada 30m (110 luminarias)             │
│ ├── Andenes: LED 40W cada 20m (160 luminarias)               │
│ ├── Parque lineal: LED decorativo (25 luminarias)            │
│ └── Plaza encuentro: LED ornamental (15 luminarias)          │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMAS INTELIGENTES                                           │
│ ├── Control automático: Fotoceldas + temporizadores           │
│ ├── Dimming: Reducción 50% después 23:00                     │
│ ├── Monitoreo remoto: Desde CCO Morrison                      │
│ ├── Mantenimiento predictivo: Sensores LED                    │
│ └── Eficiencia energética: 60% vs. tecnología anterior       │
└─────────────────────────────────────────────────────────────────┘
```

### **Sistema Señalización Integrada**
- **A-UF2-S01**: Señalización vial principal (estándar INVIAS)
- **A-UF2-S02**: Señalización urbana La Gómez (específica)
- **A-UF2-S03**: Señalización variante (bypass claro)
- **A-UF2-S04**: Señalización nuevo peaje (coordinada con reubicado)
- **A-UF2-S05**: VMS dinámicos (2 unidades, gestión tráfico)

---

## 🔄 INTEGRACIÓN Y COORDINACIÓN

### **Coordinación Triple Sistema**
```
┌─────────────────────────────────────────────────────────────────┐
│              COORDINACIÓN TRIPLE UF2                          │
├─────────────────────────────────────────────────────────────────┤
│ COORDINACIÓN UF1 → UF2                                         │
│ ├── Empalme PK30+000: Transición geométrica perfecta          │
│ ├── Cronograma: UF1 termina antes UF2 inicia                 │
│ ├── Materiales: Continuidad especificaciones                  │
│ └── Calidad: Mismos estándares y controles                    │
├─────────────────────────────────────────────────────────────────┤
│ COORDINACIÓN UF2 → UF3                                         │
│ ├── Peajes: Operación coordinada (nuevo + reubicado)          │
│ ├── Comunicaciones: Sistema unificado                         │
│ ├── Cronograma: Sincronización crítica                        │
│ └── Usuarios: Información integrada                           │
├─────────────────────────────────────────────────────────────────┤
│ COORDINACIÓN INTERNA UF2                                       │
│ ├── Vía principal + variante: Construcción paralela           │
│ ├── Calzada adicional: Integración urbana                     │
│ ├── Nuevo peaje: Sincronización con variante                  │
│ └── Gestión social: Proceso unificado                         │
└─────────────────────────────────────────────────────────────────┘
```

### **Integración con Sistemas Transversales**
- **I-UF2-01**: CCO Morrison (monitoreo dual peajes)
- **I-UF2-02**: Sistema central recaudo (unificado)
- **I-UF2-03**: Red comunicaciones (fibra óptica + backup)
- **I-UF2-04**: Mantenimiento integrado (recursos compartidos)
- **I-UF2-05**: Gestión tráfico (coordinación UF1-UF3)

---

## 📊 INDICADORES ARQUITECTURA UF2

### **Capacidad y Desempeño**
- **Vía principal**: 1,500 veh/h/carril (Nivel Servicio C)
- **Variante La Gómez**: 1,000 veh/h (bypass efectivo 80%)
- **Calzada adicional**: 800 veh/h (tráfico local)
- **Nuevo peaje**: 1,500 veh/h (3 casetas operativas)

### **Integración Social y Urbana**
- **Aceptación comunitaria**: ≥ 80% (encuestas)
- **Empleo local**: 40% mano obra no calificada
- **Obras adicionales**: Según acuerdos comunitarios
- **Mantenimiento conjunto**: 5 años post-construcción

---

## ✅ CRITERIOS VALIDACIÓN ARQUITECTURA UF2

### **Técnicos**
- ✅ Integración perfecta vía principal + variante + peaje
- ✅ Coordinación operacional dual peajes
- ✅ Calzada adicional integrada con trama urbana
- ✅ Sistemas auxiliares funcionando según especificaciones

### **Sociales**
- ✅ Aprobación comunidad La Gómez ≥ 80%
- ✅ Compensaciones acordadas y ejecutadas
- ✅ Obras comunitarias adicionales entregadas
- ✅ Empleo local según compromisos

### **Operacionales**
- ✅ Construcción coordinada sin conflictos mayores
- ✅ Nuevo peaje operativo según capacidad
- ✅ Variante funcionando como bypass efectivo
- ✅ Integración exitosa con UF1 y UF3

---

## 🎯 PRÓXIMOS PASOS UF2

### **Críticos Inmediatos**
- [ ] Aprobación comunidad La Gómez (crítico)
- [ ] Coordinación operacional dual peajes
- [ ] Sincronización cronograma con UF1 y UF3
- [ ] Gestión predial variante

### **Implementación Compleja**
- [ ] Gestión social intensiva (4 meses)
- [ ] Construcción coordinada 4 elementos
- [ ] Integración sistemas tecnológicos
- [ ] Seguimiento post-construcción

---
**Próximo paso**: T03 - Arquitectura UF1 y UF4 (construcción estándar)