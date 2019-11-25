/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.porism.servicedirectoryservice.services;

import com.porism.servicedirectoryservice.models.Phone;
import com.porism.servicedirectoryservice.repositories.PhoneRepository;
import java.util.Collection;
import org.springframework.beans.factory.annotation.Autowired;

/**
 *
 * @author Administrator
 */
@org.springframework.stereotype.Service
public class PhoneService implements IPhoneService {
    @Autowired
    private PhoneRepository repository;

    @Override
    public Collection<Phone> saveAll(Collection<Phone> phones) {
        repository.saveAll(phones);
        return phones;
    }    
}
