// Data Integration Layer para V&V Corporación Comercial DSS
// Esta capa maneja la integración con fuentes externas de datos

export interface DataSource {
  id: string
  name: string
  type: "streamlit" | "database" | "api" | "file"
  status: "connected" | "disconnected" | "error"
  lastSync: Date
  config: Record<string, any>
}

export interface StreamlitConfig {
  url: string
  apiKey?: string
  endpoints: {
    projects: string
    clients: string
    kpis: string
    serviceAreas: string
  }
}

export interface DatabaseConfig {
  host: string
  port: number
  database: string
  username: string
  password: string
  ssl: boolean
}

// Mock data sources configuration
export const dataSources: DataSource[] = [
  {
    id: "streamlit-main",
    name: "Streamlit Analytics",
    type: "streamlit",
    status: "connected",
    lastSync: new Date("2024-01-15T10:30:00"),
    config: {
      url: "https://vv-analytics.streamlit.app",
      endpoints: {
        projects: "/api/projects",
        clients: "/api/clients",
        kpis: "/api/kpis",
        serviceAreas: "/api/service-areas",
      },
    },
  },
  {
    id: "postgres-main",
    name: "PostgreSQL Principal",
    type: "database",
    status: "connected",
    lastSync: new Date("2024-01-15T11:00:00"),
    config: {
      host: "localhost",
      port: 5432,
      database: "vv_corporacion",
      ssl: true,
    },
  },
  {
    id: "erp-api",
    name: "Sistema ERP",
    type: "api",
    status: "disconnected",
    lastSync: new Date("2024-01-14T15:20:00"),
    config: {
      baseUrl: "https://erp.vvcorporacion.com/api",
      version: "v1",
    },
  },
]

// Data fetching functions
export class DataIntegrationService {
  static async fetchFromStreamlit(endpoint: string, config: StreamlitConfig) {
    try {
      const response = await fetch(`${config.url}${endpoint}`, {
        headers: {
          "Content-Type": "application/json",
          ...(config.apiKey && { Authorization: `Bearer ${config.apiKey}` }),
        },
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      return await response.json()
    } catch (error) {
      console.error("Error fetching from Streamlit:", error)
      throw error
    }
  }

  static async syncKPIData() {
    // Simulated KPI data sync
    return {
      revenue: 2450000,
      projects: { active: 24, completed: 156, pending: 8 },
      clients: { total: 89, active: 67, new: 12 },
      satisfaction: 94.2,
      lastUpdated: new Date(),
    }
  }

  static async syncProjectData() {
    // Simulated project data sync
    return {
      projects: [
        {
          id: "P001",
          name: "Automatización Planta ABB",
          status: "En Progreso",
          progress: 75,
          client: "ABB",
        },
      ],
      lastUpdated: new Date(),
    }
  }

  static async syncClientData() {
    // Simulated client data sync
    return {
      clients: [
        {
          id: "C001",
          name: "ABB",
          status: "Activo",
          revenue: 1250000,
          satisfaction: 96,
        },
      ],
      lastUpdated: new Date(),
    }
  }

  static async testConnection(dataSource: DataSource): Promise<boolean> {
    try {
      switch (dataSource.type) {
        case "streamlit":
          const response = await fetch(`${dataSource.config.url}/health`)
          return response.ok
        case "database":
          // Simulate database connection test
          return true
        case "api":
          const apiResponse = await fetch(`${dataSource.config.baseUrl}/health`)
          return apiResponse.ok
        default:
          return false
      }
    } catch (error) {
      console.error("Connection test failed:", error)
      return false
    }
  }
}

// Export configuration for Streamlit integration
export const streamlitIntegration = {
  setupInstructions: `
# Configuración de Integración con Streamlit

## 1. Instalar dependencias en tu aplicación Streamlit:
\`\`\`bash
pip install streamlit pandas plotly requests
\`\`\`

## 2. Crear endpoints API en tu app Streamlit:
\`\`\`python
import streamlit as st
import pandas as pd
import json
from datetime import datetime

# Endpoint para KPIs
@st.cache_data
def get_kpi_data():
    return {
        "revenue": 2450000,
        "projects": {"active": 24, "completed": 156},
        "satisfaction": 94.2,
        "timestamp": datetime.now().isoformat()
    }

# Endpoint para proyectos
@st.cache_data
def get_projects_data():
    return {
        "projects": [
            {
                "id": "P001",
                "name": "Automatización Planta ABB",
                "status": "En Progreso",
                "progress": 75
            }
        ]
    }
\`\`\`

## 3. Configurar CORS en Streamlit:
\`\`\`python
st.set_page_config(
    page_title="V&V Analytics",
    page_icon="📊",
    layout="wide"
)
\`\`\`

## 4. URL de tu aplicación Streamlit:
Actualiza la configuración con la URL de tu app desplegada.
  `,

  sampleCode: `
# Ejemplo de integración con el DSS
import requests
import json

def sync_with_dss():
    dss_endpoint = "http://localhost:3000/api/sync"
    
    data = {
        "source": "streamlit",
        "kpis": get_kpi_data(),
        "projects": get_projects_data(),
        "timestamp": datetime.now().isoformat()
    }
    
    response = requests.post(dss_endpoint, json=data)
    return response.json()
  `,
}
