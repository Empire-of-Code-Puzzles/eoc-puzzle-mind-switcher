//Dont change it
requirejs(['ext_editor_1', 'jquery_190', 'raphael_210'],
    function (ext, $, TableComponent) {

        var cur_slide = {};

        ext.set_start_game(function (this_e) {
        });

        ext.set_process_in(function (this_e, data) {
            cur_slide["in"] = data[0];
        });

        ext.set_process_out(function (this_e, data) {
            cur_slide["out"] = data[0];
        });

        ext.set_process_ext(function (this_e, data) {
            cur_slide.ext = data;
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_process_err(function (this_e, data) {
            cur_slide['error'] = data[0];
            this_e.addAnimationSlide(cur_slide);
            cur_slide = {};
        });

        ext.set_animate_success_slide(function (this_e, options) {
            var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
            this_e.setAnimationHeight(115);
        });

        ext.set_animate_slide(function (this_e, data, options) {
            var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
            if (!data) {
                console.log("data is undefined");
                return false;
            }

            //YOUR FUNCTION NAME
            var fname = 'mind_switcher';

            if (data.ext && data.ext["show"]) {
                var checkioInputStr = fname + "(" + data.ext["show"] + ")";
            }
            else {
                checkioInputStr = fname + '({"scout", "super"},)';
            }

            var failError = function (dError) {
                $content.find('.call').html('Fail: ' + checkioInputStr);
                $content.find('.output').html(dError.replace(/\n/g, ","));
                $content.find('.answer').remove();
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
                $content.find('.explanation').remove();
                this_e.setAnimationHeight($content.height() + 60);
            };

            if (data.error) {
                failError(data.error);
                return false;
            }

            if (data.ext && data.ext.inspector_fail) {
                failError(data.ext.inspector_result_addon);
                return false;
            }

            var rightResult = data.ext["answer"];
//            var userResult = data.out;
            var result = data.ext["result"];
            var result_addon = data.ext["result_addon"];
            var state = data.ext["state"];
            var result_code = result_addon[0];
            var result_message = result_addon[1];
            var userResult = result_addon[2];


            //if you need additional info from tests (if exists)
            var explanation = data.ext["explanation"];

            $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));

            if (!result) {
                $content.find('.call').html('Fail: ' + checkioInputStr);
                $content.find('.answer').html(result_message);
                $content.find('.answer').addClass('error');
                $content.find('.output').addClass('error');
                $content.find('.call').addClass('error');
            }
            else {
                $content.find('.call').html('Pass: ' + checkioInputStr);
                $content.find('.answer').remove();
            }

            var canvas = new BodiesMinds();
            canvas.draw($content.find(".explanation")[0], state);
            if (result_code > 5) {
                canvas.animate(userResult);
            }


            this_e.setAnimationHeight($content.height() + 60);

        });

        //This is for Tryit (but not necessary)
//        var $tryit;
//        ext.set_console_process_ret(function (this_e, ret) {
//            $tryit.find(".checkio-result").html("Result<br>" + ret);
//        });
//
//        ext.set_generate_animation_panel(function (this_e) {
//            $tryit = $(this_e.setHtmlTryIt(ext.get_template('tryit'))).find('.tryit-content');
//            $tryit.find('.bn-check').click(function (e) {
//                e.preventDefault();
//                this_e.sendToConsoleCheckiO("something");
//            });
//        });
        function BodiesMinds() {
            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var padding = 10;

            var w = 100;
            var h = w * 0.6;

            var paper;

            var sizeX = padding * 4 + w * 3;
            var sizeY;
            var names = [];
            var minds = {};

            var attrRect = {"stroke": colorBlue4, "stroke-width": 3};
            var attrText = {"stroke": colorBlue4, "fill": colorBlue4, "font-family": "Roboto", "font-size": h * 0.4};
            var attrWrong = {"fill": colorOrange4, "stroke": colorOrange4};
            var attrRight = {"fill": colorBlue4, "stroke": colorBlue4};

            this.draw = function (dom, state) {
                state["sophia"] = "sophia";
                state["nikola"] = "nikola";
                names = Object.keys(state);
                var rows = Math.ceil(names.length / 3);
                sizeY = rows * h + padding * (rows + 1);
                paper = Raphael(dom, sizeX, sizeY);
                for (var i = 0; i < names.length; i++) {
                    var row = Math.floor(i / 3);
                    var col = i % 3;
                    var body = names[i];
                    var mind = state[body];

                    paper.rect(padding * (col + 1) + w * col, padding * (row + 1) + h * row,
                        w, h, w / 10).attr(attrRect);
                    paper.rect(padding * (col + 1) + w * col, padding * (row + 1) + h * row,
                        w, h / 2, w / 10).attr(attrRect);
                    paper.text(padding * (col + 1) + w * col + w / 2,
                        padding * (row + 1) + h * row + h * 0.7, body).attr(attrText);
                    var t = paper.text(0, 0, mind).attr(attrText);
                    t.x = padding * (col + 1) + w * col + w / 2;
                    t.y = padding * (row + 1) + h * row + h * 0.2;
                    t.name = mind;
                    t.transform("t" + t.x + "," + t.y);
                    if (body !== mind) {
                        t.attr(attrWrong);
                    }
                    minds[body] = t;
                }
            };

            this.animate = function (actions) {
                var stepTime = 700;
                var fullStep = stepTime * 1.3;
                for (var i = 0; i < actions.length; i++) {
                    setTimeout(function () {
                        var act = actions[i];
                        return function () {
                            var f = act[0];
                            var s = act[1];
                            var f_mind = minds[f];
                            var s_mind = minds[s];
                            minds[f] = s_mind;
                            minds[s] = f_mind;
                            var s_color = f === s_mind.name ? colorBlue4 : colorOrange4;
                            var f_color = s === f_mind.name ? colorBlue4 : colorOrange4;
                            f_mind.animate({"transform": "t" + s_mind.x + "," + s_mind.y,
                                "fill": f_color, "stroke": f_color}, stepTime);
                            s_mind.animate({"transform": "t" + f_mind.x + "," + f_mind.y,
                                "fill": s_color, "stroke": s_color}, stepTime, stepTime);
                            var tx = s_mind.x;
                            var ty = s_mind.y;
                            s_mind.x = f_mind.x;
                            s_mind.y = f_mind.y;
                            f_mind.x = tx;
                            f_mind.y = ty;
                        }
                    }(), fullStep * i);
                }
            }
        }


    }
);
