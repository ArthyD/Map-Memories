import { Injectable } from '@angular/core';
import { HttpClient  } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MapService {

  constructor(private http: HttpClient) { }

  get_json(){
    return this.http.get('http://192.168.0.107:8091/get_json')
  }

}
