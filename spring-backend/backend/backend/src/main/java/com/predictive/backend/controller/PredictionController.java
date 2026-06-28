package com.predictive.backend.controller;

import com.predictive.backend.dto.SensorRequest;
import com.predictive.backend.entity.PredictionRecord;
import com.predictive.backend.Repository.PredictionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin("*")
public class PredictionController {

    @Autowired
    private PredictionRepository repository;

    @PostMapping("/predict")
    public Object predict(@RequestBody SensorRequest request) {

        String fastApiUrl = "http://127.0.0.1:8000/predict";

        RestTemplate restTemplate = new RestTemplate();

        Map response = restTemplate.postForObject(
                fastApiUrl,
                request,
                Map.class
        );

        // Save to DB
        PredictionRecord record = new PredictionRecord();

        record.setSensor_2(request.getSensor_2());
        record.setSensor_3(request.getSensor_3());
        record.setSensor_4(request.getSensor_4());
        record.setSensor_7(request.getSensor_7());
        record.setSensor_11(request.getSensor_11());
        record.setSensor_12(request.getSensor_12());
        record.setSensor_15(request.getSensor_15());

        record.setPrediction((Integer) response.get("prediction"));
        record.setStatus((String) response.get("status"));

        record.setTimestamp(LocalDateTime.now());

        repository.save(record);

        return response;
    }

    @GetMapping("/history")
    public Object getHistory() {
        return repository.findAll();
    }
}