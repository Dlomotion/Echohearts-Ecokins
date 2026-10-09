"""Blender 4.x: read-only Eco-Kin mesh/rig validation; run in Blender Python."""
import bpy
import json

def audit():
    issues = []
    meshes = [obj for obj in bpy.data.objects if obj.type == "MESH"]
    armatures = [obj for obj in bpy.data.objects if obj.type == "ARMATURE"]
    if not meshes:
        issues.append("No mesh objects")
    if not armatures:
        issues.append("No armature objects")
    for obj in meshes:
        if any(abs(v - 1.0) > 0.001 for v in obj.scale):
            issues.append(f"{obj.name}: unapplied scale")
        if not any(m.type == "ARMATURE" for m in obj.modifiers):
            issues.append(f"{obj.name}: missing armature modifier")
        if len(obj.data.materials) == 0:
            issues.append(f"{obj.name}: missing materials")
    return {"status": "PASS" if not issues else "REVIEW", "mesh_count": len(meshes),
            "armature_count": len(armatures), "issues": issues,
            "note": "Approval, provenance and UE import are separate checks."}

if __name__ == "__main__":
    print(json.dumps(audit(), indent=2))
