def transform(event):
   
    eventName = event.getEventName()
    properties = event.getProperties()
    properties['city_name'] = "London"

    return event
