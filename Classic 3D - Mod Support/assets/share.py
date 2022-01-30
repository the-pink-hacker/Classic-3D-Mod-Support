import os
import re
from glob import glob

pack_dir = os.path.normpath("/home/ryan/Documents/Code/Resourcepacks/Classic-3D-Mod-Support/Classic 3D - Mod Support/assets")

for file_dir in glob(os.path.join(pack_dir, "**"), recursive=True):
  if file_dir.endswith(".json"):
    with open(file_dir, "r") as file:
      contents = file.read()
    regex = re.compile(".*\"credit\": \".*\",\n")
    new_contents = regex.sub("", contents)
    new_contents = new_contents.replace("shared", "minecraft")
    with open(file_dir, "w") as file:
      file.write(new_contents)
