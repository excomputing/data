
import logging

import src.data.references


class Interface:

    def __init__(self):
        """

        """

        # Logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.__logger = logging.getLogger(__name__)

    def exc(self, pollutant_id: int):
        """

        :return:
        """

        collection = src.data.references.References().exc()

        sequences = collection.sequences
        self.__logger.info(sequences.info())

        excerpt = sequences.loc[sequences['pollutant_id'] == pollutant_id, :]
        self.__logger.info(excerpt.info())
