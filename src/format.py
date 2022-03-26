import json
from pathlib import Path

if __name__ == "__main__":
    # country = open('/content/drive/MyDrive/Colab Notebooks/datasets/places/countries.json')

    # country_data = json.load(country)
    
    
    cities = open('/content/drive/MyDrive/Colab Notebooks/datasets/places/countries/84/cities.json')
    districts = open('/content/drive/MyDrive/Colab Notebooks/datasets/places/countries/84/districts.json')
    cities_data = json.load(cities)
    districts_data = json.load(districts)
    country=84
    aList = []
    for i in range(len(cities_data)):
      # get ID and Province
      # print(cities_data[i]['name'])
      # city_code = cities_data[i]['code']
      city_code = cities_data[i]['code']
      addr_province = {"name":cities_data[i]['name'],"name_with_type":cities_data[i]['name_with_type'],"province_code":cities_data[i]['code'],"country_code":'84',"id":'{}{}'.format(country,cities_data[i]['code'])}
      aList.append(addr_province)
      for j in range(len(districts_data)):
        if districts_data[j]['city_code'] == city_code:
          # print(districts_data[j]['name'],districts_data[j]['code'])
          addr_dictrict = {"name":districts_data[i]['path'],"name_with_type":districts_data[i]['path_with_type'],"province_code":districts_data[i]['city_code'],"dictrict_code":districts_data[i]['code'],"country_code":'84',"id":'{}{}{}'.format(country,districts_data[i]['city_code'],districts_data[i]['code'])}
          #find file json follow districts_code
          aList.append(addr_dictrict)
          name_wards_json = '/content/drive/MyDrive/Colab Notebooks/datasets/places/countries/84/wards/{}.json'.format(districts_data[j]['code'])
          # print(name_wards_json)
          path = Path(name_wards_json)
    
          if path.is_file():
            wards = open(name_wards_json)
            wards_data = json.load(wards)
    
            wards_list = list(wards_data)
            # print(len(wards_list))
            for k in range(len(wards_list)):
              wards_id = wards_list[k]
              # define a list
              addr_ward = {"name" : wards_data[f'{wards_id}']['path'], "name_with_type" : wards_data[f'{wards_id}']['path_with_type'],'ward_code':wards_data[f'{wards_id}']['code'],"dictrict_code":wards_data[f'{wards_id}']['parent_code'],
                      "province_code" : districts_data[j]['city_code'], "country_code":'84',"id":'{}{}{}{}'.format(country,districts_data[j]['city_code'],wards_data[f'{wards_id}']['parent_code'],wards_data[f'{wards_id}']['code'])}
              aList.append(addr_ward)
    # print(aList)
    # jsonFile = open("/content/drive/MyDrive/Colab Notebooks/datasets/data.json", "w")
    jsonFile = "/content/drive/MyDrive/Colab Notebooks/datasets/data.json"
    # jsonFile.write(str(aList))
    # jsonFile.close()
    with open(jsonFile, 'w',encoding='utf8') as json_file:
        json.dump(aList, json_file, 
                            indent=4,  
                            separators=(',',': '),ensure_ascii=False)
    