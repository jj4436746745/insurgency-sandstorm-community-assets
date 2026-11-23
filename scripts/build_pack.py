"""Build an installable, reproducible ZIP from an editable asset pack."""

import argparse
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
UNREAL_EXTENSIONS = {".uasset", ".umap", ".uexp", ".ubulk", ".uptnl"}
PACKAGE_MAGIC = {b"\xc1\x83\x2a\x9e", b"\x9e\x2a\x83\xc1"}


def build_pack(pack: Path, output: Path) -> None:
    readme = pack / "README.md"
    license_file = pack / "LICENSE"
    content = pack / "Content"
    # Include Unreal sidecar files and sort entries for repeatable builds.
    assets = sorted(
        path for path in content.rglob("*")
        if path.is_file() and path.suffix.lower() in UNREAL_EXTENSIONS
    )
    packages = [path for path in assets if path.suffix.lower() in {".uasset", ".umap"}]
    if not readme.is_file() or not packages:
        raise ValueError(f"{pack}: expected README.md and Unreal packages under Content/")
    included = [readme, *assets]
    if license_file.is_file():
        included.insert(1, license_file)
    # Keep packaged files inside the pack.
    for path in included:
        if path.is_symlink() or not path.resolve().is_relative_to(pack.resolve()):
            raise ValueError(f"{path}: expected a regular file inside the pack")
    # Check the Unreal header to catch Git LFS pointers before packaging.
    for path in packages:
        with path.open("rb") as package:
            if package.read(4) not in PACKAGE_MAGIC:
                raise ValueError(f"{path}: invalid Unreal package. Check for a Git LFS pointer.")

    output.parent.mkdir(parents=True, exist_ok=True)
    # Build beside the output so a failed build preserves the previous ZIP.
    with NamedTemporaryFile(dir=output.parent, delete=False) as temp:
        staged = Path(temp.name)
    try:
        with ZipFile(staged, "w", compression=ZIP_DEFLATED) as archive:
            for path in included:
                # Preserve install paths and use fixed timestamps and file permissions.
                entry = ZipInfo(path.relative_to(pack).as_posix())
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, path.read_bytes(), compress_type=ZIP_DEFLATED)
        staged.replace(output)
    finally:
        staged.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    packs = ROOT / "packs"
    parser.add_argument("pack", choices=sorted(path.name for path in packs.iterdir() if path.is_dir()))
    args = parser.parse_args()
    output = ROOT / "dist" / f"{args.pack}.zip"
    try:
        build_pack(packs / args.pack, output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(output)


if __name__ == "__main__":
    main()
