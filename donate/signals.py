from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from donate.models import Streamer, Ecpay, Opay
from utils.getDonateData import ecpay, opay
from schedulers.apschedulers import sched
from apscheduler.triggers.interval import IntervalTrigger
import logging, json
from utils.message_wrapper import send_message
from utils.queue_wrapper import get_queue
from django.forms.models import model_to_dict
from utils import jsonExtend

@receiver(pre_save, sender=Streamer)
def streamerPreSaveHandler(sender, instance, **kwargs):
    if ecpay(instance.ecpayId) == None:
        instance.ecpayId = None
    if opay(instance.opayId) == None:
        instance.opayId = None


@receiver(post_save, sender=Streamer)
def streamerPostSaveHandler(sender, instance, **kwargs):
    # * Create Jobs
    try:
        sched.remove_job(job_id=instance.deleteKey)
    except:
        logging.exception(f"Delete Key: {instance.deleteKey} doesn't have any Job")
    if instance.ecpayId or instance.opayId:
        sched.add_job(
            getDonateData,
            args=instance,
            trigger=IntervalTrigger(seconds=30),
            id=instance.deleteKey,
        )


@receiver(post_delete, sender=Streamer)
def streamerPostDeleteHandler(sender, instance, **kwargs):
    try:
        sched.remove_job(job_id=instance.deleteKey)
    except:
        logging.exception(f"Delete Key: {instance.deleteKey} doesn't have any Job")
    logging.info(f"{instance.deleteKey} has been delete")


def getDonateData(instance):
    # * GetData
    # * Input to Opay & Ecpay
    EcpayQuerySet = []
    OpayQuerySet = []
    if instance.ecpayId:
        EcpayQuerySet = [
            Ecpay(streamer=instance, donateId=data.pop("donateid"), **data)
            for data in ecpay(instance.ecpayId)
        ]
    if instance.opayId:
        OpayQuerySet = [
            Opay(streamer=instance, donateId=data.pop("donateid"), **data)
            for data in opay(instance.opayId)
        ]
    QuerySet = EcpayQuerySet + OpayQuerySet
    for item in QuerySet:
        try:
            item.save()
        except:
            logging.exception("Item is already in Database")


@receiver(post_save, sender=Ecpay)
def EcpayNotifySend(sender, instance, **kwargs):

    queue = get_queue("DonateNoti")
    data = model_to_dict(
        instance=instance, fields=["streamer", "donateId", "name", "amount", "msg"]
    )

    data["streamer"] = Streamer.objects.get(id=data["streamer"]).twitchId
    message = json.dumps(data, cls=jsonExtend.DecimalEncoder)
    send_message(queue=queue, message_body=message)

    pass


@receiver(post_save, sender=Opay)
def OpayNotifySend(sender, instance, **kwargs):

    queue = get_queue("DonateNoti")
    data = model_to_dict(
        instance=instance, fields=["streamer", "donateId", "name", "amount", "msg"]
    )
    data["streamer"] = Streamer.objects.get(id=data["streamer"]).twitchId
    message = json.dumps(data, cls=jsonExtend.DecimalEncoder)
    send_message(queue=queue, message_body=message)

    pass
