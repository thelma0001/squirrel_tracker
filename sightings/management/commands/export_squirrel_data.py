from django.core.management import BaseCommand
from sighting.models import SquirrelCensusDatas

class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument(
			dest='file_path',
			type=str,  
			help='export_squirrel_data',
		)

	def handle(self, *args, **options):
		file_path = options["file_path"]
		all = SquirrelCensusDatas.objects.all()
		# print(len(all))
		file = open(file_path,'w')
		file.write("Latitude,Longitude,Unique Squirrel ID,Shift,Date,Age\n")
		for data in all:
			write_str = "{},{},{},{},{},{}\n".format(data.Latitude,data.Longitude,data.Unique_Squirrel_ID,data.Shift,data.Date,data.Age)
			file.write(write_str)
		file.close()
		# print("export_squirrel_data")


if __name__ == "__main__":
	file_path = "C:/Users/Administrator/Desktop/file.csv"
	all = SquirrelCensusDatas.objects.all()
	print(len(all))
	file = open(file_path,'w')
	file.write("Latitude,Longitude,Unique Squirrel ID,Shift,Date,Age\n")
	for data in all:
		write_str = "{},{},{},{},{},{}\n".format(data.Latitude,data.Longitude,data.Unique_Squirrel_ID,data.Shift,data.Date,data.Age)
		file.write(write_str)
	file.close()