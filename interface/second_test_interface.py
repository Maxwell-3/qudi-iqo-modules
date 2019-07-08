# -*- coding: utf-8 -*-

import abc
from core.util.interfaces import InterfaceMetaclass
from core.module import interface_method


class SecondTestInterface(metaclass=InterfaceMetaclass):
    """
    """

    _modclass = 'SecondTestInterface'
    _modtype = 'interface'

    @interface_method
    @abc.abstractmethod
    def test(self):
        """
        This is for testing

        @return int: error code (0:OK, -1:error)
        """
        pass


    @interface_method
    @abc.abstractmethod
    def another_method(self):
        """
        This is for testing

        @return int: error code (0:OK, -1:error)
        """
        pass