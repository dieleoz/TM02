# T03 - ARQUITECTURA DE SISTEMAS UF5: TROPEZÓN - SAN ALBERTO

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Código**: STC-APP4G-UF5-T03
- **Fecha**: 2024-10-23
- **Responsable**: [ASIGNAR]
- **Basado en**: T02_UF5_ANALISIS_REQUISITOS.md

## 🎯 OBJETIVO DEL ANÁLISIS
Definir la arquitectura detallada de sistemas para UF5, incluyendo construcción de 9.05 km de vía nueva, Variante Tropezón, Variante La Palma e Intercambio San Alberto Acceso Sur, con máxima integración urbana.

---

## 🛣️ ARQUITECTURA SISTEMA VIAL PRINCIPAL

### **Configuración Geométrica - 9.05 KM**
```
┌─────────────────────────────────────────────────────────────────┐
│                  VÍA PRINCIPAL UF5 - 9.05 KM                  │
├─────────────────────────────────────────────────────────────────┤
│ SECCIÓN TÍPICA NUEVA                                           │
│ ├── Calzada: 7.30 m (2 carriles × 3.65 m)                     │
│ ├── Bermas: 1.80 m cada lado                                   │
│ ├── Ancho total corona: 10.90 m                                │
│ └── Velocidad diseño: 80 km/h                                  │
├─────────────────────────────────────────────────────────────────┤
│ ESTRUCTURA PAVIMENTO NUEVA                                      │
│ ├── Carpeta asfáltica: 10 cm (MDC-2)                          │
│ ├── Base granular: 25 cm (BG-1)                               │
│ ├── Sub-base granular: 35 cm (SBG-1)                          │
│ └── Mejoramiento subrasante: 50 cm (CBR ≥ 10%)               │
├─────────────────────────────────────────────────────────────────┤
│ SEGMENTACIÓN CONSTRUCTIVA                                       │
│ ├── Tramo A (0-3 km): Vía principal + conexión Variante Tropezón │
│ ├── Tramo B (3-6 km): Vía principal + conexión Variante La Palma │
│ ├── Tramo C (6-9.05 km): Vía principal + Intercambio San Alberto │
│ └── Coordinación: Construcción simultánea elementos especiales │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Constructiva Integrada**
- **A-UF5-V01**: Construcción vía principal por tramos (9 meses)
- **A-UF5-V02**: Integración simultánea con variantes (paralelo)
- **A-UF5-V03**: Construcción intercambio San Alberto (12 meses)
- **A-UF5-V04**: Coordinación con UF4 (empalme perfecto)
- **A-UF5-V05**: Gestión tráfico durante construcción múltiple

---

## 🏘️ ARQUITECTURA VARIANTE TROPEZÓN

### **Diseño Urbano Integrado**
```
┌─────────────────────────────────────────────────────────────────┐
│                    VARIANTE TROPEZÓN                           │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN BYPASS (2.5 km)                                 │
│                                                                 │
│    TROPEZÓN ●────────────────────────────────────●             │
│    CENTRO   │        VARIANTE NORTE               │             │
│    POBLADO  │     ┌─────────────────────┐        │             │
│             │     │                     │        │             │
│ ════════════●═════│   VÍA PRINCIPAL     │════════●═════════    │
│             │     │      UF5            │        │             │
│             │     └─────────────────────┘        │             │
│             │        VARIANTE SUR                │             │
│             ●────────────────────────────────────●             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ ESPECIFICACIONES TÉCNICAS                                       │
│ ├── Longitud total: 2.5 km                                     │
│ ├── Velocidad diseño: 60 km/h (zona urbana)                   │
│ ├── Calzada: 7.00 m (2 carriles × 3.50 m)                     │
│ ├── Bermas: 1.50 m (reducidas por restricciones)              │
│ └── Pendiente máxima: 4% (integración urbana)                 │
├─────────────────────────────────────────────────────────────────┤
│ CONEXIONES URBANAS                                              │
│ ├── Acceso Norte: Intersección semaforizada                    │
│ ├── Acceso Sur: Glorieta urbana                               │
│ ├── Carriles auxiliares: 80 m aceleración/desaceleración      │
│ └── Integración con red vial municipal                         │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Urbana Tropezón**
- **A-UF5-VT01**: Diseño paisajístico integrado (especies nativas)
- **A-UF5-VT02**: Andenes peatonales 2.0 m + cicloruta 1.5 m
- **A-UF5-VT03**: Iluminación LED urbana (100% cobertura)
- **A-UF5-VT04**: Barreras acústicas (150 m zona residencial)
- **A-UF5-VT05**: Sistema drenaje urbano integrado

