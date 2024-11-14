Introduction
This program identifies an efficient method of delivering packages for WGU transit so all delivery requirements can be met. It uses Python and the Greedy Nearest Neighbor Algorithm.

Data Structure Identification
Package object – Store all the components for the packages (ID, address, city, state, zipcode, deadline, weight, status, departure time, delivery time.
Truck object – Store all components for the Trucks (max # of packages, speed, load, list of packages on board the truck, mileage, address, departure time).
Chaining Hash tables – Store all packages into table from CSV file. Updated as the packages are loaded and delivered.

Explanation of Data Structure
Package objects will be used to hold the data and inserted into the hash table using the packageID as a key. 

Algorithm’s Logic
Greedy_neighbor_algorithm function – accepts truck object
	Create empty array that will hold packages that aren’t delivered yet
For loop to put all packages into an array from package hash table (this hash table will be preloaded with all the packages prior to start of function)
While loop -> while array of not delivered yet has items in it, execute a for loop to add nearest package (based on distance from hash table) into a list for the truck package list one at a time. 
	Add next closest package to truck object list
Remove package from not delivered array
Update truck mileage based on distance from hash table
Update time of truck delivery based on average speed 
Update current address of truck
((Algorithm called with first truck. Then second truck. Once trucks have returned can call algorithm with third truck. ))

Development Environment
IDE: PyCharm 2024.2.4 (Professional Edition)
Python 3.11 
Windows 10 Desktop PC 
	Processor: Intel ® Core™ i5-10400 CPU @ 2.900GHz 2.90 GHz

Space and Time complexity using Big-O notation
Time Complexity of Program – O(N^2) 
Greedy/Nearest Neighbor Time Complexity – O(N^2)
Display All Packages to UI Time Complexity – O(N)
Display One Package to UI Time Complexity – O(1)
Space Complexity – O(N)

Scalability and Adaptability
The scalability of the program is limited by the manual loading of the trucks and the truck load size (which is set to a max of 20 packages). Adapting the program would require changing the loading to be a function which would then have to determine the best order which to load the trucks. It would also require having a newly resized Hash Table with the new amount of packages required.

Software Efficiency and Maintainability 
The software is efficient enough to deliver the packages within the required rules. Is it the most efficient algorithm out there to solve this problem? Definitely not. The greedy algorithm just finds one solution that works within the constraints given.
Maintaining this software would be relatively easy given all of the comments that help explain what each section and function are. The only things to maintain would be the files and keeping up to date with Python changes.

Self-Adjusting Data Structures 
The strength of the hash table is how quickly it is to retrieve/remove/search for items stored within. This allows for a more efficient program vs. using a standard array/table.
The downside of the hash table is the maximum amount of items needed to store should be known, otherwise it has to be resized, which takes O(N) additional time to do.

Data Key
The package ID is the one item that does not change and is unique to the package. All of the other options (address, deadline, city, zip code, weight, delivery status) are not unique to the item itself, so it would not be a valid key.

Sources
Tepe, Cemal C950: Webinar-1 Let’s Go Hashing.
	Retrieved October 24, 2024, from
https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
Tepe, Cemal C950: Webinar-2 Getting Greedy, who moved my data?
	Retrieved October 24, 2024, from
https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=eee77a88-4de8-4d42-a3c3-ac8000ece256

“C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor.” WGU. https://srm--c.vf.force.com/apex/coursearticle?Id=kA03x000001DbBGCA0 
