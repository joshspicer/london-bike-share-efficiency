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
#curl -H 'Authorization: Token <YOUR_TOKEN>' \
#     -H 'Accept-Language: en_US' \
#     -H 'Content-Type: application/json' \
#     $URL > output.json


a='"start_latitude": "$LATSTART",'
b='"start_longitude": "$LONGSTART",'
c='"end_latitude": "$LATEND",'
d='"end_longitude": "$LONGEND"'


# curl -X POST \
#      -H 'Authorization: Bearer <YOUR-TOKEN>'
#      -H 'Accept-Language: en_US' \
#      -H 'Content-Type: application/json' \
#      -d '{
#        "start_latitude": "$LATSTART",
#        "start_longitude": "$LONGSTART",
#        "end_latitude": "$LATEND",
#        "end_longitude": "$LONGEND"
#      }' "https://api.uber.com/v1.2/requests/estimate"  > output.json

curl -X POST \
     -H 'Authorization: Bearer <YOUR TOKEN>
     -H 'Accept-Language: en_US' \
     -H 'Content-Type: application/json' \
     -d '{
      "${$a$b$c$d}"
     }' "https://api.uber.com/v1.2/requests/estimate"  > output.json