### **Plan Gestión Social Tropezón**
```
┌─────────────────────────────────────────────────────────────────┐
│              GESTIÓN SOCIAL TROPEZÓN                           │
├─────────────────────────────────────────────────────────────────┤
│ FASE 1: SOCIALIZACIÓN (3 meses)                               │
│ ├── Reuniones informativas: 8 sesiones                        │
│ ├── Talleres participativos: 4 talleres                       │
│ ├── Oficina información permanente                             │
│ └── Acuerdos comunitarios formalizados                        │
├─────────────────────────────────────────────────────────────────┤
│ FASE 2: COMPENSACIONES (6 meses)                              │
│ ├── Avalúos prediales: 15 predios afectados                   │
│ ├── Negociación directa: 12 casos                             │
│ ├── Expropiación: 3 casos (si necesario)                      │
│ └── Reubicación temporal: 5 familias                          │
├─────────────────────────────────────────────────────────────────┤
│ FASE 3: CONSTRUCCIÓN (12 meses)                               │
│ ├── Información semanal avances                               │
│ ├── Gestión quejas y reclamos                                 │
│ ├── Empleo local: 30% mano obra no calificada                │
│ └── Seguimiento post-construcción: 24 meses                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🌿 ARQUITECTURA VARIANTE LA PALMA

### **Diseño Ambiental Integrado**
```
┌─────────────────────────────────────────────────────────────────┐
│                    VARIANTE LA PALMA                           │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN BYPASS AMBIENTAL (1.8 km)                       │
│                                                                 │
│         LA PALMA ●──────────────────●                          │
│         CENTRO   │    VARIANTE      │                          │
│         POBLADO  │   AMBIENTAL      │                          │
│                  │  ┌─────────────┐ │                          │
│ ═════════════════●══│ VÍA PRINCIPAL │═●══════════════════      │
│                     │     UF5       │                          │
│                     └─────────────────┘                          │
│                       CORREDOR                                  │
│                      ECOLÓGICO                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│ ESPECIFICACIONES AMBIENTALES                                    │
│ ├── Longitud total: 1.8 km                                     │
│ ├── Velocidad diseño: 60 km/h                                  │
│ ├── Calzada: 7.00 m (integración ambiental)                   │
│ ├── Corredor ecológico: 50 m ancho                            │
│ └── Puentes fauna: 2 unidades (15 m ancho)                    │
├─────────────────────────────────────────────────────────────────┤
│ MEDIDAS AMBIENTALES                                             │
│ ├── Revegetalización: 5 hectáreas (especies nativas)          │
│ ├── Compensación forestal: 1:15 (área intervenida)            │
│ ├── Rescate fauna: Programa integral                           │
│ ├── Monitoreo ambiental: 5 años post-construcción             │
│ └── Educación ambiental: Programa comunitario                  │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Ecológica La Palma**
- **A-UF5-VP01**: Corredores biológicos (conectividad ecosistemas)
- **A-UF5-VP02**: Puentes fauna (2 unidades, 15 m ancho c/u)
- **A-UF5-VP03**: Sistema drenaje natural (bioretención)
- **A-UF5-VP04**: Revegetalización con especies nativas
- **A-UF5-VP05**: Monitoreo fauna automatizado (cámaras trampa)

