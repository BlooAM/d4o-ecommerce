docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
celery -A d4o_ecommerce flower
celery -A d4o_ecommerce worker -l info --pool=solo
celery -A d4o_ecommerce beat -l info