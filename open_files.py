import tarfile

# Open the tar.gz file
with tarfile.open("comm-f2f-Resistance-network.tar.gz", "r:gz") as tar:
    # Extract all files to the current directory
    tar.extractall()

    # Or, extract specific files
    # for member in tar.getmembers():
    #     if member.isfile():
    #         tar.extract(member, path="destination_folder")