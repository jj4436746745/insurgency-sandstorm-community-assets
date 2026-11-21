# Pilotable Little Bird

A player-flown Little Bird for custom Sandstorm maps. It uses the stock Sandstorm vehicle, seat, and audio systems. Place the helicopter once per desired spawn location. The helicopter creates its input relay during gameplay.

This pack targets the Sandstorm Mod Editor (UE 4.27.2). The staging check found no missing package references. Clean SDK import and gameplay validation are pending.

## Installation

1. Close the Sandstorm Mod Editor. Open the ZIP and merge the contents of its `Content` folder into `SandstormEditor/Insurgency/Content`. Keep the directory structure intact so the helicopter and both shared material packages load under their existing `/Game/...` paths.
2. Open the Sandstorm Mod Editor (UE 4.27.2) and your mod. Drag `BP_LittleBirdPilotable` from `/Game/Assets/MyBlueprints/LittleBirdPilotable` into a level that loads for the intended scenario. The airframe is assembled at runtime, so use the actor transform to position it in the editor.
3. On the placed helicopter, turn off **Despawn on Round Reset**. The helicopter Blueprint handles its own round reset and respawns from its placed transform.
4. Leave a clear area around the cockpit and both benches. Check boarding, all five seat exits, and the first round reset in your map. Test a cooked build for audio and multiplayer behavior.

## Dependencies

The archive includes two shared material instances at their original package paths. Check any existing copies before overwriting them.

- Glass uses `/Game/Assets/MyBlueprints/UnbreakableGlassOnly/MI_Generic_Window_BulletProofGlass_01`.
- Benches use `/Game/Assets/MyMaterials/Humvee/MI_Humvee_BlackRubber`.

The stock vehicle, seat, and audio assets come from the Sandstorm SDK.

## Model credit

The airframe is adapted from Helicopters MH-6 Little Bird by mario low poly. The conversion splits out the glass and rotors, changes axes and scale for Unreal, adjusts pivots, removes the source weapon geometry, and adds passenger benches. [Original model](https://sketchfab.com/3d-models/helicopters-mh-6-little-bird-69cb05db3fc3483cb729734262abf28e) · [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/)

CC BY 4.0 applies to the credited airframe adaptation. Reuse terms for the Blueprints and other pack files are pending. The two shared material instances have no separately documented redistribution terms.
