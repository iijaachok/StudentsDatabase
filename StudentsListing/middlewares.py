from django.db import connection
from django.template import Template, Context


class QueryStatistics:
    def process_response(self, request, response):

        time = sum(float(query['time']) for query in connection.queries)
        count = len(connection.queries)

        template = Template('''

            <div class="navbar-fixed-bottom row-fluid">
                <div class="navbar-inner">
                    <div class="container">

                     <i>Total query count: {{ count }}<br/>
                     Total execution time: {{ time }}</i>
                    </div>
                </div>
            </div>
            ''')

        context = {'count': count, 'time': time}

        # Kill me please
        response.content = response.content + bytes(template.render(Context(context)), 'utf-8')
        return response