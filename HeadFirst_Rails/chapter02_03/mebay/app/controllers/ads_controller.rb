class AdsController < ApplicationController
    before_filter :check_logged_in, :only=> [:edit, :update, :destroy]

    # 新建
    def new
        @ad = Ad.new
    end

    # 创建之后
    def create
        @ad = Ad.new(params[:ad])
        @ad.save
        #redirect_to "/ads/#(@ad.id)"
        redirect_to "/ads/#{@ad.id}"
    end

    # 编辑
    def edit
        @ad = Ad.find(params[:id])
    end

    # 更新
    def update
        @ad = Ad.find(params[:id])
        # 如若属性全部正确无误，就转向show页面，否则停留在edit页面
        if @ad.update_attributes(params[:ad])
            redirect_to "/ads/#{@ad.id}"
        else
            render :template=>"/ads/edit"
        end
    end

    # 显示
    def show
        @ad = Ad.find(params[:id])
    end

    # 首页
    def index
        @ads = Ad.find(:all)
    end

    # 销毁
    def destroy
        @ad = Ad.find(params[:id])
        @ad.destroy
        redirect_to '/ads/' #页面跳转
    end

    private
    def check_logged_in
        authenticate_or_request_with_http_basic("Ads") do |username,password|
            username == "admin" && password == "15263748"
        end
    end
end
