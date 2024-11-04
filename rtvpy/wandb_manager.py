# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Wandb/wandb_manager.ipynb.

# %% auto 0
__all__ = ['loadWandbArtifact', 'pushWandbArtifact']

# %% ../nbs/Wandb/wandb_manager.ipynb 2
import wandb
import pandas as pd
import os
import shutil

def loadWandbArtifact(entity: str = 'analytic', 
                      project: str = 'Risk Assessment', 
                      artifact_name: str = None, 
                      version: str = "latest", 
                      dataset:bool=True,
                      download_dir: str = "artifacts", 
                      download: bool = False) -> pd.DataFrame:
    """
    Loads a specified WandB artifact as a DataFrame if it's a dataset, 
    and optionally deletes the downloaded artifacts folder after loading.

    Parameters:
    - entity (str): Your WandB username or team name.
    - project (str): The WandB project name.
    - artifact_name (str): The name of the artifact to download.
    - version (str): The version of the artifact to download (default is 'latest').
    - download_dir (str): The local directory to save the downloaded artifact (default is 'artifacts').
    - download (bool): Whether to store a copy of the artifact on local disk

    Returns:
    - pd.DataFrame: Loaded dataset as a DataFrame if applicable.
    """
    # Initialize WandB API
    api = wandb.Api()

    # Fetch the artifact
    artifact = api.artifact(f"{entity}/{project}/{artifact_name}:{version}")

    # Download the artifact to the specified directory
    artifact_dir = artifact.download(download_dir)

    # Check if there is a CSV or similar dataset file and load it
    if dataset:
        df = None
        for file in os.listdir(artifact_dir):
            file_path = os.path.join(artifact_dir, file)
            if file.endswith('.csv'):
                df = pd.read_csv(file_path)
                break
            elif file.endswith('.xlsx'):
                df = pd.read_excel(file_path)
                break

    # Optionally delete the artifact directory after loading
    if download:
        print(file_path)
    else:
        shutil.rmtree(download_dir)

    return df


# %% ../nbs/Wandb/wandb_manager.ipynb 3
import os
import wandb
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def pushWandbArtifact(file_path: str, 
                      job_type: str, 
                      description: str = 'no description', 
                      artifact_type: str = 'dataset',
                      project:str = "Risk Assessment",
                      ) -> None:
    """
    Uploads a dataset to Weights & Biases as an artifact.

    Args:
        file_path (str): Path to the file to upload.
        job_type (str): The type of job (e.g., "training", "evaluation").
        description (str, optional): Description of the artifact. Defaults to 'no description'.
        artifact_type (str, optional): Type of the artifact (e.g., "dataset"). Defaults to 'dataset'.
        project (str, optional): Name of the Weights & Biases project. Defaults to "Risk Assessment".

    Returns:
        None
    
    Raises:
        ValueError: If file_path or job_type are not provided.
        ConnectionError: If there is an issue connecting to Weights & Biases.
    """
    # Validate arguments
    if not file_path:
        raise ValueError("File path cannot be empty. Please provide a valid path to the data file.")
    if not job_type:
        raise ValueError("Job type cannot be empty. Please provide a valid job type.")

    # Initialize Weights & Biases connection
    try:
        wandb.login(key=os.environ.get("WANDB_API_KEY"))
        wandb.init(project=project, job_type=job_type)
    except wandb.errors.CommError as e:
        raise ConnectionError("Failed to connect to Weights & Biases. Check your API key and internet connection.") from e

    # Create and log artifact
    artifact = wandb.Artifact(
        name=f"{job_type}_{os.path.basename(file_path)}",
        type=artifact_type,
        description=description,
    )
    artifact.add_file(file_path)

    try:
        wandb.log_artifact(artifact)
    finally:
        wandb.finish()

