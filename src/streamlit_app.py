import streamlit as st
import pandas as pd
from estimation import execute_regressions, generate_data
from plots import *

# Generar y ejecutar regresiones
data = generate_data()
results, results_data = execute_regressions(data)

st.set_page_config(page_title="Peru Minimum Temperature", layout="wide")

tab1, tab2, tab3 = st.tabs(["Descripcion", "Análisis y Visualización", "Politicas Publicas"])

# --- TAB 1 ---
with tab1:

    st.markdown(
    """
    # 🌡️ Análisis de Riesgo de Heladas y Friajes en el Perú

    El presente análisis busca identificar las zonas del país con mayor y menor riesgo de heladas a partir de la temperatura mínima promedio (Tmin), con el objetivo de orientar políticas públicas focalizadas en la reducción de impactos en salud, educación y producción agropecuaria.

    Se emplearon datos de Tmin promedio (°C) para los distritos del país, complementados con estadísticas descriptivas y la identificación de los 15 distritos más fríos y más cálidos.
    """
    )

    # --- NUEVO BLOQUE: Imagen + Tabla CSV ---
    st.write("---")
    st.markdown("## 🌍 1. Mapa de Temperaturas a nivel Nacional")

    # Alinear ambos elementos al mismo nivel visual
    col_img, col_table = st.columns([1, 2], vertical_alignment="top")

    with col_img:
        st.image("assets/tmin_dep.png", caption="Temperatura mínima promedio por distrito", use_container_width=True)

    with col_table:
        # Cargar CSV
        df = pd.read_csv("assets/3_3_tabla_completa_riesgo_heladas.csv")

        # Filtro por departamento
        departamentos = df["DEPARTAMEN"].unique()
        selected_dep = st.selectbox("Selecciona un departamento:", options=["Todos"] + sorted(departamentos.tolist()))

        # Aplicar filtro
        if selected_dep != "Todos":
            df_filtered = df[df["DEPARTAMEN"] == selected_dep]
        else:
            df_filtered = df

        # Mostrar tabla sin índice
        st.dataframe(df_filtered, use_container_width=True, hide_index=True)

        # Botón para descargar dataset filtrado
        csv = df_filtered.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Descargar dataset filtrado",
            data=csv,
            file_name=f"riesgo_heladas_{selected_dep if selected_dep != 'Todos' else 'general'}.csv",
            mime="text/csv",
        )

    # --- Sección de regresión previa ---
        # --- NUEVO BLOQUE: Estadísticas descriptivas ---
    st.write("---")
    st.markdown("## 📊 2. Estadísticas Descriptivas")

    st.markdown(
        """
        El análisis de las temperaturas mínimas promedio a nivel nacional muestra una alta variabilidad térmica. 
        Los indicadores siguientes resumen esta distribución climática:
        """
    )

    # Filas de métricas (puedes ajustar los grupos según tu preferencia)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Media", value="9.49 °C")
        st.metric(label="Mediana", value="8.52 °C")
        st.metric(label="Desv. Estándar", value="6.87 °C")
    with col2:
        st.metric(label="Mínimo", value="-5.19 °C")
        st.metric(label="Máximo", value="23.01 °C")
        st.metric(label="Rango", value="28.20 °C")
    with col3:
        st.metric(label="Percentil 10", value="1.15 °C")
        st.metric(label="Percentil 90", value="19.61 °C")

    st.markdown(
        """
        **Interpretación:**  
        El amplio rango térmico (≈28.2 °C) muestra una marcada heterogeneidad climática en el país, con zonas de heladas extremas (por debajo de 0 °C) 
        y regiones amazónicas con temperaturas superiores a 22 °C.  
        El *percentil 10* (≈1.15 °C) permite definir los distritos en condición de **alto riesgo de heladas**, mientras que el *percentil 90* (≈19.6 °C) 
        identifica zonas de **bajo riesgo o friajes amazónicos**.
        """
    )



# --- TAB 2 ---
with tab2:

    st.markdown(
    """
    # 📊 Análisis y Visualización sobre el Riesgo de Heladas y Friajes en el Perú

    Este análisis identifica las zonas del país con **mayor y menor riesgo de heladas**, a partir de la **temperatura mínima promedio (Tmin)** registrada en los distritos del Perú.  
    El objetivo es **apoyar la toma de decisiones y la formulación de políticas públicas** orientadas a reducir los impactos negativos de las bajas temperaturas en sectores como la salud, la educación y la producción agropecuaria.

    Los resultados incluyen estadísticas descriptivas y la identificación de los **15 distritos más fríos** (mayor riesgo) y los **15 distritos más cálidos** (menor riesgo).
    """
    )

    # --- BLOQUE 1: Top 15 con mayor riesgo ---
    st.write("---")
    st.markdown("## ❄️ 1. TOP 15 DISTRITOS CON MAYOR RIESGO DE HELADAS")

    # Alinear imagen y tabla
    col_img, col_table = st.columns([1, 2], vertical_alignment="top")

    with col_img:
        st.image("assets/3_3_top15_alto_riesgo.png", 
                 caption="Temperatura mínima promedio por distrito (mayor riesgo de heladas)", 
                 use_container_width=True)

    with col_table:
        # Cargar CSV
        df_alto = pd.read_csv("assets/3_3_top15_alto_riesgo.csv")

        # Mostrar tabla sin índice
        st.dataframe(df_alto, use_container_width=True, hide_index=True)

    # --- BLOQUE 2: Top 15 con menor riesgo ---
    st.write("---")
    st.markdown("## 🌞 2. TOP 15 DISTRITOS CON MENOR RIESGO DE HELADAS")

    # Alinear imagen y tabla
    col_img, col_table = st.columns([1, 2], vertical_alignment="top")

    with col_img:
        st.image("assets/3_3_top15_bajo_riesgo.png", 
                 caption="Temperatura mínima promedio por distrito (menor riesgo de heladas)", 
                 use_container_width=True)

    with col_table:
        # Cargar CSV
        df_bajo = pd.read_csv("assets/3_3_top15_bajo_riesgo.csv")

        # Mostrar tabla sin índice
        st.dataframe(df_bajo, use_container_width=True, hide_index=True)

