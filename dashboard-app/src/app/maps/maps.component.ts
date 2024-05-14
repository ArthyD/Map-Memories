import { Component } from '@angular/core';
import dashBoardJson from '../../assets/dashboard.json'
import { IDashboardJson, IDashBoardWidget } from '../dashboard-interface';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.css']
})
export class MapsComponent {
  sideContents:IDashBoardWidget[];
  mapContents:IDashBoardWidget[];
  dashboardJson: IDashboardJson;

  constructor() { 
    this.dashboardJson = dashBoardJson as IDashboardJson;
    this.sideContents = [];
    this.mapContents = this.dashboardJson.mapContent;
  }
}
