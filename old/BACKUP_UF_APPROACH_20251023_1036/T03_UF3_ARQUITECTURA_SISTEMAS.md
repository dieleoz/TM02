# T03 - ARQUITECTURA DE SISTEMAS UF3: RÍO SOGAMOSO - EL JUNCAL

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Código**: STC-APP4G-UF3-T03
- **Fecha**: 2024-10-23
- **Responsable**: [ASIGNAR]
- **Basado en**: T02_UF3_ANALISIS_REQUISITOS.md

## 🎯 OBJETIVO DEL ANÁLISIS
Definir la arquitectura detallada de sistemas para UF3, incluyendo mejoramiento de 77.2 km, reubicación del Peaje La Gómez e Intercambio San Martín Norte, con integración a sistemas transversales.

---

## 🛣️ ARQUITECTURA SISTEMA VIAL PRINCIPAL

### **Configuración Geométrica - 77.2 KM**
```
┌─────────────────────────────────────────────────────────────────┐
│                    MEJORAMIENTO VIAL UF3                       │
├─────────────────────────────────────────────────────────────────┤
│ SECCIÓN TÍPICA MEJORADA                                        │
│ ├── Calzada: 7.30 m (2 carriles × 3.65 m)                     │
│ ├── Bermas: 1.80 m cada lado                                   │
│ ├── Ancho total corona: 10.90 m                                │
│ └── Velocidad diseño: 80 km/h                                  │
├─────────────────────────────────────────────────────────────────┤
│ ESTRUCTURA PAVIMENTO MEJORADO                                   │
│ ├── Carpeta asfáltica: 7.5 cm (MDC-2)                         │
│ ├── Base granular: 20 cm (BG-1)                               │
│ ├── Sub-base granular: 30 cm (SBG-1)                          │
│ └── Mejoramiento subrasante: 40 cm (según CBR)                │
├─────────────────────────────────────────────────────────────────┤
│ SEGMENTACIÓN POR ESTADO ACTUAL                                  │
│ ├── Tramo A (0-25 km): Mejoramiento superficial               │
│ ├── Tramo B (25-50 km): Reconstrucción parcial                │
│ ├── Tramo C (50-77.2 km): Reconstrucción total                │
│ └── Puntos críticos: Refuerzo estructural                     │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Constructiva por Fases**
- **A-UF3-V01**: Fase 1 - Mejoramiento Tramo A (25 km) - 6 meses
- **A-UF3-V02**: Fase 2 - Reconstrucción Tramo B (25 km) - 8 meses  
- **A-UF3-V03**: Fase 3 - Reconstrucción Tramo C (27.2 km) - 10 meses
- **A-UF3-V04**: Integración con reubicación peaje - Paralelo
- **A-UF3-V05**: Integración con intercambio San Martín - Paralelo

---

## 🏢 ARQUITECTURA PEAJE LA GÓMEZ REUBICADO

### **Diseño Funcional Completo**
```
┌─────────────────────────────────────────────────────────────────┐
│                PEAJE LA GÓMEZ REUBICADO                        │
├─────────────────────────────────────────────────────────────────┤
│ PLAZA DE PEAJE (2.5 hectáreas)                                │
│ ├── 6 Casetas (4 operativas + 2 reserva)                      │
│ ├── Carriles aproximación: 150 m                               │
│ ├── Carriles salida: 100 m                                     │
│ └── Área maniobras vehículos pesados                           │
├─────────────────────────────────────────────────────────────────┤
│ EDIFICIO ADMINISTRACIÓN (200 m²)                               │
│ ├── Sala control: 40 m² (6 puestos operadores)                │
│ ├── Oficina supervisor: 20 m²                                  │
│ ├── Sala servidores: 15 m² (climatizada)                      │
│ ├── Archivo y bodega: 25 m²                                    │
│ ├── Facilidades personal: 60 m²                                │
│ ├── Cafetería usuarios: 40 m²                                  │
│ └── Servicios sanitarios: 30 m²                                │
├─────────────────────────────────────────────────────────────────┤
│ FACILIDADES OPERATIVAS                                          │
│ ├── Parqueadero administrativo: 20 espacios                    │
│ ├── Parqueadero usuarios: 15 espacios                          │
│ ├── Área carga/descarga: 2 bahías                             │
│ ├── Subestación eléctrica: 500 kVA                            │
│ └── Planta tratamiento aguas: 50 usuarios                      │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Tecnológica Peaje**
- **A-UF3-P01**: Sistema recaudo TAG + Manual (6 carriles)
- **A-UF3-P02**: Sistema pesaje dinámico WIM (2 carriles)
- **A-UF3-P03**: CCTV + reconocimiento placas (12 cámaras)
- **A-UF3-P04**: Sistema comunicaciones redundante
- **A-UF3-P05**: Integración tiempo real con CCO Morrison

