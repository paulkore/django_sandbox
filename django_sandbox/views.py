from django.http import HttpResponse


def home(request):
    html_content = '''
        <style>
            body {
                font-family: Helvetica, Arial, sans-serif;
                font-size: 12pt;
                font-weight: 400;
            }

            .main-wrapper {
                width: 500px;
                border-radius: 5px;
                margin: 25px;
                padding: 20px;
                background-color: lightblue;
            }

            .message {
                font-weight: bold;
                font-size: 16pt;
                color: green;
            }
        </style>

        <div class="main-wrapper">
            <div class="message">
                This is a sandbox app on the Django framework
            </div>
        </div>
    '''

    return HttpResponse(html_content)
