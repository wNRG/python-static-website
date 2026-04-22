import os
import shutil

def copy_static_to_public(source, destination):
    if not os.path.exists(source):
        raise Exception(f"PATH NOT FOUND: {static}")

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)

        if os.path.isfile(src_path):
            print(f"Copying FILE -> {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)
        else:
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            copy_static_to_public(src_path, dst_path)


    

