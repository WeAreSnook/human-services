/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.porism.servicedirectoryservice.services;

import com.porism.servicedirectoryservice.models.EsdExternalId;

/**
 *
 * @author Administrator
 */
public interface IEsdExternalIdService {
    public EsdExternalId save(EsdExternalId esdExternalId);
    
    public String EnsureUUID(String id, String tableName);
}
