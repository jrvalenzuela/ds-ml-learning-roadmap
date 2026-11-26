# Plan de Aprendizaje · Ciencia de Datos, ML y Desarrollo Agéntico

## Perfil y Contexto del Estudiante
- **Estudiante:** José ("Pepe") · GitHub: https://github.com/jrvalenzuela
- **Objetivo:** Profundizar en Ciencia de Datos, Análisis de Datos y Machine Learning aprendiendo haciendo, mientras domina el **desarrollo agéntico** (Antigravity / Claude Code).
- **Experiencia previa:** Usa Claude y Claude Code en el trabajo; comenzando con Antigravity y Gemini.
- **Temáticas preferidas:** Deportes, Educación y Finanzas.
- **Directorio base de proyectos:** `D:\Proyectos\`
- **Restricción de hardware local:** HUAWEI MateBook D15 (`BOHK-WAX9X`), AMD Ryzen 5 3500U, ~6,94 GB de RAM utilizable, sin GPU NVIDIA. Priorizar Python ligero en CPU (`pandas`, `polars`, `duckdb`, `sqlite`, `pandera`, `scikit-learn`, `lightgbm`, `plotly`, `pytest`) o Colab/Kaggle solo cuando haga falta GPU.
- **Versionado y CI/CD:** GitHub con **1 repositorio por proyecto**, `.gitignore` estricto para datos pesados/secretos, hooks locales livianos (`pre-commit` / `pre-push`) y pipelines progresivos en **GitHub Actions**.

---

## Ruta de Proyectos

| # | Proyecto | Carpeta | Estado | Foco Datos / ML | Foco Agéntico | Foco Git / CI-CD |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Pipeline de EDA y Calidad de Datos Reproducible** | `D:\Proyectos\eda-data-quality-pipeline` | Creado (listo para Fase 1) | Limpieza, validación (`pandera`), EDA, visualización | `AGENTS.md`, primera Skill (`data-audit`), TDD (`pytest`), `/browser` | Repo GitHub, `.gitignore` para datos, `pre-commit` liviano (`ruff`, bloqueo de archivos grandes) y primer `ci.yml` (`ruff` + `pytest`) |
| 2 | **Laboratorio de ML Tabular (estilo Kaggle en producción)** | `D:\Proyectos\ml-tabular-lab` | Pendiente | Feature engineering, CV, métricas, `LightGBM`, `SHAP`, sin *leakage* | `/grill-me` + `/plan`, Skill `leakage-check`, registro de experimentos | Flujo con ramas + PRs, hook `pre-push` / CI con *smoke test* sintético y tests anti-*data leakage* |
| 3 | **Analista Conversacional Text-to-SQL con Evaluaciones** | `D:\Proyectos\text-to-sql-evals` | Pendiente | SQL analítico (`DuckDB`/`SQLite`), *tool calling*, Evals | Conexión **MCP**, subagentes para generar *edge cases* | CI separado: tests deterministas en cada push + *evals* con LLM en `workflow_dispatch` usando GitHub Secrets |
| 4 | **Pipeline Automatizado con API Real + Data Drift** | `D:\Proyectos\api-drift-pipeline` | Pendiente | Ingesta API, `Parquet`, detección de *drift*, monitoreo | `/schedule`, hooks de validación, manejo de fallos | GitHub Actions con `schedule` (cron en la nube), subida de reportes como *artifacts* y alertas automáticas (ej. Issue si hay *drift*) |
| 5 | **Mini-Equipo Multi-Agente de Análisis de Datos** | `D:\Proyectos\multi-agent-analyst` | Pendiente | Pensamiento crítico estadístico, comunicación ejecutiva | Subagentes / `/teamwork`, gestión de contexto (`/compact`) | Rama `main` protegida con checks obligatorios, plantilla de PR y publicación automática de reportes (*artifacts* / GitHub Pages) |

---

## Bitácora de Avance y Aprendizajes
- **2026-11-25:** Se inicializó el Proyecto #1 (`D:\Proyectos\eda-data-quality-pipeline`) con `AGENTS.md`, `ROADMAP.md`, `pyproject.toml` y la skill `data-audit`.
- **2026-11-26:** Se incorporó GitHub (1 repo por proyecto), hooks locales (`pre-commit` / `pre-push`) y GitHub Actions como estándar progresivo de la ruta. Pendiente agregar el setup inicial de Git/GitHub Actions (`ruff` + `pytest` + `pre-commit`) dentro de la conversación dedicada del Proyecto #1.
- **2026-11-26:** Se creó el **Dashboard de Portafolio y Avance** (`progress.json` + `build_dashboard.py` → `docs/index.html`) listo para abrir localmente y publicarse automáticamente en **GitHub Pages** mediante `.github/workflows/pages.yml`, incluyendo seguimiento de horas invertidas, dataset, aprendizajes por pilar y bibliografía.
- **2026-11-26:** Se eligió el dataset del Proyecto #1 (Deportes): **International Football Results (1872–presente)** (`martj42/international_results`: `results.csv`, `shootouts.csv`, `goalscorers.csv`).
