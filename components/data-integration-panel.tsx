"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Alert, AlertDescription } from "@/components/ui/alert"
import {
  Database,
  Globe,
  Server,
  FileText,
  CheckCircle,
  XCircle,
  AlertTriangle,
  RefreshCw,
  Settings,
  Code,
  Link,
} from "lucide-react"
import { dataSources, DataIntegrationService, streamlitIntegration } from "@/lib/data-integration"

const getStatusIcon = (status: string) => {
  switch (status) {
    case "connected":
      return <CheckCircle className="h-4 w-4 text-green-600" />
    case "disconnected":
      return <XCircle className="h-4 w-4 text-red-600" />
    case "error":
      return <AlertTriangle className="h-4 w-4 text-yellow-600" />
    default:
      return <AlertTriangle className="h-4 w-4 text-gray-600" />
  }
}

const getStatusColor = (status: string) => {
  switch (status) {
    case "connected":
      return "bg-green-100 text-green-800 border-green-200"
    case "disconnected":
      return "bg-red-100 text-red-800 border-red-200"
    case "error":
      return "bg-yellow-100 text-yellow-800 border-yellow-200"
    default:
      return "bg-gray-100 text-gray-800 border-gray-200"
  }
}

const getTypeIcon = (type: string) => {
  switch (type) {
    case "streamlit":
      return <Globe className="h-5 w-5 text-blue-600" />
    case "database":
      return <Database className="h-5 w-5 text-green-600" />
    case "api":
      return <Server className="h-5 w-5 text-purple-600" />
    case "file":
      return <FileText className="h-5 w-5 text-orange-600" />
    default:
      return <Settings className="h-5 w-5 text-gray-600" />
  }
}

