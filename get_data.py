import requests
import os


def download_file(url, filename):
    """
    Download a file from the given URL and save it to the destination folder.

    Parameters:
        - url (str): The URL of the file to download.
        - destination_folder (str): The folder where the file should be saved. Default is the current directory.
    """
    response = requests.get(url)

    if response.status_code == 200:
        # Extracting the filename from the URL
        destination_path = os.path.join("./Data", filename)

        with open(destination_path, "wb") as file:
            file.write(response.content)

        print(f"File '{filename}' downloaded successfully.")
    else:
        print(f"Failed to download the file. Status Code: {response.status_code}")


if __name__ == "__main__":
    # Data nombres licenciés
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/b62c05d2-6b45-44e0-80a4-6e10e3f14ec6",
        "lic-data-2019.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/f3970a7b-df0e-4c3e-9f36-c93da58f4a3e",
        "lic-data-2018.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/523892b6-1eca-4680-ac4a-e93d3a896161",
        "lic-data-2017.csv",
    )

    # Permet de savoir si la donée existe ou non. Associer au code de fédération
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/e8b9085e-f9d7-4439-9e0d-8e6ede46097b",
        "liste-federation.xlsx",
    )
