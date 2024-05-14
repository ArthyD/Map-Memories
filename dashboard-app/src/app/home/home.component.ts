import { Component } from '@angular/core';
import dashBoardJson from '../../assets/dashboard.json'
import { IDashboardJson, IDashBoardWidget } from '../dashboard-interface';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  mainContents:IDashBoardWidget[];
  dashboardJson: IDashboardJson;

  constructor() { 
    this.dashboardJson = dashBoardJson as IDashboardJson;
    this.mainContents = this.dashboardJson.mainContents;
  }
}