---

## 🛤️ ARQUITECTURA INTERCAMBIO SAN ALBERTO SUR

### **Diseño Urbano Complejo**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTERCAMBIO SAN ALBERTO SUR                       │
├─────────────────────────────────────────────────────────────────┤
│ CONFIGURACIÓN: TROMPETA MODIFICADA URBANA                      │
│                                                                 │
│                    SAN ALBERTO CENTRO                          │
│                         │                                       │
│                    ┌────┴────┐                                 │
│                    │ ACCESO  │                                 │
│                    │ URBANO  │                                 │
│                    │  NORTE  │                                 │
│                    └────┬────┘                                 │
│                         │                                       │
│     ┌───────────────────┼───────────────────┐                 │
│     │    RAMPA          │         RAMPA     │                 │
│     │     SE            │          SO       │                 │
│     └───────────────────┼───────────────────┘                 │
│                         │                                       │
│ ════════════════════════════════════════════════════════════    │
│           AUTOPISTA PRINCIPAL UF5 (80 km/h)                    │
│ ════════════════════════════════════════════════════════════    │
│                         │                                       │
│                    ┌────┴────┐                                 │
│                    │ ACCESO  │                                 │
│                    │ URBANO  │                                 │
│                    │   SUR   │                                 │
│                    └─────────┘                                 │
│                                                                 │
│                  SAN ALBERTO PERIFERIA                         │
└─────────────────────────────────────────────────────────────────┘
```

### **Especificaciones Estructurales Urbanas**
- **A-UF5-I01**: Puente principal - Luz 30 m, ancho 14 m (incluye andenes)
- **A-UF5-I02**: Fundaciones - Pilotes 12 m (suelos urbanos)
- **A-UF5-I03**: 3 Rampas principales - Radio 80 m, pendiente 6%
- **A-UF5-I04**: Integración transporte público (2 paraderos)
- **A-UF5-I05**: Facilidades peatonales y ciclistas completas

### **Integración Urbana San Alberto**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTEGRACIÓN URBANA SAN ALBERTO                    │
├─────────────────────────────────────────────────────────────────┤
│ ACCESOS URBANOS CONTROLADOS                                     │
│ ├── Acceso Norte: Avenida Principal → Centro San Alberto       │
│ ├── Acceso Sur: Vía Perimetral → Zona Industrial              │
│ ├── Semáforos inteligentes: 6 intersecciones                  │
│ └── Carriles auxiliares urbanos: 120 m                        │
├─────────────────────────────────────────────────────────────────┤
│ FACILIDADES URBANAS INTEGRADAS                                 │
│ ├── Andenes peatonales: 2.5 m ancho (accesibilidad universal) │
│ ├── Cicloruta bidireccional: 2.0 m                            │
│ ├── Paraderos transporte público: 2 unidades (40 usuarios)    │
│ ├── Iluminación LED urbana: 100% cobertura                    │
│ └── Mobiliario urbano completo                                 │
├─────────────────────────────────────────────────────────────────┤
│ PAISAJISMO URBANO                                               │
│ ├── Zonas verdes: 3,500 m² (especies ornamentales)           │
│ ├── Plazoletas: 2 unidades (500 m² c/u)                      │
│ ├── Arborización urbana: 150 árboles                          │
│ ├── Jardines verticales: Muros contención                     │
│ └── Sistema riego automatizado                                 │
├─────────────────────────────────────────────────────────────────┤
│ COORDINACIÓN MUNICIPAL                                          │
│ ├── Integración POT San Alberto                                │
│ ├── Coordinación servicios públicos                           │
│ ├── Plan movilidad urbana                                      │
│ ├── Gestión tráfico urbano                                     │
│ └── Mantenimiento conjunto (5 años)                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💧 ARQUITECTURA SISTEMA DRENAJE MÚLTIPLE

### **Drenaje Integrado Tres Sistemas**
```
┌─────────────────────────────────────────────────────────────────┐
│              SISTEMA DRENAJE INTEGRADO UF5                     │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE VÍA PRINCIPAL (9.05 km)                               │
│ ├── Cunetas: Sección trapezoidal 0.8 m                        │
│ ├── Alcantarillas: 25 unidades Ø 0.90-1.50 m                 │
│ ├── Subdrenaje: Filtro francés 9.05 km                        │
│ └── Entregas: 12 puntos drenaje natural                       │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE VARIANTE TROPEZÓN                                       │
│ ├── Sistema urbano: Sumideros cada 50 m                       │
│ ├── Red colectora: Tubería concreto 300-600 mm                │
│ ├── Tratamiento: Trampa sedimentos                             │
│ └── Entrega: Sistema municipal Tropezón                        │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE VARIANTE LA PALMA                                       │
│ ├── Bioretención: Jardines infiltración                       │
│ ├── Cunetas verdes: Especies filtradoras                      │
│ ├── Humedales artificiales: 2 unidades                        │
│ └── Entrega: Quebrada La Palma (tratada)                      │
├─────────────────────────────────────────────────────────────────┤
│ DRENAJE INTERCAMBIO SAN ALBERTO                                 │
│ ├── Captación urbana: 20 sumideros                            │
│ ├── Red colectora: Tubería PVC 400-1000 mm                    │
│ ├── Cámaras inspección: 12 unidades                           │
│ ├── Planta tratamiento: 200 L/s                               │
│ └── Entrega: Río Sogamoso (tratada)                           │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Sostenible Drenaje**
- **A-UF5-D01**: Sistemas urbanos de drenaje sostenible (SUDS)
- **A-UF5-D02**: Reutilización aguas lluvias (riego paisajismo)
- **A-UF5-D03**: Monitoreo calidad agua (5 estaciones)
- **A-UF5-D04**: Integración con sistemas municipales
- **A-UF5-D05**: Plan gestión integral cuenca

