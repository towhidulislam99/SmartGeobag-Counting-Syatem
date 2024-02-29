from django.db import models

# Create your models here.

class GeobagRiverBank(models.Model):
    geobag_at_riverbank_img = models.ImageField(upload_to='Geobag_at_RiverBank_img/', default='No images')
    image_figure_text = models.CharField(max_length = 500)
    
class FilledRiverBank(models.Model):
    geobag_counting_riverbank_img = models.ImageField(upload_to='Geobag_at_RiverBank_img/', default='No images')
    counting_figure_text = models.CharField(max_length = 500)
    
class PrototypeProposed(models.Model):
    prototype_of_proposed_img = models.ImageField(upload_to='Geobag_at_RiverBank_img/', default='No images')
    proposed_figure_text = models.CharField(max_length = 500, default='Default value')
    
class PreparingDataset(models.Model):
    preparing_pataset_img = models.ImageField(upload_to='Geobag_at_RiverBank_img/', default='No images')
    preparing_dataset_figure_text = models.CharField(max_length = 500)
    
class TestingProcedures(models.Model):
    testing_procedures_img = models.ImageField(upload_to='Geobag_at_RiverBank_img/', default='No images')
    testing_procedures_figure_text = models.CharField(max_length = 500)
    

class ToonificationHeading(models.Model):
   toonification_heading = models.CharField(max_length = 500)
   
class ToonificationImage(models.Model):
   toonification_photo = models.ImageField(upload_to='ToonificationImage/', default='No images')

