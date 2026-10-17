"""Blender-only disposable asset pipeline probe; does not define game art."""
import json
import math
import sys
from pathlib import Path

import bpy

output = Path(sys.argv[sys.argv.index("--") + 1]).resolve()
output.mkdir(parents=True, exist_ok=True)
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
model = bpy.context.object
model.name = "AssetPipelineProbe"
model.rotation_euler = (math.radians(18), math.radians(15), math.radians(25))
material = bpy.data.materials.new("ProbeMaterial")
material.diffuse_color = (0.12, 0.38, 0.72, 1)
model.data.materials.append(material)

bpy.ops.object.camera_add(location=(4, -6, 4))
camera = bpy.context.object
from mathutils import Vector
camera.rotation_euler = (Vector((0, 0, 0)) - camera.location).to_track_quat("-Z", "Y").to_euler()
bpy.context.scene.camera = camera
bpy.ops.object.light_add(type="AREA", location=(2, -4, 6))
bpy.context.object.data.energy = 800
bpy.context.object.data.shape = "DISK"
bpy.context.object.data.size = 5

scene = bpy.context.scene
scene.render.engine = "CYCLES"
scene.cycles.device = "CPU"
scene.cycles.samples = 8
scene.render.threads_mode = "FIXED"
scene.render.threads = 4
scene.render.resolution_x = 256
scene.render.resolution_y = 256
scene.render.resolution_percentage = 100
scene.render.film_transparent = True
scene.render.image_settings.file_format = "PNG"
scene.render.image_settings.color_mode = "RGBA"
scene.render.filepath = str(output / "render-probe.png")

bpy.ops.wm.save_as_mainfile(filepath=str(output / "model-probe.blend"))
bpy.ops.render.render(write_still=True)
bpy.ops.object.select_all(action="DESELECT")
model.select_set(True)
bpy.context.view_layer.objects.active = model
bpy.ops.export_scene.gltf(filepath=str(output / "model-probe.glb"), export_format="GLB", use_selection=True)
(output / "blender-version.json").write_text(json.dumps({
    "version": bpy.app.version_string,
    "render_engine": scene.render.engine,
    "render_device": scene.cycles.device,
    "outputs": ["model-probe.blend", "model-probe.glb", "render-probe.png"],
}, indent=2), encoding="utf-8")
print("Blender asset verification passed.")
