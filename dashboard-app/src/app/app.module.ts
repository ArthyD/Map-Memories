import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {FormsModule} from '@angular/forms';
import { YouTubePlayerModule } from '@angular/youtube-player';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainDashboardComponent } from './main-dashboard/main-dashboard.component';
import { MapWidgetComponent } from 'src/widgets/map-widget/map-widget.component';
import {ToolbarModule} from 'primeng/toolbar';
import { MenubarModule } from 'primeng/menubar';
import {MenuModule} from 'primeng/menu';
import {ImageModule} from 'primeng/image';
import {DropdownModule} from 'primeng/dropdown';
import { Steps, StepsModule } from 'primeng/steps';
import { TableModule } from 'primeng/table';
import { PaginatorModule } from 'primeng/paginator';
import { TagModule } from 'primeng/tag';
import { InputTextModule } from 'primeng/inputtext';
import { ButtonModule } from 'primeng/button';
import {ScrollPanelModule} from 'primeng/scrollpanel';
import {DialogModule} from 'primeng/dialog';
import {CarouselModule} from 'primeng/carousel';
import { MapsComponent } from './maps/maps.component';
import { HomeComponent } from './home/home.component';
import { CardModule } from 'primeng/card';
import { InputSwitchModule } from 'primeng/inputswitch';
import { TabMenuModule } from 'primeng/tabmenu';
import { ChartModule } from 'primeng/chart';
import { ImageCarousselWidgetComponent } from 'src/widgets/image-caroussel-widget/image-caroussel-widget.component';

@NgModule({
  declarations: [
    AppComponent,
    MainDashboardComponent,
    MapWidgetComponent,
    MapsComponent,
    HomeComponent,
    ImageCarousselWidgetComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ToolbarModule,
    MenuModule,
    MenubarModule,
    ImageModule,
    HttpClientModule,
    ScrollPanelModule,
    DropdownModule,
    FormsModule,
    BrowserAnimationsModule,
    TagModule,
    ButtonModule,
    InputTextModule,
    DialogModule,
    CarouselModule,
    YouTubePlayerModule,
    PaginatorModule,
    StepsModule,
    TableModule,
    CardModule,
    InputSwitchModule,
    TabMenuModule,
    ChartModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
