import { Component } from '@angular/core';
import {MenuItem} from 'primeng/api';
import { DarkmodeService } from './darkmode.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Triss Project';
  items: MenuItem[]=[];
  currentTheme = 'bootstrap4-light-blue';

constructor(private darkmodeService: DarkmodeService) {}

ngOnInit(): void {
  this.items=[
  {
    "label":"Carte",
    "icon":"pi pi-map-marker",
    command:(event)=>{
    },routerLink: ['/maps']
  },
  {
    "label":"Cours",
    "icon":"pi pi-compass",
    command:(event)=>{

    },routerLink: ['/course']
  },
  {
      "label":"Lab",
      "icon":"pi pi-server",
      command:(event)=>{
      },routerLink: ['/lab']
  },
  {
    "label":"Plant",
    "icon":"pi pi-sun",
    command:(event)=>{
    },routerLink: ['/plant']
},
  {
      "label":"Home",
      "icon":"pi pi-home",
      command:(event)=>{
      },routerLink: ['/']
  },
  {
    "label":"",
    "icon":"pi pi-moon",
    command:(event)=>{
      this.changeTheme();
    }
  }
  ];  
 }   
 
 changeTheme(){
  if(this.currentTheme=='bootstrap4-light-blue'){
    this.darkmodeService.switchTheme('bootstrap4-dark-blue');
    this.currentTheme='bootstrap4-dark-blue';
  } else {
    this.darkmodeService.switchTheme('bootstrap4-light-blue');
    this.currentTheme='bootstrap4-light-blue';
  }
 }
}
