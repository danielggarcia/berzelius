class WebDriverFactoryInterface:

    driver_configuration = {}
    config_file_path = ""

    def _load_default_options_(self, config_file_path: str = None):
        """
        Loads default options from config/webdrivers folder and stores it in driver_configuration attribute
        :param config_file_path: path to the YAML file with the configuration
        :return:
        """
        pass

    def _create_webdriver_options_(self):
        """
        Takes the values stored in the generic dictionary driver_configuration and generates a driver-specific
        configuration object.
        :return: webdriver-specific configuration object
        """
        pass

    def create_instance(self):
        """
        Creates a WebDriver instance by loading configuration parameters provided in constructor
        :return: A configured WebDriver instance
        """
        pass