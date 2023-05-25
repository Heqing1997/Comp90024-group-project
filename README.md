# Comp90024-group-project


Backend and Frontend code are in different Braches.

For quick access. Our website can be accessed directly via URL http://172.26.135.144:5000/ within the University
of Melbourne campus network. Cisco VPN with a valid Unimelb account credential is required if you are out of university.

To run on the local computer:

1.	Clone the repository from the main branch, run:

	git clone https://github.com/Heqing1997/Comp90024-group-project.git
	cd Comp90024-group-project

2.	Install harvester dependencies:

	pip install couchdb
	pip install mastodon.py
	pip install nltk

3.	 Run the harvesters:

	python harvester_filter.py
	python mastodon_harvester.py


4.	Clone the repository from backend branch, run:

	git clone -b backend https://github.com/Heqing1997/Comp90024-group-project.git
	cd Comp90024-group-project

5.	Install dependencies: 

	cd Backend
	pip install -r requirements.txt
									

6.	Run the backend:

     	python app. py   
 

7.	Clone the repository from the frontend branch, run:
              
        git clone -b backend https://github.com/Heqing1997/Comp90024-group-project.git
        cd Comp90024-group-project

8.	Install dependencies:

	cd Frontend
	npm install
	
9.	Run the frontend:
              
        npm run dev


 

Deploy the system:

1.	Log in to the cloud instance with the key, in the main branch folder:

	cd Comp90024-group-project
	ssh -i demokey1.pem ubuntu@172.26.135.144


2.	Copy the Ansible playbook with name harvester.yam to the cloud server, in the main branch folder:

	cd Comp90024-group-project
	scp -i demokey1.pem harvester.yaml ubuntu@172.26.135.144:/home/ubuntu

 


3.	Run the harvesters on the cloud:

	ansible-playbook harvester.yaml

4.	Install Docker on the server:
   	
	Follow these commands: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository   
 


5.	Copy the Backend to the server, in the backend branch folder:

 	cd Comp90024-group-project
	scp -i demokey1.pem -r Backend ubuntu@172.26.135.144:/home/ubuntu

   


6.	Copy the Dockerfile to the server:

	scp -i demokey1.pem Dockerfile ubuntu@172.26.135.144:/home/ubuntu

7.	Build Docker images of the backend:

	sudo docker build -t flask .

8.	Build and run the container:

	sudo docker run --name flask -p 8080:8080 -d flask

9.	Copy the front end code, in the frontend branch folder:

	cd Frontend
	scp -i demokey1.pem -r dist ubuntu@172.26.135.144:/home/ubuntu

10.	Pull and build Nginx with the Docker

	sudo docker pull nginx
	sudo docker run -p 5000:80 -d nginx

11.	Copy frontend Vue.js to the Nginx:

	sudo docker cp dist/. nginx_container:/usr/share/nginx/html




