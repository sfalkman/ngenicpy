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

from ngenicpy import Ngenic
ng = Ngenic(token="YOUR-API-TOKEN")

tunes = ng.tunes()
for tune in tunes:
    print("Tune %s\nName: %s\nTune Name: %s" %
            (
                tune.uuid(),
                tune["name"],
                tune["tuneName"]
            )
    )

tune = ng.tune("TUNE-UUID")

rooms = tune.rooms()
for room in rooms:
    print("Room %s\nName: %s\nTarget Temperature: %d" %
            (
                room.uuid(),
                room["name"],
                room["targetTemperature"]
            )
    )

# Update a room
room = tune.room(roomUuid="ROOM-UUID")
room["name"] = "Livingroom"
room.update()

nodes = tune.nodes()
for node in nodes:
    node_status = node.status()

    print("Node %s\nType: %s" %
            (
                node.uuid(),
                node.getType()
            )
    )

    if node_status:
        print("Battery: %s\%\nRadio Signal: %s" %
                (
                    str(node_status.getBatteryPercentage()),
                    str(node_status.getRadioSignalPercentage())
                )
        )

    measurements = node.latest_measurements()
    for measurement in measurements:
        print("%s: %d" %
                (
                    measurement.getType(),
                    measurement["value"]
                )
        )
```

## Reference
[Ngenic Tune Public API](https://developer.ngenic.se/)
