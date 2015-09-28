from django.conf.urls import patterns, include, url


urlpatterns = patterns('home.views',
                       url(r'^$', 'index', {'template_name': 'index.html'}),
                       )



category = '''
            [
                {
                    'a': {
                        'title': 'A',
                        'content':['a1', 'a2']
                    },
                    'd': [
                        {
                            'title': 'D1',
                            'content': ['d1', 'd2', 'd3', 'd1', 'd2', 'd3', 'd1', 'd2', 'd3', 'd1', 'd2', 'd3']
                        },
                        {},
                        {}

                    ],
                    'i': {
                        'title': 'imgtitle',
                        'content': ['img1', 'img2', 'img3']
                    }
                },
                {},
                {},
            ]
            '''
