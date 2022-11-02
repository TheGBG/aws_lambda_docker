#!/usr/bin/bash

ENDPOINT="http://localhost:8000/2015-03-31/functions/function/invocations"

echo "Home response:"
curl -XGET $ENDPOINT --data "@data/home.json" | json_pp

echo "Square response:"
curl -XGET $ENDPOINT --data "@data/square.json" | json_pp
