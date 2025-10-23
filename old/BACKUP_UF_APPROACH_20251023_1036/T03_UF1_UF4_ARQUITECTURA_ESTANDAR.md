# T03 - ARQUITECTURA ESTÁNDAR UF1 Y UF4

## 📊 INFORMACIÓN GENERAL
- **Proyecto**: SABANA DE TORRES - CURUMANÍ
- **Códigos**: STC-APP4G-UF1-T03 / STC-APP4G-UF4-T03
- **Fecha**: 2024-10-23
- **Responsable**: [ASIGNAR]
- **Tipo**: Construcción nueva estándar con elementos especiales

## 🎯 OBJETIVO DEL ANÁLISIS
Definir arquitectura para UF1 (20.55 km + Puente Río Sogamoso) y UF4 (12.57 km + integración UF3-UF5), optimizando recursos por similitud técnica.

---

## 🛣️ UF1: ARQUITECTURA RÍO SOGAMOSO - LAS PAMPAS

### **Sistema Vial Principal - 20.55 KM**
```
┌─────────────────────────────────────────────────────────────────┐
│                    UF1 - VÍA NUEVA 20.55 KM                   │
├─────────────────────────────────────────────────────────────────┤
│ SECCIÓN TÍPICA ESTÁNDAR                                        │
│ ├── Calzada: 7.30 m (2 carriles × 3.65 m)                     │
│ ├── Bermas: 1.80 m cada lado                                   │
│ ├── Velocidad diseño: 80 km/h                                  │
│ └── Estructura pavimento: Nueva completa                       │
├─────────────────────────────────────────────────────────────────┤
│ SEGMENTACIÓN CONSTRUCTIVA                                       │
│ ├── Tramo A (0-9.8 km): Acceso + Puente Río Sogamoso         │
│ ├── Tramo B (9.8-20.55 km): Construcción estándar            │
│ └── Coordinación UF0: Gestión tráfico durante construcción    │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Puente Río Sogamoso (Elemento Crítico)**
```
┌─────────────────────────────────────────────────────────────────┐
│              PUENTE RÍO SOGAMOSO (PK09+800)                   │
├─────────────────────────────────────────────────────────────────┤
│ ESPECIFICACIONES ESTRUCTURALES                                  │
│ ├── Luz principal: 60 m (navegación fluvial)                  │
│ ├── Ancho total: 12 m (calzada + bermas + andenes)           │
│ ├── Gálibo vertical: 8.0 m (nivel máximo + seguridad)        │
│ ├── Vida útil: 100 años                                       │
│ └── Carga: HL-93 + sobrecarga peatonal                       │
├─────────────────────────────────────────────────────────────────┤
│ ARQUITECTURA ESTRUCTURAL                                        │
│ ├── Tipo: Vigas pretensadas + losa                            │
│ ├── Fundaciones: Pilotes 20 m (roca)                          │
│ ├── Pilas: 2 unidades en río                                  │
│ ├── Estribos: Muros contención + aletas                       │
│ └── Protección: Enrocado + gaviones                           │
├─────────────────────────────────────────────────────────────────┤
│ CONSIDERACIONES AMBIENTALES                                     │
│ ├── Licencia específica: Cruce cuerpo agua                    │
│ ├── Época construcción: Verano (caudales mínimos)             │
│ ├── Protección fauna: Paso peces + monitoreo                  │
│ ├── Calidad agua: Monitoreo durante construcción              │
│ └── Compensación: Restauración riberas                        │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Coordinación UF0**
- **A-UF1-C01**: Desvíos temporales por UF0 durante construcción
- **A-UF1-C02**: Señalización dinámica coordinada con CCO
- **A-UF1-C03**: Mantenimiento intensivo rutas alternativas UF0
- **A-UF1-C04**: Información usuarios tiempo real
- **A-UF1-C05**: Empalme perfecto UF1 → UF2 (PK30+000)

---

## 🛣️ UF4: ARQUITECTURA SABANA DE TORRES - TROPEZÓN

