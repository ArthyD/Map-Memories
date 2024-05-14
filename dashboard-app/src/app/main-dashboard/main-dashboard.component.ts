import { Component, Input, OnInit } from '@angular/core';
import { IDashBoardWidget } from '../dashboard-interface';


@Component({
  selector: 'app-main-dashboard',
  templateUrl: './main-dashboard.component.html',
  styleUrls: ['./main-dashboard.component.css']
})
export class MainDashboardComponent implements OnInit {

  @Input()
  widgetsList:IDashBoardWidget[]=[];
  
  @Input()
  sideContents:IDashBoardWidget[]=[];

  testMessage:string="";
  constructor() { 

  }

  ngOnInit(): void {
    
  }

}
