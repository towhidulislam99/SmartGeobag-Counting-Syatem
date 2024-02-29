from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import GeobagRiverBank,FilledRiverBank,PrototypeProposed,PreparingDataset,TestingProcedures,TestingProcedures,ToonificationHeading,ToonificationImage
import os

def Geobag(request):
    geobagriverbankdata = GeobagRiverBank.objects.all()
    filledriverbankdata = FilledRiverBank.objects.all()
    prototypeproposeddata = PrototypeProposed.objects.all()
    preparingdatasetdata = PreparingDataset.objects.all()
    testingproceduresdata = TestingProcedures.objects.all()
    toonificationheadingdata = ToonificationHeading.objects.all()
    toonificationimagedata = ToonificationImage.objects.all()
   
    

    data = {
        'geobagriverbankdata': geobagriverbankdata,
        'filledriverbankdata': filledriverbankdata,
        'prototypeproposeddata': prototypeproposeddata,
        'preparingdatasetdata': preparingdatasetdata,
        'testingproceduresdata': testingproceduresdata,
        'toonificationheadingdata': toonificationheadingdata,
        'toonificationimagedata': toonificationimagedata,
    }
    return render(request, 'index.html', data)

#===============================================================================================

#===============================================================================================

def Geobagdatatable(request):
    geobagriverbankdata = GeobagRiverBank.objects.all()
    filledriverbankdata = FilledRiverBank.objects.all()
    prototypeproposeddata = PrototypeProposed.objects.all()
    preparingdatasetdata = PreparingDataset.objects.all()
    testingproceduresdata = TestingProcedures.objects.all()
    toonificationheadingdata = ToonificationHeading.objects.all()
    toonificationimagedata = ToonificationImage.objects.all()
   
    

    data = {
        'geobagriverbankdata': geobagriverbankdata,
        'filledriverbankdata': filledriverbankdata,
        'prototypeproposeddata': prototypeproposeddata,
        'preparingdatasetdata': preparingdatasetdata,
        'testingproceduresdata': testingproceduresdata,
        'toonificationheadingdata': toonificationheadingdata,
        'toonificationimagedata': toonificationimagedata,
    }
    return render(request, 'GeobagDataTable.html', data)

#===============================================================================================

#===============================================================================================

def geobagriverbank(request):
     return render(request, 'geobagimageinput.html')

def geobagriverbank_input(request):
    if request.method == 'POST':

        geobag_at_riverbank_img = request.FILES.get('geobag_at_riverbank_img')
        image_figure_text = request.POST.get('image_figure_text')

        geobagimage_obj = GeobagRiverBank()
        geobagimage_obj.geobag_at_riverbank_img = geobag_at_riverbank_img
        geobagimage_obj.image_figure_text = image_figure_text
        geobagimage_obj.save()

        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable')  

    return render(request, 'Geobag_input_image.html') 

 
def geobagriverbank_edit(request, id):
    geobagriverbankdata = GeobagRiverBank.objects.get(id=id)
    data = {"geobagriverbankdata": geobagriverbankdata}
    return render(request,'geobagimageUpdate.html',data)

def geobagriverbank_update(request):
    id = request.POST.get('id')
    image_figure_text = request.POST.get('image_figure_text')
  
    # Get the user object by ID
    geobagriverbank_obj = get_object_or_404(GeobagRiverBank, id=id)
    
    # Check if new image and video files are provided
    if 'geobag_at_riverbank_img' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if geobagriverbank_obj.geobag_at_riverbank_img:
            os.remove(geobagriverbank_obj.geobag_at_riverbank_img.path)
        geobagriverbank_obj.geobag_at_riverbank_img = request.FILES['geobag_at_riverbank_img']
    
    geobagriverbank_obj.image_figure_text = image_figure_text
    geobagriverbank_obj.save()
    return redirect('Geobagdatatable')

def geobagriverbank_delete(request, id):
    geobagriverbank_obj = get_object_or_404(GeobagRiverBank, id=id)
    geobagriverbank_obj.delete()
    return redirect('Geobagdatatable')
    

#===============================================================================================

#===============================================================================================
def filledriverbank(request):
     return render(request, 'filledriverbankinput.html')

def filledriverbank_input(request):
    if request.method == 'POST':

        geobag_counting_riverbank_img = request.FILES.get('geobag_counting_riverbank_img')
        counting_figure_text = request.POST.get('counting_figure_text')

        filledriverbank_obj = FilledRiverBank()
        filledriverbank_obj.geobag_counting_riverbank_img = geobag_counting_riverbank_img
        filledriverbank_obj.counting_figure_text = counting_figure_text
        filledriverbank_obj.save()

        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable')  


    return render(request, 'filledriverbankinput.html') 

def filledriverbank_edit(request, id):
    filledriverbankdata = FilledRiverBank.objects.get(id=id)
    data = {"filledriverbankdata": filledriverbankdata}
    return render(request,'filledriverbankUpdate.html',data)

