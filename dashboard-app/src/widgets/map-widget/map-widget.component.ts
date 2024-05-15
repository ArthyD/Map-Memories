import { AfterViewInit, Component, Input, OnInit, OnDestroy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import * as L from 'leaflet';
import { MapService } from '../map.service';

@Component({
  selector: 'app-map-widget',
  templateUrl: './map-widget.component.html',
  styleUrls: ['./map-widget.component.css']
})
export class MapWidgetComponent {
  constructor(private http: HttpClient, private mapService: MapService){}

  public mapMemories:any;

  imagePath:string="";
  imageName:string="";
  visible: boolean = false;
  ngAfterViewInit(): void {
    
    // Déclaration de la carte avec les coordonnées du centre et le niveau de zoom.
    this.mapMemories = L.map('mapMemories').setView([48.3833, -2.6167], 10);
    this.mapMemories.scrollWheelZoom.disable();
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: 'Carte Souvenirs'
    }).addTo(this.mapMemories);
    
    
    const myIcon = L.icon({
      iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.2.0/images/marker-icon.png',
      iconSize: [24,36],
      iconAnchor: [12,36]
    });

    this.mapService.get_json().subscribe((data:any)=>{
      for(let location of data){
        console.log(location)
        L.marker([location.lat,location.long], {icon: myIcon}).bindPopup(location.name).on('click',()=>{
          console.log(location.path);
          this.imagePath="http://photo.anniv/get_image/"+location.path;
          this.imageName=location.name;
          this.showDialog();
        }).addTo(this.mapMemories);
      }
    });

  }

  showDialog() {
    this.visible = true;
  }


    ngOnDestroy() {
      if (this.mapMemories) {
        this.mapMemories.off();
        this.mapMemories.remove();
        }

      }

}
