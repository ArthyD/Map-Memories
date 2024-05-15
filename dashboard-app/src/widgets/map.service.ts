import { Injectable } from '@angular/core';
import { HttpClient  } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MapService {

  constructor(private http: HttpClient) { }

  get_json(){
    return this.http.get('http://127.0.0.1:8080/get_locations')
  }

}
