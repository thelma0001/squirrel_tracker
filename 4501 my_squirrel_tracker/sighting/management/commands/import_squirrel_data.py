from django.core.management import BaseCommand
from sighting.models import SquirrelCensusDatas

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			dest='file_path',
			type=str,  
			help='import_squirrel_data',
		)

	def handle(self, *args, **options):
		file_path = options["file_path"]
		if file_path.startswith('/'):
			file_path = file_path[1:]
		with open(file_path,'rb') as f:
			read_data = f.readlines()

		for data in read_data[1:]:
			data_list = data.decode().split(',')

			Latitude = data_list[0]
			Longitude = data_list[1]
			Unique_Squirrel_ID = data_list[2]
			Shift = data_list[4]
			Date = data_list[5]
			Age = data_list[7]
			# print(Latitude,Longitude, Unique_Squirrel_ID, Shift, Date, Age)
			SquirrelCensusDatas.objects.update_or_create(
				Latitude = Latitude,
				Longitude = Longitude,
				Unique_Squirrel_ID = Unique_Squirrel_ID,
				Shift = Shift,
				Date = Date,
				Age = Age,
			)

if __name__ == "__main__":
	with open("C:/Users/Administrator/Desktop/APP/path/to/file.csv",'rb') as f:
		read_data = f.readlines()

	for data in read_data[1:5]:
		data_list = data.decode().split(',')

		Latitude = data_list[0]
		Longitude = data_list[1]
		Unique_Squirrel_ID = data_list[2]
		Shift = data_list[4]
		Date = data_list[5]
		Age = data_list[7]
		print(Latitude,Longitude, Unique_Squirrel_ID, Shift, Date, Age)