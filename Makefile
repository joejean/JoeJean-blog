reserve:
	docker build -t joeblog . 
	docker run -e ENV='test' -p 8000:8000 -v `pwd`:/usr/src/app -it joeblog /bin/bash -c 'fab reserve'
	
publish:
	docker build -t joeblog . 
	docker run -e ENV='test' -p 8000:8000 -v `pwd`:/usr/src/app -it joeblog /bin/bash -c 'fab rebuild && ghp-import output/'
	

	