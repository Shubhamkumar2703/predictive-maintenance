package com.predictive.backend.entity;

import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Entity
@Data
public class PredictionRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private double sensor_2;
    private double sensor_3;
    private double sensor_4;
    private double sensor_7;
    private double sensor_11;
    private double sensor_12;
    private double sensor_15;

    private int prediction;

    private String status;

    private LocalDateTime timestamp;
}