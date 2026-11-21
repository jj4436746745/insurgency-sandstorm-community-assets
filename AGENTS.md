# Agent instructions

This repository ships editable asset packs for the Sandstorm Mod Editor (UE 4.27.2). Each pack keeps Unreal packages under `packs/<pack>/Content/` and documents installation, dependencies, and asset credits in its README.

See the [Little Bird developer note](packs/little-bird/docs/development.md) for the Blueprint graph map.

## Editing assets

- Fetch editable assets with Git LFS. Upload changed LFS objects and verify they can be fetched before merging.
- Coordinate edits to the same Unreal package. Preserve existing package paths and keep new assets in the owning pack's `/Game/Assets/` folder. Little Bird uses `/Game/Assets/MyBlueprints/LittleBirdPilotable/`.
- For editor changes, compile affected Blueprints, check package dependencies, and save only the packages you changed. The user owns PIE playtests. Do not start or run PIE.

## Checks and publishing

For Little Bird asset or packaging changes, run:

```sh
python3 scripts/build_pack.py little-bird
python3 -m zipfile -t dist/little-bird.zip
```

Keep generated ZIPs in ignored `dist/`. Keep existing links in `previews/` working and publish new versioned ZIPs through GitHub Releases. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for pull requests and release steps. Report the checks you actually ran.
