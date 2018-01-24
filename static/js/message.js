function MessageOperation(url) {
    this.url = url;
	this.bindDom();
	this.bindEvent();
}

MessageOperation.prototype = {
	bindDom: function() {
		this.resetBtn = $("#reset-btn");
		this.sendBtn = $("#send-btn");
		this.closeBtn = $("#close-btn");
		this.imgSelect = $(".img-select");
		this.dropDownMenuBtn = $("#dropdownMenu1");
		this.alertDanger = $(".alert-danger");
		this.username = $("#username");
		this.email = $("#email");
		this.message = $("#message");
		this.mediaList = $(".media-list");
	    this.sendSort = $("#send_sort");
	    this.articleId = $("#article_id");
		this.timer = null;
	},

	imgSelectEvent: function() {
		var that = this;
		this.imgSelect.unbind("click").bind("click", function() {
			var index = $(this).parent().index();
			var imgSrc = that.imgSelect.eq(index).attr("src");
			that.createDom(imgSrc, "img");
		});
	},

	sendMessageEvent: function() {
		var that = this;
		this.sendBtn.unbind("click").bind("click", function() {
			var flag = that.checkInput();
			if(!flag) {
				that.createDom("请填写好所有必填内容，谢谢!", "warning");

			} else {
				that.sendMessage();
			}

		});
	},

	createDom: function(data, type) {
		if(type == "img") {
			var str = '<img src="' + data + '" class="img-circle"/>' +
				'<input type="text" name="image" class="hidden" value="' + data + '" />';
			this.dropDownMenuBtn.html(str);
		} else if(type == "warning") {
		    var that = this;
			this.alertDanger.html("<h1>" + data + "</h1>");
			this.alertDanger.removeClass("hidden");
			clearTimeout(this.timer);
            that.timer = setTimeout(function() {
                that.alertDanger.addClass("hidden");
            }, 3000);
		} else {
			var len = data.messages.length;
			var last_page = parseInt(data.last_page);
			var send_sort = parseInt(this.sendSort.val());
			var article_id = parseInt(this.articleId.val());
			var sort_url = send_sort ? 'sort=' + send_sort + '&' : '';
			var str = "";
			for(var i = 0; i < len; ++i) {
				str += '<li class="media"><div class="media-object col-md-2">' +
					'<img src="' + data.messages[i].image + '" class="img-circle" />' +
					'<div class="triangle pull-right"></div></div>' +
					'<div class="col-md-10 message-body">' +
					'<h3 class="media-heading">' + data.messages[i].username + ':</h3>' +
					'<p>' + $("<p/>").text(data.messages[i].message).html() + '</p>' +
					'<div class="media-bottom pull-right">' +
					'<h4>' + data.messages[i].add_time + '</h4></div></div></li>';
			}

			this.mediaList.html(str);
			this.closeBtn.click();
			if($("#pre-page")){
			    $("#pre-page").remove();
			}
            $("#next-page").remove()

            len = $(".pages").length;
            if(len > 5){
                for(var i = len-1; i >=5; --i){
                    $(".pages").eq(i).remove();
                }
            }

            for(var i = 0; i < 5; ++i){
                $(".pages").eq(i).find("a").html(i+1).attr("href",
                    "?" + sort_url + (article_id ? 'id=' + article_id + '&' : '') + 'page=' + parseInt(i+1)
                )
            }

			if($(".pages").length < last_page){


                var str = '';
                if(last_page - $(".pages").length >= 2){
                    str += '<li class="pages">'
                            + '<a href="?' + sort_url
                            + (article_id ? 'id=' + article_id + '&' : '')
                            + 'page=6">...'
                            + '</a>'
                        + '</li>';
                }

                str += '<li class="pages">'
                        + '<a href="?' + sort_url
                        + (article_id ? 'id=' + article_id + '&' : '')
                         + 'page=' + last_page + '">'
                         + last_page +
                         '</a>'
                    + '</li>';



			    $(".pagination").html($(".pagination").html() + str)


			}

			if(last_page > 1){
			    var str = '<li id="next-page">'
                        + '<a href="" aria-label="Next">'
                          + '<span aria-hidden="true">下一页</span>'
                        + ' </a>'
                        + '</li>';

                $(".pagination").html($(".pagination").html() + str);

                $("#next-page").find("a").attr("href", $(".pages").eq(1).find("a").attr("href"));
			}

			$(".pages").removeClass("active");
			$(".pages").eq(0).addClass("active");
		}
	},

	sendMessage: function() {
		var that = this;
		$.ajax({
			type: "post",
			url: that.url,
			async: true,
			data: $("#send-message-form").serialize(),
			cache: false,
			success: function(data) {

				if(data.status == "success") {
					that.resetBtn.click();
					that.createDom(data, "messages");
				} else {
					that.createDom(data.warning, "warning");
				}

			}
		});
	},

	checkInput: function() {
		return this.username.val() != "" &&
			this.email.val() != "" &&
			this.message.val() != "";
	},

	bindEvent: function() {
		this.imgSelectEvent();
		this.sendMessageEvent();
	}
}