### **Sistema Vial Principal - 12.57 KM**
```
┌─────────────────────────────────────────────────────────────────┐
│                    UF4 - VÍA NUEVA 12.57 KM                   │
├─────────────────────────────────────────────────────────────────┤
│ SECCIÓN TÍPICA ESTÁNDAR                                        │
│ ├── Calzada: 7.30 m (2 carriles × 3.65 m)                     │
│ ├── Bermas: 1.80 m cada lado                                   │
│ ├── Velocidad diseño: 80 km/h                                  │
│ └── Estructura pavimento: Nueva completa                       │
├─────────────────────────────────────────────────────────────────┤
│ SEGMENTACIÓN FUNCIONAL                                          │
│ ├── Tramo A (0-4 km): Empalme UF3 + acceso Sabana Torres     │
│ ├── Tramo B (4-8 km): Construcción estándar                   │
│ ├── Tramo C (8-12.57 km): Acceso Tropezón + empalme UF5      │
│ └── Integración: Conexión crítica UF3 ↔ UF5                  │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Integración Municipal**
```
┌─────────────────────────────────────────────────────────────────┐
│              INTEGRACIÓN MUNICIPAL UF4                        │
├─────────────────────────────────────────────────────────────────┤
│ ACCESO SABANA DE TORRES                                        │
│ ├── Intersección: Glorieta R=30m                              │
│ ├── Carriles auxiliares: 100 m aceleración/desaceleración     │
│ ├── Señalización urbana: Específica municipio                 │
│ ├── Iluminación: LED integrada con red municipal              │
│ └── Coordinación: Alcaldía + servicios públicos               │
├─────────────────────────────────────────────────────────────────┤
│ ACCESO TROPEZÓN                                                │
│ ├── Intersección: Semaforizada (coordinación UF5)             │
│ ├── Carriles auxiliares: 80 m                                 │
│ ├── Integración: Con variante Tropezón UF5                    │
│ ├── Facilidades: Peatonales y ciclistas                       │
│ └── Coordinación: Con construcción UF5                        │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Coordinación UF3-UF5**
- **A-UF4-I01**: Empalme perfecto UF3 → UF4 (PK58+200)
- **A-UF4-I02**: Empalme perfecto UF4 → UF5 (PK70+760)
- **A-UF4-I03**: Cronograma sincronizado (UF3 → UF4 → UF5)
- **A-UF4-I04**: Gestión tráfico coordinada (3 UF simultáneas)
- **A-UF4-I05**: Recursos compartidos (materiales + equipos)

---

## 🔧 ARQUITECTURA SISTEMAS COMUNES UF1 Y UF4

### **Sistema Drenaje Estándar**
```
┌─────────────────────────────────────────────────────────────────┐
│              DRENAJE ESTÁNDAR UF1 Y UF4                       │
├─────────────────────────────────────────────────────────────────┤
│ UF1 - DRENAJE (20.55 km)          │ UF4 - DRENAJE (12.57 km)   │
│ ├── Cunetas: 41.1 km              │ ├── Cunetas: 25.14 km      │
│ ├── Alcantarillas: 45 unidades    │ ├── Alcantarillas: 28 unid │
│ ├── Subdrenaje: 20.55 km          │ ├── Subdrenaje: 12.57 km   │
│ └── Entregas: 18 puntos           │ └── Entregas: 12 puntos    │
├─────────────────────────────────────────────────────────────────┤
│ ESPECIFICACIONES COMUNES                                        │
│ ├── Período retorno: 25 años (menor) / 100 años (mayor)       │
│ ├── Cunetas: Sección triangular 0.8 m                         │
│ ├── Alcantarillas: Ø 0.90-1.50 m según caudal                │
│ ├── Subdrenaje: Filtro francés k≥1x10⁻³ m/s                  │
│ └── Materiales: Vida útil ≥ 50 años                           │
└─────────────────────────────────────────────────────────────────┘
```

### **Sistema Geotécnico Estándar**
- **Compactación**: ≥ 95% Proctor Modificado (ambas UF)
- **CBR subrasante**: ≥ 10% (mejorado si necesario)
- **Factor seguridad taludes**: ≥ 1.5 estático / ≥ 1.1 sísmico
- **Asentamientos**: ≤ 2.5 cm estructuras / ≤ 5.0 cm pavimentos
- **Control calidad**: Ensayos cada 500 m

### **Sistema Ambiental Estándar**
- **Compensación forestal**: 1:10 (área intervenida)
- **Rescate fauna**: Programa integral
- **Control ruido**: <70 dB día / <60 dB noche
- **Manejo residuos**: Según normativa
- **Monitoreo**: Durante construcción + 2 años post

---

## 📊 ARQUITECTURA CONSTRUCCIÓN OPTIMIZADA

