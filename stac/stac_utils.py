from ..utils import read_parameters
from geojson import Polygon
import json
import os
import rasterio
from rasterio.warp import transform_bounds


def geom_and_bbox_from_tif(img):
    """
    Function to calculate bbox and geojson polygon of the footprint, in EPSG:4326 and return it.
    :param img: (str) Path to image
    :return: geojson polygon and tuple bbox, in EPSG:4326
    """
    with rasterio.open(img) as src:
        scr_bounds = src.bounds

    # For STAC items, the destination crs must be 4326.
    dst_crs = 'EPSG:4326'
    dst_bounds = transform_bounds(src.crs, dst_crs, scr_bounds[0], scr_bounds[1], scr_bounds[2], scr_bounds[3])
    poly = Polygon([(dst_bounds[0], dst_bounds[1]),
                    (dst_bounds[0], dst_bounds[3]),
                    (dst_bounds[2], dst_bounds[3]),
                    (dst_bounds[2], dst_bounds[1]),
                    (dst_bounds[0], dst_bounds[1])
                    ])
    return poly, dst_bounds


if __name__ == '__main__':
    print('Start')
    # Script parameters
    params = read_parameters('/home/maturgeo/.PyCharmCE2019.1/config/scratches/stac_eo_item.yaml')
    json_schema = ''
    working_folder = '/wspace/disk01/dataset_kingston_rgb/stac_tests'
    img = os.path.join(working_folder, '2_RGB__0_0.tif')

    pol, bbox = geom_and_bbox_from_tif(img)

    params['geometry'] = pol
    params['bbox'] = bbox
    # Convert datetime objects to string, for json.
    params['properties']['datetime'] = str(params['properties']['datetime'])
    params['properties']['created'] = str(params['properties']['created'])
    params['properties']['updated'] = str(params['properties']['updated'])

    # Write the json.
    with open(os.path.join(working_folder, f"{params['id']}.json"), 'w') as json_file:
        dict_param = dict(params)
        json.dump(dict_param, json_file)

    # Validate the schema.

    # Read the written json. for validation
    with open(os.path.join(working_folder, f"{params['id']}.json"), 'r') as json_file:
        parsed_json = json.load(json_file)
        print(parsed_json)
    # print(params)
