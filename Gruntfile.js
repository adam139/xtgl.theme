module.exports = function (grunt) {
    'use strict';
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        // we could just concatenate everything, really
        // but we like to have it the complex way.
        // also, in this way we do not have to worry
        // about putting files in the correct order
        // (the dependency tree is walked by r.js)
        less: {
            dist: {
                options: {
                    paths: [],
                    strictMath: false,
                    sourceMap: true,
                    outputSourceFiles: true,
                    sourceMapURL: '++theme++xtgl.theme/less/barceloneta-compiled.css.map',
                    sourceMapFilename: 'xtgl/theme/theme/less/barceloneta-compiled.css.map',
                    modifyVars: {
                        "isPlone": "false"
                    }
                },
                files: {
                    'xtgl/theme/theme/less/barceloneta-compiled.css': 'xtgl/theme/theme/less/barceloneta.plone.local.less',
                }
            }
        },

        watch: {
            scripts: {
                files: ['xtgl/theme/theme/less/*.less'],
                tasks: ['less']
            }
        },
        browserSync: {
            html: {
                bsFiles: {
                    src : ['xtgl/theme/theme/less/*.less']
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    server: {
                        baseDir: "."
                    },
                }
            },
            plone: {
                bsFiles: {
                    src : ['xtgl/theme/theme/less/*.less']
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    proxy: "localhost:8080"
                }
            }
        }
    });

    // grunt.loadTasks('tasks');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('bsync', ["browserSync:html", "watch"]);
    grunt.registerTask('plone-bsync', ["browserSync:plone", "watch"]);
};
