import justpy as jp

'''
    refer to : "highcharts docs" 、 "quasar style" those website  

'''
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text= 'Analysis of Course Review',
                 classes='text-h3 text-center q-pa-md')   # a= where it belong
    p1 = jp.QDiv(a=wp, text= 'These graphs represent course review analysis')
    return wp
jp.justpy(app)