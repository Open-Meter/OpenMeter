import json
import requests  # type: ignore


class OpenMeterApi:
    """
    Api class to handle get and post requests, base_url is set to v1 right now.
    :param access_token: access_token of the client
    """

    def __init__(self, personal_access_token):
        self.base_url = "http://0.0.0.0:80/v1"
        self._api_key = personal_access_token
        self.meta_data_limit = 200
        self.timeseries_data_limit = 2000

    @property
    def get_api_key(self):
        """
        method to get the api key with which the class is instanciated.
        """
        return self._api_key

    def test_request_status(self, result):
        """
        generalized method to test the result status for exceptions.

        :param result: the response of the requests.get, requests.post....etc..
        """
        try:
            result.raise_for_status()
        except Exception as exc:
            print(exc)
            print(result.text)
            raise
        return result

    def get_sensor(self, sensor_id):
        """
        method to get the meta data of a sensor using it's id.
        Note: It is to be noted that when an id exists the other
        filtering related params would be ignored by the api.

        :param sensor_id: the id of the sensor to retrieve
        """
        local_params = {
            "access_token": self._api_key,
            "sensor_id": sensor_id,
            "page": 0,
        }
        result = requests.get(f"{self.base_url}/meta_data", params=local_params)
        result = self.test_request_status(result)
        result = json.loads(result.text)
        # result_info = result["information"]
        result_data = result["data"][0]
        return result_data

    def get_filtered_sensors(self, filter_dictionary):
        """
        method to get a list of sensors with metadata
        Note: It is to be noted that the filter_dictionary shouldn't contain
        the key 'id' which reduces the result to only one sensor(with the give id)

        :param filter_dictionary: dictionary containing the intended filters
        """
        # list to collect the results of multiple pages
        results_list = []

        local_params = {
            "access_token": self._api_key,
            "page": 0,
        }
        local_params.update(filter_dictionary)

        while True:
            result = requests.get(f"{self.base_url}/meta_data", params=local_params)
            result = self.test_request_status(result)
            result = json.loads(result.text)
            # result_info = result["information"]
            result_data = result["data"]
            results_list.extend(result_data)

            if len(result["data"]) < self.meta_data_limit:
                break
            local_params["page"] = local_params["page"] + 1

        return results_list

    def create_sensor(self, meta_data, location_id=None):
        """
        method to create a new sensor, provides the functionality to attach an existing
        location object to a new sensor being created, if no location_id is being provided,
        then the meta_data dictionary needs to contain location information.

        :param meta_data: the meta data information of a new sensor
        :param location_id: Optional, if provided, needs to be in the database.
        """
        local_params = {
            "access_token": self._api_key,
        }

        if location_id:
            local_params.update({"location_id": location_id})
        result = requests.post(
            f"{self.base_url}/meta_data", params=local_params, json=meta_data
        )
        result = self.test_request_status(result)
        result = json.loads(result.text)
        return result

    def update_sensor(self, sensor_id, meta_data):
        """
        method to update metadata of an existing sensor, location data of a sensor
        can also be updated.

        :param sensor_id: id of an existing sensor.
        :param meta_data: the dictionary with the updated information fields.
        """
        local_params = {"access_token": self._api_key, "sensor_id": sensor_id}
        result = requests.patch(
            f"{self.base_url}/meta_data", params=local_params, json=meta_data
        )
        result = self.test_request_status(result)
        result = json.loads(result.text)
        return result

    def read_attributes(self, attribute_name):
        """
        method to read the unique values of an attributes.

        :param attribute_name: the name of the metadata field
        """
        local_params = {"access_token": self._api_key, "attribute_name": attribute_name}
        result = requests.get(
            f"{self.base_url}/meta_data/distinct_values", params=local_params
        )
        result = self.test_request_status(result)
        result = json.loads(result.text)
        return result

    def get_timeseries_data(self, sensor_id, from_timestamp=None, to_timestamp=None):
        """
        method to retrieve timeseries data.

        :param sensor_id: id of an existing sensor
        :param from_timestamp: Optional, timestamp from which data is to retrieved
        :param to_timestamp: Optional, timestamp to which data is to retrieved
        """
        # list to collect the results of multiple pages
        results_list = []

        local_params = {
            "access_token": self._api_key,
            "sensor_id": sensor_id,
            "from_ts": from_timestamp,
            "to_ts": to_timestamp,
            "page": 0,
        }

        while True:
            result = requests.get(f"{self.base_url}/timeseries", params=local_params)
            result = self.test_request_status(result)
            result = json.loads(result.text)
            # result_info = result["information"]
            result_data = result["data"]
            results_list.append(result_data)

            if len(result["data"]) < self.timeseries_data_limit:
                break
            local_params["page"] = local_params["page"] + 1

        results_list = [
            dict(zip(page["timestamps"], page["values"])) for page in results_list
        ]

        combined_timeseries_data = {
            key: value for page in results_list for key, value in page.items()
        }
        return combined_timeseries_data

    def write_timeseries_data(self, sensor_id, timeseries_data):
        """
        method to add timeseries data.

        :param sensor_id: id of an existing sensor
        :param timeseries_data: dictionary object containing separate lists for
        timestamps and values.
        """
        local_params = {
            "access_token": self._api_key,
            "sensor_id": sensor_id,
        }

        result = requests.post(
            f"{self.base_url}/timeseries", params=local_params, json=timeseries_data
        )
        result = self.test_request_status(result)
        result = json.loads(result.text)
        return result
