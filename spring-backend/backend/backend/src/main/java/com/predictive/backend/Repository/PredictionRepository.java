package com.predictive.backend.Repository;

import com.predictive.backend.entity.PredictionRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PredictionRepository
        extends JpaRepository<PredictionRecord, Long> {
}