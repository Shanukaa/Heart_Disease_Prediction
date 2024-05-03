package com.example.HeartDiseasePrediction.Service;

import java.util.List;

import com.example.HeartDiseasePrediction.Model.User;





public interface UserService {

	public User saveUser(User user);

	List<User> getAllUser();

	User getUserByID(Long id);

	User updateUser(User user);
	
	void deleteUser(Long id);


}
