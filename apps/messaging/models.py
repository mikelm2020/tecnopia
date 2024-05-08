from django.db import models

from apps.abstracts.models import AbstractModel
from apps.users.models import User


class MessageModel(AbstractModel):
    """Model definition for MessageModel."""
    deleted_date = models.DateTimeField('Fecha de Eliminación', auto_now=True, auto_now_add=False, null=True)
    sender= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender') 
    receiver= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='receiver')     
    message_content = models.CharField('Contenido del mensaje', max_length=100, blank=False, null=False, unique=True)    
    
    
    class Meta:
        """Meta definition for MessageModel."""
        ordering = ["id"]
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        
    def __str__(self):
        """Unicode representation of MessageModel."""
        return f"De {self.sender} para {self.receiver}: {self.message_content}"


# TODO: cambiar por el usuario de app users. id de sender y receiver con uuid. como hacer como modo conversación    