---

## 🔧 ARQUITECTURA SISTEMAS TECNOLÓGICOS

### **Sistema Integrado ITS (Intelligent Transportation Systems)**
```
┌─────────────────────────────────────────────────────────────────┐
│                    SISTEMAS ITS UF5                           │
├─────────────────────────────────────────────────────────────────┤
│ MONITOREO Y CONTROL                                             │
│ ├── Cámaras CCTV: 15 puntos estratégicos                      │
│ ├── Detectores tráfico: 8 puntos (variantes + intercambio)    │
│ ├── VMS (Mensajes Variables): 6 unidades                      │
│ ├── Estación meteorológica: 1 unidad (La Palma)              │
│ └── Comunicación CCO: Fibra óptica + radio backup             │
├─────────────────────────────────────────────────────────────────┤
│ GESTIÓN TRÁFICO URBANO                                         │
│ ├── Semáforos inteligentes: 8 intersecciones                  │
│ ├── Sensores peatonales: 12 cruces                            │
│ ├── Información tiempo real: 4 paneles                        │
│ ├── App móvil: Información tráfico San Alberto                │
│ └── Integración transporte público                             │
├─────────────────────────────────────────────────────────────────┤
│ SEGURIDAD Y EMERGENCIAS                                         │
│ ├── Botones emergencia: 6 puntos (cada 1.5 km)              │
│ ├── Iluminación emergencia: LED + solar                       │
│ ├── Comunicación directa CCO                                   │
│ ├── GPS tracking vehículos emergencia                         │
│ └── Protocolos automatizados respuesta                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🔄 INTEGRACIÓN SISTEMAS Y COORDINACIÓN

### **Coordinación Construcción Múltiple**
```
┌─────────────────────────────────────────────────────────────────┐
│            COORDINACIÓN CONSTRUCCIÓN UF5                      │
├─────────────────────────────────────────────────────────────────┤
│ CRONOGRAMA INTEGRADO (18 meses)                               │
│ ├── Meses 1-3: Gestión social + predial                       │
│ ├── Meses 4-9: Construcción variantes (paralelo)              │
│ ├── Meses 6-15: Construcción vía principal                    │
│ ├── Meses 10-18: Construcción intercambio San Alberto         │
│ └── Meses 16-18: Integración y pruebas sistemas               │
├─────────────────────────────────────────────────────────────────┤
│ GESTIÓN TRÁFICO DURANTE CONSTRUCCIÓN                           │
│ ├── Desvíos temporales: 3 rutas alternativas                  │
│ ├── Señalización obras: Dinámica según avance                 │
│ ├── Horarios restringidos: Obras nocturnas zonas urbanas      │
│ ├── Coordinación municipal: Reuniones semanales               │
│ └── Información usuarios: Tiempo real + medios                │
├─────────────────────────────────────────────────────────────────┤
│ CONTROL CALIDAD INTEGRADO                                       │
│ ├── Laboratorio móvil: Ensayos in-situ                        │
│ ├── Topografía: Control permanente 3 elementos                │
│ ├── Supervisión ambiental: Diaria variante La Palma           │
│ ├── Supervisión social: Semanal variante Tropezón             │
│ └── Integración sistemas: Pruebas progresivas                 │
└─────────────────────────────────────────────────────────────────┘
```

### **Integración con Sistemas Transversales**
- **I-UF5-01**: Conexión CCO Morrison (fibra óptica dedicada)
- **I-UF5-02**: Coordinación con UF4 (empalme PK70+760)
- **I-UF5-03**: Integración red urbana San Alberto
- **I-UF5-04**: Coordinación autoridades municipales (2 municipios)
- **I-UF5-05**: Gestión ambiental integrada (La Palma crítica)

---

## 📊 INDICADORES ARQUITECTURA UF5

### **Capacidad y Desempeño**
- **Vía principal**: 1,500 veh/h/carril (Nivel Servicio C)
- **Variante Tropezón**: 800 veh/h (bypass efectivo)
- **Variante La Palma**: 600 veh/h (prioridad ambiental)
- **Intercambio San Alberto**: 600 veh/h por rampa

### **Sostenibilidad y Ambiente**
- **Compensación forestal**: 1:15 (75 hectáreas)
- **Rescate fauna**: 100% especies identificadas
- **Tratamiento aguas**: 100% antes entrega natural
- **Empleo local**: 30% mano obra no calificada

---

## ✅ CRITERIOS VALIDACIÓN ARQUITECTURA UF5

### **Técnicos**
- ✅ Integración perfecta 3 elementos (vía + 2 variantes + intercambio)
- ✅ Variantes operativas como bypass efectivos
- ✅ Intercambio San Alberto integrado con red urbana
- ✅ Sistemas ITS funcionando según especificaciones

### **Sociales y Ambientales**
- ✅ Aprobación comunidades Tropezón y La Palma
- ✅ Compensaciones sociales y ambientales ejecutadas
- ✅ Variante La Palma sin impacto ecosistema crítico
- ✅ Integración urbana San Alberto exitosa

### **Operacionales**
- ✅ Construcción coordinada sin conflictos
- ✅ Gestión tráfico efectiva durante construcción
- ✅ Nivel servicio vial ≥ C post construcción
- ✅ Mantenimiento integrado con municipios

---

## 🎯 PRÓXIMOS PASOS UF5

### **Validación Crítica**
- [ ] Aprobación comunidades variantes (crítico)
- [ ] Validación diseños intercambio con San Alberto
- [ ] Estudios ambientales detallados La Palma
- [ ] Plan gestión construcción múltiple

### **Implementación Compleja**
- [ ] Gestión social intensiva (6 meses)
- [ ] Licitación construcción por paquetes especializados
- [ ] Coordinación municipal formalizada
- [ ] Monitoreo ambiental continuo

---
**Próximo paso**: T03 - Arquitectura UF restantes (UF0, UF1, UF2, UF4)