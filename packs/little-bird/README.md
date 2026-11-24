# Pilotable Little Bird

Player-piloted helicopter with four passenger seats. Preview for Sandstorm Mod Editor (UE 4.27.2). Clean SDK import and gameplay validation are pending.

## Use it however you like

The original work in this pack is dedicated to the public domain. You can use, modify, share, or sell it for any purpose. You don't need permission or credit. You can keep your changes private or share them, and including the license notice is optional. [CC0 1.0 Universal](LICENSE)

Sandstorm SDK assets and trademarks follow their own terms. Downloads from Preview 3 and earlier include a separately credited airframe under CC BY 4.0.

## Install

1. With the editor closed, merge the ZIP's `Content/` into `SandstormEditor/Insurgency/Content`, preserving paths.
2. Place `/Game/Assets/MyBlueprints/LittleBirdPilotable/BP_LittleBirdPilotable` in your scenario level.
3. Turn off **Despawn on Round Reset** on the placed actor.

Add one actor tag from `LB_Airframe_01` through `LB_Airframe_04` to display an optional fleet number.

Set **Aim Angle** on the placed Little Bird to adjust the gun and pilot sight together. The default is 10 degrees down from the aircraft's forward direction.

If upgrading from Preview 3 or earlier, remove the retired `M_LittleBird_Palette.uasset` and `T_LittleBird_Palette.uasset` from `Content/Assets/MyBlueprints/LittleBirdPilotable/LittleBird/` once you have confirmed your own assets do not reference them.

The Blueprint uses assets supplied by the Sandstorm Mod Editor.