export function DataIntegrationPanel() {
  const connectedSources = dataSources.filter((ds) => ds.status === "connected")
  const disconnectedSources = dataSources.filter((ds) => ds.status !== "connected")

  const handleSync = async (sourceId: string) => {
    console.log(`[v0] Syncing data from source: ${sourceId}`)
    // Simulate sync process
    try {
      const source = dataSources.find((ds) => ds.id === sourceId)
      if (source?.type === "streamlit") {
        const data = await DataIntegrationService.syncKPIData()
        console.log(`[v0] Synced data:`, data)
      }
    } catch (error) {
      console.error(`[v0] Sync failed for ${sourceId}:`, error)
    }
  }

  const handleTestConnection = async (sourceId: string) => {
    console.log(`[v0] Testing connection for source: ${sourceId}`)
    const source = dataSources.find((ds) => ds.id === sourceId)
    if (source) {
      const isConnected = await DataIntegrationService.testConnection(source)
      console.log(`[v0] Connection test result:`, isConnected)
    }
  }

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-foreground">Integración de Datos</h1>
          <p className="text-muted-foreground">Gestión de fuentes de datos y sincronización</p>
        </div>
        <Button className="bg-primary text-primary-foreground">
          <Link className="h-4 w-4 mr-2" />
          Nueva Integración
        </Button>
      </div>

      {/* Estado General */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <CheckCircle className="h-5 w-5 text-green-600" />
              <div>
                <p className="text-2xl font-bold">{connectedSources.length}</p>
                <p className="text-sm text-muted-foreground">Conectadas</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <XCircle className="h-5 w-5 text-red-600" />
              <div>
                <p className="text-2xl font-bold">{disconnectedSources.length}</p>
                <p className="text-sm text-muted-foreground">Desconectadas</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <Database className="h-5 w-5 text-blue-600" />
              <div>
                <p className="text-2xl font-bold">{dataSources.length}</p>
                <p className="text-sm text-muted-foreground">Total Fuentes</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-4">
            <div className="flex items-center gap-2">
              <RefreshCw className="h-5 w-5 text-purple-600" />
              <div>
                <p className="text-2xl font-bold">98.5%</p>
                <p className="text-sm text-muted-foreground">Disponibilidad</p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Alertas de Estado */}
      {disconnectedSources.length > 0 && (
        <Alert>
          <AlertTriangle className="h-4 w-4" />
          <AlertDescription>
            Hay {disconnectedSources.length} fuente(s) de datos desconectada(s). Revisa la configuración para mantener
            los datos actualizados.
          </AlertDescription>
        </Alert>
      )}

      <Tabs defaultValue="sources" className="space-y-4">
        <TabsList>
          <TabsTrigger value="sources">Fuentes de Datos</TabsTrigger>
          <TabsTrigger value="streamlit">Integración Streamlit</TabsTrigger>
          <TabsTrigger value="sync">Sincronización</TabsTrigger>
          <TabsTrigger value="config">Configuración</TabsTrigger>
        </TabsList>

        <TabsContent value="sources" className="space-y-4">
          <div className="grid gap-4">
            {dataSources.map((source) => (
              <Card key={source.id} className="hover:shadow-md transition-shadow">
                <CardHeader>
                  <div className="flex items-start justify-between">
                    <div className="flex items-center gap-3">
                      {getTypeIcon(source.type)}
                      <div>
                        <CardTitle className="text-lg">{source.name}</CardTitle>
                        <p className="text-sm text-muted-foreground capitalize">{source.type}</p>
                      </div>
                    </div>
                    <div className="flex gap-2">
                      <Badge className={getStatusColor(source.status)}>
                        {getStatusIcon(source.status)}
                        <span className="ml-1 capitalize">{source.status}</span>
                      </Badge>
                    </div>
                  </div>
                </CardHeader>

                <CardContent className="space-y-4">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <p className="text-sm font-medium">Última Sincronización</p>
                      <p className="text-sm text-muted-foreground">{source.lastSync.toLocaleString("es-ES")}</p>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Configuración</p>
                      <p className="text-sm text-muted-foreground">
                        {source.type === "streamlit" && source.config.url}
                        {source.type === "database" && `${source.config.host}:${source.config.port}`}
                        {source.type === "api" && source.config.baseUrl}
                      </p>
                    </div>
                  </div>

                  <div className="flex gap-2">
                    <Button variant="outline" size="sm" onClick={() => handleSync(source.id)}>
                      <RefreshCw className="h-4 w-4 mr-2" />
                      Sincronizar
                    </Button>
                    <Button variant="outline" size="sm" onClick={() => handleTestConnection(source.id)}>
                      <CheckCircle className="h-4 w-4 mr-2" />
                      Probar Conexión
                    </Button>
                    <Button variant="outline" size="sm">
                      <Settings className="h-4 w-4 mr-2" />
                      Configurar
                    </Button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </TabsContent>

        <TabsContent value="streamlit" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Globe className="h-5 w-5 text-blue-600" />
                Integración con Streamlit
              </CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <Alert>
                <Code className="h-4 w-4" />
                <AlertDescription>
                  Sigue estas instrucciones para conectar tu aplicación Streamlit con el sistema DSS.
                </AlertDescription>
              </Alert>

              <div className="space-y-4">
                <div>
                  <h3 className="text-lg font-semibold mb-2">Estado de Conexión</h3>
                  <div className="flex items-center gap-2">
                    <CheckCircle className="h-5 w-5 text-green-600" />
                    <span>Streamlit Analytics conectado</span>
                    <Badge className="bg-green-100 text-green-800 border-green-200">Activo</Badge>
                  </div>
                </div>

                <div>
                  <h3 className="text-lg font-semibold mb-2">Endpoints Disponibles</h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                    <div className="p-3 bg-muted rounded-lg">
                      <code className="text-sm">/api/projects</code>
                      <p className="text-xs text-muted-foreground">Datos de proyectos</p>
                    </div>
                    <div className="p-3 bg-muted rounded-lg">
                      <code className="text-sm">/api/clients</code>
                      <p className="text-xs text-muted-foreground">Información de clientes</p>
                    </div>
                    <div className="p-3 bg-muted rounded-lg">
                      <code className="text-sm">/api/kpis</code>
                      <p className="text-xs text-muted-foreground">Métricas principales</p>
                    </div>
                    <div className="p-3 bg-muted rounded-lg">
                      <code className="text-sm">/api/service-areas</code>
                      <p className="text-xs text-muted-foreground">Áreas de servicio</p>
                    </div>
                  </div>
                </div>

                <div>
                  <h3 className="text-lg font-semibold mb-2">Código de Ejemplo</h3>
                  <div className="bg-muted p-4 rounded-lg overflow-x-auto">
                    <pre className="text-sm">
                      <code>{streamlitIntegration.sampleCode}</code>
                    </pre>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="sync" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle>Estado de Sincronización</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-4">
                <div className="flex items-center justify-between p-4 border rounded-lg">
                  <div className="flex items-center gap-3">
                    <Database className="h-5 w-5 text-blue-600" />
                    <div>
                      <p className="font-medium">KPIs Principales</p>
                      <p className="text-sm text-muted-foreground">Última sync: hace 5 min</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <Progress value={100} className="w-20" />
                    <CheckCircle className="h-4 w-4 text-green-600" />
                  </div>
                </div>

                <div className="flex items-center justify-between p-4 border rounded-lg">
                  <div className="flex items-center gap-3">
                    <Server className="h-5 w-5 text-purple-600" />
                    <div>
                      <p className="font-medium">Datos de Proyectos</p>
                      <p className="text-sm text-muted-foreground">Última sync: hace 10 min</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <Progress value={85} className="w-20" />
                    <RefreshCw className="h-4 w-4 text-blue-600 animate-spin" />
                  </div>
                </div>

                <div className="flex items-center justify-between p-4 border rounded-lg">
                  <div className="flex items-center gap-3">
                    <Globe className="h-5 w-5 text-green-600" />
                    <div>
                      <p className="font-medium">Información de Clientes</p>
                      <p className="text-sm text-muted-foreground">Última sync: hace 15 min</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <Progress value={100} className="w-20" />
                    <CheckCircle className="h-4 w-4 text-green-600" />
                  </div>
                </div>
              </div>

              <div className="flex gap-2">
                <Button onClick={() => handleSync("all")}>
                  <RefreshCw className="h-4 w-4 mr-2" />
                  Sincronizar Todo
                </Button>
                <Button variant="outline">
                  <Settings className="h-4 w-4 mr-2" />
                  Configurar Auto-sync
                </Button>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="config" className="space-y-4">
          <Card>
            <CardHeader>
              <CardTitle>Configuración de Integración</CardTitle>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-4">
                <div>
                  <h3 className="text-lg font-semibold mb-2">Configuración General</h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <label className="text-sm font-medium">Intervalo de Sincronización</label>
                      <select className="w-full mt-1 p-2 border rounded-md">
                        <option>Cada 5 minutos</option>
                        <option>Cada 15 minutos</option>
                        <option>Cada hora</option>
                        <option>Manual</option>
                      </select>
                    </div>
                    <div>
                      <label className="text-sm font-medium">Timeout de Conexión</label>
                      <select className="w-full mt-1 p-2 border rounded-md">
                        <option>30 segundos</option>
                        <option>60 segundos</option>
                        <option>120 segundos</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div>
                  <h3 className="text-lg font-semibold mb-2">Configuración de Streamlit</h3>
                  <div className="space-y-2">
                    <div>
                      <label className="text-sm font-medium">URL de la Aplicación</label>
                      <input
                        type="url"
                        className="w-full mt-1 p-2 border rounded-md"
                        placeholder="https://tu-app.streamlit.app"
                        defaultValue="https://vv-analytics.streamlit.app"
                      />
                    </div>
                    <div>
                      <label className="text-sm font-medium">API Key (Opcional)</label>
                      <input
                        type="password"
                        className="w-full mt-1 p-2 border rounded-md"
                        placeholder="Tu API key para autenticación"
                      />
                    </div>
                  </div>
                </div>

                <div className="flex gap-2">
                  <Button>Guardar Configuración</Button>
                  <Button variant="outline">Probar Conexión</Button>
                </div>
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}
