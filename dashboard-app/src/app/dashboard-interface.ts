export interface IDashboardJson{
    mainContents:IDashBoardWidget[];
    mapContent:IDashBoardWidget[];
    adminContent:IDashBoardWidget[];

}


export interface IStyleWidget{
    colorTitle:string;
    border: boolean;
    size:string;

}

export interface IChartStyle{
    chartColor:string;
}

export interface IDashBoardWidget{
    name:string;
    desc:string;
    type:string;
    style:IStyleWidget;
    listToDoName?:string;
    imagePath?:string;
    imageList?:any[];
    timelineEvent?:any[];
    videoId?:string;
    startSeconds?:number;
    cityLong?:number;
    cityLat?:number;
    mapContent?:string;
    startLocation?:number[];
    startZoom?:number;


}

export interface ToDoTask{
    name:string;
    done:boolean;
}