def filledriverbank_update(request):
    id = request.POST.get('id')
    counting_figure_text = request.POST.get('counting_figure_text')
  
    # Get the user object by ID
    filledriverbank_obj = get_object_or_404(FilledRiverBank, id=id)
    
    # Check if new image and video files are provided
    if 'geobag_counting_riverbank_img' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if filledriverbank_obj.geobag_counting_riverbank_img:
            os.remove(filledriverbank_obj.geobag_counting_riverbank_img.path)
        filledriverbank_obj.geobag_counting_riverbank_img = request.FILES['geobag_counting_riverbank_img']
    
    filledriverbank_obj.counting_figure_text = counting_figure_text
    filledriverbank_obj.save()
    return redirect('Geobagdatatable')

def filledriverbank_delete(request, id):
    filledriverbank_obj = get_object_or_404(FilledRiverBank, id=id)
    filledriverbank_obj.delete()
    return redirect('Geobagdatatable')


#===============================================================================================

#===============================================================================================
def prototypeproposed(request):
     return render(request, 'prototypeproposedinput.html')

def prototypeproposed_input(request):
    if request.method == 'POST':

        prototype_of_proposed_img = request.FILES.get('prototype_of_proposed_img')
        proposed_figure_text = request.POST.get('proposed_figure_text')

        prototypeproposed_obj = PrototypeProposed()
        prototypeproposed_obj.prototype_of_proposed_img = prototype_of_proposed_img
        prototypeproposed_obj.proposed_figure_text = proposed_figure_text
        prototypeproposed_obj.save()

        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable')  


    return render(request, 'prototypeproposedinput.html') 

def prototypeproposed_edit(request, id):
    prototypeproposeddata = PrototypeProposed.objects.get(id=id)
    data = {"prototypeproposeddata": prototypeproposeddata}
    return render(request,'prototypeproposedUpdate.html',data)

def prototypeproposed_update(request):
    id = request.POST.get('id')
    proposed_figure_text = request.POST.get('proposed_figure_text')
  
    # Get the user object by ID
    prototypepropose_obj = get_object_or_404(PrototypeProposed, id=id)
    
    # Check if new image and video files are provided
    if 'prototype_of_proposed_img' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if prototypepropose_obj.prototype_of_proposed_img:
            os.remove(prototypepropose_obj.prototype_of_proposed_img.path)
        prototypepropose_obj.prototype_of_proposed_img = request.FILES['prototype_of_proposed_img']
    
    prototypepropose_obj.proposed_figure_text = proposed_figure_text
    prototypepropose_obj.save()
    return redirect('Geobagdatatable')

def prototypeproposed_delete(request, id):
    prototypepropose_obj = get_object_or_404(PrototypeProposed, id=id)
    prototypepropose_obj.delete()
    return redirect('Geobagdatatable')


#===============================================================================================

#===============================================================================================
def preparingdataset(request):
     return render(request, 'preparingdatasetinput.html')

def preparingdataset_input(request):
    if request.method == 'POST':

        preparing_pataset_img = request.FILES.get('preparing_pataset_img')
        preparing_dataset_figure_text = request.POST.get('preparing_dataset_figure_text')

        preparingdataset_obj = PreparingDataset()
        preparingdataset_obj.preparing_pataset_img = preparing_pataset_img
        preparingdataset_obj.preparing_dataset_figure_text = preparing_dataset_figure_text
        preparingdataset_obj.save()

        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable')  


    return render(request, 'preparingdatasetinput.html') 

def preparingdataset_edit(request, id):
    preparingdatasetdata = PreparingDataset.objects.get(id=id)
    data = {"preparingdatasetdata": preparingdatasetdata}
    return render(request,'preparingdatasetUpdate.html',data)

def preparingdataset_update(request):
    id = request.POST.get('id')
    preparing_dataset_figure_text = request.POST.get('preparing_dataset_figure_text')
  
    # Get the user object by ID
    preparingdatase_obj = get_object_or_404(PreparingDataset, id=id)
    
    # Check if new image and video files are provided
    if 'preparing_pataset_img' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if preparingdatase_obj.preparing_pataset_img:
            os.remove(preparingdatase_obj.preparing_pataset_img.path)
        preparingdatase_obj.preparing_pataset_img = request.FILES['preparing_pataset_img']
    
    preparingdatase_obj.preparing_dataset_figure_text = preparing_dataset_figure_text
    preparingdatase_obj.save()
    return redirect('Geobagdatatable')

def preparingdataset_delete(request, id):
    preparingdatase_obj = get_object_or_404(PreparingDataset, id=id)
    preparingdatase_obj.delete()
    return redirect('Geobagdatatable')


#===============================================================================================

#===============================================================================================
def testingprocedures(request):
     return render(request, 'testingprocedureinput.html')

