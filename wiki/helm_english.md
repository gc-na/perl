# [Linux] C Shell (csh) helm用法: Manage Kubernetes applications

## Overview
The `helm` command is a package manager for Kubernetes that simplifies the deployment and management of applications on Kubernetes clusters. It allows users to define, install, and upgrade even the most complex Kubernetes applications using Helm charts.

## Usage
The basic syntax of the `helm` command is as follows:

```bash
helm [options] [arguments]
```

## Common Options
- `install`: Installs a new chart.
- `upgrade`: Upgrades a release to a new version.
- `uninstall`: Removes a release from the cluster.
- `list`: Lists all the releases in the cluster.
- `repo`: Manages Helm chart repositories.

## Common Examples
Here are some practical examples of using the `helm` command:

1. **Installing a chart**:
   ```bash
   helm install my-release stable/mysql
   ```

2. **Upgrading a release**:
   ```bash
   helm upgrade my-release stable/mysql --set mysqlRootPassword=secret
   ```

3. **Uninstalling a release**:
   ```bash
   helm uninstall my-release
   ```

4. **Listing all releases**:
   ```bash
   helm list
   ```

5. **Adding a chart repository**:
   ```bash
   helm repo add stable https://charts.helm.sh/stable
   ```

## Tips
- Always check the official documentation for the latest options and commands.
- Use `helm search` to find available charts in your repositories.
- Keep your Helm repositories updated with `helm repo update` to ensure you have the latest charts.