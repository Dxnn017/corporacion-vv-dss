import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="V&V Corporación - DSS",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar datos (en una implementación real, conectarías a una base de datos)
@st.cache_data
def load_kpi_data():
    return {
        "revenue": 2850000,
        "activeProjects": 24,
        "clientSatisfaction": 94.2,
        "efficiency": 87.5,
        "monthlyGrowth": 12.3,
        "clients": 89,
        "newClients": 12
    }

@st.cache_data
def load_projects_data():
    return pd.DataFrame([
        {
            "id": "P001",
            "name": "Automatización Planta ABB",
            "client": "ABB",
            "status": "En Progreso",
            "progress": 75,
            "budget": 450000,
            "spent": 337500,
            "area": "Automatización",
            "location": "Lima Norte",
            "start_date": "2023-01-15",
            "end_date": "2023-06-30"
        },
        {
            "id": "P002",
            "name": "Mantenimiento Siemens Q1",
            "client": "Siemens",
            "status": "Completado",
            "progress": 100,
            "budget": 280000,
            "spent": 275000,
            "area": "Mantenimiento",
            "location": "Callao",
            "start_date": "2023-02-01",
            "end_date": "2023-03-15"
        },
        {
            "id": "P003",
            "name": "Instalación Eléctrica Schneider",
            "client": "Schneider Electric",
            "status": "En Progreso",
            "progress": 45,
            "budget": 320000,
            "spent": 144000,
            "area": "Electricidad",
            "location": "San Juan de Lurigancho",
            "start_date": "2023-03-10",
            "end_date": "2023-08-20"
        },
        {
            "id": "P004",
            "name": "Sistema Refrigeración Hyundai",
            "client": "Hyundai",
            "status": "Completado",
            "progress": 100,
            "budget": 280000,
            "spent": 275000,
            "area": "Refrigeración",
            "location": "Ate",
            "start_date": "2023-01-20",
            "end_date": "2023-04-10"
        },
        {
            "id": "P005",
            "name": "Obras Civiles Planta Nuevo",
            "client": "Nueco",
            "status": "Pendiente",
            "progress": 0,
            "budget": 520000,
            "spent": 0,
            "area": "Obras Civiles",
            "location": "Lima Este",
            "start_date": "2023-06-01",
            "end_date": "2023-12-15"
        }
    ])

@st.cache_data
def load_clients_data():
    return pd.DataFrame([
        {
            "name": "ABB",
            "tier": "Premium",
            "revenue": 850000,
            "projects": 8,
            "satisfaction": 96,
            "riskLevel": "Bajo",
            "since": "2020-03-15"
        },
        {
            "name": "Siemens",
            "tier": "Premium",
            "revenue": 720000,
            "projects": 6,
            "satisfaction": 94,
            "riskLevel": "Bajo",
            "since": "2019-11-20"
        },
        {
            "name": "Schneider Electric",
            "tier": "Gold",
            "revenue": 580000,
            "projects": 5,
            "satisfaction": 92,
            "riskLevel": "Bajo",
            "since": "2021-02-10"
        },
        {
            "name": "Hyundai",
            "tier": "Gold",
            "revenue": 420000,
            "projects": 4,
            "satisfaction": 89,
            "riskLevel": "Medio",
            "since": "2021-07-22"
        },
        {
            "name": "Nueco",
            "tier": "Standard",
            "revenue": 280000,
            "projects": 2,
            "satisfaction": 85,
            "riskLevel": "Medio",
            "since": "2022-05-30"
        }
    ])