# --- TAB 3 ---
with tab3:
    st.markdown("""
        # Propuestas de Política Pública ante el Frío Extremo

        Considerando el diagnóstico de distritos con menor temperatura promedio, se proponen las siguientes **tres intervenciones estratégicas** enfocadas en las localidades de la sierra sur y altiplano del país.

        ---

        ## 🌡️ Política 1: Programa de Viviendas Térmicas Rurales (ISUR Ampliado)

        **Objetivo:**  
        Reducir en un **30% los casos de infecciones respiratorias agudas (IRA)** en población infantil de zonas altoandinas con temperaturas promedio menores a 0 °C.

        **Territorio y población objetivo:**  
        Distritos rurales de **Puno, Arequipa, Cusco, Tacna, Moquegua y Huancavelica**, identificados como los más fríos (temperatura anual promedio por debajo de los 0 °C).  
        **Población meta:** 50 000 hogares rurales en zonas por encima de los 3 800 m.s.n.m.

        **Intervención:**  
        - Implementación de **viviendas térmicamente mejoradas** (paredes aislantes, techos dobles, sistemas pasivos de calefacción solar).  
        - Complementario al programa *Mi Abrigo* (FONCODES), pero con criterios **geoespaciales basados en análisis raster**.  

        **Costo estimado:**  
        S/ 8 000 por vivienda.  
        Meta: 50 000 hogares.  
        **Costo total:** S/ 400 millones.

        **Indicadores (KPI):**  
        1. ↓ 30% casos de IRA en población infantil durante la temporada de friaje (Fuente: ESSALUD/MINSA).  
        2. ↑ 20% confort térmico reportado por hogares (Fuente: SISFOH).  
        3. ↑ 15% asistencia escolar en invierno (Fuente: MINEDU).

        ---

        ## 🐑 Política 2: Fondo de Adaptación Agropecuaria al Friaje

        **Objetivo:**  
        Reducir en **25% las pérdidas agrícolas y ganaderas** en distritos de la sierra sur expuestos a heladas recurrentes.

        **Territorio y población objetivo:**  
        Distritos agrícolas de **Puno, Cusco y Arequipa** con temperatura promedio ≤ 0 °C (aprox. 105 distritos).  
        **Población meta:** 30 000 productores agropecuarios familiares.

        **Intervención:**  
        - Entrega de **kits antiheladas agrícolas y ganaderos** (mantas térmicas, riego nocturno).  
        - **Capacitación** en calendarios agrícolas adaptativos.  
        - **Construcción de refugios ganaderos** para alpacas y ovinos.

        **Costo estimado:**  
        S/ 8 000 por productor.  
        Meta: 30 000 productores.  
        **Costo total:** S/ 240 millones.

        **Indicadores (KPI):**  
        1. ↓ 25% pérdidas reportadas en cultivos andinos (Fuente: MIDAGRI).  
        2. ↓ 15% mortalidad de alpacas y ovinos durante heladas (Fuente: SENASA).  
        3. 80% de agricultores capacitados adoptan prácticas adaptadas al clima (Fuente: MIDAGRI).

        ---

        ## 🏫 Política 3: Escuelas Seguras ante Friaje

        **Objetivo:**  
        Reducir en **40% el ausentismo escolar** por eventos de friaje en zonas altoandinas con temperaturas promedio menores a 0 °C.

        **Territorio y población objetivo:**  
        Distritos rurales en **Puno, Arequipa, Cusco, Tacna, Moquegua y Huancavelica**, identificados como los más fríos (Tmin < 0 °C).  
        **Población meta:** 20 000 estudiantes y 250 escuelas rurales.

        **Intervención:**  
        - Implementación de **protocolos escolares de abrigo y refugio térmico**.  
        - Entrega de **kits de calefacción solar y ropa térmica** a escolares.  
        - **Acondicionamiento térmico** de aulas (paredes aislantes, techos dobles, calefacción solar pasiva).

        **Costo estimado:**  
        S/ 30 000 por escuela.  
        Meta: 250 escuelas.  
        **Costo total:** S/ 7.5 millones.

        **Indicadores (KPI):**  
        1. ↓ 40% ausentismo escolar durante temporada de friaje (Fuente: MINEDU).  
        2. 100% de escuelas beneficiadas aumentan la temperatura interior en +5 °C (Fuente: MINEDU).

        ---

        ## 📈 Conclusión general

        Estas tres políticas permiten abordar el impacto del frío extremo desde tres frentes complementarios: **salud, producción y educación**, priorizando la inversión en territorios de mayor vulnerabilidad térmica.  
        Los costos estimados (≈ S/ 650 millones) son moderados frente al impacto social y económico del friaje y las heladas en el país.

        ---

    """)
