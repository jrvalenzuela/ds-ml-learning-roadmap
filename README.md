# Ruta de Aprendizaje · Ciencia de Datos, ML & Desarrollo Agéntico

Repositorio central de seguimiento y **dashboard público de portafolio** para mi ruta práctica de proyectos de Ciencia de Datos, Machine Learning, CI/CD con GitHub Actions y Desarrollo Agéntico.

## Qué incluye este repositorio

- [`progress.json`](progress.json): Fuente única de verdad con el estado de cada proyecto, fases, horas invertidas, dataset, aprendizajes esperados en 3 pilares (Datos/ML, Desarrollo Agéntico, Git/CI-CD), bibliografía y bitácora.
- [`templates/dashboard.html`](templates/dashboard.html): Plantilla visual responsiva con modo claro/oscuro, filtros, buscador y desglose por proyecto.
- [`build_dashboard.py`](build_dashboard.py): Generador liviano en Python puro (sin dependencias externas) que valida `progress.json` y construye `docs/index.html` omitiendo rutas locales privadas.
- [`.github/workflows/pages.yml`](.github/workflows/pages.yml): Workflow de GitHub Actions que reconstruye y publica automáticamente el dashboard en **GitHub Pages** en cada `push` a `main`.
- [`.agents/skills/update-dashboard/SKILL.md`](.agents/skills/update-dashboard/SKILL.md): Skill agéntica para actualizar avances, horas, datasets, bibliografía y regenerar/validar el dashboard en un solo flujo.
- [`CURRICULUM.md`](CURRICULUM.md): Resumen editorial de la ruta de aprendizaje.

## Cómo actualizar el dashboard en local

1. Edita [`progress.json`](progress.json) (o pídele al Orquestador que actualice tus avances, horas, dataset o bibliografía).
2. Ejecuta:
   ```bash
   python build_dashboard.py
   ```
3. Abre `docs/index.html` directamente en tu navegador (funciona sin servidor local).

Para validar integridad sin sobrescribir:
```bash
python build_dashboard.py --check
```

## Cómo publicarlo en GitHub Pages (3 pasos)

1. Crea un repositorio público en GitHub (por ejemplo `ds-ml-learning-roadmap`) y sube esta carpeta a la rama `main`:
   ```bash
   git init -b main
   git add .
   git commit -m "feat: initial learning roadmap dashboard"
   git remote add origin https://github.com/jrvalenzuela/ds-ml-learning-roadmap.git
   git push -u origin main
   ```
2. En GitHub, ve a **Settings → Pages → Build and deployment → Source** y selecciona **GitHub Actions**.
3. El workflow `Build & Deploy Learning Dashboard` construirá y publicará automáticamente el dashboard en:
   `https://jrvalenzuela.github.io/ds-ml-learning-roadmap/`

> **Personalización rápida:** Actualiza `"author"` y `"github_profile"` en `progress.json` y vuelve a ejecutar `python build_dashboard.py`.
