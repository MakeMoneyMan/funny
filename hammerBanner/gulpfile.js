var gulp = require('gulp')
var uglify = require('gulp-uglify')
var rename = require('gulp-rename')

gulp.task('default', function(){

return gulp.src('src/*.js')
	.pipe(gulp.dest('./dist/'))
	.pipe(rename(function(path){
		path.extname = '.min.js';
	}))
	.pipe(uglify())
	// .pipe(jsmin())
	.pipe(gulp.dest('./dist/'));

});
