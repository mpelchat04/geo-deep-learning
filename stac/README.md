# STAC info
The SpatioTemporal Asset Catalog ([STAC](https://github.com/radiantearth/stac-spec)) specification is a standardization 
attempt for geospatial assets. Such assets include (but are not limited to): 
- [Electro-Optical](https://github.com/radiantearth/stac-spec/tree/dev/extensions/eo)
imagery (visible, short-wave and mid-wave IR, etc.)  
- [Labeled AOIs for machine learning models](https://github.com/radiantearth/stac-spec/tree/dev/extensions/label)

These information are critical to have, in order to describe the context of a certain trained model. 
With this information, one will be able to answer questions such as
 - where a certain model was trained?   
 - with which imagery?  
 - what band combination?  
 - which class is it trained to classify/segment?  
 
*Geo-deep-learning* is transitioning towards the use of the STAC specification for accessing Earth observation data. 
# Yaml templates
STAC items are stored in json files. The `yaml_templates` aims to facilitate the creation of EO and LABEL STAC. 
Those have to be filled manually.  
 
# stac_utils.py usage
This utils aims to create a json STAC item from a yaml template.  
Usage:  
```python stac_utils.py /path/to/yaml/templates.yaml```  
