package com.example.HeartDiseasePrediction.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.HeartDiseasePrediction.Model.User;





public interface UserRepo extends JpaRepository<User, Long>{
	
	public User findByEmail(String email);

}
