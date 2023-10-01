from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    codeHtml_1 = """
    <!-- blog/templates/blog/home.html -->
    <html>
    <head>
        <title>Welcome to Our Website</title>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>Here you can find information about our project!</p>
    </body>
    </html> 
    """
    return HttpResponse(codeHtml_1)

def articles(request):
    codeHtml_2 = """
      <html>
      <head>
          <title>Articles</title>
      </head>
      <body>
          <h1>Articles</h1>
          <p>Here will be list of articles.</p>
      </body>
      </html>
      """
    return HttpResponse(codeHtml_2)



def currencies(request):
   codeHtml_3 = """
   <html>
   <head>
       <title>Currency</title>
   </head>
   <body>
       <h1>Currency rate</h1>
       <p>1 USD = 88.71 KGS</p>
   </body>
   </html>
   """
   return HttpResponse(codeHtml_3)
