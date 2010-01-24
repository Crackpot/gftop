require 'test_helper'

class ClientWorkoutsControllerTest < ActionController::TestCase
  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:client_workouts)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create client_workout" do
    assert_difference('ClientWorkout.count') do
      post :create, :client_workout => { }
    end

    assert_redirected_to client_workout_path(assigns(:client_workout))
  end

  test "should show client_workout" do
    get :show, :id => client_workouts(:one).to_param
    assert_response :success
  end

  test "should get edit" do
    get :edit, :id => client_workouts(:one).to_param
    assert_response :success
  end

  test "should update client_workout" do
    put :update, :id => client_workouts(:one).to_param, :client_workout => { }
    assert_redirected_to client_workout_path(assigns(:client_workout))
  end

  test "should destroy client_workout" do
    assert_difference('ClientWorkout.count', -1) do
      delete :destroy, :id => client_workouts(:one).to_param
    end

    assert_redirected_to client_workouts_path
  end
end
