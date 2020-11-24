# Mapzen Extracts


### Para o funcionamento do mapa é imprescindível seguir alguns padrões, que são:
- Os nomes dos arquivos devem seguir o padrão: admin_level_x.json e admin_level_x_simplified.json, onde X é um número começando por 0 e incrementado conforme o level do mapa.
- As "properties" necessárias para cada "feature" do mapa deve conter os seguintes atributos: osm_id (um valor único que não entre em conflito com outros mapas. Pode ser String ou Inteiro), is_in_country (osm_id do país. Caso não houver, valor padrão é None), is_in_state (osm_id do estado. Caso não houver, valor padrão é None), name e name_en.


### A execução do script de importação é feita da seguinte maneira:
1. Entrar no diretório principal do Rapidpro;
2. Ativar VirtualEnv
3. executar: `./manage.py import_geojson /path/to/maps/country/*.json`


### A extração do mapa pode ser feita de diversas maneiras. Algumas delas são:
- Procurar um shapefile na internet e transformar em json atravéz do [mapshaper](http://mapshaper.org/);
- Procurar um arquivo PBF e extraí-lo utilizando o projeto [posm-extracts](https://github.com/Ilhasoft/posm-extracts);
- Extrair o .json diretamente de plataformas de mapas;
- Encontrar jsons já prontos em repositórios e só adaptar ao padrão seguido pelo rapidpro para importação de mapa.


### Links úteis:


**Download de shapefiles**

[humdata](https://data.humdata.org/dataset)

[diva-gis](https://www.diva-gis.org/gdata)

[gadm](https://gadm.org/download_country_v3.html)

[datapages](http://www.datapages.com/gis-map-publishing-program/gis-open-files/global-framework/global-heat-flow-database/shapefiles-list)


**Download pbf ou outras extensões**

[bbbike](https://extract.bbbike.org/)

[hotosm](https://export.hotosm.org/en/v3/exports/new/describe)

[openstreetmap repository](http://download.openstreetmap.fr/extracts/)


**Documentação para extração de PBF**

[wiki ilhasoft](https://wiki.ilhasoft.mobi/index.php/Suporte/u-report/mapzen)

**Manipulação dos arquivos geojson, json, shapefile, etc**

[mapshaper](http://mapshaper.org/)
