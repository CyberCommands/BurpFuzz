#!/usr/bin/env python3
from burp import IBurpExtender
from burp import IIntruderPayloadGenerator
from burp import IIntruderPayloadGeneratorFactory

from java.util import List, Arraylist

import random

class BurpExtender(IBurpExtender, IIntruderPayloadGeneratorFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.registerIntruderPayloadGeneratorFactory(self)

        return
    
    def getGeneratorName(self):
        return "Payload Generator"
    
    def createNewInstance(self, attack):
        return Fuzzer(self, attack)


class Fuzzer(IIntruderPayloadGenerator):
    def __init__(self, extender, attack):
        self._extender = extender
        self._helpers = extender._helpers
        self._attack = attack
        self.max_payloads = 10
        self.num_iterations = 0
        return
    
    def hasMorePayloads(self):
        if self.num_iterations == self.max_payloads:
            return False
        else:
            return True
    
    def getNextPayload(self, current_payload):
        # Convert into a string.
        payload = "".join(chr(x) for x in current_payload)

        # Call our simple mutator to fuzz the POST.
        payload = self.mutate_payload(payload)

        # Increase the number of fuzzing attempts.
        self.num_iterations += 1
        
        return payload
    
    def reset(self):
        self.num_iterations = 0
        return
    
    def mutate_payload(self, original_payload):
        picker = random.randint(1,3)    # Pick a simple or even call an external script.
        offset = random.randint(0, len(original_payload)-1)     # Select a random offset in the payload to mutate.
        front, back = original_payload[:offset], original_payload[offset:]
        
        if picker == 1:     # Random offset insert a SQL Injection attempt.
            front += "'"
        elif picker == 2:   # Jam an XSS attempt in.
            front += "<script>alert('XSS');</script>"
        elif picker == 3: # Repeat a random chuck of the original payload.
            chuck_length = random.randint(0, len(back)-1)
            repeater = random.randint(1, 10)
            for _ in range(repeater):
                front += original_payload[:offset + chuck_length]
        
        return front + back