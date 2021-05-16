import 'package:rxdart/rxdart.dart';

class MovieDetailBloc {
  final _movieId = PublishSubject<int>();

  Function(int) get fetchTrailersById => _movieId.sink.add;

  dispose() async {
    _movieId.close();
  }
}
