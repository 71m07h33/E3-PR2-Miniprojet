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
        destination_path = os.path.join(".", filename)

        with open(destination_path, "wb") as file:
            file.write(response.content)

        print(f"File '{filename}' downloaded successfully.")
    else:
        print(f"Failed to download the file. Status Code: {response.status_code}")


if __name__ == "__main__":
    # Data nombres licenciés
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/1825fde3-a668-47e3-a46d-b62b5af6560a",
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
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/67e7edcc-112e-415a-aea0-07fcabd03e83",
        "lic-data-2016.csv",
    )

    # Data nombre clubs
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/419b4123-f213-4e54-a02e-ca9535c6df35",
        "clubs-data-2019.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/9348012d-9baa-451b-89e1-55817837c521",
        "clubs-data-2018.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/33d0b1a2-b939-443c-80a2-367c5b7d138d",
        "clubs-data-2017.csv",
    )
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/198ee5d6-4b35-49de-bda2-d49161a6e611",
        "clubs-data-2016.csv",
    )

    # Permet de savoir si la donée existe ou non. Associer au code de fédération
    download_file(
        "https://www.data.gouv.fr/fr/datasets/r/e8b9085e-f9d7-4439-9e0d-8e6ede46097b",
        "liste-federation.xlsx",
    )
