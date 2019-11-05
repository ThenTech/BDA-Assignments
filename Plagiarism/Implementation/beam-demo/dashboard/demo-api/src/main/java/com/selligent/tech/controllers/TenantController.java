package com.selligent.tech.controllers;

import com.selligent.tech.models.TimelinePair;
import com.selligent.tech.repositories.TenantRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.time.Instant;
import java.util.List;

@RestController
@RequestMapping("/tenant")
public class TenantController {

    @Autowired
    private TenantRepository tenantRepository;

    @GetMapping("/timeline")
    List<TimelinePair> getInteractionsTimeline(@RequestParam(required = true, value = "tenantId") String tenantId,
                                               @RequestParam(required = true, value = "start") Long start,
                                               @RequestParam(required = true, value = "end") Long end) throws IOException {

        return tenantRepository.fetchTimeline(tenantId, start, end);
    }
}
