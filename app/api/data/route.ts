import { type NextRequest, NextResponse } from "next/server"

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url)
  const type = searchParams.get("type")

  try {
    switch (type) {
      case "kpis":
        return NextResponse.json({
          revenue: 2850000,
          activeProjects: 24,
          clientSatisfaction: 94.2,
          efficiency: 87.5,
          monthlyGrowth: 12.3,
          timestamp: new Date().toISOString(),
        })

      case "projects":
        return NextResponse.json([
          {
            id: "P001",
            name: "Modernización Sistema Eléctrico ABB",
            client: "ABB",
            status: "En Progreso",
            progress: 75,
            budget: 450000,
            spent: 337500,
            area: "Electricidad",
            startDate: "2024-01-15",
            endDate: "2024-03-30",
          },
          {
            id: "P002",
            name: "Mantenimiento Preventivo Siemens",
            client: "Siemens",
            status: "Completado",
            progress: 100,
            budget: 280000,
            spent: 275000,
            area: "Mantenimiento",
            startDate: "2024-02-01",
            endDate: "2024-02-28",
          },
        ])

      case "clients":
        return NextResponse.json([
          {
            id: "C001",
            name: "ABB",
            tier: "Premium",
            revenue: 850000,
            projects: 8,
            satisfaction: 96,
            riskLevel: "Bajo",
          },
          {
            id: "C002",
            name: "Siemens",
            tier: "Premium",
            revenue: 720000,
            projects: 6,
            satisfaction: 94,
            riskLevel: "Bajo",
          },
        ])

      case "service-areas":
        return NextResponse.json([
          {
            area: "Electricidad",
            revenue: 980000,
            projects: 8,
            efficiency: 92,
            growth: 15.2,
          },
          {
            area: "Automatización",
            revenue: 750000,
            projects: 6,
            efficiency: 88,
            growth: 18.7,
          },
          {
            area: "Mantenimiento",
            revenue: 620000,
            projects: 10,
            efficiency: 85,
            growth: 8.3,
          },
        ])

      default:
        return NextResponse.json({ error: "Tipo de datos no válido" }, { status: 400 })
    }
  } catch (error) {
    return NextResponse.json({ error: "Error interno del servidor" }, { status: 500 })
  }
}

export async function POST(request: NextRequest) {
  try {
    const data = await request.json()
    const { type, payload } = data

    // Aquí procesarías los datos recibidos de Streamlit
    console.log(`[v0] Received ${type} data from Streamlit:`, payload)

    // Simular procesamiento y respuesta
    return NextResponse.json({
      success: true,
      message: `Datos de ${type} recibidos correctamente`,
      timestamp: new Date().toISOString(),
    })
  } catch (error) {
    return NextResponse.json({ error: "Error procesando datos" }, { status: 500 })
  }
}
