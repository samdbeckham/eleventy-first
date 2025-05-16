import os
import shutil

def copy_files(source, destination):
    if not os.path.exists(source):
        raise Exception("source path does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    if os.path.isfile(source):
        print(f"copying {source} to {destination}")
        return shutil.copy(source, destination)
    os.mkdir(destination)
    for file in os.listdir(source):
        copy_files(
            os.path.join(source, file),
            os.path.join(destination, file)
        )