### **Plan Reubicación Sin Pérdida Ingresos**
```
┌─────────────────────────────────────────────────────────────────┐
│              PLAN REUBICACIÓN PEAJE                            │
├─────────────────────────────────────────────────────────────────┤
│ FASE 1: CONSTRUCCIÓN NUEVO PEAJE (8 meses)                    │
│ ├── Construcción paralela sin afectar operación actual         │
│ ├── Instalación y pruebas sistemas tecnológicos               │
│ ├── Capacitación personal en nuevo peaje                       │
│ └── Certificación sistemas por interventoría                   │
├─────────────────────────────────────────────────────────────────┤
│ FASE 2: MIGRACIÓN OPERATIVA (48 horas)                        │
│ ├── Viernes 22:00: Cierre peaje actual                        │
│ ├── Sábado 06:00: Apertura peaje reubicado                    │
│ ├── Migración base datos y configuraciones                     │
│ └── Verificación operación normal                              │
├─────────────────────────────────────────────────────────────────┤
│ FASE 3: DEMOLICIÓN PEAJE ACTUAL (2 meses)                     │
│ ├── Desmontaje equipos reutilizables                          │
│ ├── Demolición infraestructura civil                           │
│ ├── Restauración área según PMA                                │
│ └── Integración con mejoramiento vial UF3                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛤️ ARQUITECTURA INTERCAMBIO SAN MARTÍN NORTE

### **Diseño Geométrico Detallado**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTERCAMBIO SAN MARTÍN NORTE                      │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN: DIAMANTE MODIFICADO                             │
│                                                                 │
│     ┌─────────────────────────────────────────┐                │
│     │           VÍA URBANA SAN MARTÍN         │                │
│     └─────────────┬───────────────────────────┘                │
│                   │                                             │
│     ┌─────────────┼───────────────────────────┐                │
│     │    RAMPA    │    PUENTE     │   RAMPA   │                │
│     │     NE      │   PRINCIPAL   │    NO     │                │
│     └─────────────┼───────────────────────────┘                │
│                   │                                             │
│ ════════════════════════════════════════════════════════════    │
│           AUTOPISTA PRINCIPAL UF3 (80 km/h)                    │
│ ════════════════════════════════════════════════════════════    │
│                   │                                             │
│     ┌─────────────┼───────────────────────────┐                │
│     │    RAMPA    │               │   RAMPA   │                │
│     │     SE      │               │    SO     │                │
│     └─────────────┼───────────────────────────┘                │
│                   │                                             │
│     └─────────────┴───────────────────────────┘                │
│                VÍA URBANA SAN MARTÍN                           │
└─────────────────────────────────────────────────────────────────┘
```

### **Especificaciones Estructurales**
- **A-UF3-I01**: Puente principal - Luz 35 m, ancho 12 m
- **A-UF3-I02**: Fundaciones - Pilotes 15 m, capacidad 500 ton
- **A-UF3-I03**: Superestructura - Vigas pretensadas + losa
- **A-UF3-I04**: Rampas - 4 estructuras, radio 120 m
- **A-UF3-I05**: Muros contención - Altura máxima 8 m

