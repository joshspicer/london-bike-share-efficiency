LATSTART=$1
LONGSTART=$2

LATEND=$3
LONGEND=$4


echo $LATSTART
echo $LONGSTART
echo $LATEND
echo $LONGEND

#URL="https://api.uber.com/v1.2/estimates/time?start_latitude=${LAT}&start_longitude=${LONG}"
#
#curl -H 'Authorization: Token 9OF9_bKcLSdqu_xthV9QOCfWa9Hf7DXLju0DBCe0 ' \
#     -H 'Accept-Language: en_US' \
#     -H 'Content-Type: application/json' \
#     $URL > output.json


a='"start_latitude": "$LATSTART",'
b='"start_longitude": "$LONGSTART",'
c='"end_latitude": "$LATEND",'
d='"end_longitude": "$LONGEND"'


# curl -X POST \
#      -H 'Authorization: Bearer JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAG8AAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAkAAAABwAAAAEAAAAEAAAAJIegrQTIBc2hzy3Ul4tpulsAAAAwcr9KXTjlBm5KTwTlTf8FTXUuLj38h-0gEDFkFDXj5n0peqKIwXn1DRpgYqk2lTOx5whJxaDAAZf307ZKTP4i0yViYzB5OxE-9hXzVvPYu-v6ATl2xTC2nLOyBQ6s0Du_J6PPvDuJ7zwvM4YDAAAAKLGvY7-oT_0OOgzCCQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU' \
#      -H 'Accept-Language: en_US' \
#      -H 'Content-Type: application/json' \
#      -d '{
#        "start_latitude": "$LATSTART",
#        "start_longitude": "$LONGSTART",
#        "end_latitude": "$LATEND",
#        "end_longitude": "$LONGEND"
#      }' "https://api.uber.com/v1.2/requests/estimate"  > output.json

curl -X POST \
     -H 'Authorization: Bearer JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAG8AAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAkAAAABwAAAAEAAAAEAAAAJIegrQTIBc2hzy3Ul4tpulsAAAAwcr9KXTjlBm5KTwTlTf8FTXUuLj38h-0gEDFkFDXj5n0peqKIwXn1DRpgYqk2lTOx5whJxaDAAZf307ZKTP4i0yViYzB5OxE-9hXzVvPYu-v6ATl2xTC2nLOyBQ6s0Du_J6PPvDuJ7zwvM4YDAAAAKLGvY7-oT_0OOgzCCQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU' \
     -H 'Accept-Language: en_US' \
     -H 'Content-Type: application/json' \
     -d '{
      "${$a$b$c$d}"
     }' "https://api.uber.com/v1.2/requests/estimate"  > output.json
