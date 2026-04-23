#!/usr/bin/env python3
"""Validate example-report.json against report-schema.json.

Usage:
    python3 scripts/validate_schema.py

Exit codes:
    0 — validation passed
    1 — validation failed
"""

import json, os, sys

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    schema_path = os.path.join(root, "references", "report-schema.json")
    example_path = os.path.join(root, "references", "example-report.json")

    errors = []

    # --- Check files exist ---
    for p in (schema_path, example_path):
        if not os.path.exists(p):
            errors.append(f"File not found: {p}")
    if errors:
        for e in errors:
            print(f"❌ {e}")
        sys.exit(1)

    # --- Load JSON ---
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in schema: {e}")
        sys.exit(1)

    try:
        with open(example_path, "r", encoding="utf-8") as f:
            report = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in example report: {e}")
        sys.exit(1)

    # --- Basic structural validation (stdlib only, no jsonschema dependency) ---
    required_top = ["schema_version", "executive_verdict", "scope", "evidence_pack", "findings", "conflict_map", "ordered_fix_plan"]
    for key in required_top:
        if key not in report:
            errors.append(f"Missing top-level key: {key}")

    # schema_version
    if report.get("schema_version") != "oh-my-agent-check.report.v1":
        errors.append(f"schema_version must be 'oh-my-agent-check.report.v1', got: {report.get('schema_version')}")

    # executive_verdict
    ev = report.get("executive_verdict", {})
    for k in ("overall_health", "primary_failure_mode", "most_urgent_fix"):
        if k not in ev:
            errors.append(f"executive_verdict missing: {k}")
    valid_health = {"critical", "high_risk", "unstable", "acceptable", "strong"}
    if ev.get("overall_health") not in valid_health:
        errors.append(f"overall_health must be one of {valid_health}, got: {ev.get('overall_health')}")

    # scope
    sc = report.get("scope", {})
    for k in ("target_name", "entrypoints", "channels", "model_stack", "time_window", "layers_to_audit"):
        if k not in sc:
            errors.append(f"scope missing: {k}")
    valid_layers = {
        "system_prompt", "session_history", "long_term_memory", "distillation",
        "active_recall", "tool_selection", "tool_execution", "tool_interpretation",
        "answer_shaping", "platform_rendering", "fallback_loops", "persistence"
    }
    for layer in sc.get("layers_to_audit", []):
        if layer not in valid_layers:
            errors.append(f"Invalid layer in scope: {layer}")

    # evidence_pack
    ep = report.get("evidence_pack", [])
    if not isinstance(ep, list) or len(ep) < 1:
        errors.append("evidence_pack must be a non-empty array")
    valid_kinds = {"code", "log", "db", "config", "screenshot", "test"}
    valid_time = {"current_state", "historical_state", "both"}
    for i, item in enumerate(ep):
        for k in ("kind", "source", "location", "summary", "time_scope"):
            if k not in item:
                errors.append(f"evidence_pack[{i}] missing: {k}")
        if item.get("kind") not in valid_kinds:
            errors.append(f"evidence_pack[{i}].kind must be one of {valid_kinds}")
        if item.get("time_scope") not in valid_time:
            errors.append(f"evidence_pack[{i}].time_scope must be one of {valid_time}")

    # findings
    findings = report.get("findings", [])
    if not isinstance(findings, list):
        errors.append("findings must be an array")
    valid_sev = {"critical", "high", "medium", "low"}
    valid_fix = {"code_gate", "prompt_removal", "prompt_tightening", "state_cleanup", "architecture_change"}
    for i, f_item in enumerate(findings):
        for k in ("severity", "title", "symptom", "user_impact", "source_layer",
                   "mechanism", "root_cause", "evidence_refs", "confidence",
                   "fix_type", "recommended_fix"):
            if k not in f_item:
                errors.append(f"findings[{i}] missing: {k}")
        if f_item.get("severity") not in valid_sev:
            errors.append(f"findings[{i}].severity must be one of {valid_sev}")
        if f_item.get("fix_type") not in valid_fix:
            errors.append(f"findings[{i}].fix_type must be one of {valid_fix}")
        conf = f_item.get("confidence")
        if not isinstance(conf, (int, float)) or not (0 <= conf <= 1):
            errors.append(f"findings[{i}].confidence must be 0.0-1.0, got: {conf}")
        if not isinstance(f_item.get("evidence_refs"), list) or len(f_item.get("evidence_refs", [])) < 1:
            errors.append(f"findings[{i}].evidence_refs must be a non-empty array")

    # conflict_map
    conflicts = report.get("conflict_map", [])
    valid_ct = {"stale_state", "duplication", "contradiction", "amplification", "silent_override"}
    for i, c in enumerate(conflicts):
        for k in ("from_layer", "to_layer", "conflict_type", "note"):
            if k not in c:
                errors.append(f"conflict_map[{i}] missing: {k}")
        if c.get("conflict_type") not in valid_ct:
            errors.append(f"conflict_map[{i}].conflict_type must be one of {valid_ct}")

    # ordered_fix_plan
    plan = report.get("ordered_fix_plan", [])
    for i, p_item in enumerate(plan):
        for k in ("order", "goal", "why_now", "expected_effect"):
            if k not in p_item:
                errors.append(f"ordered_fix_plan[{i}] missing: {k}")
        if not isinstance(p_item.get("order"), int) or p_item.get("order", 0) < 1:
            errors.append(f"ordered_fix_plan[{i}].order must be an integer >= 1")

    # --- Result ---
    if errors:
        print(f"❌ Validation FAILED — {len(errors)} error(s):\n")
        for e in errors:
            print(f"  • {e}")
        sys.exit(1)
    else:
        print("✅ Schema validation PASSED")
        print(f"   schema_version: {report['schema_version']}")
        print(f"   overall_health: {ev['overall_health']}")
        print(f"   findings: {len(findings)} ({sum(1 for f in findings if f['severity'] == 'critical')}C / {sum(1 for f in findings if f['severity'] == 'high')}H / {sum(1 for f in findings if f['severity'] == 'medium')}M / {sum(1 for f in findings if f['severity'] == 'low')}L)")
        print(f"   evidence: {len(ep)}")
        print(f"   conflicts: {len(conflicts)}")
        print(f"   fix plan: {len(plan)} steps")
        sys.exit(0)

if __name__ == "__main__":
    main()
