
import os
import subprocess

from traitlets.config import get_config

c = get_config()


def post_save_hook(model, os_path, contents_manager):
    cwd, name = os.path.split(os_path)

    if model["type"] == "notebook" and ".ipynb" in os_path:
        outdir = cwd + "/aspython"
        if not os.path.isdir(outdir):
            try:  
                os.mkdir(outdir)
            except OSError:  
                print ("Creation of the directory %s failed" % outdir)
            else:  
                print ("Successfully created the directory %s " % outdir)

        output = "aspython/" + name.replace(".ipynb", ".py").lower()

        subprocess.check_call(
            ["jupyter", "nbconvert", "--to", "python", "--output", output, name],
            cwd=cwd,
        )
        subprocess.check_call(["chmod", "u+x", output], cwd=cwd)


c.FileContentsManager.post_save_hook = post_save_hook

