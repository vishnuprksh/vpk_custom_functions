from IPython import get_ipython
import pandas as pd
import os

def general_notebook_settings():
    '''
    Function to customize settings for IPython environment.
    '''
    # Set the width of dataframe previews to maximum
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)

    # Enable autoreloading of external functions
    ip = get_ipython()
    ip.magic("load_ext autoreload")
    ip.magic("autoreload 2")

    print("DataFrame width maximized!")
    print("Autoreloading of functions enabled!")



def activate_parent(parent_dir_name: str) -> None:
    """
    Sets the working directory to the specified parent directory if found in the current path hierarchy.

    Args:
        parent_dir_name (str): The name of the parent directory to set as the working directory.

    Raises:
        FileNotFoundError: If the specified parent directory is not found in the path hierarchy.
    """
    current_dir = os.getcwd()

    while True:
        if os.path.basename(current_dir) == parent_dir_name:
            os.chdir(current_dir)
            print(f"Working directory set to: {current_dir}")
            return
        
        parent_dir = os.path.dirname(current_dir)
        if current_dir == parent_dir:  # Reached the root directory
            break
        
        current_dir = parent_dir

    raise FileNotFoundError(f"The parent directory '{parent_dir_name}' was not found in the path hierarchy.")



