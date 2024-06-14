if [ ! -d ./TMP/ ]; then
  mkdir ./TMP/
fi

curl http://127.0.0.1:5000/v1/get_method/ > ./TMP/get_method_v1.txt

curl http://127.0.0.1:5000/v2/get_method/Halo%20SIC5%20! > ./TMP/get_method_v2.txt

curl http://127.0.0.1:5000/v3/get_method/?params=ini%20post%20method%20v2 > ./TMP/get_method_v3.txt