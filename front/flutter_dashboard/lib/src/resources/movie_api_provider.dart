import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;

import '../models/item_model.dart';

class MovieApiProvider {
  final _apiKey = 'bc30c107ad3ab9c50cf33b064282358d';
  final _baseUrl = "api.themoviedb.org";

  Future<ItemModel> fetchMovieList() async {
    var response = await http
        .get(Uri.https(_baseUrl, '/3/movie/popular', {"api_key": _apiKey}));

    print(response.body.toString());

    if (response.statusCode == 200) {
      return ItemModel.fromJson(json.decode(response.body));
    } else {
      throw Exception('Failed to load post');
    }
  }
}