### **Cronograma Integrado UF1 y UF4**
```
┌─────────────────────────────────────────────────────────────────┐
│              CRONOGRAMA OPTIMIZADO                             │
├─────────────────────────────────────────────────────────────────┤
│ UF1 (20.55 km + Puente)           │ UF4 (12.57 km)             │
│ ├── Meses 1-3: Puente Río Sogamoso│ ├── Meses 7-9: Preparación │
│ ├── Meses 4-10: Vía principal     │ ├── Meses 10-16: Construcción│
│ ├── Meses 11-12: Acabados         │ ├── Meses 17-18: Acabados  │
│ └── Total: 12 meses                │ └── Total: 12 meses        │
├─────────────────────────────────────────────────────────────────┤
│ OPTIMIZACIÓN RECURSOS                                           │
│ ├── Equipos: Transferencia UF1 → UF4 (mes 13)                │
│ ├── Personal: Continuidad equipos especializados               │
│ ├── Materiales: Compras consolidadas                           │
│ ├── Laboratorio: Móvil compartido                              │
│ └── Supervisión: Equipo integrado                              │
└─────────────────────────────────────────────────────────────────┘
```

### **Arquitectura Control Calidad Unificado**
- **Laboratorio móvil**: Compartido UF1 y UF4
- **Especificaciones**: Idénticas (optimización)
- **Proveedores**: Calificados para ambas UF
- **Supervisión**: Equipo técnico integrado
- **Reportes**: Sistema unificado

---

## 🔄 INTEGRACIÓN CON SISTEMAS TRANSVERSALES

### **Conexiones CCO Morrison**
- **UF1**: Fibra óptica + radio backup
- **UF4**: Fibra óptica + radio backup
- **Monitoreo**: 8 cámaras UF1 + 6 cámaras UF4
- **Comunicaciones**: VHF + celular
- **Emergencias**: Protocolos estándar

### **Coordinación Operacional**
```
┌─────────────────────────────────────────────────────────────────┐
│              COORDINACIÓN OPERACIONAL                          │
├─────────────────────────────────────────────────────────────────┤
│ UF1 ↔ UF0                         │ UF4 ↔ UF3 ↔ UF5             │
│ ├── Gestión tráfico durante obra  │ ├── Secuencia constructiva │
│ ├── Desvíos por UF0               │ ├── Empalmes perfectos      │
│ ├── Mantenimiento intensivo UF0   │ ├── Cronograma sincronizado │
│ └── Información usuarios          │ └── Recursos compartidos    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 INDICADORES ARQUITECTURA UF1 Y UF4

### **Capacidad y Desempeño**
- **UF1**: 1,500 veh/h/carril (Nivel Servicio C)
- **UF4**: 1,500 veh/h/carril (Nivel Servicio C)
- **Puente Río Sogamoso**: 2,000 veh/h (sin restricciones)
- **Disponibilidad**: 95% durante construcción otras UF

### **Eficiencia Constructiva**
- **Optimización recursos**: 20% vs construcción independiente
- **Tiempo total**: 18 meses (vs 24 meses independiente)
- **Calidad**: Estándares unificados
- **Costos**: Economías escala materiales y equipos

---

## ✅ CRITERIOS VALIDACIÓN ARQUITECTURA UF1 Y UF4

### **Técnicos**
- ✅ Puente Río Sogamoso según especificaciones estructurales
- ✅ Vías nuevas cumpliendo estándares INVIAS
- ✅ Integración perfecta con UF adyacentes
- ✅ Sistemas auxiliares funcionando según diseño

### **Operacionales**
- ✅ Construcción sin afectar operación UF0
- ✅ Secuencia constructiva UF3→UF4→UF5 coordinada
- ✅ Nivel servicio mantenido durante construcción
- ✅ Empalmes perfectos con UF adyacentes

### **Contractuales**
- ✅ Cronograma integrado cumplido
- ✅ Presupuesto optimizado por economías escala
- ✅ Calidad según estándares contractuales
- ✅ Especificaciones técnicas unificadas

---

## 🎯 PRÓXIMOS PASOS UF1 Y UF4

### **UF1 - Críticos**
- [ ] Diseño detallado Puente Río Sogamoso
- [ ] Licencia ambiental específica cruce río
- [ ] Plan gestión tráfico coordinado con UF0
- [ ] Estudios geotécnicos fundaciones puente

### **UF4 - Críticos**
- [ ] Coordinación cronograma con UF3 y UF5
- [ ] Acuerdos municipales Sabana Torres y Tropezón
- [ ] Optimización recursos compartidos
- [ ] Integración con variante Tropezón UF5

### **Ambas UF - Implementación**
- [ ] Licitación construcción integrada
- [ ] Especificaciones técnicas unificadas
- [ ] Sistema control calidad compartido
- [ ] Supervisión técnica integrada

---
**Próximo paso**: Consolidación final T03 - Resumen arquitectura completa