import wua

def check_for_updates():
    # Check for available updates
    updates = wua.search("IsInstalled=0 and Type='Software'")

    # Print the number of available updates
    print(f"{len(updates)} updates available.")

    # Install available updates
    wua.install_updates(updates)
