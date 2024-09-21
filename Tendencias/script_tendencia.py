import matplotlib.pyplot as plt
import pandas as pd

# Función para generar gráficos de líneas
def generar_grafico(data, titulo, xlabel, ylabel, columnas):
    df = pd.DataFrame(data)
    df.plot(x='Año', y=columnas, marker='o')
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

# Datos para las 10 tendencias en formato de diccionarios
# 1. Microservicios
data_microservicios = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Adopción en empresas medianas (%)": [35, 45, 55, 60, 70],
    "Adopción en empresas grandes (%)": [40, 50, 65, 70, 80],
    "Tiempo de implementación promedio (meses)": [9, 8, 7, 6, 5],
    "Costo de implementación promedio (USD)": [120000, 115000, 110000, 105000, 100000]
}

# 2. Diseño basado en eventos
data_eventos = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Adopción global (%)": [25, 30, 35, 40, 50],
    "Eventos manejados por segundo (media)": [1000, 1200, 1500, 1800, 2000],
    "Reducción de tiempo de respuesta (%)": [10, 12, 15, 18, 20],
    "Aumento de rendimiento (%)": [5, 8, 10, 12, 15]
}

# 3. Serverless
data_serverless = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Porcentaje de adopción en aplicaciones nuevas (%)": [20, 25, 35, 40, 50],
    "Costos operativos reducidos (%)": [15, 20, 25, 30, 35],
    "Tiempo de respuesta medio (ms)": [500, 450, 400, 350, 300],
    "Escalabilidad dinámica (%)": [50, 55, 60, 65, 70]
}

# 4. CQRS
data_cqrs = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Adopción global (%)": [10, 15, 20, 25, 30],
    "Escalabilidad mejorada (%)": [20, 25, 30, 35, 40],
    "Reducción de latencia (%)": [5, 7, 10, 12, 15],
    "Complejidad de implementación (escala 1-10)": [7, 6, 5, 4, 3]
}

# 5. API Gateway
data_api_gateway = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Porcentaje de uso en aplicaciones distribuidas (%)": [30, 35, 45, 50, 60],
    "Tiempo de respuesta mejorado (%)": [8, 10, 12, 15, 18],
    "Latencia promedio reducida (ms)": [400, 350, 300, 250, 200],
    "Seguridad incrementada (%)": [5, 8, 10, 12, 15]
}

# 6. PWA
data_pwa = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Adopción en mercados emergentes (%)": [10, 20, 30, 40, 50],
    "Adopción en mercados desarrollados (%)": [15, 25, 35, 45, 55],
    "Usuarios recurrentes (%)": [30, 35, 40, 45, 50],
    "Aumento de tráfico móvil (%)": [5, 10, 15, 20, 25]
}

# 7. Arquitectura Hexagonal
data_hexagonal = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Porcentaje de adopción (%)": [5, 10, 15, 20, 25],
    "Tiempo de desarrollo reducido (semanas)": [2, 3, 4, 5, 6],
    "Flexibilidad de integración (%)": [10, 15, 20, 25, 30],
    "Reducción de acoplamiento (%)": [15, 20, 25, 30, 35]
}

# 8. BFF
data_bff = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Porcentaje de adopción en aplicaciones móviles (%)": [20, 30, 40, 50, 60],
    "Tasa de satisfacción del usuario final (%)": [70, 75, 80, 85, 90],
    "Reducción de complejidad frontend (%)": [10, 15, 20, 25, 30],
    "Tiempo de respuesta reducido (ms)": [300, 280, 260, 240, 220]
}

# 9. Tolerancia a fallos
data_fallos = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Porcentaje de adopción (%)": [15, 20, 25, 30, 35],
    "Reducción de caídas del sistema (%)": [10, 15, 20, 25, 30],
    "Mejoramiento en la recuperación (%)": [5, 10, 15, 20, 25],
    "Aumento de fiabilidad (%)": [20, 25, 30, 35, 40]
}

# 10. Pipeline de implementación continua
data_pipeline = {
    "Año": [2018, 2019, 2020, 2021, 2022],
    "Porcentaje de adopción en grandes empresas (%)": [40, 50, 60, 70, 80],
    "Tiempo de entrega reducido (%)": [10, 15, 20, 25, 30],
    "Errores de integración reducidos (%)": [5, 10, 15, 20, 25],
    "Productividad incrementada (%)": [15, 20, 25, 30, 35]
}

# Generación de gráficos para cada tendencia
generar_grafico(data_microservicios, 'Adopción de Microservicios', 'Año', 'Porcentaje', ['Adopción en empresas medianas (%)', 'Adopción en empresas grandes (%)'])
generar_grafico(data_eventos, 'Diseño basado en eventos', 'Año', 'Métricas', ['Adopción global (%)', 'Reducción de tiempo de respuesta (%)'])
generar_grafico(data_serverless, 'Adopción de Serverless', 'Año', 'Métricas', ['Porcentaje de adopción en aplicaciones nuevas (%)', 'Costos operativos reducidos (%)'])
generar_grafico(data_cqrs, 'Adopción de CQRS', 'Año', 'Porcentaje', ['Adopción global (%)', 'Escalabilidad mejorada (%)'])
generar_grafico(data_api_gateway, 'Uso de API Gateway', 'Año', 'Porcentaje', ['Porcentaje de uso en aplicaciones distribuidas (%)', 'Seguridad incrementada (%)'])
generar_grafico(data_pwa, 'Adopción de PWA', 'Año', 'Porcentaje', ['Adopción en mercados emergentes (%)', 'Adopción en mercados desarrollados (%)'])
generar_grafico(data_hexagonal, 'Arquitectura Hexagonal', 'Año', 'Métricas', ['Porcentaje de adopción (%)', 'Reducción de acoplamiento (%)'])
generar_grafico(data_bff, 'BFF (Backend for Frontend)', 'Año', 'Porcentaje', ['Porcentaje de adopción en aplicaciones móviles (%)', 'Tasa de satisfacción del usuario final (%)'])
generar_grafico(data_fallos, 'Tolerancia a Fallos', 'Año', 'Porcentaje', ['Porcentaje de adopción (%)', 'Aumento de fiabilidad (%)'])
generar_grafico(data_pipeline, 'Pipeline de Implementación Continua', 'Año', 'Porcentaje', ['Porcentaje de adopción en grandes empresas (%)', 'Productividad incrementada (%)'])
