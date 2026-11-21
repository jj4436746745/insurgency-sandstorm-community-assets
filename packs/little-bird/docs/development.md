# Little Bird development

Both Blueprints live under `/Game/Assets/MyBlueprints/LittleBirdPilotable/`.

- [`BP_LittleBirdPilotable`](../Content/Assets/MyBlueprints/LittleBirdPilotable/BP_LittleBirdPilotable.uasset) is the helicopter actor placed in a scenario. Its `ServerHousekeeping` graph creates the player-owned input relay at runtime.
- [`BP_LittleBirdPilotInput`](../Content/Assets/MyBlueprints/LittleBirdPilotable/BP_LittleBirdPilotInput.uasset) reads local player input and sends requests to the server.

| Area | Where to start |
| --- | --- |
| Flight | The relay's `FlyAsPilot` passes controls to the helicopter's `SimulateFlight`, which handles movement and collision. The relay's `ServerPilotPose` event calls `ApplyPilotPose`. On the helicopter, `FollowNetPose` smooths replicated movement. |
| Seats | Start in the relay's `EventGraph` at `ServerUse` for boarding and exiting. On the helicopter, `TryBoard` handles fallback boarding, `ClearSeat` handles seat cleanup, and `SetupPilotRig` creates exit points. |
| Navigation lights | The helicopter's `InitializeVisuals` creates the lamps and starts the blink timer. Its `EventGraph` positions the lamps and sets their intensity and radius. `BlinkNavigationLamps` calls `UpdateNavigationLights` to toggle visibility. |

See the [pack README](../README.md) for installation and the [agent guide](../../../AGENTS.md) for editor and packaging checks.
