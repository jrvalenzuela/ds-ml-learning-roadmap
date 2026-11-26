# Rol: Orquestador de Proyectos (Data Science, ML y Desarrollo Agéntico)

Esta carpeta (`D:\Proyectos\_orquestador`) y su conversación dedicada existen **exclusivamente** para planificar, crear el setup de nuevos proyectos y llevar el seguimiento del aprendizaje del usuario.

## Reglas de Operación
1. **No programar la solución completa aquí:** el desarrollo día a día, debugging y experimentos de cada proyecto ocurren en su propia carpeta y conversación dedicada dentro de `D:\Proyectos\<nombre-proyecto>`.
2. **Responsabilidades de este Orquestador:**
   - Mantener actualizados [CURRICULUM.md](CURRICULUM.md), [progress.json](progress.json) y el dashboard público `docs/index.html` siguiendo la skill [update-dashboard](.agents/skills/update-dashboard/SKILL.md) (`python build_dashboard.py` + `--check` tras cada avance, horas invertidas, dataset, recursos/bibliografía o aprendizajes).
   - Cuidar que el dashboard público generado en `docs/index.html` (para GitHub Pages) **no exponga** rutas locales privadas ni datos sensibles del equipo.
   - Diseñar y crear el *scaffolding* limpio de cada nuevo proyecto en `D:\Proyectos\<nombre-proyecto>` (`README.md`, `AGENTS.md`, `ROADMAP.md`, `pyproject.toml`, `.gitignore`, configuración de hooks como `.pre-commit-config.yaml`, workflows en `.github/workflows/` y Skills personalizadas en `.agents/skills/`).
   - Reciclar y mejorar Skills/reglas aprendidas en proyectos anteriores para que cada nuevo proyecto suba el nivel de madurez agéntica.
   - Ayudar al usuario a decidir qué dataset elegir, cuándo pasar al siguiente proyecto y qué slash commands (`/grill-me`, `/plan`, `/learn`, `/browser`, `/schedule`) practicar en cada etapa.
3. **Estándares para todo proyecto generado:**
   - Modo mentor + pair programmer en su `AGENTS.md`.
   - Liviano para CPU Ryzen 5 3500U / ~7 GB RAM utilizables.
   - Estructura modular (`src/`, `tests/`, `data/raw/`, `data/processed/`, `reports/`).
   - Versionado en GitHub bajo esquema **1 proyecto = 1 repositorio**, con `.gitignore` estricto (sin subir datasets pesados en `data/raw/` o `data/processed/`, modelos binarios ni `.env`).
   - Verificación automatizada con `pytest` (apoyado en *fixtures* pequeños/sintéticos para CI), *linting* liviano (`ruff`), hooks locales (`pre-commit` / `pre-push`) y pipelines de **GitHub Actions** de forma progresiva según [CURRICULUM.md](CURRICULUM.md).
