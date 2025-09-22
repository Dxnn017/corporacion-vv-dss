"use client"

import { useState } from "react"
import { DashboardHeader } from "@/components/dashboard-header"
import { DashboardSidebar } from "@/components/dashboard-sidebar"
import { KPIOverview } from "@/components/kpi-overview"
import { ProjectManagement } from "@/components/project-management"
import { ClientAnalysis } from "@/components/client-analysis"
import { ServiceAreasPerformance } from "@/components/service-areas-performance"
import { DataIntegrationPanel } from "@/components/data-integration-panel"

export default function Dashboard() {
  const [activeSection, setActiveSection] = useState("overview")

  const renderContent = () => {
    switch (activeSection) {
      case "overview":
        return <KPIOverview />
      case "projects":
        return <ProjectManagement />
      case "clients":
        return <ClientAnalysis />
      case "services":
        return <ServiceAreasPerformance />
      case "settings":
        return <DataIntegrationPanel />
      default:
        return (
          <div className="p-6">
            <h2 className="text-2xl font-bold">Sección en Desarrollo</h2>
            <p className="text-muted-foreground">Este módulo estará disponible próximamente.</p>
          </div>
        )
    }
  }

  return (
    <div className="min-h-screen bg-background">
      <DashboardHeader />
      <div className="flex">
        <DashboardSidebar activeSection={activeSection} onSectionChange={setActiveSection} />
        <main className="flex-1">{renderContent()}</main>
      </div>
    </div>
  )
}
