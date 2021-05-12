#!/usr/bin/python

import os

DIR = "dist"

MAP = {}


def fix_filenames(content):
    for sha, ext in MAP.items():
        if sha in content:
            content = content.replace("%s.%s" % (sha, ext), "%s?c=%s" % (ext, sha))
            print("Fixed %s.%s" % (sha, ext))
    return content


def main():
    for name in os.listdir(DIR):
        old = os.path.join(DIR, name)
        if (
            name.endswith(".js")
            or name.endswith("css")
            and (len([c for c in name if c == "."])) == 2
        ):
            name, sha, ext = name.split(".")
            MAP[sha] = ext
            new = os.path.join(DIR, "%s.%s" % (name, ext))
            os.rename(old, new)
            print("Rename %s.%s" % (name, ext))

        if name.endswith(".map") and len([c for c in name if c == "."]) == 3:
            name, sha, ext, m = name.split(".")
            new = os.path.join(DIR, "%s.%s.map" % (name, ext))
            os.rename(old, new)

    for name in os.listdir(DIR):
        old = os.path.join(DIR, name)
        if name.endswith(".html"):
            with open(old, "r+") as f:
                content = f.read()
                print("Fixing filenames in %s" % name)
                content = fix_filenames(content)
                f.seek(0)
                f.write(content)


if __name__ == "__main__":
    main()
