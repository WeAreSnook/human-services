/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.porism.servicedirectoryservice.services;

import com.porism.servicedirectoryservice.models.ServiceTaxonomy;
import com.porism.servicedirectoryservice.repositories.ServiceTaxonomyRepository;
import java.util.Collection;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;

/**
 *
 * @author Dominic Skinner
 */
@org.springframework.stereotype.Service
public class ServiceTaxonomyService implements IServiceTaxonomyService {
    @Autowired
    private ServiceTaxonomyRepository repository;   

    @Override
    public List<ServiceTaxonomy> findByTaxonomyIdIdAndTaxonomyIdVocabulary(String id, String vocabulary) {
        return (List<ServiceTaxonomy>) repository.findByTaxonomyIdIdAndTaxonomyIdVocabulary(id, vocabulary);
    }

    @Override
    public Collection<ServiceTaxonomy> saveAll(Collection<ServiceTaxonomy> serviceTaxonomies) {
        repository.saveAll(serviceTaxonomies);
        return serviceTaxonomies;
    }
    
    @Override
    public List<ServiceTaxonomy> findByNeed(String need) {
        return (List<ServiceTaxonomy>) repository.findByNeed(need);
    } 
    
    @Override
    public List<ServiceTaxonomy> findByCircumstance(String circumstance) {
        return (List<ServiceTaxonomy>) repository.findByCircumstance(circumstance);
    }      
}
