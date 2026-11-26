---
name: update-dashboard
description: >-
  Updates Pepe's learning roadmap data (progress.json and CURRICULUM.md), rebuilds
  the static public portfolio dashboard (docs/index.html) for GitHub Pages, and
  validates integrity and privacy. Use this skill whenever the user reports
  progress on a project, finishes a phase, logs study hours, selects a dataset,
  adds bibliography/resources, publishes a GitHub repo, or asks to update the
  dashboard.
---

# Update Learning Dashboard

Runbook para actualizar de forma consistente y segura el tablero público de portafolio en `D:\Proyectos\_orquestador\`.

## Pasos

### 1. Leer el estado actual
- Lee `progress.json` y `CURRICULUM.md` en `D:\Proyectos\_orquestador\`.
- Si el usuario menciona avances de un proyecto concreto y necesitas contrastar fases, lee también su `ROADMAP.md` (en la ruta indicada en `local_path`).

### 2. Confirmar datos mínimos (solo si faltan y aportan valor)
Si el usuario ya dio suficiente detalle, procede directo sin interrumpir. Si dio un reporte muy breve (ej. *"terminé la Fase 1"*), pregunta en máximo 2–3 viñetas si quiere registrar:
- **Horas invertidas** en esta sesión (para sumarlas a `hours_spent`).
- **Dataset / URL del repositorio** (si es nuevo).
- **Recursos / bibliografía** consultados o **lecciones aprendidas** (`takeaways`).

### 3. Actualizar `progress.json`
Edita `D:\Proyectos\_orquestador\progress.json` respetando su esquema:
- `meta.last_updated`: actualizar a la fecha actual (`YYYY-MM-DD`).
- En el proyecto correspondiente:
  - `status`: solo `"pending"`, `"in_progress"` o `"completed"`.
  - `status_label`: etiqueta legible en español (ej. `"En curso · Fase 2"`, `"Completado"`).
  - `hours_spent`: **sumar** las horas nuevas al valor previo (no sobrescribir el acumulado salvo corrección explícita).
  - `domain`, `repo_url`, `dataset` (`name`, `url`, `notes`): completar o refinar según lo reportado.
  - `phases` y `learning_outcomes` (`data_ml`, `agentic`, `git_cicd`): marcar `done: true` en lo completado; agregar ítems nuevos si surgieron aprendizajes extra.
  - `skills` y `slash_commands`: añadir nuevas skills o comandos practicados sin duplicados.
  - `resources`: agregar documentación, artículos, libros o cursos con `title`, `type`, `url` y `notes`.
  - `takeaways`: registrar aprendizajes clave al cerrar fases o el proyecto.
- `timeline`: insertar la nueva entrada **al inicio** de la lista (`date`, `project_id`, `tag`, `title`, `details`) para mantener orden cronológico inverso.

> **Regla de privacidad (portafolio público):** Nunca escribir rutas locales de Windows (`D:\...`), información de hardware privada ni credenciales en campos públicos (`summary`, `dataset.notes`, `timeline`, `takeaways`, `resources`). El único campo privado permitido es `local_path`, que `build_dashboard.py` excluye al generar el HTML.

### 4. Sincronizar `CURRICULUM.md`
- Si cambió el estado de algún proyecto, actualiza la columna **Estado** en la tabla de `D:\Proyectos\_orquestador\CURRICULUM.md`.
- Añade una línea breve con la fecha en **Bitácora de Avance y Aprendizajes** cuando haya un hito relevante.

### 5. Reconstruir y validar el dashboard
Ejecuta desde `D:\Proyectos\_orquestador\`:

```powershell
python build_dashboard.py; if ($LASTEXITCODE -eq 0) { python build_dashboard.py --check }
```

Verifica que ambos comandos terminen con código de salida `0` y que el output confirme que `docs/index.html` está actualizado.

### 6. Commit automático y publicación en GitHub Pages
- Revisa `git status` dentro de `D:\Proyectos\_orquestador\`.
- Si hay cambios en los archivos del tablero (`progress.json`, `CURRICULUM.md`, `docs/index.html`, etc.), crea un commit limpio con formato Conventional Commits (ej. `chore(progress): update project 1 phase 1 progress`).
- Pregunta a Pepe si quiere hacer `git push` ahora mismo (o haz `git push` directo si ya lo pidió en su mensaje) para disparar el deploy automático en GitHub Pages.
- Devuelve un resumen breve con el nuevo **progreso global (%)**, estado del proyecto actualizado, **horas acumuladas** y enlaces a `docs/index.html` y al dashboard publicado (`https://jrvalenzuela.github.io/ds-ml-learning-roadmap/`).
