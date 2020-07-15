from django.db import models

# Create your models here.
class DocRequestListMki(models.Model):
    description = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/',  blank=True, null=True)
    owner = models.CharField(max_length=20, blank=True)
    owner_fio = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    main_researcher = models.CharField(max_length=50, blank=True, null=True)

    list_members = models.FileField(upload_to='list_members/', blank=True, null=True)

    ver_bio = models.CharField(max_length=50, blank=True, null=True)

    accept_research = models.FileField(upload_to='accept_research/', blank=True, null=True)
    accept_research_version = models.CharField(max_length=50, blank=True, null=True)
    accept_research_date = models.CharField(max_length=50, blank=True, null=True)

    protocol_research = models.FileField(upload_to='protocol_research/', blank=True, null=True)
    protocol_research_version = models.CharField(max_length=50, blank=True, null=True)
    protocol_research_date = models.CharField(max_length=50, blank=True, null=True)

    form_inf = models.FileField(upload_to='form_inf/', blank=True, null=True)
    form_inf_version = models.CharField(max_length=50, blank=True, null=True)
    form_inf_date = models.CharField(max_length=50, blank=True, null=True)\

    cast_researcher = models.FileField(upload_to='form_inf/', blank=True, null=True)
    cast_researcher_version = models.CharField(max_length=50, blank=True, null=True)
    cast_researcher_date = models.CharField(max_length=50, blank=True, null=True)

    contract = models.FileField(upload_to='contract/', blank=True, null=True)
    contract_date = models.CharField(max_length=50, blank=True, null=True)

    advertising = models.FileField(upload_to='advertising/', blank=True, null=True)

    write_objects = models.FileField(upload_to='write_objects/', blank=True, null=True)

    name_another_doc = models.CharField(max_length=50, blank=True, null=True)
    another_doc = models.FileField(upload_to='another_doc/', blank=True, null=True)
    another_doc_version = models.CharField(max_length=50, blank=True, null=True)
    another_doc_date = models.CharField(max_length=50, blank=True, null=True)









    podpis = models.FileField(upload_to='podpis/',max_length=30)
    num_podpis = models.CharField(max_length=30,)
    date_podpis = models.CharField(max_length=30,)

    test = models.FileField(max_length=30,  blank=True, null=True)
    num_test = models.CharField(max_length=30,  blank=True, null=True)
    date_test = models.CharField(max_length=30,  blank=True, null=True)