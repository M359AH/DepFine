import urllib.request, json, re, sys

#This will find the registered && unregistered dependencies from the raw data using link have a good luck
class Depfine:

	# Init Function
	def __init__(self, url):
		self.url = url

		self.dep_objects = {
			"1":"dependencies",
			"2":"devDependencies"
		}


 	#  Lambda Function
	all_in = lambda self, data : self.dep_objects["1"] in data.keys() and self.dep_objects["2"] in data.keys()

	merge_dicts = lambda self, dict1={}, dict2={} : {**dict1, **dict2}

	def get_json_data(self, url):
		with urllib.request.urlopen(url) as res:
			return json.loads(res.read().decode())
    	#When you have a bad luck
	def package_found(self, pkg_name):
		url = f"https://corsmirror.herokuapp.com/v1/cors?url=https://registry.npmjs.com/{pkg_name}"
		status_code = urllib.request.urlopen(url).getcode()
		return status_code == 200
		#You are lucky to get this message with 404 <3
	def package_not_found(self, pkg_name):
		url = f"https://corsmirror.herokuapp.com/v1/cors?url=https://registry.npmjs.com/{pkg_name}"
		
		try:
			status_code = urllib.request.urlopen(url).getcode()
		
		except urllib.error.HTTPError as e:
			
			return "404" in str(e)


	def handel_not_founded_dep(self, data):
		if self.all_in(data):
			return self.merge_dicts(data[self.dep_objects["1"] ], data[self.dep_objects["2"]]) 

		if(self.dep_objects["1"] in data.keys() ):
			return data[self.dep_objects['1']]

		if(self.dep_objects["2"]  in data.keys() ):
			return data[self.dep_objects['2']]

		return -1

		#Nice_func
	def check(self, all_deps):
		for i in all_deps.keys():
			if self.package_not_found(i):
				print(f"Possible Unregistered Package --> {i}")

			elif self.package_found(i):
				print(f"Founded --> {i}")
			

	def dep_chcker(self):
		data = self.get_json_data(self.url)

		if self.handel_not_founded_dep(data) == -1:
			print('No Dependencies In This File')
			exit(0)

		self.check(self.handel_not_founded_dep(data))


# Code Driver
if __name__ == "__main__":
	
	if(len(sys.argv) > 1):
		df = Depfine(sys.argv[1])
		df.dep_chcker()


	else:
		print("""

DDDDDDDDDDDDD                                                FFFFFFFFFFFFFFFFFFFFFF  iiii                                       
D::::::::::::DDD                                             F::::::::::::::::::::F i::::i                                      
D:::::::::::::::DD                                           F::::::::::::::::::::F  iiii                                       
DDD:::::DDDDD:::::D                                          FF::::::FFFFFFFFF::::F                                             
  D:::::D    D:::::D     eeeeeeeeeeee    ppppp   ppppppppp     F:::::F       FFFFFFiiiiiiinnnn  nnnnnnnn        eeeeeeeeeeee    
  D:::::D     D:::::D  ee::::::::::::ee  p::::ppp:::::::::p    F:::::F             i:::::in:::nn::::::::nn    ee::::::::::::ee  
  D:::::D     D:::::D e::::::eeeee:::::eep:::::::::::::::::p   F::::::FFFFFFFFFF    i::::in::::::::::::::nn  e::::::eeeee:::::ee
  D:::::D     D:::::De::::::e     e:::::epp::::::ppppp::::::p  F:::::::::::::::F    i::::inn:::::::::::::::ne::::::e     e:::::e
  D:::::D     D:::::De:::::::eeeee::::::e p:::::p     p:::::p  F:::::::::::::::F    i::::i  n:::::nnnn:::::ne:::::::eeeee::::::e
  D:::::D     D:::::De:::::::::::::::::e  p:::::p     p:::::p  F::::::FFFFFFFFFF    i::::i  n::::n    n::::ne:::::::::::::::::e 
  D:::::D     D:::::De::::::eeeeeeeeeee   p:::::p     p:::::p  F:::::F              i::::i  n::::n    n::::ne::::::eeeeeeeeeee  
  D:::::D    D:::::D e:::::::e            p:::::p    p::::::p  F:::::F              i::::i  n::::n    n::::ne:::::::e           
DDD:::::DDDDD:::::D  e::::::::e           p:::::ppppp:::::::pFF:::::::FF           i::::::i n::::n    n::::ne::::::::e          
D:::::::::::::::DD    e::::::::eeeeeeee   p::::::::::::::::p F::::::::FF           i::::::i n::::n    n::::n e::::::::eeeeeeee  
D::::::::::::DDD       ee:::::::::::::e   p::::::::::::::pp  F::::::::FF           i::::::i n::::n    n::::n  ee:::::::::::::e  
DDDDDDDDDDDDD            eeeeeeeeeeeeee   p::::::pppppppp    FFFFFFFFFFF           iiiiiiii nnnnnn    nnnnnn    eeeeeeeeeeeeee  
                                          p:::::p                                                                               
                                          p:::::p                                                                               
                                         p:::::::p                                                                              
                                         p:::::::p                                                                              
                                         p:::::::p                                                                              
                                         ppppppppp



                      Example: python3 dep.py https://raw.RepForPack

			""")
		exit(0)

	
