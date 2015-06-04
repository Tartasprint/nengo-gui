Nengo.Viewport = function() {
    this.x = 0;
    this.y = 0;
    this.scale = 1.0;

    this.w = $("#main").width();
    this.h = $("#main").height();
    var self = this;
    window.addEventListener("resize", function() {self.on_resize();});
}

Nengo.Viewport.prototype.redraw_all = function(event) {
    for (var i in Nengo.Component.components) {
        var c = Nengo.Component.components[i];
        c.on_resize(c.w * this.scale * this.w * 2, c.h * this.scale * this.h * 2);
        c.redraw_size();
        c.redraw_pos();
    }
};

<<<<<<< HEAD:nengo_viz/static/viz_viewport.js
VIZ.Viewport.prototype.on_resize = function(event) {
    var ow = this.w;
    var oh = this.h;
    
=======
Nengo.Viewport.prototype.on_resize = function(event) {
>>>>>>> master:nengo_gui/static/viewport.js
    this.w = $("#main").width();
    this.h = $("#main").height();
    //this.redraw_all();
    for (var i in VIZ.Component.components) {
        var c = VIZ.Component.components[i];
        c.on_resize(c.w * this.scale * ow * 2, c.h * this.scale * oh * 2);
        c.redraw_size();
        c.redraw_pos();
    }
}