### **Integración Urbana San Martín**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTEGRACIÓN URBANA SAN MARTÍN                     │
├─────────────────────────────────────────────────────────────────┤
│ ACCESOS URBANOS                                                 │
│ ├── Acceso Norte: Calle 15 → Rampa NE                         │
│ ├── Acceso Sur: Carrera 10 → Rampa SE                         │
│ ├── Carriles auxiliares: 150 m aceleración/desaceleración     │
│ └── Señalización urbana específica                             │
├─────────────────────────────────────────────────────────────────┤
│ FACILIDADES URBANAS                                             │
│ ├── Andenes peatonales: 2.0 m ancho                           │
│ ├── Cicloruta: 1.5 m integrada                                │
│ ├── Iluminación LED: 100% cobertura                           │
│ ├── Semáforos: 4 intersecciones                               │
│ └── Paraderos transporte público: 2 ubicaciones               │
├─────────────────────────────────────────────────────────────────┤
│ PAISAJISMO Y AMBIENTE                                           │
│ ├── Zonas verdes: 2,500 m² (especies nativas)                 │
│ ├── Manejo aguas lluvias: Jardines infiltración               │
│ ├── Barreras acústicas: 200 m (zonas residenciales)          │
│ └── Integración arquitectónica con entorno urbano             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💧 ARQUITECTURA SISTEMA DRENAJE INTEGRAL

### **Diseño Hidrológico UF3**
```
┌─────────────────────────────────────────────────────────────────┐
│                SISTEMA DRENAJE INTEGRAL UF3                   │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE LONGITUDINAL (77.2 km)                                │
│ ├── Cunetas revestidas: Sección triangular 1.0 m              │
│ ├── Subdrenaje: Filtro francés continuo                       │
│ ├── Colectores: Tubería PVC 300-600 mm                        │
│ └── Entregas: 45 puntos a drenaje natural                     │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE TRANSVERSAL                                             │
│ ├── Alcantarillas: 120 unidades Ø 0.90-2.40 m                │
│ ├── Box culvert: 8 unidades (cruces principales)              │
│ ├── Puentes menores: 3 unidades (luces 8-15 m)               │
│ └── Obras protección: Gaviones y enrocados                    │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE ESPECIAL INTERCAMBIO                                   │
│ ├── Sistema captación: 12 sumideros                           │
│ ├── Red colectora: Tubería concreto 400-800 mm                │
│ ├── Cámaras inspección: 8 unidades                            │
│ └── Entrega final: Quebrada San Martín                        │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE PEAJE REUBICADO                                        │
│ ├── Captación aguas lluvias: 2,500 m² área                    │
│ ├── Sistema tratamiento: Trampa grasas + sedimentador         │
│ ├── Almacenamiento: Tanque 50 m³                              │
│ └── Entrega tratada: Caño La Gómez                            │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Control Inundaciones**
- **A-UF3-D01**: Modelación hidráulica HEC-RAS (77.2 km)
- **A-UF3-D02**: Sistema alerta temprana (5 estaciones)
- **A-UF3-D03**: Obras protección críticas (8 puntos)
- **A-UF3-D04**: Plan contingencia inundaciones
- **A-UF3-D05**: Integración con CCO (monitoreo tiempo real)

---

## 🔧 ARQUITECTURA SISTEMAS AUXILIARES

### **Sistema Iluminación y Señalización**
```
┌─────────────────────────────────────────────────────────────────┐
│            ILUMINACIÓN Y SEÑALIZACIÓN UF3                     │
├─────────────────────────────────────────────────────────────────┤
│ ILUMINACIÓN VIAL                                               │
│ ├── Intercambio San Martín: LED 150W (40 luminarias)          │
│ ├── Peaje reubicado: LED 100W (25 luminarias)                 │
│ ├── Intersecciones: LED 75W (15 puntos)                       │
│ └── Túneles/pasos deprimidos: LED continuo                    │
├─────────────────────────────────────────────────────────────────┤
│ SEÑALIZACIÓN VERTICAL                                           │
│ ├── Señales informativas: 45 unidades                         │
│ ├── Señales reglamentarias: 120 unidades                      │
│ ├── Señales preventivas: 80 unidades                          │
│ └── Pórticos: 8 unidades (intercambio + peaje)               │
├─────────────────────────────────────────────────────────────────┤
│ SEÑALIZACIÓN HORIZONTAL                                         │
│ ├── Demarcación continua: 154.4 km (77.2 × 2)               │
│ ├── Demarcación discontinua: 38.6 km                          │
│ ├── Flechas y símbolos: 200 unidades                          │
│ └── Tachas reflectivas: 2,500 unidades                        │
├─────────────────────────────────────────────────────────────────┤
│ SISTEMAS INTELIGENTES                                           │
│ ├── VMS (Variable Message Signs): 4 unidades                  │
│ ├── Cámaras CCTV: 12 puntos estratégicos                     │
│ ├── Detectores tráfico: 8 puntos                              │
│ └── Estaciones meteorológicas: 2 unidades                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 INTEGRACIÓN CON SISTEMAS TRANSVERSALES

