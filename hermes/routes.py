from .handlers import frontends, api

HANDLERS = [
    # Hosts
    (r"/api/v1/hosts", api.HostsHandler),
    (r"/api/v1/hosts/(?P<hostname>.*)/", api.HostHandler),

    # Event Types
    (r"/api/v1/eventtypes", api.EventTypesHandler),
    (r"/api/v1/eventtypes/(?P<id>\d+)/", api.EventTypeHandler),

    # Events
    (r"/api/v1/events", api.EventsHandler),
    (r"/api/v1/events/(?P<id>\d+)/", api.EventHandler),

    # Frontend Handlers
    (r"/.*", frontends.AppHandler),
]