def testingprocedures_input(request):
    if request.method == 'POST':

        testing_procedures_img = request.FILES.get('testing_procedures_img')
        testing_procedures_figure_text = request.POST.get('testing_procedures_figure_text')

        testingprocedures_obj = TestingProcedures()
        testingprocedures_obj.testing_procedures_img = testing_procedures_img
        testingprocedures_obj.testing_procedures_figure_text = testing_procedures_figure_text
        testingprocedures_obj.save()

        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable')  


    return render(request, 'testingprocedureinput.html') 

def testingprocedures_edit(request, id):
    testingproceduresdata = TestingProcedures.objects.get(id=id)
    data = {"testingproceduresdata": testingproceduresdata}
    return render(request,'testingprocedureUpdate.html',data)

def testingprocedures_update(request):
    id = request.POST.get('id')
    testing_procedures_figure_text = request.POST.get('testing_procedures_figure_text')
  
    # Get the user object by ID
    testingprocedures_obj = get_object_or_404(TestingProcedures, id=id)
    
    # Check if new image and video files are provided
    if 'testing_procedures_img' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if testingprocedures_obj.testing_procedures_img:
            os.remove(testingprocedures_obj.testing_procedures_img.path)
        testingprocedures_obj.testing_procedures_img = request.FILES['testing_procedures_img']
    
    testingprocedures_obj.testing_procedures_figure_text = testing_procedures_figure_text
    testingprocedures_obj.save()
    return redirect('Geobagdatatable')

def testingprocedures_delete(request, id):
    testingprocedures_obj = get_object_or_404(TestingProcedures, id=id)
    testingprocedures_obj.delete()
    return redirect('Geobagdatatable')


#     <-------Toonification Heading  Section Work -----------------> 
#====================================================================================

def toonificationheadingpage(request):
    return render(request, 'toonificationheadingpage.html')

def toonificationheadinginsert(request):
    if request.method == 'POST':
        toonification_heading = request.POST.get('toonification_heading')
        
        toonificationHeading_obj = ToonificationHeading()
        toonificationHeading_obj.toonification_heading = toonification_heading
        toonificationHeading_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable') 
    
    return render(request, 'toonificationheadingpage.html')  

def Toonificationdatatable(request):
    toonificationheadingdata = ToonificationHeading.objects.all()
    data = {"toonificationheadingdata": toonificationheadingdata}
    return render(request,'toonificationdatatable.html', data)

def ToonificationHeadingpageedit(request, id):
    toonificationheadingdata = ToonificationHeading.objects.get(id=id)
    data = {"toonificationheadingdata": toonificationheadingdata}
    return render(request,'toonificationheadingpageUpdate.html',data)

def ToonificationHeadingupdate(request):
    id = request.POST.get('id')
    toonification_heading = request.POST.get('toonification_heading')
   
    # Get the user object by ID
    toonificationHeading_obj = get_object_or_404(ToonificationHeading, id=id)
    
    toonificationHeading_obj.toonification_heading = toonification_heading
    toonificationHeading_obj.save()
    return redirect('Geobagdatatable')

def deleteToonificationHeading(request, id):
    toonificationHeading_obj = get_object_or_404(ToonificationHeading, id=id)
    toonificationHeading_obj.delete()
    return redirect('Geobagdatatable')

#     <-------Toonification Imgae/Photo Section Work -----------------> 
#====================================================================================

def toonificationimagepage(request):
    return render(request, 'toonificationimagepage.html')

def toonificationimageinsert(request):
    if request.method == 'POST':
        toonification_photo = request.FILES.get('toonification_photo')
        
        toonificationImage_obj = ToonificationImage()
        toonificationImage_obj.toonification_photo = toonification_photo
        toonificationImage_obj.save()
        
        messages.success(request, 'Data submitted successfully.')
        return redirect('Geobagdatatable')  
    
    return render(request, 'toonificationimagepage.html')  

def toonificationimagedatatable(request):
    toonificationimagedata = ToonificationImage.objects.all()
    data = {"toonificationimagedata": toonificationimagedata}
    return render(request,'toonificationimagedatatable.html', data)

def toonificationimagepageedit(request, id):
    toonificationimagedata = ToonificationImage.objects.get(id=id)
    data = {"toonificationimagedata": toonificationimagedata}
    return render(request,'tonificationimagepageUpdate.html',data)

def toonificationimageupdate(request):
    id = request.POST.get('id')

    # Get the user object by ID
    toonificationImage_obj = get_object_or_404(ToonificationImage, id=id)
    
     # Check if new image and video files are provided
    if 'toonification_photo' in request.FILES:
        # If a new image is provided, delete the old one if it exists
        if toonificationImage_obj.toonification_photo:
            os.remove(toonificationImage_obj.toonification_photo.path)
        toonificationImage_obj.toonification_photo = request.FILES['toonification_photo']
   
    toonificationImage_obj.save()
    return redirect('Geobagdatatable')

def deletetoonificationimage(request, id):
    toonificationImage_obj = get_object_or_404(ToonificationImage, id=id)
    toonificationImage_obj.delete()
    return redirect('Geobagdatatable')