import word2pdf_service_environment as ENV

from celery import Celery

app = Celery(ENV.WORD2PDF_SVC_SOURCE, broker='amqp://', backend='rpc://', include=[ENV.WORD2PDF_SVC_TASK])

if __name__ == '__main__':
    app.start()