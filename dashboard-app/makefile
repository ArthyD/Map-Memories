name :=triss-dashboard
platform := linux/arm/v7
build:
	docker build --platform $(platform) -t $(name) .
push:
	docker tag $(name):latest arthurdocq/$(name):latest 
	docker push arthurdocq/$(name):latest


