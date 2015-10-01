from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import login

from gargantext_web import views, views_optimized
import gargantext_web.corpus_views as corpus_views

from annotations import urls as annotations_urls
from annotations.views import main as annotations_main_view

import scrappers.scrap_pubmed.views as pubmedscrapper
import tests.ngramstable.views as samtest


admin.autodiscover()

urlpatterns = patterns('',

    ############################################################################
    # Admin views
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^auth/$', views.login_user),
    url(r'^auth/logout/$', views.logout_user),

    ############################################################################
    # Dynamic CSS
    url(r'^img/logo.svg$', views.logo),
    url(r'^css/bootstrap.css$', views.css),

    # REST
    url(r'^api/', include('rest_v1_0.urls')),
    url(r'^v1.0/', include('rest_v1_0.urls')),

    # TODO below to put in the rest
    url(r'^project/(\d+)/corpus/(\d+)/corpus.csv$', views.corpus_csv),
    url(r'^project/(\d+)/corpus/(tests_mvc_listdocuments+)/corpus.tests_mvc_listdocuments$', views.corpus_csv),
    url(r'^delete/(\d+)$', views.delete_node), # => api.node('id' = id, children = 'True', copies = False)
    # Visualizations
    url(r'^project/(\d+)/corpus/(\d+)/chart$', views.chart),
    url(r'^project/(\d+)/corpus/(\d+)/explorer$', views.graph),
    url(r'^project/(\d+)/corpus/(\d+)/matrix$', views.matrix),

    url(r'^chart/corpus/(\d+)/data.csv$', views.send_csv),  # => api.node.children('type' : 'data', 'format' : 'csv')
    url(r'^corpus/(\d+)/node_link.json$', views.node_link), # => api.analysis('type': 'node_link', 'format' : 'json')
    url(r'^corpus/(\d+)/adjacency.json$', views.adjacency), # => api.analysis('type': 'adjacency', 'format' : 'json')
    
    url(r'^ngrams$', views.ngrams),  # to be removed
    url(r'^nodeinfo/(\d+)$', views.nodeinfo), # to be removed ?
    # TODO above put in the rest
    
    ############################################################################
    # User Home view
    url(r'^$', views.home_view),
    url(r'^about/', views.get_about),
    url(r'^maintenance/', views.get_maintenance),

    ############################################################################
    # Project Management
    url(r'^projects/$', views.projects),
    url(r'^project/(\d+)/$', views_optimized.project),

    ############################################################################
    # Corpus management
    # Document view (main)
    url(r'^project/(\d+)/corpus/(\d+)/$', views.corpus),
    url(r'^project/(\d+)/corpus/(\d+)/documents/?$', views.corpus),

    # Journals view
    url(r'^project/(\d+)/corpus/(\d+)/journals/journals.json$', samtest.get_journals_json),
    url(r'^project/(\d+)/corpus/(\d+)/journals$', samtest.get_journals),

    # TODO rest to update corpus and information for progress bar
    url(r'^project/(\d+)/corpus/(\d+)/(\w+)/update$', views.update_nodes),

    ############################################################################
    # annotations App
    url(r'^project/(\d+)/corpus/(\d+)/document/(\d+)/$', annotations_main_view),
    url(r'^annotations/', include(annotations_urls)),
    #
    ############################################################################

    ############################################################################
    ############################################################################
    # TODO put in test folder Provisory tests
    url(r'^tests/mvc$', views.tests_mvc),
    url(r'^tests/mvc-listdocuments$', views.tests_mvc_listdocuments),

    url(r'^tests/istextquery$', pubmedscrapper.getGlobalStatsISTEXT), # api/query?type=istext ?
    url(r'^tests/pubmedquery$', pubmedscrapper.getGlobalStats),
    url(r'^tests/project/(\d+)/pubmedquery/go$', pubmedscrapper.doTheQuery),
    url(r'^tests/project/(\d+)/ISTEXquery/go$', pubmedscrapper.testISTEX),
    url(r'^tests/paginator/corpus/(\d+)/$', views.newpaginatorJSON),
    url(r'^tests/move2trash/$' , views.move_to_trash_multiple ),
    url(r'^project/(\d+)/corpus/(\d+)/terms/ngrams.json$', samtest.get_ngrams_json),
    url(r'^project/(\d+)/corpus/(\d+)/terms$', samtest.get_ngrams),
    url(r'^project/(\d+)/corpus/(\d+)/stop_list.json$', samtest.get_stoplist)
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)

if settings.MAINTENANCE:
    urlpatterns = patterns('',
        url(r'^img/logo.svg$', views.logo),
        url(r'^css/bootstrap.css$', views.css),

        url(r'^$', views.home_view),
        url(r'^about/', views.get_about),
        url(r'^admin/', include(admin.site.urls)),

        url(r'^.*', views.get_maintenance),
    )
