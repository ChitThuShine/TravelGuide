# *coding: utf-8*
from push_notifications.models import APNSDevice
import logging,os
from django.core.files.storage import default_storage
from django.db.models import FileField

# Get an instance of a logger
logger = logging.getLogger('django')
def file_cleanup(sender, **kwargs):
    """
    File cleanup callback used to emulate the old delete
    behavior using signals. Initially django deleted linked
    files when an object containing a File/ImageField was deleted.

    Usage:
    >>> from django.db.models.signals import post_delete
    >>> post_delete.connect(file_cleanup, sender=MyModel, dispatch_uid="mymodel.file_cleanup")
    """
    for fieldname in sender._meta.get_all_field_names():
        try:
            field = sender._meta.get_field(fieldname)
        except:
            field = None
        if field and isinstance(field, FileField):
            inst = kwargs['instance']
            f = getattr(inst, fieldname)
            m = inst.__class__._default_manager
            if hasattr(f, 'path') and os.path.exists(f.path)\
            and not m.filter(**{'%s__exact' % fieldname: getattr(inst, fieldname)})\
            .exclude(pk=inst._get_pk_val()):
                try:
                    default_storage.delete(f.path)
                    logger.info("On efface le fichier %s" % f.path)
                except:
                    pass

def signal_delete_model(sender,**kwargs):
    logger.info("=========================  SIGNAL DELETE  =======================")
    file_cleanup(sender,kwargs)

def signal_add_user(sender,**kwargs):
    # On récupére tous les utilisateurs qui ont pour favori l'utilisateur du produit
    # On ajoute dans la table de notification le message Notif a envoyer
    if not kwargs['created']: return None
    #Creation Code
    toUser = kwargs['instance']
    if toUser.pushToken:
        try:
            device = APNSDevice.objects.get(registration_id=toUser.pushToken, active=True)
            device.send_message('Ceci est le texte de ma notification', badge=1)
        except Exception as e:
            logger.info("Impossible d'envoyer push une exception est survenue %s", e)
    else:
        logger.info("on doit envoyer un message à un user qui n'a pas de token")



