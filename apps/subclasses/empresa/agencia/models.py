from django.db import models

'''
	SUBCLASSE DE AGENCIA
'''
class Agencia(models.Model):
	id_agencia = models.AutoField(primary_key=True)
	id_empresa = models.ForeignKey('default.Empresa', on_delete = models.CASCADE,related_name='agencia_name')
	logo = models.ImageField(upload_to="default/project",null=True, blank=True)

	def __str__(self):
		return self.id_empresa.nomefantasia
	def __unicode__(self):
		return unicode(self.id_empresa.nomefantasia)