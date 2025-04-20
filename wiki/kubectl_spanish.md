# [Linux] C Shell (csh) kubectl Uso: Interactuar con clústeres de Kubernetes

## Overview
El comando `kubectl` es la herramienta de línea de comandos para interactuar con clústeres de Kubernetes. Permite a los usuarios gestionar aplicaciones, inspeccionar recursos y realizar diversas operaciones en el entorno de Kubernetes.

## Usage
La sintaxis básica del comando `kubectl` es la siguiente:

```bash
kubectl [opciones] [argumentos]
```

## Common Options
- `get`: Recupera información sobre recursos específicos.
- `apply`: Aplica cambios a los recursos de Kubernetes a partir de un archivo de configuración.
- `delete`: Elimina recursos de Kubernetes.
- `describe`: Muestra detalles sobre un recurso específico.
- `logs`: Recupera los registros de un contenedor en un pod.

## Common Examples
Aquí hay algunos ejemplos prácticos del uso de `kubectl`:

1. **Listar todos los pods en el clúster**:
   ```bash
   kubectl get pods
   ```

2. **Aplicar un archivo de configuración**:
   ```bash
   kubectl apply -f mi-configuracion.yaml
   ```

3. **Eliminar un pod específico**:
   ```bash
   kubectl delete pod nombre-del-pod
   ```

4. **Describir un servicio**:
   ```bash
   kubectl describe service nombre-del-servicio
   ```

5. **Ver los registros de un contenedor**:
   ```bash
   kubectl logs nombre-del-pod
   ```

## Tips
- Asegúrate de tener configurado el contexto correcto para trabajar con el clúster deseado.
- Utiliza `kubectl get all` para obtener una vista general de todos los recursos en el espacio de nombres actual.
- Puedes usar `--namespace` para especificar un espacio de nombres diferente si no estás trabajando en el espacio de nombres por defecto.
- Combina `kubectl` con herramientas como `grep` para filtrar resultados y obtener información más específica.