@st.cache_data
def load_service_areas_data():
    return pd.DataFrame([
        {
            "area": "Metal Mecánica",
            "revenue": 980000,
            "projects": 8,
            "efficiency": 92,
            "growth": 15.2,
            "team_size": 12,
            "cost": 420000
        },
        {
            "area": "Electricidad",
            "revenue": 850000,
            "projects": 7,
            "efficiency": 89,
            "growth": 18.7,
            "team_size": 10,
            "cost": 380000
        },
        {
            "area": "Automatización",
            "revenue": 750000,
            "projects": 6,
            "efficiency": 88,
            "growth": 22.1,
            "team_size": 8,
            "cost": 320000
        },
        {
            "area": "Refrigeración",
            "revenue": 620000,
            "projects": 5,
            "efficiency": 85,
            "growth": 8.3,
            "team_size": 6,
            "cost": 280000
        },
        {
            "area": "Mantenimiento",
            "revenue": 580000,
            "projects": 10,
            "efficiency": 91,
            "growth": 12.5,
            "team_size": 15,
            "cost": 350000
        },
        {
            "area": "Obras Civiles",
            "revenue": 520000,
            "projects": 4,
            "efficiency": 83,
            "growth": 5.8,
            "team_size": 18,
            "cost": 410000
        }
    ])

