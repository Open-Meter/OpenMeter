"""
Easy OpenMeterApi class to play around with the Openmeter api get and post requests
works on local development instance
"""
from api.libraries.openmeter_api import OpenMeterApi


def main():
    """
    main method
    """

    # class instantiation
    my_access_token = "969AC556-9185-48B2-97D2-D72341911067"
    oh_my_api = OpenMeterApi(personal_access_token=my_access_token)

    # ------------------------------------ 1 ----------------------------------
    # # get sensor by id
    sensor_id = "9765103e-b4ba-40dc-916e-f61b94d31a1a"
    sensor_data = oh_my_api.get_sensor(sensor_id=sensor_id)
    print(sensor_data)

    # ------------------------------------ 2 ----------------------------------
    # # get list of filtered sensors - *if filters_dict contains id key,
    # # it will ignore the rest of the key value pairs*
    # filters_dict = {
    #     "energy_type": "Gas",
    #     "measurement_type": "Wirkarbeit",
    # }
    # sensors_data = oh_my_api.get_filtered_sensors(filter_dictionary=filters_dict)
    # print(sensors_data)
    # print(len(sensors_data))

    # ------------------------------------ 3 ----------------------------------
    # # post a new sensor using location id
    # sensor_metadata = {
    #     "energy_type": "Strom",
    #     "measurement_category": "Verbrauch",
    #     "measurement_type": "Wirkarbeit (Brennwert)",
    #     "measurement_unit": "kWh(Hs)",
    #     "measurement_value_type": "Zaehlerstand",
    #     "measurement_frequency": "24h",
    #     "notes": "This sensor was newly installed in 2022",
    #     "private_id": "AB_123",
    #     "measurement_timezone": "Europe_Berlin",
    # }
    # new_sensor_info = oh_my_api.create_sensor(
    #     meta_data=sensor_metadata,
    #     location_id="db8f6abd-6032-4379-8d35-9d9236a6278b",
    # )
    # print(new_sensor_info)

    # ------------------------------------ 4 ----------------------------------
    # # post a new sensor using location as part of json
    # sensor_metadata = {
    #     "energy_type": "Strom",
    #     "measurement_category": "Verbrauch",
    #     "measurement_type": "Wirkarbeit (Brennwert)",
    #     "measurement_unit": "kWh(Hs)",
    #     "measurement_value_type": "Zaehlerstand",
    #     "measurement_frequency": "24h",
    #     "notes": "This sensor was newly installed in 2022",
    #     "private_id": "private id",
    #     "measurement_timezone": "Europe_Berlin",
    #     "location": {
    #         "country": "Deutschland",
    #         "federal_state": "Baden-Wuerttemberg",
    #         "city": "Aachen",
    #         "post_code": 533101,
    #         "category": "Gewerblich",
    #         "usage": "fuer testing",
    #         "usage_detail": "string",
    #         "area": 230.5,
    #         "construction_year": 2022,
    #         "private_id": "private id",
    #     },
    # }
    # new_sensor_info = oh_my_api.create_sensor(meta_data=sensor_metadata)
    # print(new_sensor_info)

    # ------------------------------------ 5 ----------------------------------
    # # update an existing sensor metadata and/or location metadata
    # sensor_id = "1360ec05-32e0-4615-a297-c26f4bac73a2"
    # sensor_metadata_update = {
    #     "energy_type": "Strom",
    #     "location": {
    #         "country": "Italien",
    #     },
    # }
    # update_status = oh_my_api.update_sensor(sensor_id, sensor_metadata_update)
    # print(update_status)

    # ------------------------------------ 6 ----------------------------------
    # # read all the unique attributes of a sensor meta_data field
    # attribute_name = "energy_type"
    # all_attributes = oh_my_api.read_attributes(attribute_name=attribute_name)
    # print(all_attributes)

    # ------------------------------------ 7 ----------------------------------
    # # read timeseries data of a sensor
    # sensor_id = "9765103e-b4ba-40dc-916e-f61b94d31a1a"
    # from_timestamp = "1970-01-01 00:00:00"
    # to_timestamp = "2025-01-01 00:00:00"
    # ts_data = oh_my_api.get_timeseries_data(sensor_id, from_timestamp, to_timestamp)
    # print(ts_data)

    # ------------------------------------ 8 ----------------------------------
    # # create or update timeseries data of an existing sensor
    # sensor_id = "8ed9d9b8-bf06-4ed0-833d-b9258f2fac06"
    # timeseries_data = {
    #     "timestamps": [
    #         "2021-02-02 15:00:00",
    #         "2021-02-02 15:15:00",
    #         "2021-02-02 15:30:00",
    #     ],
    #     "values": [15, 16, 17],
    # }
    # status_update = oh_my_api.write_timeseries_data(sensor_id, timeseries_data)
    # print(status_update)


if __name__ == "__main__":
    main()
