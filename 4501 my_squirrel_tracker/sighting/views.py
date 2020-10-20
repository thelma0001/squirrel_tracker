from django.shortcuts import render
from sighting.models import SquirrelCensusDatas

# Create your views here.
from django.http import HttpResponse,request,response
from django.core.paginator import Paginator
from django.db.models import Max,Count,Avg,Min

def get_page_list(page,data_len,page_num=7):
	lis = list(range(page-2,page+page_num-2))
	if lis[0]<=0 or lis[-1]>=data_len:
		lis = list(range(1,page_num+1)) + ["..."] + [data_len-1,data_len]
	elif lis[-1]>=data_len:
		lis = [1,2] + ["..."] + list(range(data_len-page_num+1,data_len+1))
	else:
		lis = lis + ["..."] + [data_len-1,data_len]
	next_page = page +1
	if next_page>data_len:
		next_page = data_len
	lis = lis + [next_page]
	lis = [str(l) for l in lis]
	return lis

def sightings(request):
	try:
		page = int(request.GET["page"])
	except:
		page = 1
	num = 10
	all_data_liat = SquirrelCensusDatas.objects.all()
	data_len = len(all_data_liat)//num + 1
	page_list = get_page_list(page,data_len)

	data_list = all_data_liat[(page-1)*num:page*num]
	return render(request,"template/sightings.html",{"data":data_list, "page_list":page_list[:-1],"last_page":page_list[-1], "page":str(page)})

def add(request):
	msg = ""
	if request.POST!={}:
		scd = SquirrelCensusDatas()
		scd.Latitude = request.POST["Latitude"]
		scd.Longitude = request.POST["Longitude"]
		scd.Unique_Squirrel_ID = request.POST["Unique_Squirrel_ID"]
		scd.Shift = request.POST["Shift"]
		scd.Date = request.POST["Date"]
		scd.Age = request.POST["Age"]
		id_len = len(SquirrelCensusDatas.objects.filter(Unique_Squirrel_ID=scd.Unique_Squirrel_ID))
		if scd.Unique_Squirrel_ID == "" or scd.Latitude=="" or scd.Longitude=="" :
			msg = "Added Failed! Latitude, Longitude and Unique Squirrel ID can't be empty!"
		elif id_len>0:
			msg = "Added Failed! Unique Squirrel ID is exist!"
		else:
			try:
				scd.save()
				msg = "Added successfully!"
			except:
				msg = "Added Failed! Failed to add data!"

	return render(request,"template/add.html",{"msg":msg})
	# return render(request,"template/add.html",{"data":data_list, "page_list":page_list[:-1],"last_page":page_list[-1], "page":str(page)})

def update(request):
	msg = ""
	if request.POST!={}:
		scd = SquirrelCensusDatas()
		scd_filter = SquirrelCensusDatas.objects.filter(Unique_Squirrel_ID=request.POST["Unique_Squirrel_ID"])
		id_len = len(scd_filter)
		if id_len>0:
			scd.id = scd_filter[0].id
			scd.Latitude = request.POST["Latitude"]
			scd.Longitude = request.POST["Longitude"]
			scd.Unique_Squirrel_ID = request.POST["Unique_Squirrel_ID"]
			scd.Shift = request.POST["Shift"]
			scd.Date = request.POST["Date"]
			scd.Age = request.POST["Age"]

			if scd.Unique_Squirrel_ID == "" or scd.Latitude=="" or scd.Longitude=="" :
				msg = "Updated Failed! Latitude, Longitude and Unique Squirrel ID can't be empty!"
			else:
				try:
					scd.save()
					msg = "Updated successfully!"
				except:
					msg = "Updated Failed!"
		else:
			msg = "Updated Failed! Unique Squirrel ID is not exist!"

	return render(request,"template/update.html",{"msg":msg})

def stats(request):	
	scd = SquirrelCensusDatas.objects
	scd2 = SquirrelCensusDatas
	data_count = scd.count()
	Unique_Squirrel_ID_count = scd.count()
	Date_min = scd.filter().aggregate(Min('Date'))["Date__min"]
	Date_max = scd.filter().aggregate(Max('Date'))["Date__max"]
	Age_Adult_count = scd.filter(Age="Adult").count()
	Age_Juvenile_count = scd.filter(Age="Juvenile").count()
	Shift_AM_count = scd.filter(Shift="AM").count()
	Shift_PM_count = scd.filter(Shift="PM").count()
	Latitude_min = scd.filter().aggregate(Min('Latitude'))["Latitude__min"]
	Latitude_max = scd.filter().aggregate(Max('Latitude'))["Latitude__max"]
	Latitude_avg = scd.filter().aggregate(Avg('Latitude'))["Latitude__avg"]
	Longitude_min = scd.filter().aggregate(Min('Longitude'))["Longitude__min"]
	Longitude_max = scd.filter().aggregate(Max('Longitude'))["Longitude__max"]
	Longitude_avg = scd.filter().aggregate(Avg('Longitude'))["Longitude__avg"]

	dic = {
		"data_count": data_count,
		"Unique_Squirrel_ID_count": Unique_Squirrel_ID_count,
		"Date_min": Date_min,
		"Date_max": Date_max,
		"Age_Adult_count": Age_Adult_count,
		"Age_Juvenile_count": Age_Juvenile_count,
		"Shift_AM_count": Shift_AM_count,
		"Shift_PM_count": Shift_PM_count,
		"Latitude_min": Latitude_min,
		"Latitude_max": Latitude_max,
		"Latitude_avg": Latitude_avg,
		"Longitude_min": Longitude_min,
		"Longitude_max": Longitude_max,
		"Longitude_avg": Longitude_avg,
	}
	return render(request,"template/stats.html",dic)

if __name__ == "__main__":
	page_num = 7
	data_len = 2034
	page = 2028
	lis = list(range(page-2,page+page_num-2))
	if lis[0]<=0 or lis[-1]>=data_len:
		lis = list(range(1,page_num+1)) + ["..."] + [data_len-1,data_len]
	elif lis[-1]>=data_len:
		lis = [1,2] + ["..."] + list(range(data_len-page_num+1,data_len+1))
	else:
		lis = lis + ["..."] + [data_len-1,data_len]
	next_page = page +1
	if next_page>data_len:
		next_page = data_len
	lis = [page,] + lis + [next_page]
	lis = [str(l) for l in lis]