# Contributing

Use the Insurgency: Sandstorm Mod Editor (UE 4.27.2). Coordinate changes to the same Blueprint, mesh, or other binary package before editing it because Git cannot merge Unreal packages. Save packages in the editor and preserve their paths relative to `Content/`. Give new packs a dedicated folder under `/Game/Assets/` and document any dependencies the SDK must supply.

Include the editor version, changed package paths, and validation results in your pull request. For a preview, report clean SDK import, missing references, and any gameplay or cooked-build checks you actually ran. Include each third-party asset's source, author, and reuse terms before adding it.

## Build a pack ZIP

```sh
python3 scripts/build_pack.py little-bird
```

This writes `dist/little-bird.zip` with the pack README and installable files at their `Content/` paths. Use GitHub Releases for new versioned downloads. Record the exact SDK version and validation status in the release notes. The original download in `previews/` remains available for existing links.

The current editable packages are small enough for regular Git. Revisit Git LFS when larger packs or frequent binary revisions start to grow the repository.
