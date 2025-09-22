"use client"

import { BarChart3, FolderOpen, Users, Settings, Wrench, TrendingUp, Calendar, FileText } from "lucide-react"
import { Button } from "@/components/ui/button"
import { cn } from "@/lib/utils"

interface SidebarProps {
  activeSection: string
  onSectionChange: (section: string) => void
}

export function DashboardSidebar({ activeSection, onSectionChange }: SidebarProps) {
  const menuItems = [
    { id: "overview", label: "Resumen General", icon: BarChart3 },
    { id: "projects", label: "Proyectos", icon: FolderOpen },
    { id: "clients", label: "Clientes", icon: Users },
    { id: "services", label: "Áreas de Servicio", icon: Wrench },
    { id: "analytics", label: "Análisis", icon: TrendingUp },
    { id: "calendar", label: "Calendario", icon: Calendar },
    { id: "reports", label: "Reportes", icon: FileText },
    { id: "settings", label: "Configuración", icon: Settings },
  ]

  return (
    <aside className="w-64 border-r bg-card">
      <div className="p-6">
        <h2 className="text-lg font-semibold text-foreground mb-4">Sistema DSS</h2>
        <nav className="space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon
            return (
              <Button
                key={item.id}
                variant={activeSection === item.id ? "default" : "ghost"}
                className={cn(
                  "w-full justify-start gap-3",
                  activeSection === item.id && "bg-primary text-primary-foreground",
                )}
                onClick={() => onSectionChange(item.id)}
              >
                <Icon className="h-4 w-4" />
                {item.label}
              </Button>
            )
          })}
        </nav>
      </div>
    </aside>
  )
}
