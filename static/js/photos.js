function PhotoOperation() {
	this.initDom();
	this.bindEvent();
}

PhotoOperation.prototype = {
	initDom: function() {
		var main_height = $(".main").height();
		var windowWidth = $(window).width();
		var windowHeight = $(window).height();
		$(".photo-show-container").height(main_height);
		$(".photo-show-body").width(0.8 * windowWidth);
		$(".photo-show-body").height(0.8 * windowHeight);
		$(".photo-show-body").css("left", 0.1 * windowWidth);
		$(".photo-show-body").css("top", 0.15 * windowHeight);

	},

	updateDom: function(data) {
		var str = '<div class="col-md-2 photo-btn text-center fade-outstanding">' +
			'<span class="glyphicon glyphicon-chevron-left"  id="photo-btn-left"></span></div>' +
			'<div class="col-md-8 photo-img text-center">' +
			'<img src="' + data.imgSrc + '" class="' + data.imgClass + ' fade-rotateTop"/>' +
			'</div>' +
			'<div class="col-md-2 photo-btn text-center fade-outstanding">' +
			'<span class="glyphicon glyphicon-chevron-right" id="photo-btn-right"></span></div>';

		this.photoContainer.removeClass("hidden");
		this.photoBody.html(str);
		var that = this;

		$(".photo-btn span").unbind("click").bind("click", function(event) {
			event.stopPropagation();
			var id = $(this).attr("id");
			if(id == "photo-btn-left") {
				that.imgBtns.eq(data.leftIndex).click();
			} else {
				that.imgBtns.eq(data.rightIndex).click();
			}
		});

		this.photoBody.children(".photo-img")
			.unbind("click").bind("click", function(event) {
				event.stopPropagation();
			});
	},

	bindDom: function() {
		this.photoContainer = $(".photo-show-container");
		this.photoBody = $(".photo-show-body");
		this.imgBtns = $(".box ul li a");
		var that = this;
		var len = this.imgBtns.length;

		this.imgBtns.unbind("click").bind("click", function() {
			var index = $(this).parent().index();
			var leftIndex = index - 1 < 0 ? len - 1 : index - 1;
			var rightIndex = ++index % len;
			var data = {
				imgSrc: $(this).children().attr("src"),
				imgClass: $(this).children().attr("class"),
				leftIndex: leftIndex,
				rightIndex: rightIndex
			}

			that.updateDom(data);

		});

		this.photoContainer.unbind("click").bind("click", function() {
			$(this).addClass("hidden");
		});
	},

	bindEvent: function() {
		this.bindDom()
	}

}