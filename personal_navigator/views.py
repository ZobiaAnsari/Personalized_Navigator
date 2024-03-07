from django.http import HttpResponse

def nav(request):
    s= '''<h2>Navigation Bar</h2>
    <a href="https://www.youtube.com/"> YouTube </a><br>
    <a href="https://www.instagram.com/"> Instagram </a><br>
    <a href="https://github.com/ZobiaAnsari"> Github </a><br>
    <a href="https://www.netflix.com/"> Netflix </a><br>
    '''
    return HttpResponse(s)
