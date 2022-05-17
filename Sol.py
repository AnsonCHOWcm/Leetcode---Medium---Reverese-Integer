#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 21:59:19 2022

@author: ccm
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        
        if (x <0):
            digit = a[1:]
        else :
            digit = a
            
        total_length = len(digit)
        
        res = 0
        
        for i in range(total_length):
            
            res = res + int(digit[i])*10**(i)
            
        if (x<0):
            res = -1 * res
            if (res < -1 * 2**(31)):
                return (0)
            else :
                return (res)
        else : 
            if (res >  2**(31) -1):
                return (0)
            else :
                return (res)