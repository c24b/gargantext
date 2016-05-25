from django.conf.urls import patterns, url

# Module "Graph Explorer"
from graphExplorer.rest         import Graph
from graphExplorer.views        import explorer
from graphExplorer.intersection import intersection


# TODO : factor urls
# url will have this pattern:
# ^explorer/$corpus_id/view
# ^explorer/$corpus_id/data.json
# ^explorer/$corpus_id/intersection

urlpatterns = [ url(r'^explorer/intersection/(\w+)$', intersection     )
              , url(r'^projects/(\d+)/corpora/(\d+)/explorer$', explorer       )
              , url(r'^projects/(\d+)/corpora/(\d+)/graph$'   , Graph.as_view())
              , url(r'^projects/(\d+)/corpora/(\d+)/node_link.json$', Graph.as_view())
              ]