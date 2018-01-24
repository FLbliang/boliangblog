function GoodClick(url) {
    this.url = url;
	this.bindDom();
	this.bindEvent();
}

GoodClick.prototype = {
	bindDom: function() {
		this.warningTimer = null;
		this.goodclickTimer = null;
		this.can_click = true;
		this.goodclickBtn = $(".good-click").find("span");
		this.goodclickNum = $(".good-click").find("small");
		this.goodclickForm = $("#good-click-form");
		this.alertDanger = $(".alert-danger");

	},

	createDom: function(data, type) {
		if(type == "warning") {
			this.alertDanger.html("<h1>" + data + "</h1>");
			this.alertDanger.removeClass("hidden");
			clearTimeout(this.warningTimer);
			var that = this;
			this.warningTimer = setTimeout(function() {
				that.alertDanger.addClass("hidden");
			}, 3000);
		} else {
			this.goodclickNum.html(data.goodclick_nums);
		}
	},

	sendGoodclick: function() {
		var that = this;
		$.ajax({
			type: "post",
			url: that.url,
			async: true,
			cache: false,
			data: that.goodclickForm.serialize(),
			success: function(data) {
				if(data.status == "success") {
					that.can_click = false;
					clearTimeout(that.goodclickTimer);
					that.goodclickTimer = setTimeout(function() {
						that.can_click = true;
					}, 30000)
					that.createDom(data, "success");
				} else {
					that.createDom("哎呀！好像点赞没成功！ 过一会再点赞好吗", "warning");
				}
			}
		});
	},

	sendEvent: function() {
		var that = this;
		this.goodclickBtn.unbind("click").bind("click", function() {
			if(!that.can_click) {
				that.createDom("三分钟内只能点赞一次喔!", "warning");
			} else {
				that.sendGoodclick();
			}

		});
	},

	bindEvent: function() {
		this.sendEvent();
	}
}