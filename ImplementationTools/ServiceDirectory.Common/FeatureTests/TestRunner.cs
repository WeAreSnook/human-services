﻿using ServiceDirectory.Common.Pagination;
using System;

namespace ServiceDirectory.Common.FeatureTests
{
    internal class TestRunner
    {
        internal async static System.Threading.Tasks.Task<bool> HasPassed(string apiBaseUrl, IFeatureTest test)
        {
            bool result = false;
            Paginator paginator = new Paginator();
            try
            {
                await paginator.PaginateServices(apiBaseUrl, async delegate (dynamic serviceList, int totalPages)
                {
                    if (serviceList == null)
                    {
                        result = false;
                    }
                    foreach (dynamic s in serviceList.content)
                    {
                        if (s != null && Convert.ToString(s.id.Value) == test.ServiceID)
                        {
                            result = true;
                        }
                    }
                }, test.Parameters);
            }
            catch
            {
                //error logging not required here
                return false;
            }
            return result;
        }
    }
}