# Sidebar
st.sidebar.markdown(
    """
    <div style="text-align: center; padding: 10px; background-color: #003DA5; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: white; margin: 0;">🏢 V&V Corporación</h2>
        <p style="color: #FFCC00; margin: 0;">Comercial S.A.C</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

# Selector de módulos
st.sidebar.subheader("📊 Módulos de Análisis")
selected_module = st.sidebar.selectbox(
    "Seleccionar módulo:",
    ["Dashboard Principal", "Análisis de Proyectos", "Análisis de Clientes", "Áreas de Servicio", "Reportes Avanzados"]
)

# Filtros globales 
st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Filtros Globales")

# Filtro de fecha corregido - solución robusta
try:
    # Intentar crear un rango de fechas por defecto
    default_start = date(2023, 1, 1)
    default_end = date(2023, 6, 30)
    
    # Widget de selección de fecha con manejo de errores
    selected_dates = st.sidebar.date_input(
        "Rango de Fechas",
        value=[default_start, default_end],
        min_value=date(2020, 1, 1),  # Desde 2020
        max_value=date(2025, 12, 31),  # Hasta 2025 
        help="Selecciona un rango de fechas para filtrar los datos"
    )
    
    # Validar que se hayan seleccionado exactamente 2 fechas
    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
        st.sidebar.success(f"Período seleccionado: {start_date} - {end_date}")
    else:
        st.sidebar.warning("Por favor selecciona un rango de fechas completo")
        start_date, end_date = default_start, default_end
        
except Exception as e:
    st.sidebar.error(f"Error en selección de fechas: {str(e)}")
    # Valores por defecto en caso de error
    start_date, end_date = date(2023, 1, 1), date(2023, 6, 30)

# Mostrar el período seleccionado
st.sidebar.markdown(f"**Período activo:** {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}")

# Header principal
st.markdown("""
<div style="background: linear-gradient(90deg, #003DA5 0%, #0066CC 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; text-align: center; margin: 0;">
        🏗️ V&V Corporación Comercial S.A.C
    </h1>
    <p style="color: #FFCC00; text-align: center; margin: 0.5rem 0 0 0; font-size: 1.1rem;">
        Sistema de Soporte a Decisiones - DSS Analytics
    </p>
</div>
""", unsafe_allow_html=True)

# Dashboard Principal
if selected_module == "Dashboard Principal":
    st.header("📈 Dashboard Ejecutivo")
    
    # Cargar datos
    kpis = load_kpi_data()
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #28a745, #20c997); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">💰 Ingresos Mensuales</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">S/ {kpis['revenue']:,.0f}</h2>
            <p style="margin: 0; color: #d4edda;">+{kpis['monthlyGrowth']}% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #007bff, #0056b3); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">📁 Proyectos Activos</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{kpis['activeProjects']}</h2>
            <p style="margin: 0; color: #cce7ff;">+{kpis['newClients']} nuevos ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffc107, #e0a800); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">😊 Satisfacción Cliente</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{kpis['clientSatisfaction']}%</h2>
            <p style="margin: 0; color: #fff3cd;">+1.2% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #dc3545, #c82333); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">⚡ Eficiencia Operativa</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{kpis['efficiency']}%</h2>
            <p style="margin: 0; color: #f8d7da;">+3.5% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Gráficos de resumen
    col1, col2 = st.columns(2)
    
    with col1:
        # Ingresos por área de servicio
        areas_data = load_service_areas_data()
        
        fig_pie = px.pie(
            areas_data, 
            values='revenue', 
            names='area',
            title="📊 Distribución de Ingresos por Área de Servicio",
            color_discrete_sequence=['#003DA5', '#0066CC', '#FFCC00', '#FF6B35', '#28a745', '#6f42c1'],
            hole=0.4  # Donut chart
        )
        fig_pie.update_traces(
            textposition='inside', 
            textinfo='percent+label',
            hovertemplate='<b>%{label}</b><br>Ingresos: S/ %{value:,.0f}<br>Porcentaje: %{percent}<extra></extra>'
        )
        fig_pie.update_layout(
            showlegend=True,
            legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.01),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Evolución mensual (datos simulados)
        monthly_data = pd.DataFrame({
            'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            'Ingresos': [2200000, 2350000, 2180000, 2450000, 2680000, 2850000],
            'Proyectos': [18, 20, 19, 22, 25, 24],
            'Clientes': [75, 78, 80, 82, 85, 89]
        })
        
        fig = go.Figure()
        
        # Add area chart for revenue
        fig.add_trace(go.Scatter(
            x=monthly_data['Mes'],
            y=monthly_data['Ingresos'],
            mode='lines+markers',
            name='Ingresos',
            line=dict(color='#003DA5', width=3),
            marker=dict(size=8, color='#FFCC00', line=dict(width=2, color='#003DA5')),
            fill='tonexty',
            fillcolor='rgba(0, 61, 165, 0.1)',
            hovertemplate='<b>%{x}</b><br>Ingresos: S/ %{y:,.0f}<extra></extra>',
            yaxis='y'
        ))
        
        # Add bar chart for projects (secondary axis)
        fig.add_trace(go.Bar(
            x=monthly_data['Mes'],
            y=monthly_data['Proyectos'],
            name='Proyectos',
            marker_color='#28a745',
            opacity=0.6,
            hovertemplate='<b>%{x}</b><br>Proyectos: %{y}<extra></extra>',
            yaxis='y2'
        ))
        
        fig.update_layout(
            title="📈 Evolución Mensual - Ingresos y Proyectos",
            xaxis_title="Mes",
            yaxis=dict(
                title="Ingresos (S/)",
                titlefont=dict(color="#003DA5"),
                tickfont=dict(color="#003DA5")
            ),
            yaxis2=dict(
                title="Proyectos",
                titlefont=dict(color="#28a745"),
                tickfont=dict(color="#28a745"),
                anchor="x",
                overlaying="y",
                side="right"
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified',
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        # Add grid
        fig.update_xaxis(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
        fig.update_yaxis(showgrid=True, gridwidth=1, gridcolor='rgba(128,128,128,0.2)')
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Métricas Adicionales
    st.markdown("### 📊 Métricas Adicionales")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Project completion rate
        projects = load_projects_data()
        completed = len(projects[projects['status'] == 'Completado'])
        completion_rate = (completed / len(projects)) * 100
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = completion_rate,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Tasa de Completación"},
            delta = {'reference': 80},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "#003DA5"},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col2:
        # Client distribution by tier
        clients = load_clients_data()
        tier_counts = clients['tier'].value_counts()
        
        fig_donut = px.pie(
            values=tier_counts.values,
            names=tier_counts.index,
            title="Distribución de Clientes por Tier",
            color_discrete_map={
                'Premium': '#003DA5',
                'Gold': '#FFCC00',
                'Standard': '#0066CC'
            },
            hole=0.6
        )
        fig_donut.update_layout(height=300)
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col3:
        # Team efficiency by area
        areas_data['efficiency_score'] = areas_data['efficiency']
        
        fig_bar_eff = px.bar(
            areas_data.sort_values('efficiency', ascending=True),
            x='efficiency',
            y='area',
            orientation='h',
            title="Eficiencia por Área",
            color='efficiency',
            color_continuous_scale='RdYlGn',
            text='efficiency'
        )
        fig_bar_eff.update_traces(texttemplate='%{text}%', textposition='inside')
        fig_bar_eff.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_bar_eff, use_container_width=True)

# Análisis de Proyectos
elif selected_module == "Análisis de Proyectos":
    st.header("🏗️ Análisis Detallado de Proyectos")
    
    projects = load_projects_data()
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.selectbox("Estado:", ["Todos"] + list(projects['status'].unique()))
    with col2:
        area_filter = st.selectbox("Área:", ["Todas"] + list(projects['area'].unique()))
    with col3:
        client_filter = st.selectbox("Cliente:", ["Todos"] + list(projects['client'].unique()))
    
    # Aplicar filtros
    filtered_df = projects.copy()
    if status_filter != "Todos":
        filtered_df = filtered_df[filtered_df['status'] == status_filter]
    if area_filter != "Todas":
        filtered_df = filtered_df[filtered_df['area'] == area_filter]
    if client_filter != "Todos":
        filtered_df = filtered_df[filtered_df['client'] == client_filter]
    
    # Métricas rápidas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Proyectos", len(filtered_df))
    with col2:
        total_budget = filtered_df['budget'].sum()
        st.metric("Presupuesto Total", f"S/ {total_budget:,.0f}")
    with col3:
        total_spent = filtered_df['spent'].sum()
        st.metric("Total Gastado", f"S/ {total_spent:,.0f}")
    with col4:
        if len(filtered_df) > 0:
            avg_progress = filtered_df['progress'].mean()
            st.metric("Progreso Promedio", f"{avg_progress:.1f}%")
        else:
            st.metric("Progreso Promedio", "N/A")
    
    # Gráficos
    if len(filtered_df) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            # Progreso de proyectos
            fig_bar = px.bar(
                filtered_df, 
                x='name', 
                y='progress',
                color='status',
                title="📊 Progreso de Proyectos (%)",
                color_discrete_map={
                    'En Progreso': '#FFCC00',
                    'Completado': '#28a745',
                    'Pendiente': '#dc3545'
                },
                text='progress'
            )
            fig_bar.update_traces(texttemplate='%{text}%', textposition='outside')
            fig_bar.update_layout(
                xaxis_tickangle=-45,
                yaxis_title="Progreso (%)",
                xaxis_title="Proyecto",
                showlegend=True,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            # Solo actualizar el rango del eje Y si hay datos
            if len(filtered_df) > 0:
                fig_bar.update_yaxis(range=[0, 110])
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            # Utilización de presupuesto
            filtered_df['budget_utilization'] = (filtered_df['spent'] / filtered_df['budget']) * 100
            
            fig_scatter = px.scatter(
                filtered_df,
                x='budget',
                y='spent',
                size='progress',
                color='area',
                hover_name='name',
                title="💰 Presupuesto vs Gasto Real",
                labels={'budget': 'Presupuesto (S/)', 'spent': 'Gastado (S/)'},
                color_discrete_sequence=px.colors.qualitative.Set2
            )
            # Add diagonal line for perfect budget utilization
            if len(filtered_df) > 0:
                max_budget = filtered_df['budget'].max()
                fig_scatter.add_shape(
                    type="line",
                    x0=0, y0=0, x1=max_budget, y1=max_budget,
                    line=dict(color="red", width=2, dash="dash"),
                )
            fig_scatter.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("No hay proyectos que coincidan con los filtros seleccionados.")
    
    # Tabla detallada
    st.subheader("📋 Detalles de Proyectos")
    
    if len(filtered_df) > 0:
        # Formatear columnas monetarias para mejor visualización
        display_df = filtered_df.copy()
        display_df['budget'] = display_df['budget'].apply(lambda x: f"S/ {x:,.0f}")
        display_df['spent'] = display_df['spent'].apply(lambda x: f"S/ {x:,.0f}")
        display_df['progress'] = display_df['progress'].apply(lambda x: f"{x}%")
        
        st.dataframe(display_df, use_container_width=True)
        
        # Opción para descargar datos
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar datos como CSV",
            data=csv,
            file_name="proyectos_vv_corporacion.csv",
            mime="text/csv",
        )
    else:
        st.info("No hay datos para mostrar con los filtros actuales.")

# Análisis de Clientes
elif selected_module == "Análisis de Clientes":
    st.header("👥 Análisis de Clientes")
    
    clients = load_clients_data()
    
    # Métricas de clientes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("👥 Total Clientes", len(clients))
    with col2:
        premium_clients = len(clients[clients['tier'] == 'Premium'])
        st.metric("⭐ Clientes Premium", premium_clients)
    with col3:
        avg_satisfaction = clients['satisfaction'].mean()
        st.metric("😊 Satisfacción Promedio", f"{avg_satisfaction:.1f}%")
    with col4:
        total_revenue = clients['revenue'].sum()
        st.metric("💰 Ingresos Totales", f"S/ {total_revenue:,.0f}")
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        tier_filter = st.selectbox("Categoría:", ["Todas"] + list(clients['tier'].unique()))
    with col2:
        risk_filter = st.selectbox("Nivel de Riesgo:", ["Todos"] + list(clients['riskLevel'].unique()))
    
    # Aplicar filtros
    filtered_clients = clients.copy()
    if tier_filter != "Todas":
        filtered_clients = filtered_clients[filtered_clients['tier'] == tier_filter]
    if risk_filter != "Todos":
        filtered_clients = filtered_clients[filtered_clients['riskLevel'] == risk_filter]
    
    # Gráficos de análisis
    if len(filtered_clients) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            # Ingresos por cliente
            fig_bar = px.bar(
                filtered_clients.sort_values('revenue', ascending=True),
                x='revenue',
                y='name',
                orientation='h',
                color='tier',
                title="💰 Ingresos por Cliente",
                color_discrete_map={
                    'Premium': '#003DA5',
                    'Gold': '#FFCC00',
                    'Standard': '#0066CC'
                }
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        
        with col2:
            # Satisfacción vs Proyectos
            fig_scatter = px.scatter(
                filtered_clients,
                x='projects',
                y='satisfaction',
                size='revenue',
                color='tier',
                hover_name='name',
                title="📊 Satisfacción vs Número de Proyectos",
                labels={'projects': 'Número de Proyectos', 'satisfaction': 'Satisfacción (%)'}
            )
            st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("No hay clientes que coincidan con los filtros seleccionados.")
    
    # Tabla de clientes
    st.subheader("📋 Cartera de Clientes")
    
    if len(filtered_clients) > 0:
        # Formatear columnas para mejor visualización
        display_clients = filtered_clients.copy()
        display_clients['revenue'] = display_clients['revenue'].apply(lambda x: f"S/ {x:,.0f}")
        display_clients['satisfaction'] = display_clients['satisfaction'].apply(lambda x: f"{x}%")
        
        st.dataframe(display_clients, use_container_width=True)
        
        # Opción para descargar datos
        csv = filtered_clients.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Descargar datos como CSV",
            data=csv,
            file_name="clientes_vv_corporacion.csv",
            mime="text/csv",
        )
    else:
        st.info("No hay datos para mostrar con los filtros actuales.")

# Áreas de Servicio
elif selected_module == "Áreas de Servicio":
    st.header("⚙️ Rendimiento por Áreas de Servicio")
    
    areas_data = load_service_areas_data()
    
    # Métricas por área
    col1, col2 = st.columns(2)
    
    with col1:
        # Ingresos y eficiencia
        fig_bar = go.Figure()
        
        fig_bar.add_trace(go.Bar(
            name='Ingresos (Miles S/)',
            x=areas_data['area'],
            y=areas_data['revenue'] / 1000,
            yaxis='y',
            offsetgroup=1,
            marker_color='#003DA5'
        ))
        
        fig_bar.add_trace(go.Bar(
            name='Eficiencia (%)',
            x=areas_data['area'],
            y=areas_data['efficiency'],
            yaxis='y2',
            offsetgroup=2,
            marker_color='#FFCC00'
        ))
        
        fig_bar.update_layout(
            title='💼 Ingresos vs Eficiencia por Área',
            xaxis=dict(title='Área de Servicio', tickangle=45),
            yaxis=dict(title='Ingresos (Miles S/)', side='left'),
            yaxis2=dict(title='Eficiencia (%)', side='right', overlaying='y'),
            barmode='group'
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        # Crecimiento por área
        fig_growth = px.bar(
            areas_data.sort_values('growth', ascending=True),
            x='growth',
            y='area',
            orientation='h',
            title="📈 Crecimiento por Área de Servicio (%)",
            color='growth',
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig_growth, use_container_width=True)
    
    # Análisis detallado
    st.subheader("📊 Análisis Multidimensional")
    
    # Calcular ROI
    areas_data['roi'] = (areas_data['revenue'] - areas_data['cost']) / areas_data['cost'] * 100
    
    fig_bubble = px.scatter(
        areas_data,
        x='projects',
        y='efficiency',
        size='revenue',
        color='roi',
        hover_name='area',
        title="🎯 Proyectos vs Eficiencia (Tamaño = Ingresos, Color = ROI)",
        labels={
            'projects': 'Número de Proyectos',
            'efficiency': 'Eficiencia (%)',
            'roi': 'ROI (%)',
            'revenue': 'Ingresos'
        },
        color_continuous_scale='RdYlGn'
    )
    st.plotly_chart(fig_bubble, use_container_width=True)
    
    # Tabla detallada
    st.subheader("📋 Detalles por Área de Servicio")
    
    # Formatear columnas para mejor visualización
    display_areas = areas_data.copy()
    display_areas['revenue'] = display_areas['revenue'].apply(lambda x: f"S/ {x:,.0f}")
    display_areas['cost'] = display_areas['cost'].apply(lambda x: f"S/ {x:,.0f}")
    display_areas['efficiency'] = display_areas['efficiency'].apply(lambda x: f"{x}%")
    display_areas['growth'] = display_areas['growth'].apply(lambda x: f"{x}%")
    display_areas['roi'] = display_areas['roi'].apply(lambda x: f"{x:.1f}%")
    
    st.dataframe(display_areas, use_container_width=True)
    
    # Opción para descargar datos
    csv = areas_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar datos como CSV",
        data=csv,
        file_name="areas_servicio_vv_corporacion.csv",
        mime="text/csv",
    )

# Reportes Avanzados (continuación)
elif selected_module == "Reportes Avanzados":
    st.header("📊 Reportes y Análisis Avanzados")
    
    # Análisis comparativo
    st.subheader("🔍 Análisis Comparativo Integral")
    
    # Cargar todos los datos
    kpis = load_kpi_data()
    projects = load_projects_data()
    clients = load_clients_data()
    areas = load_service_areas_data()
    
    # Crear dashboard comparativo
    col1, col2 = st.columns(2)
    
    with col1:
        # Rendimiento por cliente vs área
        client_area_summary = projects.groupby(['client', 'area']).agg({
            'budget': 'sum',
            'spent': 'sum',
            'progress': 'mean'
        }).reset_index()
        
        fig_heatmap = px.density_heatmap(
            client_area_summary,
            x='area',
            y='client',
            z='progress',
            title="🎯 Mapa de Calor: Progreso por Cliente y Área",
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
    
    with col2:
        # Análisis de rentabilidad
        areas['roi'] = (areas['revenue'] / areas['team_size']) / 1000
        
        fig_roi = px.bar(
            areas.sort_values('roi', ascending=True),
            x='roi',
            y='area',
            orientation='h',
            title="💎 ROI por Área (Ingresos/Empleado en Miles)",
            color='roi',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_roi, use_container_width=True)
    
    # Resumen ejecutivo
    st.subheader("📈 Resumen Ejecutivo")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"""
        **💰 Situación Financiera**
        - Ingresos: S/ {kpis['revenue']:,.0f}
        - Crecimiento: +{kpis['monthlyGrowth']:.1f}%
        - Proyectos activos: {kpis['activeProjects']}
        - Período: {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}
        """)
    
    with col2:
        best_area = areas.loc[areas['growth'].idxmax()]
        st.success(f"""
        **🚀 Área de Mayor Crecimiento**
        - {best_area['area']}: +{best_area['growth']:.1f}%
        - Ingresos: S/ {best_area['revenue']:,.0f}
        - Eficiencia: {best_area['efficiency']}%
        """)
    
    with col3:
        best_client = clients.loc[clients['revenue'].idxmax()]
        st.warning(f"""
        **⭐ Cliente Principal**
        - {best_client['name']} ({best_client['tier']})
        - Ingresos: S/ {best_client['revenue']:,.0f}
        - Satisfacción: {best_client['satisfaction']}%
        """)
    
    # Análisis predictivo simple (simulado)
    st.subheader("🔮 Proyecciones Futuras")
    
    # Simular datos de proyección
    months = ['Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
    projected_revenue = [3000000, 3150000, 3300000, 3450000, 3600000, 3750000]
    
    fig_projection = go.Figure()
    fig_projection.add_trace(go.Scatter(
        x=months,
        y=projected_revenue,
        mode='lines+markers',
        name='Proyección 2023',
        line=dict(color='#28a745', width=3, dash='dot'),
        marker=dict(size=8, color='#28a745')
    ))
    
    # Añadir datos históricos
    historical_months = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun']
    historical_revenue = [2200000, 2350000, 2180000, 2450000, 2680000, 2850000]
    
    fig_projection.add_trace(go.Scatter(
        x=historical_months,
        y=historical_revenue,
        mode='lines+markers',
        name='Histórico 2023',
        line=dict(color='#003DA5', width=3),
        marker=dict(size=8, color='#003DA5')
    ))
    
    # Proyección 2024
    months_2024 = ['Ene 24', 'Feb 24', 'Mar 24', 'Abr 24', 'May 24', 'Jun 24']
    projected_2024 = [3900000, 4050000, 4200000, 4350000, 4500000, 4650000]
    
    fig_projection.add_trace(go.Scatter(
        x=months_2024,
        y=projected_2024,
        mode='lines+markers',
        name='Proyección 2024',
        line=dict(color='#FF6B35', width=3, dash='dot'),
        marker=dict(size=8, color='#FF6B35')
    ))
    
    fig_projection.update_layout(
        title="📊 Proyección de Ingresos 2023-2024",
        xaxis_title="Mes",
        yaxis_title="Ingresos (S/)",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig_projection, use_container_width=True)
    
    # Análisis de tendencias por año
    st.subheader("📅 Análisis de Tendencia Anual")
    
    # Datos simulados por año
    yearly_data = pd.DataFrame({
        'Año': [2020, 2021, 2022, 2023],
        'Ingresos': [18500000, 21500000, 24500000, 28500000],
        'Clientes': [45, 62, 75, 89],
        'Proyectos': [120, 145, 168, 195]
    })
    
    fig_yearly = go.Figure()
    
    fig_yearly.add_trace(go.Bar(
        x=yearly_data['Año'],
        y=yearly_data['Ingresos'],
        name='Ingresos',
        marker_color='#003DA5',
        hovertemplate='Año: %{x}<br>Ingresos: S/ %{y:,.0f}<extra></extra>'
    ))
    
    fig_yearly.add_trace(go.Scatter(
        x=yearly_data['Año'],
        y=yearly_data['Clientes'],
        name='Clientes',
        mode='lines+markers',
        yaxis='y2',
        line=dict(color='#FFCC00', width=3),
        marker=dict(size=8, color='#FFCC00'),
        hovertemplate='Año: %{x}<br>Clientes: %{y}<extra></extra>'
    ))
    
    fig_yearly.update_layout(
        title="📈 Evolución Anual - Ingresos y Clientes",
        xaxis_title="Año",
        yaxis=dict(
            title="Ingresos (S/)",
            titlefont=dict(color="#003DA5"),
            tickfont=dict(color="#003DA5")
        ),
        yaxis2=dict(
            title="Número de Clientes",
            titlefont=dict(color="#FFCC00"),
            tickfont=dict(color="#FFCC00"),
            anchor="x",
            overlaying="y",
            side="right"
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_yearly, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>V&V Corporación Comercial S.A.C - Sistema Integrado de Análisis</p>
    <p>📞 972 257 767 | 📍 Calle Manuel Ubalde N° 1125 - A. PJ. El Porvenir</p>
    <p>© 2023 - Todos los derechos reservados</p>
</div>
""", unsafe_allow_html=True)
