from IPython import get_ipython
import pandas as pd

def general_settings():
    '''
    Function to customize settings for IPython environment.
    '''
    # Set the width of dataframe previews to maximum
    # pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)

    # Enable autoreloading of external functions
    ip = get_ipython()
    ip.magic("load_ext autoreload")
    ip.magic("autoreload 2")

    print("DataFrame width maximized!")
    print("Autoreloading of functions enabled!")


