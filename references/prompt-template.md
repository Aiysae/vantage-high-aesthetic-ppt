# Embedded-image prompt template

Use one prompt per slide. Keep the wording exact for all visible text.

~~~text
Use case: productivity-visual
Asset type: finished <aspect ratio> PowerPoint slide image
Primary request: create one finished editorial scene where the visual metaphor and all visible text are generated together
Scene/backdrop: <background and environment>
Main scene: <3–5 objects, each with a semantic role>
Spatial relationship: <what the arrangement means>
Composition/framing: <camera angle, focal point, negative-space area, crop safety>
Style/medium: tactile miniature set, editorial still-life photography, realistic materials
Lighting/mood: <direction, softness, emotional temperature>
Color palette: <neutral base + main accent + optional secondary>
Text (verbatim):
1. title: “...”
2. subtitle: “...”
3. physical label on <object>: “...”
4. physical label on <object>: “...”
Typography: <Chinese type character, size hierarchy, material surface>
Constraints: every phrase above must be legible simplified Chinese and physically integrated into the scene; no extra words; no logo; no watermark
Avoid: pasted text boxes, floating UI labels, garbled Chinese, random characters, clutter, collage, cartoon style
~~~

## Example: FDE definition page

~~~text
Primary request: a copper bridge connecting a rough-stone business world to translucent-blue AI product blocks
Main scene: left objects represent people, process, and data; right objects represent Prompt, Skill, and Agent; one faceless woven figure crosses the bridge
Text (verbatim):
1. title: “FDE：把业务问题变成可验证产品”
2. subtitle: “深入现场，理解 SOP，推动采用”
3. paper label: “人”
4. paper label: “流程”
5. paper label: “数据”
6. glass labels: “Prompt”, “Skill”, “Agent”
7. bridge plaque: “FDE”
~~~

The title, subtitle, and labels remain inside the generated image. The PPT page contains the image as a full-bleed asset.
