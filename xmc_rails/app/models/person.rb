#coding: utf-8
class Person < ActiveRecord::Base
  #可用属性
  attr_accessible :birthday, :body_temperature, :can_send_email, :country, :description, :email, :favorite_time, :graduation_year, :name, :price, :secret, :photo

  #姓名
  validates_presence_of :name, :message => "不可为空"

  #密码
  #validates_presence_of :secret, :message => "不可为空"
  validates_length_of :secret, :in => 6..24 , :message => "长度为6到24"
  validates_format_of :secret, :with => /[0-9]/, :message => "至少有一个数字"
  #validates_format_of :secret, :with => /[A-Z]/, :message => "至少有一个大写字母"
  #validates_format_of :secret, :with => /[a-z]/, :message => "至少有一个小写字母"

  #国家
  validates_inclusion_of :country, :in => ['Canada', 'Mexico', 'UK', 'USA'], :message => "must be one of Canada, Mexico, UK or USA"

  #邮箱
  validates_format_of :email, :with => /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\Z/i, :message => "doesn't look like a proper email address"
  #validates_uniqueness_of :email, :case_sensitive => false, :message => "已被注册"
  validates_uniqueness_of :email, :case_sensitive => false, :scope => [:name, :secret], :message => "has already been entered, you can't sign in twice"

  #毕业时间
  validates_numericality_of :graduation_year, :allow_nil => true, :greater_than => 1920, :less_than_or_equal_to => Time.now.year, :only_integer => true

  #体温
  validates_numericality_of :body_temperature, :allow_nil => true, :greater_than_or_equal_to => 60, :less_than_or_equal_to => 130, :only_integer => false

  #价钱
  validates_numericality_of :price, :allow_nil => true, :only_integer => false

  #生日
  validates_inclusion_of :birthday, :in => Date.civil(1900, 1, 1) .. Date.today, :message => "must be between January 1st, 1900 and today"

  #最爱时间
  validates_presence_of :favorite_time

  #更复杂的校验
  # if person says 'can send email', then we'd like them to fill their
  # description in, so we understand who it is we're sending mail to
  validates_presence_of :description, :if => :require_description_presence?
  # we define the supporting condition here
  def require_description_presence?
    self.can_send_email
  end

  #自定义验证
  def description_length_words
    # only do this validation if description is provided
    unless self.description.blank? then
      # simple way of calculating words: split the text on whitespace
      num_words = self.description.split.length
      if num_words < 5 then
        self.errors.add(:description, "must be at least 5 words long")
      elsif num_words > 50 then
        self.errors.add(:description, "must be at most 50 words long")
      end
    end
  end

  # NEW FOR CHAPTER 8
  # 增加图片功能
  # after the person has been written to the database, deal with
  # writing any image data to the filesystem
  after_save :store_photo

  # File.join is a cross-platform way of joining directories,
  # we could have written "#{Rails.root}/public/photo_store"
  PHOTO_STORE = File.join Rails.root, 'public', 'photo_store', 'people'

  # when photo data is assigned via the upload, store the file data
  # for later and assign the file extension, e.g. ".jpg"
  def photo=(file_data)
    unless file_data.blank?
      # store the uploaded data into a private instance variable
      @file_data = file_data
      # figure out the last part of the file name and use this as
      # the file extension. e.g. from "me.jpg" will return "jpg"
      self.extension = file_data.original_filename.split('.').last.downcase
    end
  end

  # if a photo file exists, then we have a photo
  def has_photo?
    File.exists? photo_filename
  end

  # return a path we can use in HTML for the image
  def photo_path
    "/photo_store/people/#{id}.#{extension}"
  end

  # where to write the image file to
  def photo_filename
    File.join PHOTO_STORE, "#{id}.#{extension}"
  end

  private

  # called after saving, to write the uploaded image to the filesystem
  def store_photo
    if @file_data
      # make the photo_store directory if it doesn't exist already
      FileUtils.mkdir_p PHOTO_STORE
      # write out the image data to the file
      File.open(photo_filename, 'wb') do |f|
        f.write(@file_data.read)
      end
      # avoid repeat-saving
      @file_data = nil
    end
  end

end