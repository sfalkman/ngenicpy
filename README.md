# Ngenic Tune Python API Wrapper
This python package simplifies access to the Ngenic Tune API.  
It can be used for viewing or edit your Tune configuration.

**NOTE**: This API wrapper is not yet finished, and only implements a subset of all the APIs. The interface may very well change.

## Prerequisite
### Obtain an API token
An API token may be obtained here: https://developer.ngenic.se/

## Example
```python
import json

from ngenic import Ngenic
ng = Ngenic(token="YOUR-API-TOKEN")

tunes = ng.tunes()
for tune in tunes:
    print(json.dumps(tune.json()))

tune = ng.tune("TUNE-UUID")

rooms = tune.rooms()
for room in rooms:
    print(json.dumps(room.json()))

room = tune.room(roomUuid="ROOM-UUID")
room["name"] = "Livingroom"
room.update()
```

## Reference
[Ngenic Tune Public API](https://developer.ngenic.se/)