### **Conexiones CCO Morrison**
- **I-UF3-01**: Fibra óptica dedicada (backup por UF0)
- **I-UF3-02**: Monitoreo tiempo real peaje reubicado
- **I-UF3-03**: Control remoto intercambio San Martín
- **I-UF3-04**: Gestión tráfico durante construcción
- **I-UF3-05**: Coordinación emergencias y mantenimiento

### **Coordinación con Otras UF**
- **C-UF3-01**: Empalme UF2 → UF3 (transición peajes)
- **C-UF3-02**: Coordinación UF3 → UF4 (continuidad vial)
- **C-UF3-03**: Gestión tráfico UF0 durante construcción UF3
- **C-UF3-04**: Integración cronograma construcción
- **C-UF3-05**: Comunicaciones unificadas

---

## 📊 INDICADORES ARQUITECTURA UF3

### **Capacidad y Desempeño**
- **Vía principal**: 1,500 veh/h/carril (Nivel Servicio C)
- **Peaje reubicado**: 2,000 veh/h (6 casetas)
- **Intercambio**: 800 veh/h por rampa
- **Disponibilidad**: 95% anual (mantenimiento incluido)

### **Calidad y Durabilidad**
- **Pavimento**: IRI ≤ 2.5 m/km, vida útil 20 años
- **Estructuras**: Vida útil 75 años
- **Sistemas tecnológicos**: Disponibilidad 99.5%
- **Drenaje**: Período retorno 100 años

---

## ✅ CRITERIOS VALIDACIÓN ARQUITECTURA UF3

### **Técnicos**
- ✅ Integración perfecta peaje reubicado sin pérdida ingresos
- ✅ Intercambio San Martín operativo según capacidad
- ✅ Mejoramiento 77.2 km cumple estándares INVIAS
- ✅ Sistemas auxiliares integrados con CCO

### **Operacionales**
- ✅ Construcción por fases sin afectar UF0
- ✅ Reubicación peaje en máximo 48 horas
- ✅ Intercambio integrado con red urbana San Martín
- ✅ Nivel servicio vial ≥ C durante y post construcción

### **Contractuales**
- ✅ Cumplimiento especificaciones técnicas
- ✅ Cronograma 24 meses total UF3
- ✅ Presupuesto dentro límites aprobados
- ✅ Calidad según estándares contractuales

---

## 🎯 PRÓXIMOS PASOS UF3

### **Validación Técnica**
- [ ] Aprobación diseños intercambio por estructurista
- [ ] Validación plan reubicación peaje con operador
- [ ] Modelación hidráulica detallada
- [ ] Integración con cronograma maestro proyecto

### **Implementación**
- [ ] Licitación construcción por paquetes
- [ ] Gestión predial intercambio San Martín
- [ ] Coordinación con autoridades San Martín
- [ ] Plan comunicaciones usuarios durante construcción

---
**Próximo paso**: T03 - Arquitectura UF5 (Tropezón - San Alberto)