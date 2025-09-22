import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import numpy as np

# Configuración de la página
try:
    st.set_page_config(
        page_title="V&V Corporación - DSS",
        page_icon="🏗️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
except Exception as e:
    st.error(f"Error en configuración: {e}")

@st.cache_data
def load_kpi_data():
    """Load KPI data with enhanced error handling"""
    try:
        data = {
            "revenue": 2850000,
            "activeProjects": 24,
            "clientSatisfaction": 94.2,
            "efficiency": 87.5,
            "monthlyGrowth": 12.3,
            "clients": 89,
            "newClients": 12
        }
        # Validate data types
        for key, value in data.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Invalid data type for {key}: {type(value)}")
        return data
    except Exception as e:
        st.error(f"Error loading KPI data: {e}")
        return {}

@st.cache_data
def load_projects_data():
    """Load projects data as DataFrame with enhanced validation"""
    try:
        data = [
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
                "end_date": "2023-07-30"
            },
            {
                "id": "P002",
                "name": "Sistema Eléctrico Schneider",
                "client": "Schneider Electric",
                "status": "Completado",
                "progress": 100,
                "budget": 320000,
                "spent": 315000,
                "area": "Electricidad",
                "location": "Lima Centro",
                "start_date": "2023-02-01",
                "end_date": "2023-05-15"
            },
            {
                "id": "P003",
                "name": "Refrigeración Industrial Carrier",
                "client": "Carrier",
                "status": "En Progreso",
                "progress": 60,
                "budget": 280000,
                "spent": 168000,
                "area": "Refrigeración",
                "location": "Callao",
                "start_date": "2023-03-10",
                "end_date": "2023-08-20"
            },
            {
                "id": "P004",
                "name": "Mantenimiento Preventivo Siemens",
                "client": "Siemens",
                "status": "Pendiente",
                "progress": 25,
                "budget": 150000,
                "spent": 37500,
                "area": "Mantenimiento",
                "location": "Lima Sur",
                "start_date": "2023-04-01",
                "end_date": "2023-09-30"
            },
            {
                "id": "P005",
                "name": "Obras Civiles Constructora ABC",
                "client": "Constructora ABC",
                "status": "En Progreso",
                "progress": 85,
                "budget": 520000,
                "spent": 442000,
                "area": "Obras Civiles",
                "location": "Lima Este",
                "start_date": "2023-01-20",
                "end_date": "2023-06-15"
            }
        ]
        df = pd.DataFrame(data)
        # Validate DataFrame structure
        required_columns = ['id', 'name', 'client', 'status', 'progress', 'budget', 'spent', 'area']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Missing required columns in projects data")
        return df
    except Exception as e:
        st.error(f"Error loading projects data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_clients_data():
    """Load clients data as DataFrame with error handling"""
    try:
        data = [
            {
                "id": "C001",
                "name": "ABB",
                "sector": "Industrial",
                "projects_count": 3,
                "total_revenue": 850000,
                "satisfaction": 95.5,
                "location": "Lima Norte",
                "contract_date": "2022-06-15"
            },
            {
                "id": "C002",
                "name": "Schneider Electric",
                "sector": "Eléctrico",
                "projects_count": 2,
                "total_revenue": 520000,
                "satisfaction": 92.8,
                "location": "Lima Centro",
                "contract_date": "2022-08-20"
            },
            {
                "id": "C003",
                "name": "Carrier",
                "sector": "HVAC",
                "projects_count": 2,
                "total_revenue": 480000,
                "satisfaction": 94.2,
                "location": "Callao",
                "contract_date": "2022-09-10"
            },
            {
                "id": "C004",
                "name": "Siemens",
                "sector": "Automatización",
                "projects_count": 4,
                "total_revenue": 720000,
                "satisfaction": 96.1,
                "location": "Lima Sur",
                "contract_date": "2022-05-05"
            },
            {
                "id": "C005",
                "name": "Constructora ABC",
                "sector": "Construcción",
                "projects_count": 1,
                "total_revenue": 520000,
                "satisfaction": 93.7,
                "location": "Lima Este",
                "contract_date": "2022-12-01"
            }
        ]
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error loading clients data: {e}")
        return pd.DataFrame()

@st.cache_data
def load_service_areas_data():
    """Load service areas data as DataFrame with error handling"""
    try:
        data = [
            {"area": "Metal Mecánica", "revenue": 650000, "projects": 8, "efficiency": 89.5},
            {"area": "Electricidad", "revenue": 520000, "projects": 6, "efficiency": 92.1},
            {"area": "Automatización", "revenue": 480000, "projects": 5, "efficiency": 87.3},
            {"area": "Refrigeración", "revenue": 410000, "projects": 4, "efficiency": 85.7},
            {"area": "Mantenimiento", "revenue": 390000, "projects": 7, "efficiency": 91.2},
            {"area": "Obras Civiles", "revenue": 400000, "projects": 3, "efficiency": 88.9}
        ]
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error loading service areas data: {e}")
        return pd.DataFrame()

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

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Filtros Globales")

try:
    default_start = date(2023, 1, 1)
    default_end = date(2023, 6, 30)
    
    selected_dates = st.sidebar.date_input(
        "Rango de Fechas",
        value=[default_start, default_end],
        min_value=date(2020, 1, 1),
        max_value=date(2025, 12, 31),
        help="Selecciona un rango de fechas para filtrar los datos"
    )
    
    if isinstance(selected_dates, (list, tuple)) and len(selected_dates) == 2:
        start_date, end_date = selected_dates
        if start_date <= end_date:
            st.sidebar.success(f"Período seleccionado: {start_date} - {end_date}")
        else:
            st.sidebar.error("La fecha de inicio debe ser anterior a la fecha de fin")
            start_date, end_date = default_start, default_end
    else:
        st.sidebar.warning("Por favor selecciona un rango de fechas completo")
        start_date, end_date = default_start, default_end
        
except Exception as e:
    st.sidebar.error(f"Error en selección de fechas: {str(e)}")
    start_date, end_date = date(2023, 1, 1), date(2023, 6, 30)

st.sidebar.markdown(f"**Período activo:** {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}")

# Header principal
st.markdown(
    """
    <div style="background: linear-gradient(90deg, #003DA5, #0056b3); padding: 2rem; border-radius: 15px; margin-bottom: 2rem; text-align: center;">
        <h1 style="color: white; margin: 0; font-size: 2.5rem;">🏗️ V&V Corporación Comercial S.A.C</h1>
        <p style="color: #FFCC00; margin: 0.5rem 0 0 0; font-size: 1.2rem;">Sistema de Soporte a Decisiones - DSS Analytics</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Dashboard Principal
if selected_module == "Dashboard Principal":
    st.header("📈 Dashboard Ejecutivo")
    
    kpis = load_kpi_data()
    if not kpis:
        st.error("No se pudieron cargar los datos KPI")
        st.stop()
    
    # Métricas principales con diseño mejorado
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #28a745, #20c997); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">💰 Ingresos Mensuales</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">S/ {kpis.get('revenue', 0):,.0f}</h2>
            <p style="margin: 0; color: #d4edda;">+{kpis.get('monthlyGrowth', 0)}% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #007bff, #0056b3); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">📁 Proyectos Activos</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{kpis.get('activeProjects', 0)}</h2>
            <p style="margin: 0; color: #cce7ff;">+{kpis.get('newClients', 0)} nuevos ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffc107, #e0a800); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">😊 Satisfacción Cliente</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{kpis.get('clientSatisfaction', 0)}%</h2>
            <p style="margin: 0; color: #fff3cd;">+1.2% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #dc3545, #c82333); padding: 1.5rem; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3 style="margin: 0; font-size: 1.2rem;">⚡ Eficiencia Operativa</h3>
            <h2 style="margin: 0.5rem 0; font-size: 2rem;">{kpis.get('efficiency', 0)}%</h2>
            <p style="margin: 0; color: #f8d7da;">+3.5% ↗️</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        try:
            areas_data = load_service_areas_data()
            
            if not areas_data.empty:
                fig_pie = px.pie(
                    areas_data, 
                    values='revenue', 
                    names='area',
                    title="🏭 Distribución de Ingresos por Área de Servicio",
                    color_discrete_sequence=['#003DA5', '#FFCC00', '#28a745', '#dc3545', '#17a2b8', '#6f42c1']
                )
                fig_pie.update_traces(
                    textposition='inside', 
                    textinfo='percent+label',
                    hovertemplate='<b>%{label}</b><br>Ingresos: S/ %{value:,.0f}<br>Porcentaje: %{percent}<extra></extra>'
                )
                fig_pie.update_layout(
                    showlegend=True,
                    legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.05),
                    margin=dict(t=50, b=50, l=50, r=150),
                    font=dict(size=12)
                )
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.error("No se pudieron cargar los datos de áreas de servicio")
                st.info("Mostrando datos en formato tabla:")
                st.dataframe(areas_data)
        except Exception as e:
            st.error(f"Error al crear gráfico de áreas: {e}")
            st.info("Intenta recargar la página o contacta al administrador")
    
    with col2:
        try:
            monthly_data = pd.DataFrame({
                'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
                'Ingresos': [2200000, 2350000, 2180000, 2420000, 2650000, 2850000]
            })
            
            # Validate data
            if monthly_data.empty or 'Mes' not in monthly_data.columns or 'Ingresos' not in monthly_data.columns:
                raise ValueError("Invalid monthly data structure")
            
            fig_line = px.line(
                monthly_data, 
                x='Mes', 
                y='Ingresos',
                title="📈 Evolución de Ingresos Mensuales",
                markers=True
            )
            fig_line.update_traces(
                line=dict(color='#003DA5', width=4),
                marker=dict(size=10, color='#FFCC00', line=dict(width=2, color='#003DA5')),
                hovertemplate='<b>%{x}</b><br>Ingresos: S/ %{y:,.0f}<extra></extra>'
            )
            fig_line.update_layout(
                xaxis_title="Mes",
                yaxis_title="Ingresos (S/)",
                yaxis=dict(tickformat=',.0f'),
                hovermode='x unified',
                font=dict(size=12)
            )
            st.plotly_chart(fig_line, use_container_width=True)
        except Exception as e:
            st.error(f"Error al crear gráfico de evolución: {e}")
            st.info("Mostrando datos en formato tabla:")
            if 'monthly_data' in locals():
                st.dataframe(monthly_data)

elif selected_module == "Análisis de Proyectos":
    st.header("🏗️ Análisis Detallado de Proyectos")
    
    try:
        projects_df = load_projects_data()
        if projects_df.empty:
            st.error("No se pudieron cargar los datos de proyectos")
            st.stop()
        
        # Filtros
        col1, col2, col3 = st.columns(3)
        with col1:
            status_filter = st.selectbox("Estado:", ["Todos"] + list(projects_df['status'].unique()))
        with col2:
            area_filter = st.selectbox("Área:", ["Todas"] + list(projects_df['area'].unique()))
        with col3:
            client_filter = st.selectbox("Cliente:", ["Todos"] + list(projects_df['client'].unique()))
        
        # Aplicar filtros
        filtered_df = projects_df.copy()
        if status_filter != "Todos":
            filtered_df = filtered_df[filtered_df['status'] == status_filter]
        if area_filter != "Todas":
            filtered_df = filtered_df[filtered_df['area'] == area_filter]
        if client_filter != "Todos":
            filtered_df = filtered_df[filtered_df['client'] == client_filter]
        
        # Métricas de proyectos
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
        
        # Gráficos mejorados
        if len(filtered_df) > 0:
            col1, col2 = st.columns(2)
            
            with col1:
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
                fig_bar.update_traces(
                    texttemplate='%{text}%', 
                    textposition='outside',
                    hovertemplate='<b>%{x}</b><br>Progreso: %{y}%<br>Estado: %{fullData.name}<extra></extra>'
                )
                fig_bar.update_layout(
                    xaxis=dict(tickangle=-45),
                    yaxis=dict(range=[0, 110]),
                    showlegend=True
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            
            with col2:
                fig_scatter = px.scatter(
                    filtered_df,
                    x='budget',
                    y='spent',
                    size='progress',
                    color='area',
                    title="💰 Presupuesto vs Gasto Real",
                    hover_data=['name', 'client'],
                    size_max=20
                )
                fig_scatter.update_traces(
                    hovertemplate='<b>%{customdata[0]}</b><br>Cliente: %{customdata[1]}<br>Presupuesto: S/ %{x:,.0f}<br>Gastado: S/ %{y:,.0f}<br>Progreso: %{marker.size}%<extra></extra>'
                )
                fig_scatter.update_layout(
                    xaxis_title="Presupuesto (S/)",
                    yaxis_title="Gasto Real (S/)"
                )
                st.plotly_chart(fig_scatter, use_container_width=True)
            
            # Tabla de proyectos
            st.subheader("📋 Detalle de Proyectos")
            st.dataframe(
                filtered_df[['name', 'client', 'status', 'progress', 'budget', 'spent', 'area']],
                use_container_width=True
            )
        else:
            st.warning("No hay proyectos que coincidan con los filtros seleccionados")
    
    except Exception as e:
        st.error(f"Error en análisis de proyectos: {e}")

elif selected_module == "Análisis de Clientes":
    st.header("👥 Análisis de Clientes")
    
    try:
        clients_df = load_clients_data()
        if clients_df.empty:
            st.error("No se pudieron cargar los datos de clientes")
            st.stop()
        
        # Métricas de clientes
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Clientes", len(clients_df))
        with col2:
            total_revenue = clients_df['total_revenue'].sum()
            st.metric("Ingresos Totales", f"S/ {total_revenue:,.0f}")
        with col3:
            avg_satisfaction = clients_df['satisfaction'].mean()
            st.metric("Satisfacción Promedio", f"{avg_satisfaction:.1f}%")
        with col4:
            total_projects = clients_df['projects_count'].sum()
            st.metric("Total Proyectos", total_projects)
        
        # Gráficos de clientes
        col1, col2 = st.columns(2)
        
        with col1:
            fig_clients_revenue = px.bar(
                clients_df.sort_values('total_revenue', ascending=True),
                x='total_revenue',
                y='name',
                orientation='h',
                title="💼 Ingresos por Cliente",
                color='total_revenue',
                color_continuous_scale='Blues'
            )
            fig_clients_revenue.update_traces(
                hovertemplate='<b>%{y}</b><br>Ingresos: S/ %{x:,.0f}<extra></extra>'
            )
            fig_clients_revenue.update_layout(
                xaxis_title="Ingresos (S/)",
                yaxis_title="Cliente"
            )
            st.plotly_chart(fig_clients_revenue, use_container_width=True)
        
        with col2:
            fig_satisfaction = px.scatter(
                clients_df,
                x='projects_count',
                y='satisfaction',
                size='total_revenue',
                color='sector',
                title="📈 Satisfacción vs Número de Proyectos",
                hover_data=['name'],
                size_max=20
            )
            fig_satisfaction.update_traces(
                hovertemplate='<b>%{customdata[0]}</b><br>Proyectos: %{x}<br>Satisfacción: %{y}%<br>Sector: %{fullData.name}<extra></extra>'
            )
            fig_satisfaction.update_layout(
                xaxis_title="Número de Proyectos",
                yaxis_title="Satisfacción (%)"
            )
            st.plotly_chart(fig_satisfaction, use_container_width=True)
        
        # Tabla de clientes
        st.subheader("📊 Detalle de Clientes")
        st.dataframe(clients_df, use_container_width=True)
    
    except Exception as e:
        st.error(f"Error en análisis de clientes: {e}")

elif selected_module == "Áreas de Servicio":
    st.header("🏭 Análisis de Áreas de Servicio")
    
    try:
        areas_df = load_service_areas_data()
        if areas_df.empty:
            st.error("No se pudieron cargar los datos de áreas de servicio")
            st.stop()
        
        # Métricas de áreas
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Áreas", len(areas_df))
        with col2:
            total_revenue = areas_df['revenue'].sum()
            st.metric("Ingresos Totales", f"S/ {total_revenue:,.0f}")
        with col3:
            total_projects = areas_df['projects'].sum()
            st.metric("Total Proyectos", total_projects)
        with col4:
            avg_efficiency = areas_df['efficiency'].mean()
            st.metric("Eficiencia Promedio", f"{avg_efficiency:.1f}%")
        
        # Gráficos de áreas
        col1, col2 = st.columns(2)
        
        with col1:
            fig_areas_revenue = px.bar(
                areas_df.sort_values('revenue', ascending=False),
                x='area',
                y='revenue',
                title="💰 Ingresos por Área de Servicio",
                color='revenue',
                color_continuous_scale='Viridis'
            )
            fig_areas_revenue.update_traces(
                hovertemplate='<b>%{x}</b><br>Ingresos: S/ %{y:,.0f}<extra></extra>'
            )
            fig_areas_revenue.update_layout(
                xaxis=dict(tickangle=-45),
                xaxis_title="Área de Servicio",
                yaxis_title="Ingresos (S/)"
            )
            st.plotly_chart(fig_areas_revenue, use_container_width=True)
        
        with col2:
            fig_efficiency = px.scatter(
                areas_df,
                x='projects',
                y='efficiency',
                size='revenue',
                color='area',
                title="⚡ Eficiencia vs Número de Proyectos",
                size_max=20
            )
            fig_efficiency.update_traces(
                hovertemplate='<b>%{fullData.name}</b><br>Proyectos: %{x}<br>Eficiencia: %{y}%<br>Ingresos: S/ %{marker.size:,.0f}<extra></extra>'
            )
            fig_efficiency.update_layout(
                xaxis_title="Número de Proyectos",
                yaxis_title="Eficiencia (%)"
            )
            st.plotly_chart(fig_efficiency, use_container_width=True)
        
        # Tabla de áreas
        st.subheader("📋 Detalle de Áreas de Servicio")
        st.dataframe(areas_df, use_container_width=True)
    
    except Exception as e:
        st.error(f"Error en análisis de áreas: {e}")

elif selected_module == "Reportes Avanzados":
    st.header("📊 Reportes y Análisis Avanzados")
    
    try:
        # Cargar todos los datos
        kpis = load_kpi_data()
        projects = load_projects_data()
        clients = load_clients_data()
        areas = load_service_areas_data()
        
        if projects.empty or clients.empty or areas.empty:
            st.error("No se pudieron cargar todos los datos necesarios")
            st.stop()
        
        # Análisis de tendencias anuales
        st.subheader("📈 Análisis de Tendencia Anual")
        
        yearly_data = pd.DataFrame({
            'Año': [2020, 2021, 2022, 2023],
            'Ingresos': [18500000, 21500000, 24500000, 28500000],
            'Clientes': [45, 62, 75, 89],
            'Proyectos': [120, 145, 168, 195]
        })
        
        try:
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
                mode='lines+markers',
                name='Clientes',
                yaxis='y2',
                line=dict(color='#FFCC00', width=3),
                marker=dict(size=10),
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
                legend=dict(x=0.01, y=0.99),
                hovermode='x unified',
                font=dict(size=12)
            )
            
            st.plotly_chart(fig_yearly, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error creando gráfico anual: {e}")
            st.info("Mostrando datos en formato tabla:")
            st.dataframe(yearly_data)
        
        # Proyección futura
        st.subheader("🔮 Proyección de Crecimiento")
        
        projection_data = pd.DataFrame({
            'Año': [2024, 2025, 2026],
            'Ingresos_Proyectados': [32500000, 37000000, 42000000],
            'Clientes_Proyectados': [105, 125, 150]
        })
        
        fig_projection = go.Figure()
        
        # Datos históricos
        fig_projection.add_trace(go.Scatter(
            x=yearly_data['Año'],
            y=yearly_data['Ingresos'],
            mode='lines+markers',
            name='Ingresos Históricos',
            line=dict(color='#003DA5', width=3),
            marker=dict(size=8)
        ))
        
        # Proyecciones
        fig_projection.add_trace(go.Scatter(
            x=projection_data['Año'],
            y=projection_data['Ingresos_Proyectados'],
            mode='lines+markers',
            name='Ingresos Proyectados',
            line=dict(color='#FFCC00', width=3, dash='dash'),
            marker=dict(size=8)
        ))
        
        fig_projection.update_layout(
            title="🚀 Proyección de Ingresos 2024-2026",
            xaxis_title="Año",
            yaxis_title="Ingresos (S/)",
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_projection, use_container_width=True)
        
        # Resumen ejecutivo
        st.subheader("📋 Resumen Ejecutivo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🎯 Puntos Clave:**
            - Crecimiento sostenido del 15% anual
            - Diversificación exitosa en 6 áreas de servicio
            - Alta satisfacción del cliente (94.2%)
            - Cartera de 89 clientes activos
            """)
        
        with col2:
            st.markdown("""
            **📈 Oportunidades:**
            - Expansión en automatización industrial
            - Nuevos mercados en Lima Sur
            - Servicios de mantenimiento predictivo
            - Alianzas estratégicas con proveedores
            """)
    
    except Exception as e:
        st.error(f"Error en reportes avanzados: {e}")
        st.info("Algunos módulos pueden no estar disponibles temporalmente")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 1rem; background-color: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
        <p style="margin: 0; color: #6c757d;">© 2023 V&V Corporación Comercial S.A.C - Sistema de Soporte a Decisiones</p>
        <p style="margin: 0; color: #6c757d; font-size: 0.9rem;">Desarrollado con Streamlit | Datos actualizados en tiempo real</p>
    </div>
    """, 
    unsafe_allow_html=True
)

if __name__ == "__main__":
    try:
        # Main execution logic can be placed here if needed
        pass
    except Exception as e:
        st.error(f"Error en la aplicación: {e}")
        st.info("Por favor, recarga la página o contacta al administrador.")
