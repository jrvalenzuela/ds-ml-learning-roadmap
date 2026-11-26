"""Generador estático del Dashboard de Portfolio y Avance de Aprendizaje.

Lee `progress.json` y `templates/dashboard.html` y genera `docs/index.html`
listo para abrir localmente con doble clic o publicar gratis en GitHub Pages.
Sin dependencias externas (solo biblioteca estándar de Python 3.11+).
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "progress.json"
TEMPLATE_PATH = ROOT / "templates" / "dashboard.html"
OUTPUT_DIR = ROOT / "docs"
OUTPUT_HTML = OUTPUT_DIR / "index.html"
NOJEKYLL_PATH = OUTPUT_DIR / ".nojekyll"

VALID_STATUSES = {"pending", "in_progress", "completed"}
PILLARS = ("data_ml", "agentic", "git_cicd")


def validate_data(raw: dict[str, Any]) -> None:
    if "meta" not in raw or "projects" not in raw:
        raise ValueError("progress.json debe contener las claves 'meta' y 'projects'.")
    if not isinstance(raw["projects"], list) or not raw["projects"]:
        raise ValueError("'projects' debe ser una lista no vacía.")
    for project in raw["projects"]:
        for required in ("id", "number", "title", "status"):
            if required not in project:
                raise ValueError(f"Proyecto sin campo requerido '{required}': {project}")
        if project["status"] not in VALID_STATUSES:
            raise ValueError(
                f"Estado inválido '{project['status']}' en proyecto '{project['id']}'. "
                f"Válidos: {sorted(VALID_STATUSES)}"
            )


def enrich_for_public_dashboard(raw: dict[str, Any]) -> dict[str, Any]:
    """Calcula métricas agregadas y omite rutas locales privadas del output público."""
    public_projects: list[dict[str, Any]] = []

    total_phases_done = 0
    total_phases_required = 0
    total_outcomes_done = 0
    total_outcomes = 0
    total_hours_spent = 0.0
    total_hours_estimated = 0.0
    total_resources = 0
    all_skills: set[str] = set()

    counts = {"completed": 0, "in_progress": 0, "pending": 0}
    pillar_totals = {p: {"done": 0, "total": 0} for p in PILLARS}

    for project in raw["projects"]:
        counts[project["status"]] += 1

        phases = project.get("phases", [])
        required_phases = [ph for ph in phases if not ph.get("optional")]
        phases_done = sum(1 for ph in required_phases if ph.get("done"))
        phases_total = len(required_phases)
        total_phases_done += phases_done
        total_phases_required += phases_total

        outcomes_by_pillar = project.get("learning_outcomes", {})
        proj_outcomes_done = 0
        proj_outcomes_total = 0
        for pillar in PILLARS:
            items = outcomes_by_pillar.get(pillar, [])
            done_count = sum(1 for item in items if item.get("done"))
            pillar_totals[pillar]["done"] += done_count
            pillar_totals[pillar]["total"] += len(items)
            proj_outcomes_done += done_count
            proj_outcomes_total += len(items)

        total_outcomes_done += proj_outcomes_done
        total_outcomes += proj_outcomes_total

        hours_spent = float(project.get("hours_spent", 0) or 0)
        hours_estimated = float(project.get("hours_estimated", 0) or 0)
        total_hours_spent += hours_spent
        total_hours_estimated += hours_estimated

        resources = project.get("resources", [])
        total_resources += len(resources)
        all_skills.update(project.get("skills", []))

        # Progreso del proyecto: combina fases obligatorias y aprendizajes esperados
        denom = phases_total + proj_outcomes_total
        if project["status"] == "completed":
            progress_pct = 100
        elif denom > 0:
            progress_pct = round(((phases_done + proj_outcomes_done) / denom) * 100)
        else:
            progress_pct = 0

        # Copiamos el proyecto excluyendo `local_path` para mantener el portafolio público limpio
        public_proj = {k: v for k, v in project.items() if k != "local_path"}
        public_proj["computed_progress"] = progress_pct
        public_proj["computed_phases_done"] = phases_done
        public_proj["computed_phases_total"] = phases_total
        public_projects.append(public_proj)

    overall_denom = total_phases_required + total_outcomes
    overall_progress = (
        round(((total_phases_done + total_outcomes_done) / overall_denom) * 100)
        if overall_denom > 0
        else 0
    )

    pillars_stats = {
        pillar: {
            "done": vals["done"],
            "total": vals["total"],
            "pct": round((vals["done"] / vals["total"]) * 100) if vals["total"] > 0 else 0,
        }
        for pillar, vals in pillar_totals.items()
    }

    def fmt_hours(value: float) -> int | float:
        return int(value) if value.is_integer() else round(value, 1)

    return {
        "meta": raw["meta"],
        "projects": public_projects,
        "timeline": raw.get("timeline", []),
        "stats": {
            "overall_progress": overall_progress,
            "total_projects": len(public_projects),
            "completed": counts["completed"],
            "in_progress": counts["in_progress"],
            "pending": counts["pending"],
            "phases_done": total_phases_done,
            "phases_total": total_phases_required,
            "outcomes_done": total_outcomes_done,
            "outcomes_total": total_outcomes,
            "hours_spent": fmt_hours(total_hours_spent),
            "hours_estimated": fmt_hours(total_hours_estimated),
            "skills_total": len(all_skills),
            "resources_total": total_resources,
            "pillars": pillars_stats,
        },
    }


def render_html(payload: dict[str, Any]) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    # Escapar cierre de etiquetas script por seguridad al inyectar JSON en HTML
    safe_json = json.dumps(payload, ensure_ascii=False, indent=2).replace("</", "<\\/")

    title = html.escape(payload["meta"].get("title", "Learning Dashboard"))
    description = html.escape(payload["meta"].get("subtitle", ""))

    return (
        template.replace("__PAGE_TITLE__", title)
        .replace("__PAGE_DESCRIPTION__", description)
        .replace("__DASHBOARD_DATA__", safe_json)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Construye el dashboard estático para GitHub Pages.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Valida progress.json y verifica que docs/index.html está actualizado sin escribir.",
    )
    args = parser.parse_args()

    raw = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    validate_data(raw)
    payload = enrich_for_public_dashboard(raw)
    rendered = render_html(payload)

    if args.check:
        if not OUTPUT_HTML.exists():
            raise SystemExit("ERROR: docs/index.html no existe. Ejecuta `python build_dashboard.py`.")
        current = OUTPUT_HTML.read_text(encoding="utf-8")
        if current != rendered:
            raise SystemExit(
                "ERROR: docs/index.html está desactualizado respecto a progress.json. "
                "Ejecuta `python build_dashboard.py`."
            )
        print("OK: progress.json válido y docs/index.html actualizado.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML.write_text(rendered, encoding="utf-8")
    NOJEKYLL_PATH.write_text("", encoding="utf-8")

    s = payload["stats"]
    print(
        f"Dashboard generado en {OUTPUT_HTML} | "
        f"Progreso global: {s['overall_progress']}% | "
        f"Proyectos: {s['total_projects']} ({s['in_progress']} en curso) | "
        f"Horas: {s['hours_spent']}h / {s['hours_estimated']}h"
    )


if __name__ == "__main__":
    main()
