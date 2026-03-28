# MEP Standards Quick Reference

## Việt Nam Standards (TCVN / QCVN)

| Mã | Tên | Áp dụng |
|----|-----|---------|
| TCVN 5687:2010 | Thông gió ĐHKK - Tiêu chuẩn thiết kế | Outdoor conditions, indoor requirements |
| TCVN 2622:1995 | PCCC cho nhà và công trình | Hydrant flow, duration, fire risk |
| TCVN 7336:2021 | PCCC - Sprinkler tự động | Density, design area, K-factor, hazard groups |
| QCVN 06:2022/BXD | An toàn cháy cho nhà và công trình | Building classification, fire resistance |
| QCVN 02:2020/BCA | Điều kiện PCCC phương tiện cơ giới | Fire pump requirements |
| QCVN 22:2016/BYT | Chiếu sáng - Mức chiếu sáng tối thiểu | Lux requirements by room type |
| TCVN 6151 | Ống nhựa PVC | Drainage pipe standards |
| TCVN 7447 | Hệ thống lắp đặt điện hạ áp | Electrical installation rules |

## International Standards

| Mã | Tên | Áp dụng |
|----|-----|---------|
| ASHRAE 62.1 | Ventilation for Acceptable IAQ | Outdoor air flow rate calculation |
| ASHRAE 90.1 | Energy Standard for Buildings | Energy efficiency requirements |
| FM Global DS 2-0 | Installation of Sprinklers | FM approved sprinkler design (IBC areas) |
| NFPA 13 | Sprinkler Systems | Reference for sprinkler layout |
| NFPA 20 | Fire Pumps | Pump selection and testing |
| IEC 60364 | Low-voltage Installations | Electrical design standard |
| ASPE Vol.2-2010 | Plumbing Engineering Design | WSFU/DFU fixture calculations |
| BS 8519 | Fire Alarm Systems | Alarm system design |

## Typical Design Parameters (Vietnam - Southern Climate)

### Outdoor Design Conditions
| Parameter | Value | Ref |
|-----------|-------|-----|
| Dry-bulb (Summer) | 35.4°C | ASHRAE/TCVN |
| Wet-bulb (Summer) | 28.5°C | |
| Relative Humidity | 78.85% | |

### Indoor Design Conditions
| Area | Temp (°C) | RH (%) | Ref |
|------|-----------|--------|-----|
| Office | 24±1 | 55±5 | ASHRAE 55 |
| Production | 28-30 | ≤70 | Client requirement |
| Server/Elec room | 22±1 | 40-55 | Equipment spec |
| Warehouse | Natural vent | - | - |

### Lighting Levels (QCVN 22:2016)
| Area | Lux | Fixture Type |
|------|-----|-------------|
| Office | 500 | LED Panel 40W |
| Production | 300 | LED High-bay 150W |
| Warehouse | 200 | LED High-bay 100W |
| Corridor | 100 | LED Downlight 15W |
| Parking | 50 | LED Flood 100W |
| WC | 150 | LED Panel 40W |
| Pump room | 200 | LED Tube 36W |

### Fire Fighting (Sprinkler)
| Hazard Group | Density (l/s/m²) | Design Area (m²) | Duration (min) |
|--------------|------------------|-------------------|----------------|
| Light Hazard (LH) | 0.10 | 84 | 30 |
| OH-1 | 0.22 | 160 | 60 |
| OH-2 | 0.44 | 90 | 60 |
| TB-1 (TCVN) | 0.22 | 160 | 60 |
| TB-2 (TCVN) | 0.44 | 260 | 60 |
| Extra Hazard (EH) | 0.50+ | 260+ | 90 |

### Piping Materials (Common Vietnam Project)
| System | Indoor | Underground | Outdoor |
|--------|--------|-------------|---------|
| Water Supply | PPR PN10 | HDPE PN10 | HDPE PN10 |
| Hot Water | PPR PN20 | - | - |
| Drainage | PVC Class II | PVC Class III | HDPE |
| Fire (Indoor) | BSP SCH40 | HDPE | HDPE |
| Fire (Sprinkler) | GIP SCH40 | - | - |
| Chilled Water | BSP SCH40 w/insulation | - | - |

### Electrical (Typical Vietnam Factory)
| Parameter | Value |
|-----------|-------|
| MV Supply | 22kV |
| LV Distribution | 400/230V, 50Hz, 3P+N+E |
| Transformer | Oil immersed 500-1000kVA |
| Cable | Cu/XLPE/PVC (IEC 60502) |
| Max Voltage Drop | Main: 5%, Branch: 3% |
| Power Factor | ≥0.9 (with capacitor bank) |
| Emergency | Diesel Generator 100-500kVA |
