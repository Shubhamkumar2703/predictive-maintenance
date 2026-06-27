package com.predictive.backend.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import com.predictive.backend.dto.SensorRequest;

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class PredictionController {

    @PostMapping("/predict")
    public Object predict(@RequestBody SensorRequest request) {

        String fastApiUrl = "http://127.0.0.1:8000/predict";

        RestTemplate restTemplate = new RestTemplate();

        Object response = restTemplate.postForObject(
                fastApiUrl,
                request,
                Object.class
        );

        return response;
    }
}