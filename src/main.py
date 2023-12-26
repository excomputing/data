"""Module main.py"""
import logging
import os
import sys
import pandas as pd


def main():
    """
    Entry point
    """

    # Log
    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Pollutants')

    date = pd.Timestamp.today().date() - pd.Timedelta('1 day')
    values = pd.date_range(start=date - pd.Timedelta('28 days'), end=date, freq='D').to_list()
    datestr_ = [str(value.date()) for value in values]
    logger.info(datestr_)

    # Try
    # pollutant_id = 1
    # interface = src.data.interface.Interface(pollutant_id=pollutant_id, restart=True)
    # interface.exc(datestr_=datestr_)

    connector = src.s3.connector.Connector()
    parameters: src.elements.connector.Connector = connector.exc()
    logger.info(parameters)

    src.references.interface.Interface(parameters=parameters).exc()

    # Deleting __pycache__
    src.functions.cache.Cache().delete()
    

if __name__ == '__main__':

    # Paths
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Modules
    import src.data.api
    import src.data.interface
    import src.functions.objects
    import src.functions.cache
    import src.s3.connector
    import src.s3.profile
    import src.elements.connector
    import src.references.interface

    main()
