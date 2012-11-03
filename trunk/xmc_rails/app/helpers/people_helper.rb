module PeopleHelper
  
  def button_select(model_name, target_property, button_source)
    list = button_source.sort
    if list.length <4
      list.collect do |item|
        radio_button(model_name, target_property, item[1]) + h(item[0])
      end.join('<br/>')
    else
      select(model_name, target_property, list)
    end
  end
  
end